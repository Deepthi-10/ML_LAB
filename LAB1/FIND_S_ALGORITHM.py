import csv 
a=[]
with open('/kaggle/input/lab1-ml/dataset_lab1.csv','r') as csvfile:
as csvfile:
for row in csv.reader(csvfile):
    a.append(row)
    print(a)
print("number of training instances:",len(a))
num_attribute=len(a[0])-1
print("initial hypothesis:")
hypothesis=['0']*num_attribute
print(hypothesis)
for i in range(0,len(a)):
    if a[i][num_attribute]=='yes'
        for j in range(0,num_attribute):
            if hypothesis[j]=='0'or hypothesis[j]==a[i][j]:
                hypothesis[j]=a[i][j]
            else:
                hypothesis[j]='?'
        print("hypothesis for training instance}}is:".format(i+1),hypothesis)
print("maximally specific hypthesis for the training instance is :")
print(hypothesis)          
