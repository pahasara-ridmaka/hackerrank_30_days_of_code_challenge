class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self, firstName: str, lastName: str, idNumber: int, scores: [int] ):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    def calculate(self) -> str:
        avgScore = sum(scores) / len(scores)
        if (avgScore<40):
            grade = "T"
        elif (avgScore < 55):
            grade = "D"
        elif (avgScore < 70):
            grade = "P"
        elif (avgScore < 80):
            grade = "A"
        elif (avgScore < 90):
            grade = "E"
        elif (avgScore <= 100):
            grade = "O"
        else:
            grade = ""
        
        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())