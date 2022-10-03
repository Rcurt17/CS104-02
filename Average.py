#Made on 10/3/2022
howManyTestScores = int(input("How many test score will you like to average: "))

total = 0

howManyEntered = 0

testGrades = 0

while howManyEntered < howManyTestScores:
    testGrades = int(input("Enter Test Score: "))
    total += testGrades
    howManyEntered += 1
    
average = (total / howManyEntered)
print(average)
    



