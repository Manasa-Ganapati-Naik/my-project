# my-project

## Dataset Description
The dataset consists of 200+ synthetic and/or real legal case metadata entries intended for automating the generation of legal filings. It includes both structured and unstructured data for tasks like classification and text generation.

### Key Columns:
- `Jurisdiction`: The legal authority (e.g., California, NY).
- `Court`: Specific court handling the case (e.g., LA Superior Court).
- `Case_Type`: Type of case (e.g., Unlawful Detainer, Civil, Criminal).
- `Filing_Type`: Motion, Petition, etc.
- `Summary_of_Facts`: Brief unstructured summary of the legal issue.
- `Generated_Filing_Text`: Ground truth or expected output legal draft (if supervised).
- `Plaintiff`, `Defendant`: Party details.

### Source:
This dataset is synthetically generated using a legal case template generator based on California court standards. No real client data is used.

### Use in This Project:
- Used to train classification models (Random Forest, LSTM, CNN) to predict case types based on fact summaries.
- Used to fine-tune and evaluate a T5 transformer model for drafting legal motions.




