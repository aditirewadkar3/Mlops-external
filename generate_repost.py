import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset
import os

reference_data = pd.read_csv("reference.csv")

current_data = pd.read_csv("data/addition_data.csv")

report = Report([
    DataDriftPreset()
])

result = report.run(
    current_data,
    reference_data
)

os.makedirs("reports", exist_ok=True)

result.save_html("reports/drift_report.html")

print("Evidently report generated successfully!")