# AI-Based Student Error Prediction System

## Overview

This project is an AI-powered system that analyzes how students solve engineering problems. Instead of just giving answers, it identifies mistakes, detects missing steps, predicts future exam errors, and generates targeted practice problems.

## Features

* Step-by-step solution analysis
* Mistake detection and explanation
* Prediction of future exam mistakes
* Pattern recognition in student thinking
* Targeted practice problem generation
* Stores past analyses in a history file

## Technologies Used

* Python
* OpenAI API
* VS Code

## How to Run the Project

1. Download or clone the repository:

```
git clone https://github.com/mohamedhassan-droid/ai-student-error-prediction-system.git
```

2. Open the folder in VS Code

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file and add your API key:

```
OPENAI_API_KEY=your_api_key_here
```

5. Run the program:

```
python main.py
```

## How It Works

* User enters a problem and a student solution
* The AI analyzes the solution
* It identifies mistakes and missing steps
* Predicts future exam errors
* Generates a targeted practice problem
* Saves results in `mistake_history.txt`

## Example Output

The system outputs:

* Overall assessment
* Mistakes found
* Missing steps
* Pattern of thinking
* Future exam risk prediction
* Targeted practice problem
* Corrected solution

## Author

Mohamed Hassan
