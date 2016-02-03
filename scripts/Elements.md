# Elements SQL Queries

#### Select the TIV and the GU AAL by zip code based off industrial exposure runs

```SQL
SELECT Zip, TIV, GUbyZIP FROM
(SELECT RefID, SUM(GU) GUbyZIP FROM
(SELECT * FROM IF_RES_RDFL_E95_Riv2_RES2013_P1.dbo.pml WHERE PMLLevelType = 'PostalCode' AND AnalysisRunID = 1
UNION
SELECT * FROM IF_RES_RDFL_E95_Riv2_RES2013_P2.dbo.pml WHERE PMLLevelType = 'PostalCode' AND AnalysisRunID = 1)A
GROUP BY A.RefID)B
RIGHT JOIN
(SELECT PostalCodeID Zip, SUM(TIV) TIV  FROM
((SELECT PostalcodeID, SUM(TIV) TIV FROM IF_EXP_RDFL_E95_Riv2_RES2013_P1.dbo.Address INNER JOIN IF_EXP_RDFL_E95_Riv2_RES2013_P1.dbo.site ON
Address.ExtPropertyID = Site.ExtSiteID GROUP BY PostalCodeID)
UNION
(SELECT PostalcodeID, SUM(TIV) TIV FROM IF_EXP_RDFL_E95_Riv2_RES2013_P2.dbo.Address INNER JOIN IF_EXP_RDFL_E95_Riv2_RES2013_P2.dbo.site ON
Address.ExtPropertyID = Site.ExtSiteID GROUP BY PostalCodeID))C
GROUP BY C.PostalCodeID ) D
ON B.RefID = D.Zip
ORDER BY Zip
```
