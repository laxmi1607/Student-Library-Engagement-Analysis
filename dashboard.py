import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Library Analytics", layout="wide")
data = pd.read_excel("cleaned_student_library_dataset.xlsx", sheet_name="Cleaned_Data")

st.title("Student Library Engagement and Academic Performance")
st.caption("Fundamentals of Data Science Project")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Students", len(data))
c2.metric("Average Exam Score", f"{data['Exam_Score'].mean():.2f}")
c3.metric("Digital Resource Users", f"{(data['Digital_Resources']=='Yes').mean()*100:.0f}%")
c4.metric("Avg Library Visits/Week", f"{data['Library_Visits_Per_Week'].mean():.0f}")

st.sidebar.header("Filters")
departments = st.sidebar.multiselect("Department", sorted(data["Department"].unique()), default=sorted(data["Department"].unique()))
genders = st.sidebar.multiselect("Gender", sorted(data["Gender"].unique()), default=sorted(data["Gender"].unique()))
filtered = data[data["Department"].isin(departments) & data["Gender"].isin(genders)]

left, right = st.columns(2)
with left:
    st.subheader("Exam Score Distribution")
    fig, ax = plt.subplots()
    ax.hist(filtered["Exam_Score"], bins=10, edgecolor="black")
    ax.set_xlabel("Exam Score")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

with right:
    st.subheader("Study Hours vs Exam Score")
    fig, ax = plt.subplots()
    ax.scatter(filtered["Average_Study_Hours"], filtered["Exam_Score"])
    ax.set_xlabel("Average Study Hours")
    ax.set_ylabel("Exam Score")
    st.pyplot(fig)

st.subheader("Simple Findings")
st.write("Average library visits per week:", round(data["Library_Visits_Per_Week"].mean()))
st.write("Correlation between study hours and exam score:", round(data["Average_Study_Hours"].corr(data["Exam_Score"]), 3))

st.subheader("Simple Exam Score Estimator")
x = data["Average_Study_Hours"]
y = data["Exam_Score"]
x_mean = x.mean()
y_mean = y.mean()
slope = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()
intercept = y_mean - slope * x_mean

hours = st.slider("Average Study Hours", 0.5, 6.0, 3.0, 0.5)
prediction = intercept + slope * hours
st.success(f"Estimated Exam Score: {prediction:.1f}")
st.caption("This is only a simple academic demonstration using a synthetic dataset.")
