from src.anomaly_detection import IsolationForestAnomalyDetection
from src.utils import generate_data
from src.config_parser import parse_config
from src.logger import initialize_logger

# Initialize logger
logger = initialize_logger()

def main():

    """
    Entry point for the anomaly detection process.

    Initializes the Isolation Forest Anomaly Detection object,
    generates synthetic streaming data, and initiates the visualization of anomalies.

    Returns:
    - None
    """

    try:
        # Parse configuration from config file
        num_samples, window_size, contamination_rate = parse_config('config.ini')

        # Initialize anomaly detection object
        detector = IsolationForestAnomalyDetection(window_size=window_size, contamination=contamination_rate)
        data_stream = generate_data(n_samples=num_samples)
        detector.visualize(data_stream)
        logger.info("Anomaly detection process completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during anomaly detection: {e}", exc_info=True)

if __name__ == "__main__":
    main()
