person={'name':'John', 'age':26}

sentence='My name is ' + person['name'] + ' i am ' + str(person['age']) + ' years old'

print(sentence)

sentence2='My Name is {} and i am {} years old'.format(person['name'], person['age'])

print(sentence2)

sentence3='My Name is {0} and i am {1} years old index'.format(person['name'], person['age'])

print(sentence3)

sentence4='my name is {0[name]} and i am {1[age]} years old internal pass'.format(person, person)
print(sentence4)


class person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
pl=person('Jack', '26')

sentence5='My name is {0.name} and my age is  {0.age} from the function '.format(pl)

print(sentence5)


for i in range(1,10):
    
    print('the value is : {:}'.format(i))
for x in range(1,10):
    print('the value is : {:02}'.format(x))

pi=3.145386

print('Pi is : {:.2f}'.format(pi)) # two decimal points


numbers = 'i mb is equal to {:,}'.format(100**2) # this is to separate by commas

print(numbers)