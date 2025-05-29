
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.barplot(x=df.index, y=df["Similarity_Score"], hue=df["Tutarlılık"])
plt.title("Reçete-Şikayet Benzerlik Skoru")
plt.xlabel("Kayıt Numarası")
plt.ylabel("Benzerlik Skoru")
plt.tight_layout()
plt.show()