from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the input values from the form
    fo = float(request.form["fo"])
    fhi = float(request.form["fhi"])
    flo = float(request.form["flo"])
    jitterPercent = float(request.form["jitterPercent"])
    jitterAbs = float(request.form["jitterAbs"])
    rap = float(request.form["rap"])
    ppq = float(request.form["ppq"])
    jitterDDP = float(request.form["jitterDDP"])
    shimmer = float(request.form["shimmer"])
    shimmerDB = float(request.form["shimmerDB"])
    apq3 = float(request.form["apq3"])
    apq5 = float(request.form["apq5"])
    apq = float(request.form["apq"])
    shimmerDDA = float(request.form["shimmerDDA"])
    nhr = float(request.form["nhr"])
    hnr = float(request.form["hnr"])
    rpde = float(request.form["rpde"])
    dfa = float(request.form["dfa"])
    spread1 = float(request.form["spread1"])
    spread2 = float(request.form["spread2"])
    d2 = float(request.form["d2"])
    ppe = float(request.form["ppe"])

    # Create a feature vector from the input values
    features = [fo, fhi, flo, jitterPercent, jitterAbs, rap, ppq, jitterDDP, shimmer, shimmerDB, apq3, apq5, apq, shimmerDDA, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]

    # Perform the prediction
    prediction = model.predict([features])[0]
    form_data = request.form.to_dict()
    if prediction == 1:
        result = 'Positive'
    else:
        result = 'Negative'

    # Return the prediction result to the user
    return render_template("result.html", prediction=result, data = form_data)

if __name__ == "__main__":
    app.run(debug=True)
