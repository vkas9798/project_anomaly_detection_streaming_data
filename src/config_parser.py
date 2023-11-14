import configparser
from src.logger import initialize_logger

# Initialize logger
logger = initialize_logger()

def parse_config(config_file):

    """
    Parse the configuration file containing parameters for the anomaly detection system.

    Parameters:
    - config_file: Path to the configuration file.

    Returns:
    - Tuple containing window size, contamination rate, and data path parsed from the configuration file.
    """

    logger.info(f"Parsing configuration from {config_file}.")

    config = configparser.ConfigParser()
    config.read(config_file)

    # Fetch parameters
    anomaly_detection_params = config['AnomalyDetection']
    num_samples = int(anomaly_detection_params.get('num_samples'))
    window_size = int(anomaly_detection_params.get('window_size'))
    contamination_rate = float(anomaly_detection_params.get('contamination_rate'))

    logger.info("Configuration parsed successfully.")

    return num_samples, window_size, contamination_rate
