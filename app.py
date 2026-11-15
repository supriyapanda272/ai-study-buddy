# AI STUDY BUDDY
# A beginner-friendly Python study assistant

def ask_question():
    print("\n--- Ask a Study Question ---")
    question = input("Enter your question: ").lower()

    answers = {
        "python": "Python is a beginner-friendly programming language.",
        "variable": "A variable stores data in a program.",
        "loop": "A loop repeats a block of code.",
        "function": "A function is a reusable block of code.",
        "list": "A list stores multiple items in one variable.",
        "database": "A database stores and organizes information.",
        "ai": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence.",
        "algorithm": "An algorithm is a step-by-step procedure for solving a problem."
    }

    found = False

    for keyword, answer in answers.items():
        if keyword in question:
            print("\nStudy Buddy:", answer)
            found = True
            break

    if not found:
        print("\nStudy Buddy: I don't know that topic yet.")
        print("Try asking about Python, variables, loops, functions, lists, databases, AI or algorithms.")


def create_study_plan():
    print("\n--- Create Your Study Plan ---")

    subject = input("Enter your subject: ")
    hours = input("How many hours can you study today? ")

    try:
        hours = float(hours)

        if hours <= 0:
            print("Please enter a number greater than zero.")
            return

        study_time = hours * 60
        session = study_time / 3

        print("\nYour Study Plan")
        print("-------------------------")
        print("Subject:", subject)
        print(f"Total study time: {hours:g} hours")
        print(f"Session 1: {session:.0f} minutes - Learn concepts")
        print(f"Session 2: {session:.0f} minutes - Practise questions")
        print(f"Session 3: {session:.0f} minutes - Revise topics")

    except ValueError:
        print("Please enter a valid number of hours.")


def summarize_notes():
    print("\n--- Notes Summarizer ---")
    print("Enter your notes in one line.")

    notes = input("Your notes: ").strip()

    if not notes:
        print("Please enter some notes first.")
        return

    sentences = [
        sentence.strip()
        for sentence in notes.replace("!", ".").replace("?", ".").split(".")
        if sentence.strip()
    ]

    print("\nSummary:")
    print(". ".join(sentences[:2]) + ("." if sentences else ""))


def generate_quiz():
    print("\n--- Python Quiz ---")

    questions = [
        {
            "question": "1. Which function displays output in Python?",
            "options": ["1. input()", "2. print()", "3. type()"],
            "answer": "2"
        },
        {
            "question": "2. Which symbol starts a comment in Python?",
            "options": ["1. #", "2. //", "3. **"],
            "answer": "1"
        },
        {
            "question": "3. Which data type stores True or False?",
            "options": ["1. str", "2. list", "3. bool"],
            "answer": "3"
        }
    ]

    score = 0

    for item in questions:
        print("\n" + item["question"])

        for option in item["options"]:
            print(option)

        answer = input("Your answer (1, 2 or 3): ").strip()

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print(f"\nYour score: {score}/{len(questions)}")


def main():
    while True:
        print("\n" + "=" * 35)
        print("          AI STUDY BUDDY")
        print("=" * 35)
        print("1. Ask a study question")
        print("2. Create a study plan")
        print("3. Summarize notes")
        print("4. Generate a quiz")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            ask_question()
        elif choice == "2":
            create_study_plan()
        elif choice == "3":
            summarize_notes()
        elif choice == "4":
            generate_quiz()
        elif choice == "5":
            print("Goodbye! Keep learning.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()