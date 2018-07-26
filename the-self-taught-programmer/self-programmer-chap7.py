#Chapter 7 challenges

#challenge 1
"""Print each item in a list"""
l = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i in l:
    print(i)


#challenge 2
"""Print number from 25 - 50 """
for i in range(25, 51):
    print(i)

#challenge 3
"""Print list and its index """
s = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i, show in enumerate(s):
    print(i)
    print(show)

#challenge 4
"""Write a program with an infinite loop """
guess = [0, 11, 22, 34, 54, 50, 6, 17, 89, 99]
while True:
	n = input("Guess a number or type 'q' to quit").lower()
	if n == 'q':
		break
	n = int(n)
	if n in guess:
		print("You've guess correct")
	else:
		print("Nope, try again")

#challenge 5
""" Multiply all of the numbers from two lists """
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
hold = []
for i in list1:
    for j in list2:
        hold.append(i*j)
print(sorted(hold))
