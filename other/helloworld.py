def main():
    print("hello world!")


main()
print("Albert")

f = 101
print(f)

print("======================== Global vs.local variables in functions")


# Global vs.local variables in functions
def some_function():
    global f


print(f)
f = "changing global variable"
some_function()
print(f)
# delete variable
# del f
print(f)

print("======================== Tuple")
# Tuple
x = ("Guru99", 20, "Education")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print(company)
print(emp)
print(profile)

print("======================== if elif else")
a = (5, 6)
b = (6, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

print("======================== Dictionary")
# Dictionary
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Dict.update({"Sarah": 9})
print(Dict)
print((Dict['Tiffany']))
del Dict['Charlie']
print(Dict)
# The items() method returns a list of tuple pairs (Key, Value) in the dictionary.
print("Students Name: %s" % list(Dict.items()))

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("variable Type: %s" % type(Dict))

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("printable string:%s" % str(Dict))

print("======================== Pass Statement")
# Pass Statement
# We use pass statement to write empty loops. Pass is also used for empty control statement, function and classes.
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

# print("======================== Tuple")
print("======================== Using enumerate():  enumerate() is used to loop through the containers printing \n"
      "the index number along with the value present in that particular index.")
for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)

# print("======================== Tuple")
print(
    "======================== Loop zip(): Using zip(): zip() is used to combine 2 similar \n"
    "containers(list-list or dict-dict) printing the values sequentially. The loop exists \n"
    "only till the smaller container ends.")
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']
for question, answer in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))

# print("======================== Tuple")
print("======================== Using iteritem(): iteritems() is gone in Python3")
d = {"geeks": "for", "only": "geeks"}

# using iteritems to print the dictionary key-value pair
# print("The key value pair using iteritems is : ")
# for i, j in d.iteritems():
#     print(i, j)

# using items to print the dictionary key-value pair
print("The key value pair using items is : ")
for i, j in d.items():
    print(i, j)

# print("======================== Tuple")
