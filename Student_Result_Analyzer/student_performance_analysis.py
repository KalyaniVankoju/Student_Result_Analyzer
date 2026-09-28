import pandas as pd
from pathlib import Path

charts_folder = Path(__file__).resolve().parent / "charts"
charts_folder.mkdir(exist_ok=True)

# ============================================================
# 1. LOAD AND INSPECT DATA
# ============================================================

df = pd.read_csv("student_performance.csv")

subjects = ["Math", "Science", "English", "Computer"]

print("Data Preview:")
print(df.head())

print("\nData Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nStudents by Branch:")
print(df["Branch"].value_counts())


# ============================================================
# 2. CREATE DERIVED COLUMNS
# ============================================================

df["Total_Marks"] = (
    df["Math"]
    + df["Science"]
    + df["English"]
    + df["Computer"]
)

df["Average_Marks"] = df["Total_Marks"] / 4


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 35:
        return "D"
    else:
        return "F"


df["Grade"] = df["Average_Marks"].apply(assign_grade)


df["Result"] = (
    (df["Average_Marks"] >= 35)
    & (df[subjects].min(axis=1) >= 35)
).map({
    True: "Pass",
    False: "Fail"
})


def assign_performance_level(average):
    if average >= 75:
        return "High"
    elif average >= 60:
        return "Moderate"
    else:
        return "Needs Attention"


df["Performance_Level"] = (
    df["Average_Marks"].apply(assign_performance_level)
)


# ============================================================
# 3. CLASS-LEVEL ANALYSIS
# ============================================================

subject_averages = df[subjects].mean()

highest_subject = subject_averages.idxmax()
lowest_subject = subject_averages.idxmin()

performance_counts = (
    df["Performance_Level"].value_counts()
)

largest_group = performance_counts.idxmax()
largest_count = performance_counts.max()

performance_percentages = (
    performance_counts / len(df)
) * 100

subject_std = df[subjects].std()

most_variable_subject = subject_std.idxmax()


# ============================================================
# 4. STUDENT-LEVEL ANALYSIS
# ============================================================

top_students = (
    df.sort_values(
        "Average_Marks",
        ascending=False
    )
    .head(5)
)

students_needing_attention = (
    df[df["Performance_Level"] == "Needs Attention"]
    .sort_values("Average_Marks")
)


# ============================================================
# 5. BRANCH ANALYSIS
# ============================================================

branch_performance = (
    df.groupby("Branch")["Average_Marks"]
    .mean()
    .sort_values(ascending=False)
)


# ============================================================
# 6. RELATIONSHIP ANALYSIS
# ============================================================

attendance_correlation = (
    df["Attendance"]
    .corr(df["Average_Marks"])
)

study_correlation = (
    df["Study_Hours"]
    .corr(df["Average_Marks"])
)


# ============================================================
# 7. KEY FINDINGS
# ============================================================

print("\n" + "=" * 60)
print("                 KEY FINDINGS")
print("=" * 60)

print(
    f"\nStrongest Subject : "
    f"{highest_subject} ({subject_averages.max():.2f})"
)

print(
    f"Weakest Subject   : "
    f"{lowest_subject} ({subject_averages.min():.2f})"
)

print(
    f"Most Variable Subject : "
    f"{most_variable_subject} ({subject_std.max():.2f})"
)

print(
    f"\nLargest Performance Group : "
    f"{largest_group} ({largest_count} students)"
)

print("\nPerformance Distribution:")
print(performance_counts)

print("\nPerformance Percentages:")
print(performance_percentages.round(2))

print(
    f"\nAttendance vs Marks Correlation : "
    f"{attendance_correlation:.2f}"
)

print(
    f"Study Hours vs Marks Correlation : "
    f"{study_correlation:.2f}"
)


# ============================================================
# 8. TOP 5 STUDENTS
# ============================================================

print("\n" + "=" * 60)
print("                    TOP 5 STUDENTS")
print("=" * 60)

print(
    top_students[
        [
            "Student_ID",
            "Branch",
            "Average_Marks",
            "Grade",
            "Attendance",
            "Study_Hours"
        ]
    ]
)


# ============================================================
# 9. STUDENTS NEEDING ATTENTION
# ============================================================

print("\n" + "=" * 60)
print("              STUDENTS NEEDING ATTENTION")
print("=" * 60)

print(
    students_needing_attention[
        [
            "Student_ID",
            "Branch",
            "Average_Marks",
            "Attendance",
            "Study_Hours"
        ]
    ]
)


# ============================================================
# 10. BRANCH PERFORMANCE
# ============================================================

print("\n" + "=" * 60)
print("                 BRANCH PERFORMANCE")
print("=" * 60)

print(branch_performance)

# ============================================================
# 7. VISUALIZATION
# ============================================================

import matplotlib.pyplot as plt


# ============================================================
# Figure 1: Average Marks by Subject
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    subject_averages.index,
    subject_averages.values
)

plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.savefig(
    charts_folder / "Figure_1.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================================
# Figure 2: Grade Distribution
# ============================================================

grade_counts = df["Grade"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

plt.bar(
    grade_counts.index,
    grade_counts.values
)

plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig(
    charts_folder / "Figure_2.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()