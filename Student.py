import LearningStyles

class Student():

    def __init__(self, name, age, auditory, visual, kinetic, pace, social):
        self.name = name
        self.age = age
        self.learningStyles = []
        self.learnignStyles.append(LearningStyles(auditory, visual, kinetic, pace, social))

    def addAttributes(self, attributes):
        self.learningStyles.append(attributes)

    def getLastAttributes(self):
        return self.learningStyles[-1]

    def getAllAttributes(self):
        return self.learningStyles