import random
import itertools
import webbrowser

#welcome message
print("Hello! Welcome to the chore generator. \nMy name is THEE best chore generator in the world, but you can call me CG. \nI was created for you to be responsible for cleaning something in your suite. \nHere we go ;)")
print("\n")

#roomates' names
names = input("Enter roomates' names separated by space (i.e. name1 name2 name3): ")
names = names.split()

#chores
tasks = input("Enter tasks separated by comma and no following space (i.e task1,task2,task3): ")
tasks = tasks.split(",")

#greetings
greetings = ["Hey, ", "'Sup, ", "What's good, ", "Hi, "]

print("\n")

#randomize lists
random.shuffle(names)
random.shuffle(tasks)
random.shuffle(greetings)

#fix repeats in names and chores
for (greeting, name, task) in zip(greetings, names, tasks):
    print(greeting + name + "! You're responsible for " + task)


#playlist choice
print("\n")
print("Cleaning is better with music. Here's something for you to listen to while you clean ;)")

print("\n")
genre = input("Pick a genre: ")

print("\n")

webbrowser.open("https://www.youtube.com/results?search_query=" + genre + "+playlist")
print("\n")

print("Well I'm not going to do EVERYTHING for you. Go find something. Byeeeee//////")


