# 🎓 Student Result Analyzer using NumPy

A beginner-friendly Python project that analyzes student marks using **NumPy**. This project demonstrates how NumPy can be used for statistical analysis, filtering, sorting, ranking, and grading of student performance.

---

## 📌 Features

- Generate random marks for students
- Calculate:
  - Total Marks
  - Average Marks
  - Highest Marks
  - Lowest Marks
  - Median
  - Standard Deviation
  - Variance
- Performance Analysis
  - Students scoring 90+
  - Students scoring 75–89
  - Students scoring 60–74
  - Students scoring 35–59
  - Students scoring below 35
- Pass / Fail Analysis
  - Number of students passed
  - Number of students failed
  - Pass percentage
  - Fail percentage
  - Distinction count
- Display Top 5 and Bottom 5 performers
- Find Unique Marks
- Grade Distribution

---

## 🛠 Technologies Used

- Python 3
- NumPy

---

## 📂 Project Structure

```
Student_Result_Analyzer/
│
├── student_result_analyzer.py
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Student_Result_Analyzer.git
```

Go to the project directory

```bash
cd Student_Result_Analyzer
```

Install the required package

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python student_result_analyzer.py
```

---

## 📊 Sample Output

```
========== BASIC STATISTICS ==========

Total Marks : 1685
Average Marks : 56.17
Highest Mark : 100
Lowest Mark : 5

========== PASS / FAIL ANALYSIS ==========

Students Passed : 22
Students Failed : 8
Pass Percentage : 73.33%
```

---

## 🔄 Project Workflow

Here is a plain-language walkthrough of what happens from start to finish when you run the program:

1. **Start the program**  
   Running `python student_result_analyzer.py` calls the `main()` function, which acts as the entry point and orchestrates every step below.

2. **Generate student data**  
   `generate_marks()` uses NumPy's random number generator to produce an array of **30 marks**, each between **0 and 100**, simulating a class of students.

3. **Compute basic statistics**  
   `show_statistics()` feeds that marks array into NumPy functions to instantly calculate and display:
   - Total marks, average, highest, lowest, median, standard deviation, and variance.

4. **Analyse performance by band**  
   `performance_analysis()` uses **NumPy boolean masking** to slice the array into five score bands (A → F) and lists which students fall into each band.

5. **Determine pass / fail outcomes**  
   `pass_fail_analysis()` counts how many students passed (≥ 35), failed (< 35), and earned a distinction (≥ 90), then converts the counts to percentages.

6. **Rank students**  
   `show_rankings()` sorts the array with `np.sort()` and `np.argsort()` to identify and print the **top 5** and **bottom 5** performers by mark.

7. **Find unique marks**  
   `unique_marks()` uses `np.unique()` to list every distinct mark that appears in the class, removing duplicates.

8. **Display grade distribution**  
   `grade_distribution()` counts how many students landed in each letter-grade bucket (A, B, C, D, F) and prints a summary table.

9. **Output is printed to the console**  
   All results are displayed in clearly labelled sections directly in the terminal — no files are written and no external database is needed.

```
run script
    │
    ▼
generate_marks()          ← random NumPy array of 30 marks
    │
    ├─► show_statistics()      ← mean, max, min, std, variance …
    ├─► performance_analysis() ← grade bands via boolean masking
    ├─► pass_fail_analysis()   ← pass/fail counts & percentages
    ├─► show_rankings()        ← top 5 / bottom 5 by argsort
    ├─► unique_marks()         ← deduplicated marks via np.unique
    └─► grade_distribution()   ← count per grade bucket
```

---

## 📚 NumPy Concepts Used

- ndarray
- Random Number Generation
- Boolean Masking
- Statistical Functions
- Sorting
- argsort()
- unique()
- count_nonzero()
- Array Indexing
- Filtering

---

## 🎯 Learning Objectives

This project was created to practice:

- NumPy fundamentals
- Statistical analysis
- Boolean indexing
- Array manipulation
- Writing modular Python code using functions

---

## 👨‍💻 Author

**Vankoju Kalyani**

B.Tech Computer Science Engineering

---

## ⭐ Future Improvements

- **Load real data** — read student names, IDs, and marks from a CSV file using Pandas instead of generating random values
- **Multi-subject support** — extend the analyzer to handle marks across several subjects and compute per-subject and overall GPA
- **Visualization** — plot grade distribution histograms and score-vs-rank charts with Matplotlib or Seaborn
- **Export reports** — save the full analysis (statistics, rankings, grade distribution) to a CSV or PDF file
- **Weighted scoring** — allow different subjects to carry different weights when calculating the final aggregate
- **Persistent storage** — store student records in a SQLite database so results can be queried across multiple sessions
- **Interactive CLI with advanced menu-based result analysis** — add a menu-driven interface so the user can choose which analysis to run without editing code
- **Unit tests** — write `pytest` tests for each analysis function to guard against regressions as the project grows

---

## 📜 License

This project is intended for learning and educational purposes.