import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_FILE = "tips.csv"

data = pd.read_csv(DATA_FILE, encoding="Latin1")

data.columns = (
    data.columns
    .str.strip()
    .str.replace("ï»¿", "", regex=False)
)

categorical_columns = ["sex", "smoker", "day", "time"]

for column in categorical_columns:
    data[column] = data[column].astype(str).str.strip()


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

missing_values = X.isnull().sum()

if missing_values.sum() > 0:

    print("=" * 70)
    print("UYARI: EKSİK DEĞER TESPİT EDİLDİ")
    print("=" * 70)

    print(missing_values[missing_values > 0])

    valid_rows = X.notnull().all(axis=1)

    X = X[valid_rows]
    y = y[valid_rows]

    print(
        f"\nEksik değer içeren {len(data) - len(X)} satır "
        "analizden çıkarıldı."
    )

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

models = {

    "Linear Regression": LinearRegression(),

    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),

    "HistGradientBoosting": HistGradientBoostingRegressor(
        random_state=42
    )
}

results = []

for model_name, model in models.items():

    print(f"\n{model_name} eğitiliyor...")

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        y_pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            y_pred
        )
    )

    r2 = r2_score(
        y_test,
        y_pred
    )

    results.append({
        "Model": model_name,
        "MAE": mae,
        "RMSE": rmse,
        "R²": r2
    })

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="R²",
    ascending=False
)

print("\n" + "=" * 70)
print("MODEL KARŞILAŞTIRMASI")
print("=" * 70)

print(
    results_df.to_string(
        index=False,
        formatters={
            "MAE": "{:.4f}".format,
            "RMSE": "{:.4f}".format,
            "R²": "{:.4f}".format
        }
    )
)

best_model = results_df.iloc[0]

print("\n" + "=" * 70)
print("EN BAŞARILI MODEL")
print("=" * 70)

print(f"Model : {best_model['Model']}")
print(f"MAE   : {best_model['MAE']:.4f}")
print(f"RMSE  : {best_model['RMSE']:.4f}")
print(f"R²    : {best_model['R²']:.4f}")