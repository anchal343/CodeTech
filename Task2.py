def calculate_letter_grade(average):
    if average >= 90:
        return 'A', 4.0
    elif average >= 80:
        return 'B', 3.0
    elif average >= 70:
        return 'C', 2.0
    elif average >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def main():
    print("Welcome to the student grade tracker!")

    grades = []
    while True:
        try:
            grade_input = input("Enter a grade (or -1 to finish): ")
            grade = float(grade_input)
            if grade == -1:
                break
            elif grade < 0 or grade > 100:
                print("Invalid grade. Please enter a grade between 0 and 100.")
            else:
                grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if not grades:
        print("No grades entered. Exiting program.")
        return

    average_grade = sum(grades) / len(grades)
    letter_grade, gpa = calculate_letter_grade(average_grade)

    print("\nGrade Summary:")
    print(f"Grades entered: {grades}")
    print(f"Average grade: {average_grade:.2f}")
    print(f"Letter grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
