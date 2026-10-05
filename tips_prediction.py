import numpy as np
import pandas as pd

from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

DATA_FILE = "tips.csv"

data = pd.read_csv(DATA_FILE, encoding="Latin1")

data.columns = (
    data.columns
    .str.strip()
    .str.replace("ï»¿", "", regex=False)
)

print("=" * 60)
print("BAHŞİŞ TAHMİN SİSTEMİ")
print("=" * 60)
print(f"\nVeri setindeki gözlem sayısı: {len(data)}")
print(f"Kullanılan özellikler: {len(data.columns) - 1}")

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

data["day"] = data["day"].map({
    "Sun": 0,
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6
})

features = [
    "total_bill",
    "sex",
    "smoker",
    "day",
    "time",
    "size"
]

X = data[features]
y = data["tip"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

model = HistGradientBoostingRegressor(
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

tolerance = 1.0

correct_predictions = np.abs(y_pred - y_test) <= tolerance

tolerance_accuracy = (
    np.mean(correct_predictions) * 100
)

print("\n" + "=" * 60)
print("MODEL PERFORMANSI")
print("=" * 60)

print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")
print(
    f"±$1 tolerans dahilindeki tahmin oranı: "
    f"{tolerance_accuracy:.2f}%"
)

results = pd.DataFrame({
    "Gerçek Bahşiş": y_test.values,
    "Tahmin Edilen Bahşiş": y_pred
})

results["Tahmin Hatası"] = (
    results["Gerçek Bahşiş"]
    - results["Tahmin Edilen Bahşiş"]
)

print("\n" + "=" * 60)
print("TAHMİN SONUÇLARI")
print("=" * 60)

print(results.head(10).to_string(index=False))