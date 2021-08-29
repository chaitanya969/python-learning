#to find total and avg of a student
htno = int(input('enter the hallticket no:'))
name = input('enter student name : ')
s1 = int(input('enter the subject1 marks: '))
s2 = int(input('enter the subject2 marks: '))
s3 = int(input('enter the subject3 marks: '))

total = s1+s2+s3
avg = total/3
print('student result: ')

print('total marks obtained: ', total)
print('average of the marks: ', avg)