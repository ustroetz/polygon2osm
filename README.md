# polygon2osm
Converts a [polygon filter](http://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format) to a GeoJSON file.

Setup virtual environment
```
make setup-env
```

Install requirements
```
make bootstrap
```

Download a polygon filter from [Geofabrik](http://download.geofabrik.de/)
```
wget http://download.geofabrik.de/europe/italy.poly
```

Convert it to GeoJSON
```
python polygon2geojson.py italy.poly
```
