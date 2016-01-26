
import json

STATEHOOD_TABLE = """State,Date
Delaware,1787-12-07
Pennsylvania,1787-12-12
New Jersey,1787-12-18
Georgia,1788-01-02
Connecticut,1788-01-09
Massachusetts,1788-02-06
Maryland,1788-04-28
South Carolina,1788-05-23
New Hampshire,1788-06-21
Virginia,1788-06-25
New York,1788-07-26
North Carolina,1789-12-21
Rhode Island,1790-05-29
Vermont,1791-03-04
Kentucky,1792-06-01
Tennessee,1796-06-01
Ohio,1803-03-01
Louisiana,1812-04-30
Indiana,1816-12-11
Mississippi,1817-12-10
Illinois,1818-12-03
Alabama,1819-12-14
Maine,1820-03-15
Missouri,1821-08-10
Arkansas,1836-06-15
Michigan,1837-01-26
Florida,1845-03-03
Texas,1845-12-29
Iowa,1846-12-28
Wisconsin,1848-05-29
California,1850-09-09
Minnesota,1858-05-11
Oregon,1859-02-14
Kansas,1861-01-29
West Virginia,1863-06-20
Nevada,1864-10-31
Nebraska,1867-03-01
Colorado,1876-08-01
North Dakota,1889-11-02
South Dakota,1889-11-02
Montana,1889-11-08
Washington,1889-11-11
Idaho,1890-07-03
Wyoming,1890-07-10
Utah,1896-01-04
Oklahoma,1907-11-16
New Mexico,1912-01-06
Arizona,1912-02-14
Alaska,1959-01-03
Hawaii,1959-08-21
"""

statehood = dict(
    [line.split(',') for line in STATEHOOD_TABLE.split("\n")[1:-1]])

ctx = {
  "@context": {
    "Feature": "http://example.com/vocab#Feature",
    "FeatureCollection": "http://example.com/vocab#FeatureCollection",
    "GeometryCollection": "http://example.com/vocab#GeometryCollection",
    "Instant": "http://www.w3.org/2006/time#Instant",
    "Interval": "http://www.w3.org/2006/time#Instant",
    "LineString": "http://example.com/vocab#LineString",
    "MultiLineString": "http://example.com/vocab#MultiLineString",
    "MultiPoint": "http://example.com/vocab#MultiPoint",
    "MultiPolygon": "http://example.com/vocab#MultiPolygon",
    "Point": "http://example.com/vocab#Point",
    "Polygon": "http://example.com/vocab#Polygon",
    "bbox": {
      "@container": "@list",
      "@id": "http://example.com/vocab#bbox"
    },
    "coordinates": {
      "@id": "http://example.com/vocab#coordinates"
    },
    "datetime": "http://www.w3.org/2006/time#inXSDDateTime",
    "description": "http://purl.org/dc/terms/description",
    "earliestStop": "http://example.com/vocab#earliestStop",
    "features": {
      "@container": "@set",
      "@id": "http://example.com/vocab#coordinates"
    },
    "geometry": "http://example.com/vocab#geometry",
    "id": "http://example.com/vocab#id",
    "latestStart": "http://example.com/vocab#latestStart",
    "properties": "http://example.com/vocab#properties",
    "start": "http://www.w3.org/2006/time#hasBeginning",
    "stop": "http://www.w3.org/2006/time#hasEnding",
    "title": "http://purl.org/dc/terms/title",
    "type": "http://example.com/vocab#type",
    "when": "http://example.com/vocab#when"
  }
}

collection = json.load(open('/us.geojson'))

dst_features = []

for feature in collection['features']:
    name = feature['properties']['NAME']
    feature['when'] = {'type': 'Interval', 'start': statehood[name]}

    where = feature['geometry']
    coords = where['coordinates']
    if where['type'] == 'Polygon':
        for j, ring in enumerate(coords):
            for i, point in enumerate(ring):
                coords[j][i] = [round(v, 5) for v in point]
    elif where['type'] == 'MultiPolygon':
        for k, part in enumerate(coords):
            for j, ring in enumerate(part):
                for i, point in enumerate(ring):
                    coords[k][j][i] = [round(v, 5) for v in point]

    dst_features.append(feature)

collection['features'] = dst_features
collection['@context'] = ctx

json.dump(collection, open('us-statehood.geojson', 'w'), indent=2)

