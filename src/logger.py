import logging
import os

def initialize_logger():
    """
    Initialize the logger for the anomaly detection system.

    Returns:
    - Logger object
    """
    # Create 'log' directory if it doesn't exist
    log_dir = 'log'
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger('anomaly_detection_logger')
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create a file handler for logging to a file in the 'log' directory
    log_file = os.path.join(log_dir, 'anomaly_detection.log')
    file_handler = logging.FileHandler(log_file)

    # Set the logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger
