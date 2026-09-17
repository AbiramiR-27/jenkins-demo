"""
Grade Calculator Application
Calculates student letter grades, averages, and generates grade reports.
"""

def calculate_grade(score):
    """Return the letter grade for a given percentage score."""
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(scores):
    """Calculate the average score of a list of marks."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def generate_report(student_name, subject_scores):
    """Generate and display a student grade report."""
    print("=" * 45)
    print(f" STUDENT GRADE REPORT: {student_name.upper()} ")
    print("=" * 45)

    for subject, score in subject_scores.items():
        grade = calculate_grade(score)
        print(f"  {subject:<18}: {score:>5.1f}%  ->  Grade {grade}")

    avg = calculate_average(list(subject_scores.values()))
    overall_grade = calculate_grade(avg)

    print("-" * 45)
    print(f"  Average Score     : {avg:>5.2f}%")
    print(f"  Overall Grade     : Grade {overall_grade}")
    print("=" * 45)
    return overall_grade


if __name__ == "__main__":
    sample_scores = {
        "Mathematics": 92.5,
        "Science": 88.0,
        "English": 79.5,
        "History": 84.0,
        "Computer Science": 96.0,
    }
    generate_report("Alice Smith", sample_scores)