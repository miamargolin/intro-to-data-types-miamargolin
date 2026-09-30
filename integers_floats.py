""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" #count amount of words in any sentence
sentence = input("Enter your sentence: ")
print(sentence)
y= sentence.split( )
print(y)
print(len(y)) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

    x = "test"
print(f"hello {x}") """
""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" number = int(input("Enter your number: "))
print(number)
if number % 2 == 0:
    print("even")
elif number % 2 == 1:
    print("odd")
else:
    print("input a positive integer") """

""" tip = 0 
total = 0
bill = float(input("How much was your bill?"))
service = (input("How was your service?(bad, okay, good, great): ")).lower()
if service == "bad":
    tip = 0
elif service == "okay":
    tip = 15
elif service == "good":
    tip = 20
elif service == "great":
    tip = 25

total = bill + (bill * tip / 100)
print(total) """





def spaces(N,Y,T):
    x = 0
    for i in range(N):
        if Y[i] == "C" and T[i] == "C":
            x += 1
    print(x)
spaces(5, "CC..C", ".CC..")





