import numpy as np
import pandas as pd

data=pd.read_csv('enjoysport.csv')
concepts=np.array(data.iloc[:0:-1])
print("Instances are : ",concepts)
target=np.array(data.iloc[:,-1])
print("Target values are : ",target)
def learn(concepts,target):
    specific_h=concepts[0].copy()
    print("Initializtion of specific_h and general_h")
    print("Specific Boundary : ",specififc_h)
    general_h=['?']
    for i in range(len(specific_h)):
        print("Generic Boundary : ",general_h)
    for i,h in enumerate(concepts):
        print("Instance",i+1,"is : ",h)
        if target[i]=="yes":
            print("Instance is positive")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = "?"
                    general_h[x][x]="?"
        if target[i]=="no":
            print("Instance is negative")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]="?"
            print("Specific Boundary after ",i+1,"Instance is : ",specific_h)
            print("General Boundary after ",i+1,"Instance is : ",general_h)
