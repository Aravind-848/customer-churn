import pandas as pd
import numpy as np
np.random.seed(42)
n = 200
data = {
    "tenure": np.random.randint(1, 72, n),
    "MonthlyCharges": np.random.uniform(20, 120, n).round(2),
    "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], n),
    "InternetService": np.random.choice(["DSL", "Fiber optic", "No"], n),
    "PaymentMethod": np.random.choice(
        ["Electronic check", "Mailed check", "Credit card", "Bank transfer"], n
    ),
}
df = pd.DataFrame(data)
df["Churn"] = np.where(
    (df["Contract"] == "Month-to-month") & (df["tenure"] < 12),
    "Yes",
    np.random.choice(["Yes", "No"], n, p=[0.3, 0.7])
)
df.to_csv("telco_churn_sample.csv", index=False)
print("Dataset created successfully!")

