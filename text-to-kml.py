# Script by Gloria Pappalardo with help from Tammy Woodard. Clark Labs. 2021. Credit to Rene Nyffenegger
# (https://github.com/ReneNyffenegger/about-GoogleEarth/blob/master/kml/elements/Point/inline-Style.kml)
# for KML formatting code.

# input is txt file with 2 points (top left x,y, bottom right x,y) from bounding box created with TerrSet Placemarks

# open txt file as csv
import csv

with open('D:\\Pass\\Gloria\\Python_TXTKML\\orlando_points.txt', 'r') as input_to_csv:
    contents = csv.reader(input_to_csv, delimiter=',')
    # for csv values, read and assign each in turn to a variable (x = longitude, y = latitude, placemark = the
    # name of the study area)
    for value in contents:
        x1 = value[0]
        y1 = value[1]
        x2 = value[2]
        y2 = value[3]
        placemark = value[4]

# box_values concatenates the values into the correct format for the KML file
box_values = x1 + ',' + y1 + ',0,' + x2 + ',' + y1 + ',0,' + x2 + ',' + y2 + ',0,' + x1 + ',' + y2 + ',0,' + x1 + ',' + y1 + ',0'

# data conversion for creation of the center point location for the label
x1float = float(x1)
y1float = float(y1)
x2float = float(x2)
y2float = float(y2)

# polygon_center sets the point for the label
centerx = (x1float + ((x2float - x1float) / 2))
centery = (y2float + ((y1float - y2float) / 2))
polygon_center = str(centerx) + ' ' + str(centery)

# kml_format inputs values into the KML format for the output file
kml_format = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
        	<Placemark>
			<name>{placemark}</name>
			<MultiGeometry>
				<Point>
					<coordinates>{polygon_center}</coordinates>
				</Point>
				<LineString>
					<coordinates>{box_values}</coordinates>
				</LineString>
			</MultiGeometry>
		</Placemark>
</Document>
</kml>
'''

# kml_product is a new file with kml_format written into it
kml_product = open(r'D:\\Pass\\Gloria\\Python_TXTKML\\orlando_points.kml', 'w')
kml_product.write(kml_format)
kml_product.close()
# output is KML with bounding box and a label ready to view in Google Earth
