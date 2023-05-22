list =[]
n=int(input("Number of elements:"))
print("Input Numbers:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list) 
for i in range(0,n-1):
 if list[i] <0:
      list.pop(i)
print("postive numbers:")
print (list)    
