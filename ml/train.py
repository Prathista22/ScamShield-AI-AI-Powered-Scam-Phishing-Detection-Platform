"""
Train the ScamShield AI text classifier.

    python train.py

Loads data/sample_dataset.csv, cleans the text, vectorizes it with TF-IDF,
trains a Logistic Regression classifier, prints evaluation metrics, and
saves the fitted vectorizer + model to disk.

NOTE: sample_dataset.csv is a small starter set (~20 rows) meant to prove
the pipeline runs end-to-end. Replace it with a much larger labeled dataset
(see the blueprint's "Dataset Requirements" section) before final submission
— accuracy on this tiny sample is not meaningful on its own.
"""
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
)

from preprocess import clean_text

DATA_PATH = "data/sample_dataset.csv"


def main():
    df = pd.read_csv(DATA_PATH)
    df["clean_text"] = df["text"].apply(clean_text)

    # Small demo datasets can have too few examples per class to stratify —
    # fall back to a plain split if that happens.
    try:
        X_train, X_test, y_train, y_test = train_test_split(
            df["clean_text"], df["label"], test_size=0.3, random_state=42,
            stratify=df["label"],
        )
    except ValueError:
        X_train, X_test, y_train, y_test = train_test_split(
            df["clean_text"], df["label"], test_size=0.3, random_state=42,
        )

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=3000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)

    print("=== Evaluation ===")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.3f}")
    print(f"Precision: {precision_score(y_test, y_pred, average='macro', zero_division=0):.3f}")
    print(f"Recall   : {recall_score(y_test, y_pred, average='macro', zero_division=0):.3f}")
    print(f"F1-score : {f1_score(y_test, y_pred, average='macro', zero_division=0):.3f}")
    print("\nConfusion matrix:")
    print(confusion_matrix(y_test, y_pred, labels=model.classes_))
    print("\nPer-class report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    joblib.dump(vectorizer, "vectorizer.pkl")
    joblib.dump(model, "model.pkl")
    print("\nSaved vectorizer.pkl and model.pkl")


if __name__ == "__main__":
    main()
