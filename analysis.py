import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "tips.csv"

data = pd.read_csv(DATA_FILE, encoding="Latin1")

data.columns = (
    data.columns
    .str.strip()
    .str.replace("ï»¿", "", regex=False)
)

data["sex"] = data["sex"].map({
    "Female": 0,
    "Male": 1
})

data["smoker"] = data["smoker"].map({
    "No": 0,
    "Yes": 1
})

data["time"] = data["time"].map({
    "Lunch": 0,
    "Dinner": 1
})

print("=" * 60)
print("VERİ SETİ ANALİZİ")
print("=" * 60)

print(f"\nGözlem sayısı : {len(data)}")
print(f"Sütun sayısı  : {len(data.columns)}")

print("\nVeri seti hakkında genel bilgiler:")
print(data.info())

print("\nİstatistiksel özet:")
print(data.describe())

plt.figure(figsize=(8, 5))

plt.scatter(
    data["total_bill"],
    data["tip"],
    alpha=0.7
)

plt.xlabel("Toplam Hesap ($)")
plt.ylabel("Bahşiş ($)")
plt.title("Toplam Hesap ile Bahşiş İlişkisi")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

plt.scatter(
    data["size"],
    data["tip"],
    alpha=0.7
)

plt.xlabel("Masa Kişi Sayısı")
plt.ylabel("Bahşiş ($)")
plt.title("Masa Kişi Sayısı ile Bahşiş İlişkisi")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

day_order = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

data["day"] = pd.Categorical(
    data["day"],
    categories=day_order,
    ordered=True
)

day_tip = data.groupby(
    "day",
    observed=False
)["tip"].mean()

plt.figure(figsize=(8, 5))

day_tip.plot(
    kind="bar"
)

plt.xlabel("Gün")
plt.ylabel("Ortalama Bahşiş ($)")
plt.title("Günlere Göre Ortalama Bahşiş")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()

time_tip = data.groupby("time")["tip"].mean()

time_tip.index = [
    "Öğle",
    "Akşam"
]

plt.figure(figsize=(7, 5))

time_tip.plot(
    kind="bar"
)

plt.xlabel("Öğün")
plt.ylabel("Ortalama Bahşiş ($)")
plt.title("Öğünlere Göre Ortalama Bahşiş")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()

print("\nAnaliz tamamlandı.")