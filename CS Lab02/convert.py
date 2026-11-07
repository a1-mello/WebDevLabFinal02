import pandas as pd
import json

df = pd.read_csv("stations.csv")

data = {
    "chart_title": "Busiest Train Stations in Japan",
    "data_points": df.to_dict("records")
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
