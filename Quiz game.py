import random
while True:
    quiz_questions=[{"question":"Who is prime minister of india?","options":['A.Narenda Modi','B.Rahul Gandhi','C.Indra Gandhi','D.Nehru'],'answer':'A'},
                    {"question":"Who is the Chef Minister of Telangana?","options":['A.Kcr','B.Revanth Reddy','C.kisan reddy','D.KTR'],'answer':'B'},
                   {"question":"Which team won ipl title in 2016?","options":['A.SRH','B.CSK','C.KKR','D.MI'],"answer":"A"},
                   {'question':'Which team won 2011 Cricket World Cup?',"options":['A.Astrila','B.Bangladesh','C.India','D.pakisthan'],"answer":"C"}]

    def present_question(question):
        print(question["question"])
        for choice in question['options']:
            print(choice)
        user_answer=input("Enter your answer(A,B,C,D):")
        return user_answer.upper()


    def check_answer(question,user_answer):
        return user_answer==question["answer"]

    def play_quiz_game():
        score=0
        random.shuffle(quiz_questions)
        for question in quiz_questions:
            user_answer=present_question(question)
            if check_answer(question,user_answer):
                print('Correct answer!')
                score +=1
            else:
                print("Incorrect answer.The correct answer is :",question['answer'])

            print()
        print("Quiz finished!")
        print("Your final score is:",score)
                                                                 
    play_quiz_game()
    repeat=input("Do you want play again?(yes/no):")
    if repeat.lower()!="yes":
       break
print("Thankyou for playing quiz")
                                                                          
                                                                      
