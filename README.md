# Student Performance Data Analysis

A Python-based data analysis project that analyzes student academic performance, identifies performance patterns, studies relationships between academic and behavioral factors, and generates visual insights.

The project uses a simulated dataset of 150 students across four branches: CSE, ECE, IT, and MECH.

---

## Project Overview

Academic performance can be studied using multiple factors such as subject marks, attendance, and study habits.

This project analyzes student performance data to answer questions such as:

- Which subject has the highest and lowest average performance?
- How are students distributed across different performance levels?
- Which students may require additional academic attention?
- Which subject shows the greatest variation in marks?
- How does attendance relate to academic performance?
- How do study hours relate to academic performance?
- How does average performance differ across branches?

The project generates visualizations and exports the processed dataset with additional analytical columns.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV

---

## Project Structure

```text
Student_Result_Analyzer/
│
├── data_generator.py
├── student_performance_analysis.py
├── student_performance.csv
├── student_performance_results.csv
├── report.md
├── requirements.txt
├── README.md
│
└── charts/
    ├── Figure_1.png
    ├── Figure_2.png
    ├── Figure_3.png
    ├── Figure_4.png
    ├── Figure_5.png
    └── Figure_6.png
```

---

## Dataset

The project uses a simulated dataset containing **150 students**.

The dataset is generated using `data_generator.py`, which creates student performance data using randomized values and relationships between academic and behavioral factors.

### Dataset Columns

| Column | Description |
|---|---|
| `Student_ID` | Unique identifier for each student |
| `Branch` | Student's academic branch |
| `Math` | Mathematics marks |
| `Science` | Science marks |
| `English` | English marks |
| `Computer` | Computer subject marks |
| `Attendance` | Attendance percentage |
| `Study_Hours` | Average study hours per day |

### Branches

The dataset contains students from four branches:

- CSE
- ECE
- IT
- MECH

### Dataset Generation

The dataset can be generated automatically using:

```bash
python data_generator.py
```

This creates:

```text
student_performance.csv
```

---

## Analysis Performed

### 1. Data Inspection

The project performs:

- Dataset preview
- Dataset shape analysis
- Statistical summary
- Missing-value detection
- Duplicate detection
- Branch-wise student count

### 2. Derived Columns

The following analytical columns are created:

- `Total_Marks`
- `Average_Marks`
- `Grade`
- `Result`
- `Performance_Level`

### 3. Student Performance Analysis

The project identifies:

- Top-performing students
- Students requiring additional attention
- Grade distribution
- Performance-level distribution
- Subject-wise averages
- Subject-wise variation

### 4. Branch Analysis

Average student performance is analyzed across:

- CSE
- ECE
- IT
- MECH

### 5. Relationship Analysis

The project calculates the correlation between:

- Attendance and average marks
- Study hours and average marks

---

## Visualizations

The project generates six visualizations using Matplotlib.

### 1. Average Marks by Subject

Compares the average marks across the four subjects.

### 2. Grade Distribution

Shows the number of students belonging to each grade.

### 3. Distribution of Average Marks

Shows how average marks are distributed across students.

### 4. Attendance vs Average Marks

Visualizes the relationship between attendance and academic performance.

### 5. Study Hours vs Average Marks

Visualizes the relationship between study hours and academic performance.

### 6. Average Marks by Branch

Compares average academic performance across the four branches.

All visualizations are saved inside the `charts/` directory.

---

## How to Run

Follow these steps to run the project on a new machine.

### 1. Clone the Repository

```bash
git clone https://github.com/KalyaniVankoju/Student_Result_Analyzer.git
```

Move into the project directory:

```bash
cd Student_Result_Analyzer
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The main dependencies are:

- Pandas
- Matplotlib

### 4. Generate the Dataset

Run:

```bash
python data_generator.py
```

This generates:

```text
student_performance.csv
```

### 5. Run the Analysis

Run:

```bash
python student_performance_analysis.py
```

The program will:

- Load the generated dataset
- Inspect the data
- Create derived columns
- Analyze student performance
- Analyze branch performance
- Calculate correlations
- Display key findings
- Generate six charts
- Export the processed dataset

---

## Generated Outputs

After running the analysis, the following outputs are available.

### Processed Dataset

```text
student_performance_results.csv
```

This file contains the original dataset along with the calculated columns:

- `Total_Marks`
- `Average_Marks`
- `Grade`
- `Result`
- `Performance_Level`

### Charts

Six visualization files are generated inside the `charts/` directory:

```text
charts/
├── Figure_1.png
├── Figure_2.png
├── Figure_3.png
├── Figure_4.png
├── Figure_5.png
└── Figure_6.png
```

### Report

```text
report.md
```

This file contains a concise summary of the major findings from the analysis.

---

## Key Findings

Based on the current simulated dataset:

- Computer had the highest average marks.
- Math had the lowest average marks.
- Needs Attention was the largest performance group with 60 students.
- 35 students were classified as High performers.
- Attendance showed a strong positive relationship with average marks, with a correlation of approximately **0.81**.
- Study hours showed a positive relationship with average marks, with a correlation of approximately **0.59**.
- Average performance varied across the four branches.

> **Note:** These findings are based on the current simulated dataset generated by the project.

---

## Learning Outcomes

Through this project, I practiced:

- Loading CSV data using Pandas
- Inspecting and validating datasets
- Checking for missing values
- Detecting duplicate records
- Creating derived columns
- Applying conditional logic
- Filtering and sorting data
- Grouping and aggregation
- Calculating statistical summaries
- Correlation analysis
- Data visualization using Matplotlib
- Exporting processed datasets
- Writing analytical findings
- Structuring a reproducible Python data-analysis project

---

## Future Improvements

Possible improvements include:

- Interactive dashboards using Plotly or Power BI
- More detailed statistical analysis
- Student performance prediction using Machine Learning
- Early-warning system for students requiring academic support
- Interactive filtering by branch and performance level
- Larger and more realistic datasets
- Additional student-related features

---

## Disclaimer

This project uses a **simulated dataset created for educational and demonstration purposes**.

The relationships and findings in this project should not be interpreted as conclusions about real students or real academic performance.

---

## Author

**Kalyani Vankoju**

Computer Science Engineering