# Machine Learning

## Problem Statement
Design and build an AI-powered system that can automatically generate draft legal filings — such as motions, petitions, complaints, or affidavits — using structured case metadata.

## Dataset Description
- Original Dataset:
  - File: `C:\Users\manas\Downloads\convertcsv.csv`
  - Source: https://case.law/caselaw/?reporter=f-supp-3d&volume=392
  - Contains metadata like `name`, `docket_number`, and other case details

- Cleaned Dataset (used for training):
  - File: `cleaned_legal_metadata.csv`
  - Cleaned by removing missing/invalid records, normalizing text fields, and deriving the target variable (`case_type`)
 

### Features:
- Logistic Regression with TF-IDF
- Random Forest Classifier
- Deep Learning with:
  - Simple RNN
  - LSTM (Long Short-Term Memory)
- Side-by-side model performance comparison
- Graphical accuracy visualization


### Model Overview:
| Model               | Technique        | Accuracy (Sample) |
|---------------------|------------------|-------------------|
| Logistic Regression | TF-IDF + Linear  | 67%               |
| Random Forest       | TF-IDF + Tree    | 78%               |
| Simple RNN          | DL Sequential    | 67%               |
| LSTM                | DL Sequential    | 67%               |


### Fine Tuning
- Logistic Regression with TF-IDF
  - GridSearchCV for hyperparameter tuning
  - multiple C values and solvers (liblinear, lbfgs)
- Random Forest Classifier
  - RandomizedSearchCV, which is faster and ideal when trying multiple parameters.
  - Cross-validation (cv=5) and F1 macro for balanced evaluation
- Deep Learning with:
  - Simple RNN
    - Increase embedding dimension from 64 to 128 
    - Added dropout to reduce overfitting and after the embedding
    - Increase RNN units from 64 to 128 — more capacity.
    - Increase batch size
- LSTM (Long Short-Term Memory)
    - Embedding(128) and LSTM(128) layers for better representation.
    - Dropout(0.3) added to reduce overfitting.
    - EarlyStopping to avoid training too long.
    - Increased max_words, max_len, and batch_size for better performance.


### Model Overview:(After Tuning)
| Model               | Technique        | Accuracy (Sample) |
|---------------------|------------------|-------------------|
| Logistic Regression | TF-IDF + Linear  | 72%               |
| Random Forest       | TF-IDF + Tree    | 72%               |
| Simple RNN          | DL Sequential    | 67%               |
| LSTM                | DL Sequential    | 67%               |




