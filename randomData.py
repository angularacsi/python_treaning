import random

ran = random.randint(1, 30)
print(ran)

greeting = ['hello', 'world', 'hi', 'fine', 'goodbye']
colors = ['black', 'red', 'green', 'yellow', 'brown', 'orange']

value = random.choice(greeting)  # display one random value
result = random.choices(colors, k=10) # displays a list of 10 elements from colors list
result2=random.choices(colors,weights=[18,18,2,10,20,2],k=10) # giving higher weights for each element based on thier order
print(value)

print(value + "   wale")
print(result)
print(result2)


deck=list(range(1,53))
random.shuffle(deck)
hand=random.sample(deck,k=5)
print(hand)

print(deck)