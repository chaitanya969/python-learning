#to convert kilometeres into miles

kms = float(input('enter the kilometers'))
conv_fac = 0.6213
miles = kms * conv_fac
print('%0.2f kilometers is equal to the %0.2f miles' %(kms,miles))