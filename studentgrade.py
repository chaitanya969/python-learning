#to find total and avg of a student
htno = int(input('enter the hallticket no:'))
name = input('enter student name : ')
s1 = int(input('enter the subject1 marks: '))
s2 = int(input('enter the subject2 marks: '))
s3 = int(input('enter the subject3 marks: '))

total = s1+s2+s3
avg = total/3

if s1>=35 and s2>=35 and s3>=35:
    result='PASS'
    if avg>=70:
        grade = 'A -- Grade'
    elif avg>=60 and avg<70:
        grade = 'B -- Grade'
    elif avg >=60 and avg < 70:
        grade = 'B -- Grade'
    elif avg >=50 and avg < 60:
        grade = 'C -- Grade'
    elif avg >= 35 and avg < 500:
        grade = 'D -- Grade'
else:
    result = 'FAIL'
    grade = 'F -- Grad'

print('student result: ')

print('total marks obtained: ', total)
print('average of the marks: ', avg)
print('final result obtained: ', result)
print('grade secured: ', grade)