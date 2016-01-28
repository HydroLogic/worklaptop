# Notes
---
---
---
## Git

    git add --all
    git commit -m "new notes and scripts"
    git push -u origin master

## Random Command Lines
---

    gdal_rasterize -3d -a_nodata -9999 -tr 0.00027777778 0.00027777778 -tap -l FP_StLouis FP_StLouis.vrt FP_StLouis.tif

    for %f in (*Flow.shp) do shp2pgsql -s 4269 -a -D -t 2d %f public.flowlines | psql -U postgres -d nhd -q

    for %X in (*.shp) do ogr2ogr -t_srs EPSG:4269 -s_srs EPSG:4326 C:\01_DATA\01_CompleteHydrologyConUSA\Hydropostgis\wgs\4269\%X %X

    for %X in (*.shp) do ogr2ogr -f PostgreSQL PG:"dbname=shapes user='postgres' password='elements'" *.shp


## psql
---
    psql -U postgres -d shapes -c "\d"


##Web APIs
---
###Snowfall rasters
1. [http://www.nohrsc.noaa.gov/snowfall/](NOAA/NWS Snowfall rasters)


## Examples of Map Dashboards
####[https://spotfire.cloud.tibco.com/spotfire/wp/render/22694204537/analysis?file=/users/annamarianow/public/california%20drought&waid=6zaDFLK7QEaq5UbmFzKIe-0716011da9yf5y&wavid=0](TIBCO and the CA Drought)

