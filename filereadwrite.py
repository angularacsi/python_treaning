f=open("test.txt", "r");
print(f.name);
print(f.mode);
f.close();
# this is one of the way to open a file

with open("test.txt", "r") as f1:
    # f_content=f1.readline(); # first line of the file
    # print(f_content)
    # f2=f1.readlines()
    # print(f2)
    
    f_contents=f1.read(10) # used to read 100 characters of the file
    print(f_contents)
    
"""  for line in f1:
        print(line, end='**') # print each line without newline
    
"""
with open ('test2.txt', 'w') as f2: # this creates a new file and writes on it
    f2.write('Hello, this is a test!')
    f2.seek(0)
    f2.write('R')


with open('test2.txt', 'r') as rf:  #read the orginal file and copy it to the other file
    with open('test2_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)



with open('test2.JEPG', 'rb') as rf:  #read the orginal file and copy it to the other file for image
    with open('test2_copy.txt', 'wb') as wf:
        for line in rf:
            wf.write(line)
        
    