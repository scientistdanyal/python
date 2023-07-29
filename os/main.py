import os


# print(os.name)
# print(os.sep)
# print(os.uname())  # to find system details
# print(os.getcwd())  #to find current working directory

current = os.getcwd()

# for root, dirname, filename in os.walk(current):
#     print(dirname)



if not os.path.exists('new_folder'):
    os.makedirs('new_folder')



new_folder = os.path.join(current, 'new_folder')

new_file = os.path.join(new_folder,'sample.py')

with open(new_file,'w') as f:
    f.write('print("Hello, World")')


print('done')