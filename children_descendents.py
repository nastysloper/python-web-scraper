'''
Difference between children method and descendents method

children method returns only direct children

descendants method returns direct as well as nested children.

In this example you can see the descendants method returns the navigable string in <title>
'''

from bs4 import BeautifulSoup

in_file = open('tags.html')
data = in_file.read()
in_file.close()
soup = BeautifulSoup(data, 'lxml')

head = soup.head
print("head.contents:")
print len(head.contents)
print head.contents
print('\n')
print("head.descendants:")
print head.descendants
print('\n')
for index, child in enumerate(head.descendants):
    print(index)
    print(child)


