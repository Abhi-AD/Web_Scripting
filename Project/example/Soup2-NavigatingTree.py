# Navigating the tree
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

# # # Going down
# print(soup.head)
# print(soup.title)
# print(soup.body.b)
# print(soup.body.a)
# print(soup.find_all("a"))


# #.contents and .children
head_tag = soup.head
# print(head_tag)
# print(head_tag.contents)
title_tag = head_tag.contents[0]
# print(title_tag)
# print(title_tag.contents)
# print(len(soup.contents))
# print(soup.contents[0].name)
text = title_tag.contents[0]
# print(text.contents)
# for child in title_tag.children:
#     # print(child)


# # .descendants
# print(head_tag.contents)
# for child in head_tag.descendants:
#     print(child)
# print(len(list(soup.children)))
# print(len(list(soup.descendants)))


# # string
# print(title_tag.string)
# print(head_tag.contents)
# print(head_tag.string)
# print(soup.html.string)


# # .strings and stripped_strings
# for string in soup.strings:
#     print(repr(string))

# for string in soup.stripped_strings:
#     print(repr(string))


# # # Going up

# parent
title_tag = soup.title
# print(title_tag)
# print(title_tag.parent)
# print(title_tag.string.parent)
html_tag = soup.html
# print(type(html_tag.parent))
# print(soup.parent)

# # #parents
# link = soup.a
# print(link)
# for parent in link.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)


# Going sideways
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", "lxml")
# print(sibling_soup.prettify())

# # .next_sibling and .previous_sibling
# print(sibling_soup.b.next_sibling)
# print(sibling_soup.c.previous_sibling)
# print(sibling_soup.b.previous_sibling)
# print(sibling_soup.c.next_sibling)
# print(sibling_soup.b.string)
# print(sibling_soup.b.string.next_sibling)

# link = soup.a
# print(link)
# print(link.next_sibling)
# print(link.next_sibling.next_sibling)


# # .next_siblings and .previous_siblings
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))

# print("*************")
# for sibling in soup.find(id="link3").previous_siblings:
#     print(repr(sibling))


# # # Going back and forth
# # .next_element and .previous_element
# last_a_tag = soup.find("a", id="link3")
# print(last_a_tag)
# print(last_a_tag.next_sibling)
# # print(last_a_tag.next_element)
# print(last_a_tag.previous_element)
# print(last_a_tag.previous_element.next_element)

# # .next_elements and .previous_elements
# for element in last_a_tag.next_elements:
#     print(repr(element))
