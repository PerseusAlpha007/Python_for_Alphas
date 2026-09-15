# lambda argument: expression
a = lambda x : x ** 2
print(a(int(input("Enter a niumber :"))))

print((lambda a,b,c: a if a>b>c else(b if b>c>a else c))(52,35,42))

print(list(map((lambda a:0 if a%2==0 else 1),([20,25,1,35,105]))))
print((lambda s :s.upper())("distinguish"))

print((lambda a:"Acsess Granted" if a == 2007 else "Acsess Denied")(2007))