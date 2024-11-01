#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:07:59 2024

@author: sofaisma
"""

import pandas as pd
import numpy as np
from scipy.stats import shapiro, f_oneway


file_path = 'Trial 1.xlsx'  
data = pd.read_excel(file_path, None)


predator_df = data['Predator']

#Assign data 
control_pre = predator_df['Control: Pre-predator']
control_post = predator_df['Control: Post-predator']
treatment_24h_pre = predator_df[['24HD1: Pre-predator', '24HD2: Pre-predator']].values.flatten()
treatment_24h_post = predator_df[['24HD1: Post-predator', '24HD2: Post-predator']].values.flatten()
treatment_48h_pre = predator_df[['48HD1: Pre-predator', '48HD2: Pre-predator']].values.flatten()
treatment_48h_post = predator_df[['48HD1: Post-predator', '48HD2: Post-predator']].values.flatten()


control_diff = control_post - control_pre
treatment_24h_diff = treatment_24h_post - treatment_24h_pre
treatment_48h_diff = treatment_48h_post - treatment_48h_pre

#  Shapiro-Wilk test
normality_results = {
    "Control Pre": shapiro(control_pre),
    "Control Post": shapiro(control_post),
    "24H Pre": shapiro(treatment_24h_pre),
    "24H Post": shapiro(treatment_24h_post),
    "48H Pre": shapiro(treatment_48h_pre),
    "48H Post": shapiro(treatment_48h_post)
}

# ANOVA for pre-predator velocities for the baseline analysis 
anova_pre = f_oneway(control_pre, treatment_24h_pre, treatment_48h_pre)

# ANOVA for post-predator velocities to ensure difference in obtained data
anova_post = f_oneway(control_post, treatment_24h_post, treatment_48h_post)

#  ANOVA for velocity difference  to understand response impact
anova_diff = f_oneway(control_diff, treatment_24h_diff, treatment_48h_diff)

#  Pairwise ANOVA tests:
# 24-hour treatment vs control
anova_24h_vs_control_pre = f_oneway(control_pre, treatment_24h_pre)
anova_24h_vs_control_post = f_oneway(control_post, treatment_24h_post)
anova_24h_vs_control_diff = f_oneway(control_diff, treatment_24h_diff)

# 48-hour treatment vs control
anova_48h_vs_control_pre = f_oneway(control_pre, treatment_48h_pre)
anova_48h_vs_control_post = f_oneway(control_post, treatment_48h_post)
anova_48h_vs_control_diff = f_oneway(control_diff, treatment_48h_diff)

# Compile pairwise results
pairwise_anova_results = {
    "24H vs Control Pre-Predator": anova_24h_vs_control_pre,
    "24H vs Control Post-Predator": anova_24h_vs_control_post,
    "24H vs Control Velocity Difference": anova_24h_vs_control_diff,
    "48H vs Control Pre-Predator": anova_48h_vs_control_pre,
    "48H vs Control Post-Predator": anova_48h_vs_control_post,
    "48H vs Control Velocity Difference": anova_48h_vs_control_diff
}

# Print the output
print("Normality Results:", normality_results)
print("\nOverall ANOVA Results:")
print("Pre-Predator Velocities:", anova_pre)
print("Post-Predator Velocities:", anova_post)
print("Velocity Difference (Post - Pre):", anova_diff)
print("\nPairwise ANOVA Results (24H and 48H vs Control):", pairwise_anova_results)
