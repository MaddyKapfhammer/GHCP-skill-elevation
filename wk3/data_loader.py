import pandas as pd

class DataLoader:
    """
    Loads datasets from various sources (currently supports CSV).
    """
    def __init__(self, file_path: str):
        """
        Initialize DataLoader with the path to the data file.
        Args:
            file_path (str): Path to the CSV file.
        """
        self.file_path = file_path

    def load_csv(self) -> pd.DataFrame:
        """
        Loads a CSV file into a pandas DataFrame.
        Returns:
            pd.DataFrame: Loaded data.
        """
        try:
            df = pd.read_csv(self.file_path)
            # Log the shape of the loaded data
            print(f"Loaded data with shape: {df.shape}")
            return df
        except Exception as e:
            print(f"Error loading CSV: {e}")
            raise