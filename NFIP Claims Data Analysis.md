# NFIP Claims Data Analysis

* Aggregate sums of building payments by year
```SQL
SELECT [YEAR] year
    ,[FIPS] fips
    ,left(FLOODZONE,1) fldzone
    ,sum([TOTCLMS]) totalclaims
    ,sum([PAYBLDG]) buildingpay
    ,sum([PAYCONT]) contentspay
    ,sum([PAYICC]) iicpay
  FROM [NFIP_Flood_DB].[dbo].[Claims_CLSMY_to2014]
  group by [YEAR],[FIPS],left([FLOODZONE],1)
  order by [YEAR],[FIPS]
  ```

  * Next we can then average over the years
  ```SQL
  SELECT
--year
fips
,fldzone
,count(year) totyears
,avg(totalclaims) avgclaims
,avg(buildingpay) avgbldpay
,avg(contentspay) avgconpay
,avg(iicpay) avgiicpay
 FROM
(SELECT [YEAR] year
    ,[FIPS] fips
    ,left(FLOODZONE,1) fldzone
      ,sum([TOTCLMS]) totalclaims
      ,sum([PAYBLDG]) buildingpay
      ,sum([PAYCONT]) contentspay
      ,sum([PAYICC]) iicpay
  FROM [NFIP_Flood_DB].[dbo].[Claims_CLSMY_to2014]
  group by [YEAR],[FIPS],left([FLOODZONE],1)
--  order by [YEAR],[FIPS]
  ) a
  group by fips,fldzone
  order by fips,fldzone
  ```
