for i in range(1,int(input("Enter No. of rows :"))+1):
    for j in range(i):
        print(i,end = " ")
    print()

c = input("Enter a character :")
for i in range(1,int(input("Enter No. of rows :"))+1):
    for j in range(i):
        print(c,end = " ")
    print()

k = "A"
for i in range(1,int(input("Enter No. of rows :"))+1):
    for j in range(i):
        print(k,end = " ")
        k = ord(k)
        k += 1
        k = chr(k)        
    print() 