import string
test_string = "Tutorials point is a learning platform"
# printing original string
print ("The original string is: " + test_string)
# using sum() + strip() + split() function
res = sum([i.strip(string.punctuation).isalpha() for i in
test_string.split()])
# no of words
print ("The number of words in string are : " + str(res))