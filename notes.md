# Notes
Here's just a few command snippits that I am holding onto for reference sake...
## Git

    git add --all
    git commit -m "new notes and scripts"
    git push -u origin master

## Random Command Lines

    gdal_rasterize -3d -a_nodata -9999 -tr 0.00027777778 0.00027777778 -tap -l FP_StLouis FP_StLouis.vrt FP_StLouis.tif

    for %f in (*Flow.shp) do shp2pgsql -s 4269 -a -D -t 2d %f public.flowlines | psql -U postgres -d nhd -q

    for %X in (*.shp) do ogr2ogr -t_srs EPSG:4269 -s_srs EPSG:4326 C:\01_DATA\01_CompleteHydrologyConUSA\Hydropostgis\wgs\4269\%X %X

    for %X in (*.shp) do ogr2ogr -f PostgreSQL PG:"dbname=shapes user='postgres' password='elements'" *.shp

## Python and stuff

1. [Rasterio Masks](http://snorf.net/blog/2014/11/09/masking-rasterio-layers-with-vector-features/)
1. [GeoAlchemy2 Documentation](https://geoalchemy-2.readthedocs.org/en/0.2.6/orm_tutorial.html)
1. [SQL Alchemy Awesome List](https://github.com/dahlia/awesome-sqlalchemy#gis-and-spatial-databases)

## PostgreSQL

### psql

    psql -U postgres -d shapes -c "\d"

### PostGIS
1. [Boundless PostGIS Intro](http://workshops.boundlessgeo.com/postgis-intro/)

##Web APIs

###Snowfall rasters
1. [NOAA/NWS Snowfall rasters](http://www.nohrsc.noaa.gov/snowfall/)


## Examples of Map Dashboards
1. [TIBCO and the CA Drought](https://spotfire.cloud.tibco.com/spotfire/wp/render/22694204537/analysis?file=/users/annamarianow/public/california%20drought&waid=6zaDFLK7QEaq5UbmFzKIe-0716011da9yf5y&wavid=0)

