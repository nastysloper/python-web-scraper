from bs4 import BeautifulSoup


def read_file():
    in_file = open('tags.html')
    data = in_file.read()
    in_file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

meta = soup.meta  # target the first occurrence of the meta tag
print(meta)
print(meta.get('charset'))  # supports get method as well as
print(meta['charset'])  # access via a dictionary

div = soup.div  # target the first occurrence of the div tag
print(div)
print(div)

body = soup.body
print("body:")
print(body)

'''  Modify some attributes (how would this be useful?)

body['style'] = 'new style'

'''

body['style'] = 'that new style'
print body['class']
print body['style']

title = soup.title
print title.string
print('\n\n\n')
print("Using body.contents, children are: ")
for child in body.contents:
    print(child if child is not None else '')