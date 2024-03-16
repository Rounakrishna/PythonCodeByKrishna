def armstrong(num):
    
    count=0
    for i in str(num):
        sum=int(i)**len(str(num))
        count+=sum
    if count==num:
        return print(num,"is an Armstrong number")
    else:
        return print(num,"is not an Armstrong number")
    

print(armstrong(153))