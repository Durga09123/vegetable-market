from flask import Flask, render_template, request
from model import predict_price
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    predictions = []
    vegetable = ""

    if request.method == "POST":

        # Get selected vegetable safely
        vegetable = request.form.get("vegetable", "").strip()

        # Predict only when vegetable is selected
        if vegetable:

            today = datetime.now()

            # Predict next 7 days
            for i in range(1, 8):

                future_date = today + timedelta(days=i)

                price = predict_price(
                    vegetable,
                    future_date
                )

                predictions.append({
                    "date": future_date.strftime("%d-%m-%Y"),
                    "price": price
                })

    return render_template(
        "index.html",
        predictions=predictions,
        vegetable=vegetable
    )


if __name__ == "__main__":
    app.run(debug=True)