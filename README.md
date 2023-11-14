# Isolation Forest Anomaly Detection with Concept Drift Handling

Author: Vikas Kumar Sharma (22RJ60R01, IIT Kharagpur)

This project showcases anomaly detection using the Isolation Forest algorithm along with handling concept drift in a streaming data scenario.

## Overview

The project demonstrates a Python-based anomaly detection system using Isolation Forest, capable of detecting anomalies in streaming data. It employs the `river` library for concept drift detection and adaptation.

## Features

- Anomaly detection using Isolation Forest.
- Concept drift handling with the `river` library.
- Visualization of anomalies in a streaming data scenario.

## Installation

1. Clone the repository:

git clone https://github.com/vkas9798/project_anomaly_detection_streaming_data.git


2. Install the required dependencies:

pip install -r requirements.txt


## Usage

Run the main script `main.py` to start the anomaly detection visualization:


## Folder Structure

- **src/**: Contains Python source code.
- **data/**: Directory for storing data files.
- **results/**: Directory to save detected anomalies CSV files.
- **requirements.txt**: File listing required Python packages.

## Code Documentation

The project code includes the following main files:

- `anomaly_detection.py`: Contains the `IsolationForestAnomalyDetection` class for anomaly detection with concept drift handling.
- `utils.py`: Utility functions for generating data, handling folders, and saving anomalies to CSV.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the Apache License.
