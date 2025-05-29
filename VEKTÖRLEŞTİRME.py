
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
complaint_vecs = vectorizer.fit_transform(df["Complaint_Clean"])
prescription_vecs = vectorizer.transform(df["Prescription_Clean"])