#Chapter 9 challenges

#challenge 1
""" find a file and  print it's content using Python """
with open("/Users/kirawashington/projects/spam-and-eggs/os-mod.txt", "r") as f:
	print(f.read())

# >>To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. --Ralph Waldo Emerson

#challenge 2
""" Write a program that asks a user a question and save it to a file """
n = input("What is your favorite color? ")
with open("user-input.txt", "w") as f:
	f.write(n)
#read what's in user-input.txt
with open("user-input.txt", "r") as f:
    print(f.read())
#>> black

#challenge 3
"""Take the items in a list and write them to a CSV file"""
list1 = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.txt", "w") as f:
	w = csv.writer(f, delimiter="|")
	for i in list1:
		w.writerow(i)
#read what's in movies.txt
with open("movies.txt", "r") as f:
	print(f.read())

# >> Top Gun|Risky Business|Minority Report
#    Titanic|The Revenant|Inception
#    Training Day|Man on Fire|Flight
