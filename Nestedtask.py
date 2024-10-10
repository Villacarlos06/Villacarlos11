names = [
    ['Alice', 'Bob', 'Charlie']
    ['David', 'Eve', 'Frank']
    ['Grace', 'Heidi', 'Ivan']
    ['Judy', 'Ken', 'Laura']
]    

for data in names:
  for you in data:
    if you == "Alice":
       data.remove("Alice")
    print(data)
    break
    print ("Alice exist, remove from the list")



 else:
      print("Alice not found, Enter a new name to add: ")
      new_name = input("Enter a name:")
      names.append(new_name)


print(names)      

  