from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

class ModelEvaluator:
    """
    Evaluates trained models and generates reports.
    """
    def __init__(self, model, X_test, y_test):
        """
        Initialize ModelEvaluator with model and test data.
        Args:
            model: Trained model.
            X_test: Test features.
            y_test: Test labels.
        """
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.y_pred = None

    def predict(self):
        """
        Generates predictions on the test set.
        """
        print("Generating predictions...")
        self.y_pred = self.model.predict(self.X_test)

    def evaluate_metrics(self) -> dict:
        """
        Calculates and returns common classification metrics.
        Returns:
            dict: Dictionary of metrics.
        """
        if self.y_pred is None:
            self.predict()
        metrics = {
            "accuracy": accuracy_score(self.y_test, self.y_pred),
            "precision": precision_score(self.y_test, self.y_pred, average="weighted", zero_division=0),
            "recall": recall_score(self.y_test, self.y_pred, average="weighted", zero_division=0),
            "f1": f1_score(self.y_test, self.y_pred, average="weighted", zero_division=0),
        }
        print(f"Evaluation metrics: {metrics}")
        return metrics

    def generate_report_pdf(self, output_path: str = "evaluation_report.pdf"):
        """
        Generates a comprehensive PDF evaluation report.
        Args:
            output_path (str): Path to save the PDF report.
        """
        if self.y_pred is None:
            self.predict()
        # Generate classification report and confusion matrix
        report = classification_report(self.y_test, self.y_pred)
        cm = confusion_matrix(self.y_test, self.y_pred)
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.title("Confusion Matrix")
        plt.ylabel("True Label")
        plt.xlabel("Predicted Label")
        plt.tight_layout()
        plt.savefig("confusion_matrix.png")
        plt.close()
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Model Evaluation Report", ln=True, align="C")
        pdf.multi_cell(0, 10, txt=report)
        pdf.image("confusion_matrix.png", x=10, y=60, w=100)
        pdf.output(output_path)
        print(f"PDF report saved to {output_path}.")