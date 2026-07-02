#list dupes are kept
names = ["A", "Bb", "C", "Bb", "A", 7, "D", "aa", "B","bb"]
roll = [1,2,3,4,5,6,7,8,9]
roll.extend(names)
roll.append(names)
unique_names = set(names)
print(unique_names)
print(roll)
print(roll[1:7]) #this prints the elements from index 1 to 6, (7 is not included)


#set, no dupes are shown
names = {"A", "A", "C", "A", "A", "A",99}; 
unique_names = set(names)
print(unique_names)
a = {1,2,2,3}
b = {3,4,6,5}
c = a|b #joins two sets
print (a.symmetric_difference(b)) #find the elements that are in either of the sets, but not in both
print (c)


#array. arrays keeps the dupes too
from array import array
arr = array('i', [1,2,3,4,5,6,7,8,9])

student1 = {"Math", "Physics", "English", "Computer"}
student2 = {"Physics", "Chemistry", "Math", "pe", 77}
results = student1.union(student2) #this finds the unique values that are in either of the two sets
print(results)
usub = student1 & student2 #this finds the unique values that are common to both sets
print(usub)



#dictionary. dictionary keeps the dupes too
student = {"Alice": 85, "Bob": 90, "Charlie": 78, "Alice": 92} # duplicate key will overwrite the previous value
print(student)
print(student["Alice"])
print(student["Bob"]) # prints 90, the value assigned to the key "Bob