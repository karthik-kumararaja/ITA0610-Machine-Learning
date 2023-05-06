import csv
a=[]
with open ('enjoysport.csv')as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)
print("The total number of training instances are : ",len(a))
num_attribute = len(a[0])-1
hypothesis = ['0']*num_attribute
print("The initial hypothesis is : ",hypothesis)
for i in range (0,len(a)):
    if a[i][num_attribute]=='yes':
        print("Instance",i+1,"is ",a[i]," and is positive instance")
        for j in range(0,len(a)):
            if hypothesis[j]=='0' or hypothesis[j]==a[i][j]:
                hypothesis[j]=a[i][j]
            else:
                hypothesis[j]='?'
            print("The hypothesis of the training instance ",i+1," is : ",hypothesis)
    if a[i][num_attribute]=='no':
        print("Instance ",i+1,"is ",a[i]," and is negative instance. Hence ignored")
        print("The hypothesis for the training instaance",i+1,"is : ",hypothesis)
print("The maximally specific hypothesis for the training instance is ",hypothesis)
