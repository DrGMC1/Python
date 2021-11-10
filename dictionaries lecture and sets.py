#### a simple dictionary
phonebook = {'black panter':'555-1111',
             'super woman':'555-2222',
             'robin':'555-3333'}
print (phonebook ['black panter'])
print (phonebook ['robin'])


####Creating Dictionaries (From a List)
myPantry = [['candy', 5],['cookies', 16],['ice cream', 2]]
myDict = dict(myPantry)
print(myDict)

#Accessing Values
dogBreeds = {"A" : "Akita", "B" : "Basenji", "C" : "Chesapeake Bay Retriever"}
print("dogBreeds at C:", dogBreeds["C"])
print("dogBreeds at B:", dogBreeds["B"])

###Updating Values
dogBreeds = {"A" : "Akita", "B" : "Basenji", "C" : "Chesapeake Bay Retriever"}
##dogBreeds["B"] = "Beagle"
##print(dogBreeds)

#Adding New Key:Value Pairs
dogBreeds["D"] = "Boxer"
dogBreeds["E"] = "Doberman"
print(dogBreeds)

#Deleting Key:Value Pairs
del dogBreeds["D"]
print(dogBreeds)

#Getting the Number of Elements
dogBreeds = {"A" : "Akita", "B" : "Basenji", "C" : "Chesapeake Bay Retriever"}
print(len(dogBreeds))

#clear method
phonebook1 = {'Chris':'555-1111', 'Katie':'555-2222'}
phonebook1.clear()
print(phonebook1)

#get method
phonebook2 = {'Chris':'555-1111', 'Katie':'555-12345'}
x = phonebook2.get('Katie')
print(x)

# Items Method
phonebook3 = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
x = phonebook3.items()
print (x)

# Keys method
phonebook4 = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
x = phonebook3.keys()
print (x)

#The pop() method
phonebook5 = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
x = phonebook5.pop('Chris')
print (x)
print(phonebook5)

#values method
phonebook6 = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
x = phonebook6.values()
print (x)

