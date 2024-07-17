def general_knowledge_quiz():
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Jupiter", "Saturn", "Neptune", "Earth"],
            "answer": "Jupiter"
        }
    ]
    
    print("Welcome to the General Knowledge Quiz!\n")
    
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        
        user_answer = input("Your answer: ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")
    
    print(f"You got {score} out of {len(questions)} questions correct.")

def python_quiz():
    score = 0
    questions = [
        {
            "question": "What is the output of the following Python code?\nprint(2 + 2 * 3)",
            "options": ["8", "10", "12", "14"],
            "answer": "8"
        },
        {
            "question": "Which of the following is used to define a function in Python?",
            "options": ["func", "def", "fun", "define"],
            "answer": "def"
        },
        {
            "question": "What is the result of the expression '3' + '4' in Python?",
            "options": ["7", "34", "Error", "None of the above"],
            "answer": "34"
        }
    ]
    
    print("Welcome to the Python Programming Quiz!\n")
    
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        
        user_answer = input("Your answer: ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")
    
    print(f"You got {score} out of {len(questions)} questions correct.")

def main():
    print("Welcome to the Quiz Program!\n")
    print("Choose a quiz genre:")
    print("1. General Knowledge")
    print("2. Python Programming")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        general_knowledge_quiz()
    elif choice == '2':
        python_quiz()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
