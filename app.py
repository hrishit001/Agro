from flask import Flask, render_template, request, jsonify, send_from_directory
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os
import io
import base64


app = Flask(__name__)

# Load CSV and model
data = pd.read_csv("crop_data_india_500.csv")
model = joblib.load("crop_prediction_model.joblib")
le_state, le_city = joblib.load("encoders.joblib")

# Get state list
states = sorted(data["State"].unique().tolist())

    
@app.route("/")
def home():
    
    return render_template("index.html", states=states)
    


@app.route("/get_cities/<state>")
def get_cities(state):
    try:
        cities = sorted(data[data["State"] == state]["City"].unique().tolist())
        return jsonify(cities)
    except Exception as e:
        print("Error fetching cities:", e)
        return jsonify([])

@app.route("/predict", methods=["POST"])
def predict():
    try:
        state = request.form["state"]
        city = request.form["city"]
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        rainfall = float(request.form["rainfall"])

        # Encode state and city
        state_encoded = le_state.transform([state])[0]
        city_encoded = le_city.transform([city])[0]


        input_data = [[temperature, humidity, rainfall, state_encoded, city_encoded]]
        predicted_crop = model.predict(input_data)[0]

        # Generate histogram
        plt.figure(figsize=(7, 4))
        feature_importances = model.feature_importances_
        features = ['temperature', 'humidity', 'rainfall', 'State', 'City']
        plt.barh(features, feature_importances, color='forestgreen')
        plt.xlabel("Importance")
        plt.title("Feature Importance in Crop Prediction Model")
        plt.tight_layout()

        # Convert plot to base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        plot_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
        plt.close()

        pdf_filename = f"{predicted_crop.lower()}.pdf"
        pdf_path = os.path.join("Static/pdf", pdf_filename)

        pdf_exists = os.path.exists(pdf_path)
        return render_template(
            "result.html",
            crop=predicted_crop,
            pdf_file=pdf_filename if pdf_exists else None,
            plot_data=plot_data,
            city=city,
            state=state
        )

    except Exception as e:
        print("Error in prediction:", e)
        return f"An error occurred: {e}"

@app.route("/download/<filename>")
def download_pdf(filename):
    return send_from_directory("Static/pdf", filename, as_attachment=True)

@app.route("/crop_distribution_map")
def crop_distribution_map():
    return render_template("crop_map.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))

