import random
import re

knowledge_base = {
    # Greetings
    "hello": "Hey there! I'm EduBot, your engineering study buddy. Ask me anything about college life, exams, or studies!",
    "hi": "Hi! How can I help you today? Type 'help' to see what I can answer.",
    "hey": "Hey! Ready to help you ace engineering. What's on your mind?",

    # About the bot
    "who are you": "I'm EduBot! I answer questions about engineering student life.",
    "what can you do": "I can help you with: CGPA calculation, study tips, exam advice, attendance rules, and general college queries. Type 'help' to see all topics.",
    "help": (
        "Topics I can help with:\n"
        " - cgpa → How to calculate CGPA\n"
        " - attendance → Attendance rules\n"
        " - study tips → How to study effectively\n"
        " - exam tips → How to prepare for exams\n"
        " - backlog → What is a backlog?\n"
        " - python → Python learning tips\n"
        " - project → Project ideas\n"
        " - stress → Dealing with exam stress\n"
        " - joke → A programming joke\n"
        " - bye / exit → End the chat"
    ),

    # CGPA
    "cgpa": "CGPA = Sum of (Grade Points × Credits) / Total Credits.\nFor example, if you scored 9 in a 4-credit subject: contribution = 36.\nAdd all such values and divide by total credits. Aim for 8+!",
    "how to calculate cgpa": "CGPA = Σ(Grade Point × Credit Hours) / Σ(Credit Hours)\nMost colleges use a 10-point grading scale. Check your university handbook for the exact grade-to-point conversion.",
    "gpa": "GPA is for one semester; CGPA is the cumulative average across all semesters. Both are calculated using (Grade Point × Credits) / Total Credits.",

    # Attendance
    "attendance": "Most colleges require a minimum of 75% attendance to be eligible to sit in exams. Below 75% can lead to detainment. Mark your attendance every class!",
    "attendance rule": "The standard rule: attend at least 75 out of every 100 lectures. If you fall below, you may get a 'detained' status and cannot appear for the end-semester exam.",
    "how many leaves": "With the 75% rule: if there are 100 lectures, you can miss at most 25. For 60 lectures in a subject, you can miss at most 15. Plan wisely!",

    # Study tips
    "study tips": "Top 5 study tips:\n 1. Use the Pomodoro technique (25 min study, 5 min break)\n 2. Study from handwritten notes for better retention\n 3. Solve previous year question papers\n 4. Teach concepts to a friend\n 5. Sleep 7-8 hours, your brain needs rest!",
    "how to study": "Start with understanding > memorising. Break chapters into small topics. Practice problems daily. Revise every weekend. Make short notes.",
    "study": "Consistent daily study (2-3 hours) beats last-minute cramming. Use spaced repetition for technical subjects.",

    # Exam tips
    "exam tips": "Exam preparation tips:\n 1. Start 2 weeks before, don't wait!\n 2. Solve last 5 years' question papers\n 3. Focus on high-weightage topics first\n 4. Write practice answers by hand\n 5. Sleep well the night before the exam",
    "exam": "For exams: prioritise high-weightage units, practice writing speed, and revise formula sheets daily. Don't skip numericals!",
    "how to prepare": "Break your syllabus into daily targets. Finish theory first, then practicals and numericals. Attempt mock tests under timed conditions.",

    # Backlogs
    "backlog": "A backlog means you failed a subject and need to re-appear in the next attempt. Avoid backlogs, they delay graduation and affect placements. If you have one, focus on clearing it immediately!",
    "kt": "KT (Keep Term) is when you fail a subject, same as a backlog. You must clear it in subsequent exam cycles. Don't let KTs pile up!",

    # Python tips
    "python": "Python tips for beginners:\n 1. Learn: variables → loops → functions → lists → dictionaries\n 2. Practice on w3schools.com or hackerrank.com\n 3. Build small projects like this chatbot!\n 4. Use VS Code or PyCharm as your editor",
    "how to learn python": "Start from the basics: print(), variables, input(). Then loops (for, while). Then functions. Then data structures (list, dict). Then libraries (math, random). Practice every day!",

    # Projects
    "project": "Some mini Python project ideas:\n 1. Student grade calculator\n 2. Quiz game\n 3. Simple chatbot (like this one!)\n 4. Number guessing game\n 5. Expense tracker\n 6. ATM simulation",
    "project ideas": "Great beginner projects:\n - Calculator\n - To-do list\n - Password generator\n - Rock Paper Scissors game\n - Basic data analysis with CSV files",

    # Stress
    "stress": "Engineering is tough but manageable! Tips:\n - Take breaks, burnout is real\n - Exercise for 20 minutes daily\n - Talk to friends or family\n - Don't compare yourself to others\n - Sleep is NOT a waste of time!",
    "exam stress": "Before exams: take deep breaths, stay hydrated, eat well, and avoid all-nighters. A rested brain performs far better. You've got this!",

    # Fun
    "fun": "Why do programmers prefer dark mode?\n...Because light attracts bugs!",

    # Goodbye / thanks
    "bye": "Goodbye! All the best for your studies. Keep coding!",
    "exit": "Exiting EduBot. Good luck with your termwork!",
    "quit": "See you next time. Keep learning!",
    "thank you": "You're welcome! Feel free to ask anytime. Best of luck!",
    "thanks": "Happy to help! All the best for your exams!",
}

# A few fun programming jokes
jokes = [
    "Why do Java developers wear glasses?\nBecause they don't C#!",
    "A SQL query walks into a bar, walks up to two tables and asks...\n'Can I JOIN you?'",
    "Why did the programmer quit his job?\nBecause he didn't get arrays!",
    "How many programmers does it take to change a light bulb?\nNone, that's a hardware problem!",
    "Why do Python programmers prefer snake_case?\nBecause they love snakes!",
]

EXIT_KEYWORDS = ["bye", "exit", "quit"]

# Longest keys first, so "exam stress" is checked before "stress" or "exam"
SORTED_KEYS = sorted(knowledge_base, key=len, reverse=True)


def get_response(user_input):
    """
    Match user input to the knowledge base and return a response.
    Uses whole-word matching, so 'cgpa calculation' matches 'cgpa',
    but 'this' does NOT match 'hi'.
    """
    user_input = user_input.lower().strip()

    # Jokes are random, so handle them separately
    if "joke" in user_input:
        return random.choice(jokes)

    # Exact match first
    if user_input in knowledge_base:
        return knowledge_base[user_input]

    # Partial (whole-word) keyword match
    for key in SORTED_KEYS:
        if re.search(r"\b" + re.escape(key) + r"\b", user_input):
            return knowledge_base[key]

    # Default response
    return (
        "Hmm, I didn't quite understand that. Try asking about:\n"
        "cgpa, attendance, study tips, exam tips, python, project, stress, or type 'help'."
    )


def display_welcome():
    """Print a welcome banner when the chatbot starts."""
    print("=" * 55)
    print("Welcome to EduBot - Your Study Buddy!")
    print("PPS Mini Project | B.Tech AI & Data Science")
    print("=" * 55)
    print("Type your question below. Type 'bye' to exit.\n")


# Main chat loop (only used when running in the terminal)
def main():
    display_welcome()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("EduBot: Please type something! (or 'bye' to exit)\n")
            continue

        response = get_response(user_input)
        print(f"\nEduBot: {response}\n")

        # Exit if user says bye/exit/quit
        if user_input.lower() in EXIT_KEYWORDS:
            break


# Entry point: runs main() only when you run this file directly,
# NOT when Streamlit imports get_response from it.
if __name__ == "__main__":
    main()