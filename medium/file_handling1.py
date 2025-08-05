import csv
try:
    with open('file_handling1.csv','r') as file:
        data = csv.reader(file)
        result={}
        for row in data:
            name = row[0]
            marks = row[1:]
            avg = sum([int(x) for x in marks])/len(marks)
            print("Average for ",name, " is ",avg)
        
except Exception as e:
    print(e)