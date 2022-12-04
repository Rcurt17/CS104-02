Names = []
for y in range (10):
    name = input ("Enter names for list: ")
    Names.append(name)
print(Names)

for y in range (10):
    print (Names.pop (0))


print (Names)
