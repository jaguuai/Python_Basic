#Ouestion sınıfı
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    
    def checkAnswer(self,answer):
        return self.answer==answer

#Quiz sınıfı
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestion(self):
        return self.questions[quiz.questionIndex]
    def displayQuestion(self):
        question=self.getQuestion()
        print(f"Soru {self.questionIndex+1}: {question.text}")

        for q in question.choices:
            print("-"+q)
        answer=input("cevap:")
        self.guess(answer)
        self.loadQuestion()

    def quess(self,answer):
        question=self.getQuestion

        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1
        self.displayQuestion()
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScoer(self):
        print(f"Score:{self.score}")


q1=Question("En iyi programalam dili hangisidir ?",["c#","python","javascript","java"],"python")
q2=Question("En popüler programalam dili hangisidir ?",["c#","python","javascript","java"],"c#")
q3=Question("En kazandıran programalam dili hangisidir ?",["c#","python","javascript","java"],"python")

questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.displayQuestion()
question=quiz.getQuestion()

