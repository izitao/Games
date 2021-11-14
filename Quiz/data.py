from urllib.request import urlopen
import json

#difficulty etc. can be changed at https://opentdb.com/api_config.php by replacing the new url link in the url variable

url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"
response = urlopen(url)
raw_question_data = json.loads(response.read())
#print(raw_question_data)

#CONTINUE BELOW TO question_data VARIABLE!!!

'''question_data = [
    {"category": "General Knowledge",
     "type": "boolean",
     "difficulty": "easy",
     "question": "Gumbo is a stew that originated in Louisiana.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "History", "type": "boolean", "difficulty": "easy",
     "question": "The Spitfire originated from a racing plane.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Books", "type": "boolean", "difficulty": "easy",
     "question": "The &quot;Berenstein Bears&quot; is the correct spelling of the educational children&#039;s book series&#039; name.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "Bulls are attracted to the color red.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "Minecraft can be played with a virtual reality headset.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In the &quot;Half-Life&quot; series, &quot;H.E.V&quot; stands for &quot;Hazardous Evasiveness Vest&quot;",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
     "question": "A Saxophone is a brass instrument.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean",
     "difficulty": "easy", "question": "Kiznaiver is an adaptation of a manga.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "There are 2 player roles in Trouble in Terrorist Town.",
     "correct_answer": "False", "incorrect_answers": ["True"]}
]'''


'''for question in question_data:
        print(question["question"])
        print(question["correct_answer"])'''


question_data = raw_question_data["results"]


