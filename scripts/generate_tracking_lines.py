# Import necessary QGIS modules
from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsField
from PyQt5.QtCore import QVariant

# Define the input point layer name
input_layer_name = "reprojected"  # Replace with your actual layer name

# Load the input point layer
input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]

# Check if the layer exists
if not input_layer.isValid():
    raise Exception(f"Layer '{input_layer_name}' not found in '{geopackage_path}'!")

# Create a new line layer to store the results
line_layer = QgsVectorLayer("LineString?crs=" + input_layer.crs().authid(), "bird_tracking_lines", "memory")

# Define fields for the line layer
fields = [
    QgsField("Identifier", QVariant.String),
    QgsField("Start_Time", QVariant.DateTime),
    QgsField("End_Time", QVariant.DateTime),
]

line_layer.dataProvider().addAttributes(fields)
line_layer.updateFields()

# Initialize a dictionary to store points for each bird
bird_points = {}

# Loop through features in the input layer
for feature in input_layer.getFeatures():
    bird_id = feature["Identifier"]
    datetime = feature["DateTime"]

    # Check if the bird_id is already in the dictionary
    if bird_id not in bird_points:
        bird_points[bird_id] = {"start_datetime": datetime, "end_datetime": datetime, "points": []}
    else:
        bird_points[bird_id]["end_datetime"] = datetime

    bird_points[bird_id]["points"].append((datetime, feature.geometry().asPoint()))

# Create line segments for each bird's path
lines = []
for bird_id, data in bird_points.items():
    if len(data["points"]) > 1:
        # Sort points by datetime
        sorted_points = sorted(data["points"], key=lambda x: x[0])
        
        # Create line segments
        for i in range(len(sorted_points) - 1):
            start_time = sorted_points[i][0]
            end_time = sorted_points[i+1][0]
            line = QgsGeometry.fromPolyline([QgsPoint(sorted_points[i][1]), QgsPoint(sorted_points[i+1][1])])
            feature = QgsFeature()
            feature.setGeometry(line)
            feature.setAttributes([bird_id, start_time, end_time])
            lines.append(feature)

# Add line features to the line layer
line_layer.dataProvider().addFeatures(lines)

# Add the line layer to the map
QgsProject.instance().addMapLayer(line_layer)

# Refresh the QGIS interface
iface.mapCanvas().refresh()