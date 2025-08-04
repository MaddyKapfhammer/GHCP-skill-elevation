from data_loader import DataLoader
from preprocessor import DataPreprocessor
from model_trainer import ModelTrainer
from evaluator import ModelEvaluator
import argparse

def main():
    """
    Main entry point for the end-to-end ML pipeline demo.
    Parses arguments, runs all pipeline steps, and generates reports.
    """
    parser = argparse.ArgumentParser(description="End-to-End ML Pipeline.")
    parser.add_argument("data_path", help="Path to the input dataset (CSV).")
    parser.add_argument("--target", default="target", help="Name of the target column.")
    parser.add_argument("--model", default="LogisticRegression", help="Model type: LogisticRegression or RandomForest.")
    parser.add_argument("--model_out", default="trained_model.joblib", help="Path to save the trained model.")
    parser.add_argument("--report_out", default="evaluation_report.pdf", help="Path to save the evaluation report.")
    args = parser.parse_args()

    print(f"Starting ML pipeline for {args.data_path}...")

    # 1. Load data
    loader = DataLoader(args.data_path)
    df = loader.load_csv()

    # 2. Preprocess data
    preprocessor = DataPreprocessor(df)
    df_clean = preprocessor.clean()
    X_train, X_test, y_train, y_test = preprocessor.split(target=args.target)

    # 3. Train model
    trainer = ModelTrainer(model_type=args.model)
    trainer.train_model(X_train, y_train)
    trainer.save_model(args.model_out)

    # 4. Evaluate model
    evaluator = ModelEvaluator(trainer.get_model(), X_test, y_test)
    evaluator.predict()
    evaluator.evaluate_metrics()
    evaluator.generate_report_pdf(args.report_out)

    print("Pipeline complete.")

if __name__ == "__main__":
    main()