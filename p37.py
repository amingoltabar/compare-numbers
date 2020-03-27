my_list=[]
for i in range(6):
    my_list.append(int(input('Enter the number ')))
s=0
for i in range(6):
    s+=my_list[i]
ave=s/6
smallcount=0
bigcount=0
equalcount=0
for i in range(6):
    if my_list[i]>ave:
        bigcount+=1
    elif my_list[i]==ave:
        equalcount+=1
    else:
        smallcount+=1
print('average is',ave)
print('Number of numbers which are bigger than average :',bigcount)
print('Number of numbers which are smaller than average :',smallcount)
print('Number of numbers which are equal to average :',equalcount)
                 
    
    
