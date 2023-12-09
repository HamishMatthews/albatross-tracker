# Albatross Tracking Data - ETL and Visualization

Fisheries New Zealand and the Department of Conservation have conducted tracking of various albatross species since January 2019. They have tracked 75 Antipodean and Gibson's wandering albatross, and 14 Salvin's albatross, with data starting from October 2018.

## Data Source
Daily locational data from GPS and Argos transmitters were collected and uploaded to a series of dedicated satellites, before being downloaded to a wildlife tracking service in France. You can access the dataset [here](https://catalogue.data.govt.nz/dataset/albatross-tracking-data).

## Tools and Technologies Used
This repository contains Python scripts and uses several technologies and libraries for data extraction, transformation, loading (ETL), and visualization, including:
- Python
- Geopandas
- Postgres
- SQLAlchemy
- QGIS
- CV2 (OpenCV)

## Visualizing the Flight Paths
The main purpose of this project is to generate a temporal animation that shows the flight paths of the 88 tracked albatross birds. You can watch the animated flight paths in the following YouTube video:

[![Embedding a YouTube Video](https://img.youtube.com/vi/OBuCILn5W2c/0.jpg)](https://www.youtube.com/watch?v=OBuCILn5W2c)

<sup>Video: Animated Flight Paths of 88 Albatross Birds</sup>

To replicate the analysis or visualize the data on your own, you can follow the provided notebook.
