import csv
import random
NUM_STUDENTS = 150
OUTPUT_FILE = "student_performance.csv"

BRANCHES = ["CSE", "ECE", "IT", "MECH"]

COLUMNS = [
    "Student_ID",
    "Branch",
    "Math",
    "Science",
    "English",
    "Computer",
    "Attendance",
    "Study_Hours",
]
def clamp(value, low=0, high=100):
    return max(low, min(high, int(round(value))))
def pick_branch():
    return random.choice(BRANCHES)
def make_one_student(student_number):
    branch = pick_branch()

    ability = random.gauss(60, 15)

    if branch in ("CSE", "IT"):
        computer_bonus = random.uniform(4, 12)
    else:
        computer_bonus = random.uniform(-6, 4)

    math_score = clamp(ability + random.gauss(0, 10))
    science_score = clamp(ability + random.gauss(0, 12))
    english_score = clamp(ability + random.gauss(0, 10))
    computer_score = clamp(
        ability + computer_bonus + random.gauss(0, 10)
    )
    attendance = clamp(
        ability + random.gauss(20, 8),
        low=40,
        high=100
    )

    study_hours = max(
        0,
        round(random.gauss(ability / 12, 1.5), 1)
    )
    student_id = f"S{student_number:04d}"

    return [
        student_id,
        branch,
        math_score,
        science_score,
        english_score,
        computer_score,
        attendance,
        study_hours,
    ]
def build_rows(num_students):
    rows = []

    for i in range(1, num_students + 1):
        rows.append(make_one_student(i))

    return rows
def write_csv(filename, columns, rows):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(columns)
        writer.writerows(rows)
def main():
    rows = build_rows(NUM_STUDENTS)
    write_csv(OUTPUT_FILE, COLUMNS, rows)

    print(f"{OUTPUT_FILE} created successfully!")
    print(f"Students: {len(rows)}")
    print(f"Columns: {len(COLUMNS)}")


if __name__ == "__main__":
    main()