# file = open('turtle.txt','r')


# content = file.read()

# print('turtle_name' in content)

# file.close()


with open('turtle.txt','r') as file:
    content = file.read()
    print(content)