# mini calculator
 
first= input("enter first no")
operator=input("enter operator(+,-,*,/)")
second=input("enter second no")
first=int(first)
second=int(second)
if operator =="+":
    print(first + second)
elif operator =="-":
       print(first - second)
elif operator =="*":
       print(first * second)
elif operator =="/":
       print(first / second) 
else:
      print("invalid operation")



