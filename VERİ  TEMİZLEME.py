
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # sadece harf ve boşluk bırak
    text = re.sub(r"\s+", " ", text)  # fazla boşlukları sil
    return text.strip()

df["Complaint_Clean"] = df["Patient Complaint"].apply(clean_text)
df["Prescription_Clean"] = df["Medical Prescription"].apply(clean_text)