qa_pairs = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the color of the sky on a clear day?", "answer": "blue"}
]

# Loop through each question
for qa in qa_pairs:
    # Ask the user the question
    user_answer = input(qa["question"] + " ")
    
    # Check if the user's answer is correct
    if user_answer.strip().lower() == qa["answer"].lower():
        print("Correct!")
    else:
        print(f"Sorry, that's not right. The correct answer is: {qa['answer']}")