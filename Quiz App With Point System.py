questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "correct_answer": "Mount Everest"
    },
    {
        "question": "Who wrote the Harry Potter series?",
        "options": ["J.K. Rowling", "Stephenie Meyer", "Suzanne Collins", "George R.R. Martin"],
        "correct_answer": "J.K. Rowling"
    },
    {
        "question" : "After second World War, the world was divided into the blocks of",
        "options" : ["U.S.A & China", "USSR & China", "Japan & Korea", "U.S.A & USSR"],
        "correct_answer": "U.S.A & USSR"

    },
     {
        "question": "Which organisation came into existence in April 1949?",
        "options": ["SEATO", " CENTO", " NATO", " Warsaw Pact"],
        "correct_answer": "NATO"
    },

{
     "question": "The Cold War was fought between the United States and",
        "options": ["China", " Canada", "The USSR", "Germany"],
        "correct_answer": "The USSR"
},
{

        "question": "Traces of canals have been found at the Harappan site of",
        "options": ["Dholavira in Gujarat", " Shortughai in Afghanistan", "Kalibangan in Rajasthan", "Sind"],
        "correct_answer": "Shortughai in Afghanistan"
},

{

        "question": "Which of these sites of Harappan Civilisation belong to Haryana?",
        "options": ["Kalibangan", "Lothal", " Shortugai", "Banawali"],
        "correct_answer": "Banawali"
},
    
    {

        "question": "Neyveli lignite mines are located at -",
        "options": [" Tamil Nadu", "UP", "Delhi", "Banawali"],
        "correct_answer": "Tamil Nadu"
},

  {

        "question": "The largest solar power plant is located at -",
        "options": ["Ahemdabad" , "Madhopur","Thar desert", "Bhopal"],
        "correct_answer": "Madhopur"
},

 {

        "question": " The First World War ended with the defeat of Ottoman Turkey ",
        "options": ["False" , "True",],
        "correct_answer": "True"
},

 {

        "question": " The Non-cooperation programme was adopted finally at the Congress session at Nagpur in January 1920. ",
        "options": ["False" , "True",],
        "correct_answer": "False"
},

 {

        "question": "In most countries the making of the new national identity was a short process.",
        "options": ["False" , "True",],
        "correct_answer": "False"
},

{

        "question": ". In 1920, Gandhiji decided to launch a nationwide Satyagraha against the proposed Rowlatt Act.",
        "options": ["False" , "True",],
        "correct_answer": "False"
},


{

        "question": " In December 1929, the Lahore Congress formalised the demand of ‘Purna Swaraj’ in India.",
        "options": ["False" , "True",],
        "correct_answer": "True"
},

{

        "question": "When the tribals chanted Gandhiji’s name and raised slogans demanding ‘Swatantra Bharat’ they were also emotionally relating to an all-India agitation.",
        "options": ["False" , "True",],
        "correct_answer": "True"
},

{

        "question": " Mahatma Gandhiji wanted a non-violent civil disobedience against unjust laws, which started with a hartal on 8 April.",
        "options": ["False" , "True",],
        "correct_answer": "False"
},

]

score = 0

for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Enter your answer: ")
    if answer == question["correct_answer"]:
        score += 1

print(f"Your final score is {score} out of {len(questions)}")