import random 
knowledge_base = {
# Greetings     
"hello": "Hey there! I'm EduBot, your engineering study buddy. Ask me anything about college life, exams, or studies!",     
"hi": "Hi! How can I help you today? Type 'help' to see what I can answer.",     
"hey": "Hey! Ready to help you ace engineering. What's on your mind?",     
# About the bot     
"who are you": "I'm EduBot — a simple Python chatbot built as a PPS mini project. I can answer questions about engineering student life!",     
"what can you do": "I can help you with: CGPA calculation, study tips, exam advice, attendance rules, and general college queries. Type 'help' to see all topics.",
  "help": "Topics I can help with:\n  - cgpa  → How to calculate CGPA\n - attendance → Attendance rules\n  - study tips  → How to study effectively\n  - exam tips 
  → How to prepare for exams\n  - backlog        → What is a backlog?\n  - python       → Python learning tips\n  - project   → Project ideas\n  - stress   
  → Dealing with exam stress\n  - bye / exit     → End the chat",
# CGPA     
"cgpa": "CGPA = Sum of (Grade Points × Credits) / Total Credits.\nFor example, if you scored 9 in a 4-credit subject: contribution = 36.
\nAdd all such values and divide by total credits. Aim for 8+!", 
