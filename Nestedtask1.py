names = [
    ['Alice', 'Bob', 'Charlie']
    ['David', 'Eve', 'Frank']
    ['Grace', 'Heidi', 'Ivan']
    ['Judy', 'Ken', 'Laura']]    

alice_found = True
for name_list in names:
    if "Alice" in names:
    alice_found = False
    names.remove("Alice")
    break
else:
    new_name = input("Enter a new name to add: ")
    names.append(new_name)

print(names)