from sklearn.base import ClassifierMixin
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

class ModelTrainer:
    """
    Trains and saves machine learning models.
    """
    def __init__(self, model_type: str = "LogisticRegression"):
        """
        Initialize ModelTrainer with a model type.
        Args:
            model_type (str): Type of model to train ('LogisticRegression' or 'RandomForest').
        """
        self.model = None
        self.model_type = model_type

    def train_model(self, X_train, y_train):
        """
        Initializes and trains the specified ML model.
        Args:
            X_train: Training features.
            y_train: Training labels.
        """
        print(f"Training {self.model_type} model...")
        if self.model_type == "LogisticRegression":
            self.model = LogisticRegression(max_iter=200)
        elif self.model_type == "RandomForest":
            self.model = RandomForestClassifier()
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")
        self.model.fit(X_train, y_train)
        print("Model training complete.")

    def save_model(self, path: str):
        """
        Saves the trained model to a file.
        Args:
            path (str): File path to save the model.
        """
        if self.model is None:
            raise ValueError("No model trained to save.")
        joblib.dump(self.model, path)
        print(f"Model saved to {path}.")

    def get_model(self) -> ClassifierMixin:
        """
        Returns the trained model.
        Returns:
            ClassifierMixin: The trained model instance.
        """
        return self.model