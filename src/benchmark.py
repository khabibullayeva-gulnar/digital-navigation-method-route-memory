
import pandas as pd
import yaml

# Load configuration
with open("configs/config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Load sample data
data_path = config["data"]["sample_path"]
df = pd.read_csv(data_path)

# Metrics
primary_metric = config["metrics"]["primary"]
secondary_metric = config["metrics"]["secondary"]

# Calculate average results for each group
results = df.groupby("group")[
    [primary_metric, secondary_metric]
].mean()

print("Digital Navigation Route Memory Benchmark")
print("-----------------------------------------")
print(results)

# Save results
results.to_csv("benchmark_results.csv")

print("\nResults saved to benchmark_results.csv")
