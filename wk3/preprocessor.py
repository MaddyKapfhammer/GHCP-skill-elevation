import pandas as pd
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    """
    Handles data cleaning, feature engineering, and splitting.
    """
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a DataFrame.
        Args:
            df (pd.DataFrame): Raw data.
        """
        self.df = df

    def clean(self) -> pd.DataFrame:
        """
        Cleans the data (e.g., fills missing values).
        Returns:
            pd.DataFrame: Cleaned data.
        """
        # Example: fill numeric NaNs with mean
        df_clean = self.df.copy()
        for col in df_clean.select_dtypes(include='number').columns:
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)
        print("Filled missing numeric values with column means.")
        return df_clean

    def split(self, target: str, test_size: float = 0.2, random_state: int = 42):
        """
        Splits the data into train/test sets.
        Args:
            target (str): Name of the target column.
            test_size (float): Fraction for test set.
            random_state (int): Random seed.
        Returns:
            X_train, X_test, y_train, y_test
        """
        X = self.df.drop(columns=[target])
        y = self.df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        print(f"Split data: {X_train.shape[0]} train, {X_test.shape[0]} test samples.")
        return X_train, X_test, y_train, y_test