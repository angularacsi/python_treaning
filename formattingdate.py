import datetime
dates=datetime.datetime(2024,9,24,12,30,45)

outputformat='The date is {:%B %d,%Y}'.format(dates)



print(outputformat)

outputformat2 = 'The date is {:%Y-%m-%d %H:%M:%S}'.format(dates)
print(outputformat2)

outputformat3 = 'The date is {:%m/%d/%y}'.format(dates)
print(outputformat3)

outputformat4 = 'The date is {:%a, %b %d, %Y}'.format(dates)
print(outputformat4)

outputformat5 = 'The time is {:%I:%M:%S %p}'.format(dates)
print(outputformat5)

outputformat6= 'The date is {:%A, %B %d, %Y}'.format(dates)
print(outputformat6)

