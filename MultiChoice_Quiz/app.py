from Question import Question

question_prompts = [     #these are the questions that we will ask to users
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",   #this is prompt1
    "What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",     #this is prompt2
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"     #this is prompt3
]

questions =  [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions): 
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer ==  question.answer:
            score +=1
    print ("you got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)