import numpy as np
import csv
import os
import datetime
from src.logger import initialize_logger

# Initialize logger
logger = initialize_logger()

def generate_data(n_samples):

    """
    Generate synthetic data simulating streaming data with anomalies, seasonal variation, and random noise.

    Parameters:
    - n_samples: Number of data points to generate.

    Returns:
    - NumPy array containing the generated synthetic data.
    """

    logger.info(f"Generating synthetic data with {n_samples} samples.")
    normal_data = np.sin(np.linspace(0, 100, num=n_samples)) + np.random.normal(0, 0.3, size=n_samples)
    seasonal_variation = 0.5 * np.sin(0.1 * np.arange(n_samples))  # Seasonal variation
    random_noise = np.random.normal(0, 0.1, size=n_samples)  # Random noise
    anomaly_data = np.random.uniform(low=-3, high=3, size=n_samples // 10)  # Introducing anomalies

    data = np.concatenate([normal_data, seasonal_variation + random_noise, anomaly_data])
    return data.reshape(-1, 1)

def create_results_folder():

    """
    Create a results folder if it doesn't exist to store detected anomalies in CSV format.
    
    Returns:
    - None
    """

    logger.info("Creating results folder.")
    if not os.path.exists('results'):
        os.makedirs('results')

def save_anomalies_to_csv(anomalies, session_num):

    """
    Save detected anomalies to a CSV file with timestamp, data point number, value, and anomaly score.

    Parameters:
    - anomalies: List of detected anomalies (tuple of data point number, value, and anomaly score).
    - session_num: The session number to create the CSV file.

    Returns:
    - None
    """

    logger.info(f"Saving {len(anomalies)} anomalies to CSV for session {session_num}.")
    filename = f"results/session_{session_num}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['DataPointNumber', 'DataPointValue', 'AnomalyScore', 'DateTime'])
        for anomaly in anomalies:
            date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current date and time
            writer.writerow([anomaly[0], anomaly[1], anomaly[2], date_time])
