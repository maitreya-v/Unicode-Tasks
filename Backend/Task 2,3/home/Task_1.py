def madmax(a,b):
  dict={}
  for i in range(a,b):
     c=0
     binary=bin(i)
     for index in binary:
         if(index=='1' and c=='1'):
             answer=True
             break
         else:
             answer=False
         c=index
     dict[i]=answer
  return dict


madmax(2,7)