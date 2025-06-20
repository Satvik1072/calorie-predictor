# 🔥 Calorie Burnt Predictor

A machine learning-powered web app that estimates the number of calories burnt during exercise based on user inputs like age, gender, heart rate, and workout duration.  
Built using **Gradio**, trained with **XGBoost**, and deployed with Hugging Face Spaces.

---

### 🚀 Live Demo  
👉 [Click here to try the app](https://huggingface.co/spaces/WalterCodes/Calorie-burnt-predictor)

---

### 📌 Features
- Predicts calories burnt using physiological and workout data
- Interactive, responsive UI using Gradio + custom CSS
- Generates a downloadable PDF report with user inputs and results
- Deployed and accessible 24/7 via Hugging Face Spaces


🧠 Tech Stack
| Tool            | Purpose                                |
|-----------------|----------------------------------------|
| Python          | Core programming language              |
| Scikit-learn    | Data preprocessing                     |
| XGBoost         | Regression model training              |
| Gradio          | Frontend UI for model interaction      |
| FPDF            | PDF generation for reports             |
| Hugging Face    | Hosting and deployment                 |


🧪 Input Parameters

- Gender (Male/Female)
- Age (in years)
- Height (in cm)
- Weight (in kg)
- Exercise Duration (in minutes)
- Heart Rate (in bpm)
- Body Temperature (in °C)


### ⚙️ How to Run Locally

```bash
git clone https://github.com/yourusername/calorie-burnt-predictor
cd calorie-burnt-predictor
pip install -r requirements.txt
python app.py


