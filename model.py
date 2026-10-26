import pandas as pd
from sklearn.ensemble import RandomForestRegressor


# Load dataset
data = pd.read_csv("dataset.csv")

# Convert date
data["Date"] = pd.to_datetime(data["Date"])

# Create useful features
data["Day"] = data["Date"].dt.day
data["Month"] = data["Date"].dt.month
data["Year"] = data["Date"].dt.year

# Convert vegetable names to numbers
data["Vegetable_Code"] = data["Vegetable"].astype("category").cat.codes

# Features and target
X = data[
    [
        "Day",
        "Month",
        "Year",
        "Vegetable_Code"
    ]
]

y = data["Price"]

# Create Machine Learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X, y)


def predict_price(vegetable, date):
    """
    Predict vegetable price for a given date.
    """

    date = pd.to_datetime(date)

    # Get vegetable code
    vegetable_codes = dict(
        zip(
            data["Vegetable"],
            data["Vegetable_Code"]
        )
    )

    if vegetable not in vegetable_codes:
        return None

    vegetable_code = vegetable_codes[vegetable]

    # Prepare input
    input_data = pd.DataFrame(
        [[
            date.day,
            date.month,
            date.year,
            vegetable_code
        ]],
        columns=[
            "Day",
            "Month",
            "Year",
            "Vegetable_Code"
        ]
    )

    # Prediction
    prediction = model.predict(input_data)

    return round(float(prediction[0]), 2)