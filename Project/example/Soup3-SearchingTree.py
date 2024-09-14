html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from bs4 import BeautifulSoup, NavigableString


soup = BeautifulSoup(html_doc, "html.parser")


# # a sting
# print(soup.find_all("b"))

# # A regular expression
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)

# for tag in soup.find_all(re.compile("t")):
#     print(tag.name)


# # A list
# print(soup.find_all(["a", "b"]))

# """true"""
# for tag in soup.find_all(True):
#     print(tag.name)


# A function
# def has_class_but_no_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")


# print(soup.find_all(has_class_but_no_id))


# def not_lacie(href):
#     return href and not re.compile("lacie").search(href)


# print(soup.find_all(href=not_lacie))


# def surrounded_by_strings(tag):
#     return isinstance(tag.next_element, NavigableString) and isinstance(
#         tag.previous_element, NavigableString
#     )


# for tag in soup.find_all(surrounded_by_strings):
#     print(tag.name)


# # find_all()
# print(soup.find_all("title"))
# print(soup.find_all("p", "title"))
# print(soup.find_all("a"))

# print(soup.find_all(id="link2"))
# print(soup.find(string=re.compile("sisters")))


# # The name argument
# print(soup.find_all("title"))

# # The keyword arguments
# print(soup.find_all(id="link2"))
# print(soup.find_all(href=re.compile("elsie")))
# print(soup.find_all(id=True))
# print(soup.find_all(href=re.compile("elsie"), id="link1"))
# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# print(data_soup.find_all(data-foo="value")) # syntax: error
# print(data_soup.find_all(attrs={"data-foo": "value"}))
name_soup = BeautifulSoup('<input name="email"/>', features="lxml")
print(name_soup.find_all(name="email"))
print(name_soup.find_all(attrs={"name": "email"}))
