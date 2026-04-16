# 🧠 Diabetes Prediction System (Machine Learning Project)

A full-stack Machine Learning project that predicts the risk of diabetes using a Support Vector Machine (SVM) model.
The system takes user health inputs and provides a real-time prediction through a web interface.

---

## 🚀 Features

* 🔬 Machine Learning model using **SVM**
* 🧹 Data preprocessing (handling missing values & scaling)
* 📊 Model evaluation (accuracy, confusion matrix, classification report)
* 💾 Model saving using `.pkl` files
* 🌐 Flask backend API for predictions
* 💻 Interactive and modern web UI
* ⚡ Real-time prediction from user input

---

## 🧠 How It Works

1. User enters health data in the web interface
2. Data is sent to the Flask backend
3. Backend:

   * Loads trained model
   * Scales input data
   * Predicts diabetes risk
4. Result is returned and displayed on the UI

---

## 🛠️ Tech Stack

* **Python**
* **Scikit-learn**
* **Flask**
* **NumPy & Pandas**
* **HTML / CSS / JavaScript**

---

## 📁 Project Structure

```
diabetes-project/
│
├── app.py                     # Flask backend
├── main.py                    # Model training script
├── diabetes_model.pkl         # Trained ML model
├── scaler.pkl                 # Data scaler
├── diabetes_predictor.html    # Frontend UI
├── diabetes.csv               # Dataset
├── README.md                  # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/diabetes-prediction-ml.git
cd diabetes-prediction-ml
```

---

### 2. Install dependencies

```
pip install flask scikit-learn joblib numpy pandas
```

---

### 3. Run the application

```
python app.py
```

---

### 4. Open in browser

```
http://localhost:5000
```

---

## 📊 Model Details

* Algorithm: **Support Vector Machine (SVM)**
* Kernel used: `linear` / `rbf` (tested both)
* Accuracy: ~75%
* Evaluation Metrics:

  * Precision
  * Recall
  * F1-score
  * Confusion Matrix

---

## 📥 Input Features

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

## 📤 Output

* **0 → No Diabetes (Lower Risk)**
* **1 → Diabetes (Higher Risk)**
* Optional: Probability score

---

## ⚠️ Disclaimer

This project is for educational purposes only.
It is not intended for real medical diagnosis. Always consult a healthcare professional.

---

## 🙌 Author

**Aditya Ashok Shelke**

---

## ⭐ Future Improvements

* Add probability visualization
* Improve model accuracy
* Deploy project online
* Add user authentication
* Store prediction history

---

## 🌟 If you like this project

Give it a ⭐ on GitHub!
