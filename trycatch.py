try: # try to execute the command
    f=open('test.txt', 'r')
    if f.name == 'test.txt':
        raise Exception
    f.readlines()
    
 
    print(f)
except Exception as e: #else raise an exception when something is wrong
    print('some error occurred')
    print(e)
except FileNotFoundError: #else raise an exception when something is wrong
    print('file not found')
else: #else raise an exception when
    print('file opened successfully')
finally: 
    print(f)
    f.close() # always close the file even if an error occurred or not