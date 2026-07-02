# My first automation script in Python
import os

def welcome_message():
    user_name = "Isaac"
    print(f"Hello, {user_name}! Your remote work environment is ready.")
    print("Simulating data pipeline processing...")

# 🚀 NEW: Adding a simple data processing function
def process_data_scores():
    scores = [85, 90, 78, 92, 88]
    average = sum(scores) / len(scores)
    print(f"Data analysis complete. Average score: {average}")

if __name__ == "__main__":
    welcome_message()
    process_data_scores()  # Running the new function