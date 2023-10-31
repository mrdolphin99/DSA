#using a
numDays = int(input("How many day's temperature? "))
total = 0
for i in range(1,numDays + 1):
    nextDay = int(input("Day " + str(i) + ': '))
    total +=nextDay
avg = round(total/numDays,2)
print('AVG temp of these days: ',avg)

#Using python list
temp = []

for i in range(numDays):
    nextDay = int(input("Day " + str(i) + ': '))
    temp.append(nextDay)
    total +=temp[i]
    
