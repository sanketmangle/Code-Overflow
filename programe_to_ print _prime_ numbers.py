start=input('Enter lower boundary:')
End = input('Enter upper boundary:')
lenght=list()
for i in range(start, End):
    if i%2!=0:
        lenght.append(i)
    else:
        continue
x=len(lenght)
print(lenght)
print('There are' +'  '+ `x` +'  '+ 'prime numbers between' +' '+ `start` +' '+ 'and' + ' '+`End`+ '.' )
