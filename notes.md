# Notes
Here's just a few command snippits that I am holding onto for reference sake...
## Git
* [Github Cheatsheet](https://github.com/tiimgreen/github-cheat-sheet#readme)
### Git pushes
    git add --all
    git commit -m "new notes and scripts"
    git push -u origin master

### Add a submodule to my github page
    git submodule init
    git submodule update

### Random Webpage shit
@mention a GitHub username to generate a link to their profile

## Random Command Lines


#### csvKit




#### GDAL and OGR
```Shell
gdal_rasterize -3d -a_nodata -9999 -tr 0.00027777778 0.00027777778 -tap -l FP_StLouis FP_StLouis.vrt FP_StLouis.tif

for %f in (*Flow.shp) do shp2pgsql -s 4269 -a -D -t 2d %f public.flowlines | psql -U postgres -d nhd -q

for %X in (*.shp) do ogr2ogr -t_srs EPSG:4269 -s_srs EPSG:4326 C:\01_DATA\01_CompleteHydrologyConUSA\Hydropostgis\wgs\4269\%X %X

for %X in (*.shp) do ogr2ogr -f PostgreSQL PG:"dbname=shapes user='postgres' password='elements'" *.shp
```
#### Bash and Other Shell
[Rename and take out spaces and parathesis](https://unix.stackexchange.com/questions/110213/remove-whitespace-and-parentheses-in-filenames-with-sed)
```Shell
for file in ./*; do mv "$file" "${file/ (*)/}"; done
```

## Python and stuff
* [Awesome list of python links!](http://awesome-python.com/)
### GeoDjango Project Examples
1. [GeoQ](https://github.com/ngageoint/geoq) - Django web application to collect geospatial features and manage feature collection among groups of users

### Interesting Links and Tutorials
1. [Interactive charting with C3 - D3 based reusable code](http://c3js.org/gettingstarted.html)
1. [Rasterio Masks](http://snorf.net/blog/2014/11/09/masking-rasterio-layers-with-vector-features/)
1. [GeoAlchemy2 Documentation](https://geoalchemy-2.readthedocs.org/en/0.2.6/orm_tutorial.html)
1. [SQL Alchemy Awesome List](https://github.com/dahlia/awesome-sqlalchemy#gis-and-spatial-databases)
1. [Creating a GeoDjango app with Leaflet](http://blog.mathieu-leplatre.info/geodjango-maps-with-leaflet.html)
1. [github - CartoDB Tutorial](https://github.com/clhenrick/cartodb-tutorial)
1. [github - GDAL Hillshade Tutorial](https://github.com/clhenrick/gdal_hillshade_tutorial)
1. [github - The art of the command line](https://github.com/jlevy/the-art-of-command-line)
1.
#### Discussions
1. [Streaming NWS Hazard Data](https://github.com/ngageoint/geoq/issues/188)

## PostgreSQL
1. [PostgreSQL Window Tutorial](http://www.postgresql.org/docs/current/static/tutorial-window.html)

#### PostGIS

Code:
[Using window function to get order rank:](https://gis.stackexchange.com/questions/168308/how-to-do-a-spatial-join-in-postgis-that-returns-on-the-minimum-value-of-point-i)
```SQL
SELECT osm_id, gid, dn
FROM   (
         SELECT b.osm_id, p.gid, p.dn,
                row_number() OVER (PARTITION BY osm_id order by dn) as rank
         FROM   buffer b, dem_points p
         WHERE  ST_Within(p.geom, b.geom)
       ) joined
WHERE  rank = 1
```

Links:
* [Geoprocessing with PostGIS - CartoDB pt.1](http://blog.cartodb.com/geoprocessing-in-postgis/)
* [Concave Hull examples](http://www.bostongis.com/postgis_concavehull.snippet)
* [PostGIS workshop from OSGeo](http://revenant.ca/www/postgis/workshop/advanced.html)
* [github - PostgreSQL & PostGIS Cheatsheet](https://gist.github.com/clhenrick/ebc8dc779fb6f5ee6a88)
* [Efficient Spatial Joins with python](https://gis.stackexchange.com/questions/102933/more-efficient-spatial-join-in-python-without-qgis-arcgis-postgis-etc)
* [Intersecting two shapefiles with python](https://gis.stackexchange.com/questions/178765/intersecting-two-shapefiles-from-python-or-command-line?lq=1)

#### psql
List all the tables inside the database
```Shell
psql -U postgres -d shapes -c "\d"
```
General pgsql help stuff
```Shell
\h                 # help on SQL commands
\?                 # help on psql commands, such as \? and \h
\l                 # list databases
\c database_name   # connect to a database
\d                 # list of tables
\d table_name      # schema of a given table
\du                # list roles
\e                 # edit in $EDITOR
```

#### Other General Notes

#### Links and shit
1. [Flood Inundation Mapper](http://water.usgs.gov/osw/flood_inundation/)
1. [Marsh/Torrent NFS competitor - Schinnerer Flood](http://www.schinnerer.com/Content/Industries/Flood/Pages/Landing_Pages/Flood.aspx)


#### Geonode and ROGUE-Geonode
1. [HIU Guide](http://hiu-beta.state.gov/guides/rogue-geonode)


#### PostGIS
1. [Boundless PostGIS Intro](http://workshops.boundlessgeo.com/postgis-intro/)
1. [Good intro to dealing with PostGIS SQL queries](https://www.dataiku.com/learn/guide/other/geo/convert-coordinates-with-PostGIS.html)

## Web APIs

####Snowfall rasters
1. [NOAA/NWS Snowfall rasters](http://www.nohrsc.noaa.gov/snowfall/)


## Examples of Map Dashboards
1. [TIBCO and the CA Drought](https://spotfire.cloud.tibco.com/spotfire/wp/render/22694204537/analysis?file=/users/annamarianow/public/california%20drought&waid=6zaDFLK7QEaq5UbmFzKIe-0716011da9yf5y&wavid=0)

