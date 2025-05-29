
from sklearn.metrics.pairwise import cosine_similarity

df["Similarity_Score"] = [
    cosine_similarity(complaint_vecs[i], prescription_vecs[i])[0][0]
    for i in range(len(df))
]