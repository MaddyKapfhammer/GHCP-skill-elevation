import pytest
import pandas as pd
import numpy as np
from data_loader import DataLoader
from preprocessor import DataPreprocessor
from model_trainer import ModelTrainer
from evaluator import ModelEvaluator

@pytest.fixture
def dummy_data_csv(tmp_path):
    """
    Creates a dummy CSV file for testing data loading and preprocessing.
    """
    data = {
        'feature_A': [10, 20, np.nan, 40, 50],
        'feature_B': ['X', 'Y', 'X', 'Z', 'Y'],
        'target': [0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    csv_path = tmp_path / "dummy_data.csv"
    df.to_csv(csv_path, index=False)
    return str(csv_path)

def test_data_loader_load_csv(dummy_data_csv):
    """
    Test that DataLoader loads CSV correctly.
    """
    loader = DataLoader(dummy_data_csv)
    df = loader.load_csv()
    assert not df.empty
    assert 'feature_A' in df.columns

def test_preprocessor_clean_and_split(dummy_data_csv):
    """
    Test DataPreprocessor cleaning and splitting.
    """
    loader = DataLoader(dummy_data_csv)
    df = loader.load_csv()
    pre = DataPreprocessor(df)
    df_clean = pre.clean()
    X_train, X_test, y_train, y_test = pre.split(target='target')
    assert not df_clean.isnull().any().any()
    assert X_train.shape[0] + X_test.shape[0] == df.shape[0]

def test_model_trainer_and_evaluator(dummy_data_csv):
    """
    Test ModelTrainer and ModelEvaluator integration.
    """
    loader = DataLoader(dummy_data_csv)
    df = loader.load_csv()
    pre = DataPreprocessor(df)
    df_clean = pre.clean()
    X_train, X_test, y_train, y_test = pre.split(target='target')
    trainer = ModelTrainer()
    trainer.train_model(X_train, y_train)
    model = trainer.get_model()
    evaluator = ModelEvaluator(model, X_test, y_test)
    evaluator.predict()
    metrics = evaluator.evaluate_metrics()
    assert 'accuracy' in metrics