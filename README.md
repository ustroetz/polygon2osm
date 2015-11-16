# polygon2osm
Converts a polygon filter to a GeoJSON

Converts a [polygon filter](http://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format) to a GeoJSON file.

Download a polygon filter from Geofabrik
```
wget http://download.geofabrik.de/europe/italy.poly
```

Convert it to GeoJSON
```
python polygon2geojson.py italy.poly
```