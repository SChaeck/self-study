totalCredit = 0.0
totalPoint = 0.0
gradeToPoint = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20) :
    subject, credit, grade = input().split()
    if grade == "P" :
        continue    
    
    totalCredit += float(credit)
    totalPoint += float(credit) * gradeToPoint[grade]

print(totalPoint/totalCredit)