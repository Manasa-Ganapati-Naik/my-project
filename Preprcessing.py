import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = r"C:\Users\manas\OneDrive\Documents\Legal ML.xlsx"
df= pd.read_excel(file)

# Fill or drop missing
df.dropna(subset=["Generated_Filing_Text"], inplace=True)

# Label encoding for classification (optional)
from sklearn.preprocessing import LabelEncoder
df["Case_Type_Encoded"] = LabelEncoder().fit_transform(df["Case_Type"])

# Check for class balance
import matplotlib.pyplot as plt

# Plot the class distribution
df["Case_Type"].value_counts().plot(kind="bar")

# Improve readability
plt.title("Distribution of Case Types")
plt.xlabel("Case Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig("case_type_distribution.png")
plt.show()