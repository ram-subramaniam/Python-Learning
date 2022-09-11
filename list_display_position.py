Names =  ['Ram','Sam','Tara','Carolina']

# Position and upper
print(Names[0].upper())

#Concat
print("Name is "+Names[2])

#changing or replacing -1 is last in the line.
Names[-1]='Tom'
print("New NAME is "+Names[-1])

# Append new value to list.
Names.append ('Tom')
print(Names)

# Insert in a position
Names.insert (1,"Preetha")
print(Names)

# delete in a position
del Names[2]
print(Names)