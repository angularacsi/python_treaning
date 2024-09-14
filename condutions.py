language='java'

if language=='python':
    print("This is true")
    
elif language=='java':
    print("the language is java")
else:
    print("This is none of the supported languages")

user='admin'
logged_in=True #false will be logged

if user=='admin' and logged_in:
    print("You are logged in as admin")
else:
    print("You are not logged in")