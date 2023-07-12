import random

questions = [
    "What is the capital of Afghanistan?",
    "How much is Afghanistan's population?",
    "Which year did Afghanistan take its independence?"
]

trueOption = [
    "kabul",
    "30 million",
    "1919"
]

options = ["A", "B", "C", "D"]

question_options = {}

student_scores = {}  # Dictionary to store the student's exam scores

# Assign options to each question
for i, question in enumerate(questions):
    # Get the options for the current question
    q_options = [
        "Kabul", "Bamiyan", "Herat", "Ghazni"
    ] if i == 0 else [
        "30 million", "50 million", "65 million", "17 million"
    ] if i == 1 else [
        "1876", "1919", "1976", "2000"
    ]

    # Shuffle the options
    shuffled_options = options[:]
    random.shuffle(shuffled_options)

    # Create the question options dictionary
    question_options[question] = {
        shuffled_options[j]: q_options[j] for j in range(len(shuffled_options))
    }


def save_exam_result(access_code, score):
    if access_code in student_scores:
        student_scores[access_code].append(score)
    else:
        student_scores[access_code] = [score]
