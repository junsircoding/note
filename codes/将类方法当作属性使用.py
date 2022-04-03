class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('wrong')
        self.__score = score

s = Student('Bob', 59)
s.score = 45
print(s.score)