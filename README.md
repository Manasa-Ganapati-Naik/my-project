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




