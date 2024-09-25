import csv


names=[]

with open('patrons.csv', 'r') as f:
    csv_data=csv.reader(f)
    #we don't want header and first line of the data
    next(csv_data)
    next(csv_data)
    # print (list(csv_data))
    for line in csv_data:
        if line[0] =='No Reward':
            break
        # print(line)
        names.append(f"{line[0]} {line[1]}") # we are appending on our empty list

    for name in names:
        
        print(name)

html_output=f"<P>There are currently {len(names)} public contributors :thank you</p>"
        
print(html_output)