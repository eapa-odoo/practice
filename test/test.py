print('hello world')
if(5>2):
    print('5 is greater than 2')

x = 4
print(x)
x = 'Demo'
print(x)

x = str(3)
print(x)
print(type(x))
x = int(3)
print(x)
print(type(x))
x = float(2)
print(x)
print(type(x))

myVariableName = 3
MyVariableName = 3
my_variable_name = 3

fruits = ['apple', "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = """Multiline string
has 3 quotes
and also you can specify single quotes"""
x = "Hello"
for y in x:
    print(y)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) 

# list overview
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) 

