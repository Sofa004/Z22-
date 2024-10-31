#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:52:05 2024

@author: sofaisma
"""

# Import required libraries
from scipy.stats import shapiro, f_oneway
import pandas as pd

# Load the Excel data file
file_path = '/mnt/data/Trial 1.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet2')  # Assuming "Sheet2" is the foraging data

# Extract data for each treatment group
control_foraging = data['Control']
treatment_24h_foraging = data[['24HD1', '24HD2']].values.flatten()
treatment_48h_foraging = data[['48HD1', '48HD2']].values.flatten()

# 1. Perform Shapiro-Wilk normality test for each group
normality_results = {
    "Control": shapiro(control_foraging),
    "24H": shapiro(treatment_24h_foraging),
    "48H": shapiro(treatment_48h_foraging),
}

# Display Shapiro-Wilk normality test results
print("Shapiro-Wilk Test Results for Foraging Latency:")
for group, result in normality_results.items():
    print(f"{group}: Statistic={result.statistic:.4f}, p-value={result.pvalue:.4f}")

# Check if all groups meet normality assumptions (p > 0.05 indicates normal distribution)
if all(result.pvalue > 0.05 for result in normality_results.values()):
    print("\nAll groups passed the normality test. Proceeding with ANOVA.")

    # 2. Perform ANOVA to compare foraging latency across groups
    anova_result = f_oneway(control_foraging, treatment_24h_foraging, treatment_48h_foraging)
    print("\nANOVA Test Results for Foraging Latency:")
    print(f"F-statistic={anova_result.statistic:.4f}, p-value={anova_result.pvalue:.4f}")

    # Interpret results
    if anova_result.pvalue < 0.05:
        print("\nConclusion: There is a statistically significant difference in foraging latency among the groups.")
    else:
        print("\nConclusion: No statistically significant difference in foraging latency was found among the groups.")

else:
    print("\nNormality assumption was not met for one or more groups. ANOVA may not be appropriate.")
    print("Consider using a non-parametric test, such as the Kruskal-Wallis test.")


