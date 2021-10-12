#Write a Python program to convert temperatures to and from celsius, fahrenheit

Temp = int(input())
Unit = input() # input unit as c or f
if Unit == 'c':
    F = (Temp* (9/5)) + 32
    print('after converting Temp:{} F'.format(F))
else:
    C = (Temp - 32) * (5/9)
    print('after converting Temp:{} C'.format(C))
