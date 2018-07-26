#Chapter 6 challenges

#challenge 1
"""prints every character in the word camus"""
c = "camus"
for i in c:
    print(i)

#challenge 2
"""Program collects two strings from user and inserts them into another string"""
n1 = input("Enter a noun")
n2 = input("Enter an animal")
s = "Yesterday I wrote a {}. I sent it to {}!".format(n1, n2)
print(s)

#challenge 3
"""Use method to make string grammatically correct (proper capitalization)"""
m = "aldous Huxley was born in 1894.".capitalize()
#added because capitalize() turns "H" to lowercase
m = m.replace("h", "H")
print(m)

#challenge 4
"""convert string into list"""
l = "Where now? Who now? When now?".split("?")
print(l)

#challenge 5
"""convert list to string; be sure period does not have an extra space"""
fox = ["The", "fox", "jumped", "over", "the", "fence" "."]
fox = " ".join(fox)
fox = fox.replace(" .", ".")
print(fox)

#challenge 6
"""Replace each instance of 's' with '$'"""
r = "A screaming comes across the sky."
r = r.replace("s", "$")
print(r)

#challenge 7
"""Use a method to find the first instance of the letter m"""
find = "Hemingway".index("m")
print(find)

#challenge 8
"""Find a dialogue in your favorite book and turn it into a string"""
d = "People are capable, at any time in their lives, of doing what they dream of. ― Paulo Coelho, The Alchemist"
print(d)

#challenge 9
"""create a string using concatenation and, then, multiplication"""
create = "three "
print(create + create + create)
print(create * 3)

#challenge 10
"""Slice a string"""
sl = "It was a bright cold day in April, and the clocks were striking thirteen"
print(sl[:33])
