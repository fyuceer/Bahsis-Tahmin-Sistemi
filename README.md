# 💰 Bahşiş Tahmin Sistemi

Python ve makine öğrenmesi kullanılarak geliştirilen bu proje, restoran hesap bilgileri üzerinden **bahşiş miktarını analiz etmeyi ve tahmin etmeyi** amaçlamaktadır.

Proje kapsamında veri seti üzerinde keşifsel veri analizi gerçekleştirilmiş, farklı regresyon modelleri eğitilmiş ve modeller performans metrikleri kullanılarak karşılaştırılmıştır.

## Proje Özellikleri

- Veri setinin temel istatistiksel analizi
- Toplam hesap ve bahşiş arasındaki ilişkinin incelenmesi
- Masa kişi sayısı ile bahşiş arasındaki ilişkinin incelenmesi
- Günlere göre ortalama bahşiş analizi
- Öğle ve akşam öğünlerinin karşılaştırılması
- Kategorik değişkenlerin sayısallaştırılması
- Birden fazla makine öğrenmesi modelinin karşılaştırılması
- Bahşiş miktarı tahmini
- MAE, RMSE ve R² metrikleri ile model değerlendirmesi
- ±1 dolar tolerans içerisinde kalan tahminlerin oranının hesaplanması

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Veri Seti

Projede restoran müşterilerine ait aşağıdaki bilgileri içeren `tips.csv` veri seti kullanılmaktadır:

| Değişken | Açıklama |
|---|---|
| `total_bill` | Toplam hesap tutarı |
| `sex` | Müşterinin cinsiyeti |
| `smoker` | Sigara kullanımı |
| `day` | Haftanın günü |
| `time` | Öğün türü |
| `size` | Masadaki kişi sayısı |
| `tip` | Bahşiş miktarı |

`tip` değişkeni modelin tahmin etmeye çalıştığı **hedef değişkendir**.

## Proje Yapısı

```text
Bahsis-Tahmin-Sistemi/
│
├── analysis.py
├── model_comparison.py
├── tips_prediction.py
├── tips.csv
├── requirements.txt
├── .gitignore
└── README.md
```
### `analysis.py`

Veri setinin keşifsel analizini gerçekleştirir.

- Veri setinin gözlem ve sütun sayısını gösterir.
- İstatistiksel özet oluşturur.
- Toplam hesap ile bahşiş arasındaki ilişkiyi görselleştirir.
- Kişi sayısı ile bahşiş arasındaki ilişkiyi inceler.
- Günlere göre ortalama bahşiş miktarını gösterir.
- Öğle ve akşam öğünlerini karşılaştırır.

### `model_comparison.py`

Farklı regresyon algoritmalarını kullanarak modelleri karşılaştırır.

**Projede kullanılan modeller:**

- Linear Regression
- Random Forest Regressor
- HistGradientBoosting Regressor

Modeller aynı eğitim/test ayrımı üzerinden değerlendirilir.

**Kullanılan performans metrikleri:**

- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**
- **R² (R-squared)**

Modeller R² değerlerine göre sıralanarak en başarılı model belirlenir.

### `tips_prediction.py`

Bahşiş tahmini için `HistGradientBoostingRegressor` modeli kullanılır.

Model, aşağıdaki özellikleri kullanarak `tip` değerini tahmin eder:

```text
total_bill
sex
smoker
day
time
size
```
## Model Değerlendirmesi

Projede modeller aşağıdaki metrikler kullanılarak değerlendirilmiştir:

### MAE

Tahminlerin gerçek değerlerden ortalama ne kadar saptığını gösterir.

**Düşük MAE daha iyi performans anlamına gelir.**

### RMSE

Tahmin hatalarını kareleri üzerinden değerlendirir ve büyük hataları daha fazla cezalandırır.

**Düşük RMSE daha iyi performans anlamına gelir.**

### R²

Modelin hedef değişkendeki değişimin ne kadarını açıklayabildiğini gösterir.

**Yüksek R² daha iyi performans anlamına gelir.**

### ±$1 Tolerans

Tahmin edilen bahşiş ile gerçek bahşiş arasındaki farkın 1 dolar veya daha az olduğu tahminlerin yüzdesi hesaplanmaktadır.

Bu metrik, modelin pratik tahmin başarısını değerlendirmek amacıyla kullanılmaktadır.

## Örnek Çıktı

Model karşılaştırması sonucunda terminal üzerinde aşağıdaki yapıya benzer bir sonuç elde edilir:

```text
======================================================================
MODEL KARŞILAŞTIRMASI
======================================================================

Model                    MAE      RMSE      R²
HistGradientBoosting     ...      ...       ...
Random Forest            ...      ...       ...
Linear Regression        ...      ...       ...

======================================================================
EN BAŞARILI MODEL
======================================================================

Model : ...
MAE   : ...
RMSE  : ...
R²    : ...
```

## Proje Akışı

Proje kapsamında aşağıdaki makine öğrenmesi süreci uygulanmıştır:

**Veri → Veri Analizi → Görselleştirme → Model Eğitimi → Model Karşılaştırması → Tahmin → Performans Değerlendirmesi**

## Geliştirme Alanları

Projenin ilerleyen aşamalarında aşağıdaki geliştirmeler yapılabilir:

- Daha fazla regresyon modeli eklenmesi
- Hiperparametre optimizasyonu yapılması
- Çapraz doğrulama uygulanması
- Tahmin sonuçlarının grafiklerle gösterilmesi
- Kullanıcının kendi restoran bilgilerini girerek tahmin alabileceği bir yapı oluşturulması

## Geliştirici
**FeyzaSultanYüceer**
