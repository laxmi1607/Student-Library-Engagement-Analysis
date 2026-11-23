# Student Library Engagement and Academic Performance
# Fundamentals of Data Science Project
# Run in IDLE using Run > Run Module (F5)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load dataset
data = pd.read_excel("cleaned_student_library_dataset.xlsx", sheet_name="Cleaned_Data")

print("FIRST 5 ROWS")
print(data.head())
print("\nNumber of rows and columns:", data.shape)

# 2. Check the data
print("\nMISSING VALUES")
print(data.isnull().sum())
print("Duplicate rows:", data.duplicated().sum())

# 3. Basic statistics
print("\nSUMMARY STATISTICS")
print(data.describe())

print("\nBASIC RESULTS")
print("Average library visits per week:", round(data["Library_Visits_Per_Week"].mean()))
print("Mean exam score:", round(data["Exam_Score"].mean(), 2))
print("Median exam score:", data["Exam_Score"].median())
print("Mode exam score:", data["Exam_Score"].mode().tolist())
print("Standard deviation of exam score:", round(data["Exam_Score"].std(), 2))

# 4. Outlier checking using IQR for Exam Score
q1 = data["Exam_Score"].quantile(0.25)
q3 = data["Exam_Score"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = data[(data["Exam_Score"] < lower) | (data["Exam_Score"] > upper)]

print("\nOUTLIER CHECK")
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower limit:", lower)
print("Upper limit:", upper)
print("Number of Exam Score outliers:", len(outliers))

# 5. Simple probability
p_digital = (data["Digital_Resources"] == "Yes").sum() / len(data)
print("\nPROBABILITY")
print("Probability that a student uses digital resources:", round(p_digital, 2))

# 6. Histogram
plt.hist(data["Exam_Score"], bins=10, edgecolor="black")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.title("Exam Score Distribution")
plt.show()

# 7. Bar chart
data["Department"].value_counts().plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.title("Students by Department")
plt.tight_layout()
plt.show()

# 8. Scatter plot
plt.scatter(data["Average_Study_Hours"], data["Exam_Score"])
plt.xlabel("Average Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.show()

# 9. Correlation and covariance
correlation = data["Average_Study_Hours"].corr(data["Exam_Score"])
covariance = data["Average_Study_Hours"].cov(data["Exam_Score"])
print("\nRELATIONSHIP BETWEEN STUDY HOURS AND EXAM SCORE")
print("Correlation:", round(correlation, 3))
print("Covariance:", round(covariance, 3))

# 10. Sample and population mean
sample = data["Exam_Score"].head(10)
population_mean = data["Exam_Score"].mean()
sample_mean = sample.mean()
print("\nSAMPLE AND POPULATION")
print("Population mean:", round(population_mean, 2))
print("Sample mean (first 10 students):", round(sample_mean, 2))

# 11. Simple manual t-test calculation
# Comparing exam scores of digital resource users and non-users
yes = data[data["Digital_Resources"] == "Yes"]["Exam_Score"]
no = data[data["Digital_Resources"] == "No"]["Exam_Score"]

mean1 = yes.mean()
mean2 = no.mean()
var1 = yes.var()
var2 = no.var()
n1 = len(yes)
n2 = len(no)

t_value = (mean1 - mean2) / np.sqrt((var1 / n1) + (var2 / n2))

print("\nMANUAL T-TEST")
print("Mean score of digital resource users:", round(mean1, 2))
print("Mean score of non-users:", round(mean2, 2))
print("Calculated t-value:", round(t_value, 3))
print("This t-value shows the difference between the two group means in standard-error units.")

# 12. Encoding
# Yes = 1 and No = 0
data["Digital_Resources_Code"] = data["Digital_Resources"].map({"Yes": 1, "No": 0})
print("\nENCODING")
print(data[["Digital_Resources", "Digital_Resources_Code"]].head())

# 13. Min-Max scaling
minimum = data["Average_Study_Hours"].min()
maximum = data["Average_Study_Hours"].max()
data["Study_Hours_Scaled"] = (data["Average_Study_Hours"] - minimum) / (maximum - minimum)
print("\nMIN-MAX SCALING")
print(data[["Average_Study_Hours", "Study_Hours_Scaled"]].head())

# 14. Simple linear regression using formula
x = data["Average_Study_Hours"]
y = data["Exam_Score"]

x_mean = x.mean()
y_mean = y.mean()

numerator = ((x - x_mean) * (y - y_mean)).sum()
denominator = ((x - x_mean) ** 2).sum()

slope = numerator / denominator
intercept = y_mean - slope * x_mean

data["Predicted_Exam_Score"] = intercept + slope * x

print("\nSIMPLE LINEAR REGRESSION")
print("Slope:", round(slope, 3))
print("Intercept:", round(intercept, 3))
print("Equation: Exam Score =", round(intercept, 2), "+", round(slope, 2), "x Study Hours")

# Mean Absolute Error calculated manually
mae = abs(y - data["Predicted_Exam_Score"]).mean()
print("Mean Absolute Error:", round(mae, 2))

# Regression graph
plt.scatter(x, y, label="Actual Data")
plt.plot(x, data["Predicted_Exam_Score"], label="Regression Line")
plt.xlabel("Average Study Hours")
plt.ylabel("Exam Score")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()

print("\nPROJECT ANALYSIS COMPLETED")
