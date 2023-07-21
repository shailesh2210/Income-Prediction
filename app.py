from flask import Flask , render_template , request 
from src.pipeline.predict_pipeline import PredictPipeline , CustomData

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            age = int(request.form.get("age")),
            workclass = int(request.form.get("workclass")),
            education_num = int(request.form.get("education_num")),
            marital_status = int(request.form.get("marital_status")),
            occupation = int(request.form.get("occupation")),
            relationship = int(request.form.get("relationship")),
            race = int(request.form.get("race")),
            sex = int(request.form.get("sex")),
            capital_gain = int(request.form.get("capital_gain")),
            capital_loss = int(request.form.get("capital_loss")),
            hours_per_week = int(request.form.get("hours_per_week")),
            native_country = int(request.form.get("native_country"))
        )
        
        final_data = data.get_data_as_df()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)

        result = pred

        if result == 0:
            return render_template("predict.html", final_result = "Your Yearly income is less than 50k or equall to 50k")
        
        else:
            return render_template("predict.html", final_result = "Your yearly Income is More than 50k ")

if __name__ == "__main__":
    app.run(host ="0.0.0.0",port=5000, debug=True)