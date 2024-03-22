data = {}
data['name'] = input("Enter name: ")
data['age'] = int(input("Enter age: "))
data['city'] = input("Enter city: ")

# Open file in append mode
f = open('data.txt', 'a')

# Writing dictionary input to a text file
f.write(str(data) + '\n')

# Close the file
f.close()

print("Data written to data.txt successfully.")




