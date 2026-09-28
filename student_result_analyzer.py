# ============================================================
# Student Result Analyzer using NumPy
# Author      : Vankoju Kalyani
# Description :
# A beginner NumPy project to analyze randomly generated
# student marks and generate useful statistics.
# ============================================================

import numpy as np


# ------------------------------------------------------------
# Generate random marks
# ------------------------------------------------------------
def generate_marks(num_students: int = 30) -> np.ndarray:
    """
    Generates random student marks between 0 and 100.

    Parameters:
        num_students (int): Number of students

    Returns:
        np.ndarray: Array of student marks
    """
    return np.random.randint(0, 101, num_students)


# ------------------------------------------------------------
# Display basic statistics
# ------------------------------------------------------------
def show_statistics(marks: np.ndarray) -> None:

    print("\n========== BASIC STATISTICS ==========\n")

    print("Marks of Students:")
    print(marks)

    print(f"\nTotal Marks           : {np.sum(marks)}")
    print(f"Average Marks         : {np.mean(marks):.2f}")
    print(f"Highest Mark          : {np.max(marks)}")
    print(f"Lowest Mark           : {np.min(marks)}")
    print(f"Median                : {np.median(marks)}")
    print(f"Standard Deviation    : {np.std(marks):.2f}")
    print(f"Variance              : {np.var(marks):.2f}")


# ------------------------------------------------------------
# Analyze student performance
# ------------------------------------------------------------
def performance_analysis(marks: np.ndarray) -> None:

    grade_a = marks[marks >= 90]
    grade_b = marks[(marks >= 75) & (marks <= 89)]
    grade_c = marks[(marks >= 60) & (marks <= 74)]
    grade_d = marks[(marks >= 35) & (marks <= 59)]
    grade_f = marks[marks < 35]

    print("\n========== PERFORMANCE ANALYSIS ==========\n")

    print("Students scoring 90 and above:")
    print(grade_a)
    print("Count :", len(grade_a))

    print("\nStudents scoring between 75 and 89:")
    print(grade_b)
    print("Count :", len(grade_b))

    print("\nStudents scoring between 60 and 74:")
    print(grade_c)
    print("Count :", len(grade_c))

    print("\nStudents scoring between 35 and 59:")
    print(grade_d)
    print("Count :", len(grade_d))

    print("\nStudents scoring below 35:")
    print(grade_f)
    print("Count :", len(grade_f))


# ------------------------------------------------------------
# Display pass/fail statistics
# ------------------------------------------------------------
def pass_fail_analysis(marks: np.ndarray) -> None:

    total_students = len(marks)

    passed = np.count_nonzero(marks >= 35)
    failed = np.count_nonzero(marks < 35)
    distinction = np.count_nonzero(marks >= 90)

    pass_percentage = (passed / total_students) * 100
    fail_percentage = (failed / total_students) * 100

    print("\n========== PASS / FAIL ANALYSIS ==========\n")

    print(f"Students Passed        : {passed}")
    print(f"Students Failed        : {failed}")
    print(f"Students with Distinction : {distinction}")

    print(f"Pass Percentage        : {pass_percentage:.2f}%")
    print(f"Fail Percentage        : {fail_percentage:.2f}%")


# ------------------------------------------------------------
# Display Top and Bottom performers
# ------------------------------------------------------------
def show_rankings(marks: np.ndarray) -> None:

    sorted_marks = np.sort(marks)
    sorted_indices = np.argsort(marks)

    print("\n========== TOP 5 STUDENTS ==========\n")

    for i in range(1, 6):
        print(f"Student {sorted_indices[-i] + 1:2} : {sorted_marks[-i]}")

    print("\n========== BOTTOM 5 STUDENTS ==========\n")

    for i in range(5):
        print(f"Student {sorted_indices[i] + 1:2} : {sorted_marks[i]}")


# ------------------------------------------------------------
# Display unique marks
# ------------------------------------------------------------
def unique_marks(marks: np.ndarray) -> None:

    unique = np.unique(marks)

    print("\n========== UNIQUE MARKS ==========\n")

    print(f"Number of Unique Marks : {len(unique)}")
    print(unique)


# ------------------------------------------------------------
# Display grade distribution
# ------------------------------------------------------------
def grade_distribution(marks: np.ndarray) -> None:

    grade_a = np.count_nonzero(marks >= 90)
    grade_b = np.count_nonzero((marks >= 75) & (marks <= 89))
    grade_c = np.count_nonzero((marks >= 60) & (marks <= 74))
    grade_d = np.count_nonzero((marks >= 35) & (marks <= 59))
    grade_f = np.count_nonzero(marks < 35)

    print("\n========== GRADE DISTRIBUTION ==========\n")

    print(f"Grade A (90-100) : {grade_a}")
    print(f"Grade B (75-89)  : {grade_b}")
    print(f"Grade C (60-74)  : {grade_c}")
    print(f"Grade D (35-59)  : {grade_d}")
    print(f"Grade F (<35)    : {grade_f}")


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
def main() -> None:

    print("=" * 55)
    print("         STUDENT RESULT ANALYZER USING NUMPY")
    print("=" * 55)

    marks = generate_marks()

    show_statistics(marks)
    performance_analysis(marks)
    pass_fail_analysis(marks)
    show_rankings(marks)
    unique_marks(marks)
    grade_distribution(marks)


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()