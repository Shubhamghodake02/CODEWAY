import random

# Define quiz questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest planet in our solar system?": "Jupiter"
}


def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions.")
    print("Let's begin!\n")


def ask_question(question, answer):
    user_answer = input(question + " ").strip().capitalize()
    if user_answer == answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is {answer}.")
        return 0


def play_quiz():
    score = 0
    questions = list(quiz_questions.items())
    random.shuffle(questions)

    for question, answer in questions:
        score += ask_question(question, answer)

    print(f"\nYour final score is: {score}/{len(questions)}")


def play_again():
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    display_welcome_message()
    while True:
        play_quiz()
        if not play_again():
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
