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





""" def spaces(N,Y,T):
    x = 0
    for i in range(N):
        if Y[i] == "C" and T[i] == "C":
            x += 1
    print(x)
spaces(5, "CC..C", ".CC..") """


""" def spaces (e, f):
    French = 0
    English = 0
    for i in range (f):
        if f[i] == "T,t" and e[i] == "T,t":
           English+=1
        if f[i] == "S,s" and e[i] == "S,s":
            French+=1  """

def find_factors(n):
    factors = []
    for i in range (1, 1+n):
        if n % i == 0:
            factors.append(i)
   
    return factors
print(find_factors(36))

def gcf(a, b):
    factors_a = find_factors(a)
    factors_b = find_factors(b)
    common_factors = [f for f in factors_a if f in factors_b]

    return max(common_factors)
print(gcf(24,36))








def wizard(owner,N, duels):
 #who owns the wand 
 last_owner = owner
 #number of times changes 
 changes = 0
 #check 1 single battle 
 #print(duels[0])
 #check first character
 

""" print(duels[0][0]) """

#check if wand changed hands 
if owner == duels [0][0]:
   




wizard("A", 3, ["BA", "CB"  ])








