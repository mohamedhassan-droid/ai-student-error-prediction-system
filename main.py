from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_student_solution(problem, student_solution):
    prompt = f"""
You are an AI learning system for engineering students.

Your job is to analyze HOW the student thinks and predict future performance.

Problem:
{problem}

Student Solution:
{student_solution}

Return your answer EXACTLY in this structured format:

1. Overall Assessment
- Clearly state if the solution is correct, partially correct, or incorrect

2. Mistakes Found
- List all mistakes in logic, math, or assumptions

3. Missing Steps
- Identify any skipped reasoning or equations

4. Pattern of Thinking
- Describe the student's mistake pattern (e.g., ignores forces, skips equilibrium, misuses formulas)

5. Future Exam Risk Prediction
- Predict what type of problem this student will likely fail and WHY

6. Targeted Practice Problem
- Generate ONE practice problem specifically designed to fix this weakness

7. Corrected Solution
- Show the correct step-by-step reasoning
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a clear engineering tutor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content


def main():
    print("AI Student Error Prediction System")
    print("=" * 50)

    problem = input("\nEnter the problem:\n")
    solution = input("\nEnter the student's solution:\n")

    print("\nAnalyzing...\n")

    feedback = analyze_student_solution(problem, solution)

    print("\n--- AI Feedback ---\n")
    print(feedback)
    with open("mistake_history.txt", "a", encoding="utf-8") as file:
        file.write("\n==============================\n")
        file.write("Problem:\n")
        file.write(problem + "\n\n")
        file.write("Student Solution:\n")
        file.write(solution + "\n\n")
        file.write("AI Feedback:\n")
        file.write(feedback + "\n")

    print("\nAnalysis saved to mistake_history.txt")

if __name__ == "__main__":
    main()