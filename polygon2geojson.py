#!/usr/bin/python
import re
import argparse
import os
import fiona
from shapely.geometry import Polygon, mapping


def remove_file(file_name):
    try:
        os.remove(file_name)
    except OSError:
        pass


def read_polygon(polygon_filename):
    with open(polygon_filename) as f:
        return f.readlines()


def clean_poylgon(polygon_data):
    coordinates = polygon_data[2:][:-2]
    coordinates = [re.split(r'[\s\t]+', item) for item in coordinates]
    coordinates = [list(filter(None, item)) for item in coordinates]
    coordinates = [(float(item[0]), float(item[1])) for item in coordinates]

    return coordinates


def write_geojson(data, polygon_filename):
    geojson_filename = polygon_filename.split('.')[0] + ".geojson"
    remove_file(geojson_filename)

    schema = {'geometry': 'Polygon', 'properties': {}}

    with fiona.open(geojson_filename, 'w', 'GeoJSON', schema) as output:
        output.write({'geometry': mapping(Polygon(data)), 'properties': {}})


def main(polygon_filename):
    polygon_data = read_polygon(polygon_filename)
    coordinates = clean_poylgon(polygon_data)
    write_geojson(coordinates, polygon_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("polygon_filename")
    args = parser.parse_args()

    main(args.polygon_filename)
