
def interpret_score(score):
    if score > 0.7:
        return "Yüksek tutarlılık"
    elif score > 0.4:
        return "Orta seviye tutarlılık"
    else:
        return "Düşük tutarlılık"

df["Tutarlılık"] = df["Similarity_Score"].apply(interpret_score)