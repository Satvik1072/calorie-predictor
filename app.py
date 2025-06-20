import gradio as gr
import numpy as np
import pickle
from fpdf import FPDF
import datetime

# Load model
model = pickle.load(open("calorie_model.pkl", "rb"))

# Prediction function
def predict_calories(gender, age, height, weight, duration, heart_rate, body_temp):
    gender_encoded = 0 if gender.lower() == "male" else 1
    input_data = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)[0]

    # Generate PDF report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Mishraji ka Calorie Burnt Predictor", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Gender: {gender}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age} years", ln=True)
    pdf.cell(200, 10, txt=f"Height: {height} cm", ln=True)
    pdf.cell(200, 10, txt=f"Weight: {weight} kg", ln=True)
    pdf.cell(200, 10, txt=f"Duration: {duration} min", ln=True)
    pdf.cell(200, 10, txt=f"Heart Rate: {heart_rate} bpm", ln=True)
    pdf.cell(200, 10, txt=f"Body Temp: {body_temp} °C", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", size=14, style="B")
    pdf.set_text_color(220, 50, 50)
    pdf.cell(200, 10, txt=f"Calories Burnt: {prediction:.2f} kcal", ln=True)

    filename = "calorie_report.pdf"
    pdf.output(filename)

    return f"🔥 You burnt approximately: {prediction:.2f} kcal", filename

custom_css = """
body {
    background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
    font-family: 'Segoe UI', sans-serif;
    color: #003366;
    text-align: center;
    margin: 0;
    padding: 0;
}

h1, h2 {
    color: #0d47a1;
}

.gr-button {
    background-color: #00bcd4 !important;
    color: white !important;
    font-weight: bold;
    border-radius: 10px;
    width: 200px;
    margin: auto;
}

.gr-input, .gr-box {
    border-radius: 10px;
}

.gr-row {
    justify-content: center;
}
"""

# Build interface
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("## 🔥 <center>Mishraji ka Calorie Burnt Predictor</center>")
    gr.Markdown("<center>Estimate your burnt calories based on your workout and vitals.</center>")

    with gr.Row():
        gender = gr.Radio(["Male", "Female"], label="Gender")
        age = gr.Number(label="Age (years)")
        height = gr.Number(label="Height (cm)")
        weight = gr.Number(label="Weight (kg)")

    with gr.Row():
        duration = gr.Number(label="Exercise Duration (min)")
        heart_rate = gr.Number(label="Heart Rate (bpm)")
        body_temp = gr.Number(label="Body Temp (°C)")

    submit_btn = gr.Button("🔥 Predict")
    output = gr.Textbox(label="Calories Burnt", lines=1)
    download = gr.File(label="Download Report")

    submit_btn.click(fn=predict_calories,
                     inputs=[gender, age, height, weight, duration, heart_rate, body_temp],
                     outputs=[output, download])

demo.launch(share=True)
