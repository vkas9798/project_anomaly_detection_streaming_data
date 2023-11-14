import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from river.drift import ADWIN

from src.utils import create_results_folder, save_anomalies_to_csv
from src.logger import initialize_logger

# Initialize logger
logger = initialize_logger()

class IsolationForestAnomalyDetection:
    def __init__(self, window_size, contamination):

        """
        Initialize Isolation Forest Anomaly Detection object.

        Parameters:
        - window_size: Size of the sliding window for processing.
        - contamination: Expected percentage of anomalies in the data.

        Returns:
        - None
        """

        self.window_size = window_size
        self.contamination = contamination
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.session_num = 1
        self.anomalies = []  # List to store anomalies
        self.plot = None
        self.adwin = ADWIN()

        # Initialize logger in the class
        self.logger = logger  # Use the initialized logger

        self.logger.info("Isolation Forest Anomaly Detection object initialized.")

    def rolling_window(self, data):

        """
        Generate a rolling window over the streaming data.

        Parameters:
        - data: The streaming data to create a rolling window from.

        Yields:
        - Tuple containing index and a sliding window of data for anomaly detection.
        """

        for i in range(len(data) - self.window_size + 1):
            yield i, data[i:i+self.window_size]

    def visualize(self, data_stream):

        """
        Perform anomaly detection visualization on the given data stream.

        Parameters:
        - data_stream: The streaming data for anomaly detection.

        Returns:
        - None
        """
        
        self.plot = plt.figure(figsize=(10, 6))
        plt.ion()  # Turn on interactive mode

        for i, window_data in self.rolling_window(data_stream):
            if len(window_data) < self.window_size or not plt.fignum_exists(self.plot.number):
                break

            try:
                self.logger.info("Performing anomaly detection visualization.")
                self.model.fit(window_data)
                anomaly_scores = self.model.decision_function(window_data)
                anomaly_labels = self.model.predict(window_data)

                anomalies = np.where(anomaly_labels == -1)[0]
                if anomalies.any():
                    self.anomalies.extend([(anomaly + i * self.window_size, window_data[anomaly][0], -anomaly_scores[anomaly]) for anomaly in anomalies])
                    print(f"Total anomalies found so far: {len(self.anomalies)}")

                if self.adwin.update(len(anomalies)):  # Check for concept drift based on number of anomalies detected
                    self.logger.info("Concept drift detected - updating model")
                    print("Concept drift detected - updating model")
                    self.model = IsolationForest(contamination=self.contamination, random_state=42)  # Update the model

                plt.clf()
                plt.plot(range((i + 1) * self.window_size - self.window_size, (i + 1) * self.window_size),
                         window_data[-self.window_size:], color='blue')
                plt.scatter(range((i + 1) * self.window_size - self.window_size, (i + 1) * self.window_size),
                            window_data[-self.window_size:], c=-anomaly_scores[-self.window_size:], cmap='coolwarm', marker='o')
                plt.title('Simulated Data Stream with Anomaly Detection')
                plt.xlabel('Index')
                plt.ylabel('Value')
                plt.ylim(-4, 4)
                plt.colorbar(label='Anomaly Score')
                plt.tight_layout()
                plt.pause(0.1)

            except Exception as e:
                self.logger.error(f"Error occurred: {e}", exc_info=True)
                
        
        plt.ioff()  # Turn off interactive mode
        plt.show(block=True)  # Blocking show to keep the window open until manually closed

        # Save anomalies to CSV at the end of visualization
        create_results_folder()
        save_anomalies_to_csv(self.anomalies,self.session_num)
        self.session_num += 1  # Prepare for the next session
