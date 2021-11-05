# Tuples Examples ITS- 250 Python

# ex 1 -Tuple items can be of any data type
my_tuple = (1, 2, 3, 4, 5)
print (my_tuple)

# ex 2- Tuple items can be of any data type

superheroes = ("Black Panter", 'Dr.Munoz', "Spider-Girl", 'Batman', 'Robin', "Black Panter",)
print (superheroes)

#ex 3 tuple can contain different data types:

myMultipleTuple1 = ("Donald", 0.5, False, 89, "male")
print(myMultipleTuple1)

# ex 4 Index accessing elements within the tuples
superheroes = ("Black Panter","Spider-Girl",'Dr.Munoz','Batman','Robin',"Black Panter")
print(superheroes[0]) # accessing tuples
print(superheroes[-2])# negative index
print(superheroes[1:4]) # range of index; ex 1
print(superheroes[1:])  # range of index; ex 2 from the beginning
print(superheroes[:5])  # range of index; ex 3 to the end of tuple


# ex 5 Tuples functions convert to a 'List'
myBFF = ("Boxer", "Chihuahua", "German Shepper", "Rottweiler")
xyz = list (myBFF)
print ('SEE now we have a list class: ' , xyz)
#print(type(myBFF))
#print(type(xyz))
# now we will append to the list
xyz.append("Pit Bull")
print(xyz)


#ex 6 function count 

names = ("Lacey", "Kieran", "Al", "anaa", "jhj", "jkhdfjh",
       "anaa", "jhj", "jkhdfjh", "anaa", "jhj", "jkhdfjh"
       "anaa", "jhj", "jkhdfjh","anaa", "jhj", "jkhdfjh"
        "anaa", "jhj", "jkhdfjh", "anaa", "jhj"   "Lacey", "Kieran",
         "Al", "anaa", "jhj", "jkhdfjh",
       "anaa", "jhj", "jkhdfjh", "anaa", "jhj", "jkhdfjh"
       "anaa", "jhj", "jkhdfjh","anaa", "jhj", "jkhdfjh"
        "anaa", "jhj", "jkhdfjh", "anaa", "jhj")

x = names.count("jhj")
print("So the 'jhj' names are exactly" , x)
