import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# 1. LOAD CSV FILE
# ----------------------------------------------------
df = pd.read_csv("C:/Users/Admin/PycharmProjects/HYPOTHEIS/dummy_people_data.csv")   # ← change filename if needed

print(df)

# ----------------------------------------------------
# 2. CALCULATE ALL SCORE COLUMNS
# ----------------------------------------------------

# Financial Stress Score (1–10)
df["Financial_Stress_Score"] = (
    ((df["Monthly_Expenses"] + df["Monthly_EMI"]) / (df["Monthly_Salary"] + 1)) * 10
).clip(1, 10).round()

# Work-Life Balance Score (1–10)
df["Work_Life_Balance_Score"] = (
    (df["Sleep_Hours_Per_Day"] / 10 * 5) +
    (df["Exercise_Per_Week"] / 7 * 3) -
    (df["Stress_Level"] / 10 * 2)
).clip(1, 10).round()

# Job Satisfaction Score (1–10)
df["Job_Satisfaction_Score"] = (
    0.4 * (df["Monthly_Salary"] / 100000 * 10) +
    0.3 * df["Work_Life_Balance_Score"] +
    0.3 * np.random.randint(4, 10, len(df))
).clip(1, 10).round()

# Physical Health Score (1–10)
df["Physical_Health_Score"] = (
    0.4 * (df["Sleep_Hours_Per_Day"] / 10 * 10) +
    0.5 * (df["Exercise_Per_Week"] / 7 * 10) -
    0.1 * (df["Age"] / 70 * 10)
).clip(1, 10).round()

# Mental Health Score (1–10)
df["Mental_Health_Score"] = (
    0.5 * (10 - df["Stress_Level"]) +
    0.3 * df["Friends_Support_Score"] +
    0.2 * df["Family_Support_Score"]
).clip(1, 10).round()

# Happiness Score
df["Happiness_Score"] = (
    0.25 * (10 - df["Financial_Stress_Score"]) +
    0.25 * df["Mental_Health_Score"] +
    0.25 * df["Job_Satisfaction_Score"] +
    0.25 * df["Work_Life_Balance_Score"]
).clip(1, 10).round()

# Is Happy (Yes or No)
df["Is_Happy"] = df["Happiness_Score"].apply(lambda x: "Yes" if x >= 6 else "No")

# ----------------------------------------------------
# 3. SAVE UPDATED DATA
# ----------------------------------------------------
df.to_csv("updated_dummy_people_data.csv", index=False)
print("Updated CSV saved!")

# ----------------------------------------------------
# 4. GRAPH PLOTTING
# ----------------------------------------------------

# Graph 1: Financial Stress Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Financial_Stress_Score"], bins=10)
plt.title("Financial Stress Score Distribution")
plt.xlabel("Score")
plt.ylabel("Count")
plt.show()

# Graph 2: Happiness Score Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Happiness_Score"], bins=10)
plt.title("Happiness Score Distribution")
plt.xlabel("Happiness Score")
plt.ylabel("Count")
plt.show()

# Graph 3: Salary vs Happiness
plt.figure(figsize=(8,5))
plt.scatter(df["Monthly_Salary"], df["Happiness_Score"])
plt.title("Salary vs Happiness Score")
plt.xlabel("Monthly Salary")
plt.ylabel("Happiness Score")
plt.show()

# Graph 4: Work-Life Balance vs Stress Level
plt.figure(figsize=(8,5))
plt.scatter(df["Work_Life_Balance_Score"], df["Stress_Level"])
plt.title("Work-Life Balance vs Stress")
plt.xlabel("Work-Life Balance Score")
plt.ylabel("Stress Level")
plt.show()

# Graph 5: Physical vs Mental Health
plt.figure(figsize=(8,5))
plt.scatter(df["Physical_Health_Score"], df["Mental_Health_Score"])
plt.title("Physical vs Mental Health")
plt.xlabel("Physical Health Score")
plt.ylabel("Mental Health Score")
plt.show()

print("All graphs generated!")
