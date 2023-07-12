import StudentDatabase
import ExamDatabase
import time
from colorama import init, Fore

init()  # Initialize colorama

def display_menu():
    print("Menu:")
    print("1. Enter the exam")
    print("2. Check your scores")
    print("3. Check your profile")
    print("4. Exit")

def get_student_info(access_code):
    if access_code in StudentDatabase.students:
        student = StudentDatabase.students[access_code]
        print("Student Information:")
        for char in f"Name: {student['name']}":
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()
        for char in f"Last Name: {student['lastName']}":
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()
        for char in f"Phone: {student['phone']}":
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()
    else:
        print("Student not found in the database.")
        print()

def print_access_granted():
    print(Fore.GREEN + "Access Granted!" + Fore.RESET)

def print_access_denied():
    print(Fore.RED + "Access Denied!" + Fore.RESET)

def evaluate_exam(answers):
    score = 0
    total_questions = len(ExamDatabase.questions)

    for i, question in enumerate(ExamDatabase.questions):
        answer = answers[i]
        correct_answer = ExamDatabase.trueOption[i]

        print(f"Question: {question}")
        print(f"Your answer: {answer}")
        print(f"Correct answer: {correct_answer}\n")

        if answer.lower() == correct_answer.lower():
            score += 1

    percentage = (score / total_questions) * 100
    return score, percentage

def save_exam_result(access_code, score):
    if access_code in ExamDatabase.student_scores:
        ExamDatabase.student_scores[access_code].append(score)
    else:
        ExamDatabase.student_scores[access_code] = [score]

code = input("Enter your access code: ")

if code in StudentDatabase.students:
    print_access_granted()
    get_student_info(code)
else:
    print_access_denied()
    exit()

print()  # Add a line break here

print("Welcome to the Exam System!")

while True:
    display_menu()
    menu = input("Please choose an option: ")

    if menu == "1":
        print("You are now entering the exam...")
        answers = []
        for i, question in enumerate(ExamDatabase.questions):
            print(f"Current question: {question}")
            options = ExamDatabase.question_options[question]
            for j, option in enumerate(ExamDatabase.options):
                print(f"{option}: {options[option]}")
            answer = input("Enter your answer (A, B, C, D): ")
            answers.append(answer)
            print()

        score, percentage = evaluate_exam(answers)
        total_questions = len(ExamDatabase.questions)
        print(f"You got {score} out of {total_questions} (complete score)")
        print(f"Your score percentage is: {percentage}%")
        save_exam_result(code, percentage)
        print()

    elif menu == "2":
        print("Checking your scores...")
        if code in ExamDatabase.student_scores:
            scores = ExamDatabase.student_scores[code]
            print("Your previous exam scores:")
            for i, score in enumerate(scores, start=1):
                print(f"Exam {i}: {score}%")
        else:
            print("You haven't taken any exams yet.")
        print()

    elif menu == "3":
        print("Checking your profile...")
        get_student_info(code)

    elif menu == "4":
        print("Exiting the Exam System...")
        break

    else:
        print("Invalid option. Please try again.")
