"""
Gillian Wolfersberger
This program determines a student's letter grade based on their final grade average.
"""
#Accept inputs from user
sFullName = input("Enter Student's full name: ").upper()
iGradeAvg = int(input("Enter final grade average: "))

#Create variable to hold letter grade
sGrade = ""

#Determine letter grade
if (iGradeAvg >= 94):
    sGrade = "A"
elif (iGradeAvg >= 90):
    sGrade = "A-"
elif (iGradeAvg >= 87):
    sGrade = "B+"
elif (iGradeAvg >= 83):
    sGrade = "B"
elif (iGradeAvg >= 80):
    sGrade = "B-"
else:
    sGrade = "C"

#Print results
print(sFullName, "had a final average of", iGradeAvg, "which resulted in an", sGrade, "for the course.")