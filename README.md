# Airline Delay Analysis Using Self-Organizing Maps (SOM)

## Overview
This project uses a Self-Organizing Map (SOM) to analyze airline delay data, identifying patterns and trends in flight delays. By examining features such as arrival delay, departure delay, and distance, the SOM helps to highlight clusters of delays and potential anomalies in the data.

## About the Dataset
The dataset contains information related to flight delays and includes the following key features:
- **ARR_DELAY**: Arrival delay of the flight.
- **DEP_DELAY**: Departure delay of the flight.
- **DISTANCE**: The distance between the origin and destination airports.
The dataset consists of 100,000 entries and 3 columns.

## Software and Hardware Requirements
### Software
- Python 3.12.4
- Required libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `minisom`

### Hardware
- Minimum 4GB RAM
- Any modern processor (dual-core or higher)
- Storage space for the dataset (50MB)

## Installation
1. Install Python (if not installed).
2. Install the required packages using pip

## Execution
To run the Self-Organizing Map and analyze the flight delay data:
1. Open a terminal in your project folder.
2. Run the Python script.

## Output
After running the script, a graph visualizing the Self-Organizing Map is displayed, which shows clusters of flight delays and potential anomalies.
(Output graph image has been attached)

## Key Insights
- The SOM map helps identify clusters of flights that have similar delay patterns.
- Darker regions on the map indicate potential anomalies, which may be flights with unusually high delays.




