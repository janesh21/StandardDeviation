import csv
import math
with open("c105.csv", newline='') as newfile:
  reader = csv.reader(newfile)
  filedata = list(reader)
data = filedata[0]

def mean (data):
    n=len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n 
    return mean

squarelist = []
for n in data:
    a = int(n)-mean(data)
    a = a**2
    squarelist.append(a)

sum= 0
for i in squarelist:
    sum=sum+i
result = sum/(len(data)-1)

stdvtn=math.sqrt(result)

print(stdvtn)