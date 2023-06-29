# we have sequence a = [1, 11, 21, 1211, 111221,
#after googling it is sequence A005150 in the OEIS
# we need to find len(a[30]) = ?

counter = 0
first = '1'
num = [first]
while counter <31:
     j = 0
     new_num = ''
     while j<len(first):
          i = j
          while j<len(first) and first[i]==first[j]:
               j+=1
          new_num+=str(j-i)+first[i]
     num+=[new_num]
     first = new_num
     counter+=1
print(len(num[30]))
#http://www.pythonchallenge.com/pc/return/5808.html





