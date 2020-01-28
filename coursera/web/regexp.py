import re

# x = "My 2 favourite numbers are 19 and 32"
# y = re.findall('[0-9]+',x)
# print(y)
# y = re.findall('[a-z]+',x)
# print(y)

# z = "This is: an text and: this is some characters"

# a = re.findall('T.+?:',z)
# print(a)

x = "From dani@gmail.com sat 12 nov 2020"
# y = re.findall('\S+@\S+',x)
# print(y)
# x = "From soul.sat@gmail.com sat 12 nov 2020"
# y = re.findall('\S+@\S+',x)
# print(y)


# y = re.findall('^From .*@([^ ]*)',x)
y = re.findall("[^dani]",x)
print(y)
