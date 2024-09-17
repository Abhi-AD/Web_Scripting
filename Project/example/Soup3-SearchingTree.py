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
# name_soup = BeautifulSoup('<input name="email"/>', features="lxml")
# print(name_soup.find_all(name="email"))
# print(name_soup.find_all(attrs={"name": "email"}))


# # Searching by CSS class
# print(soup.find_all("a", class_="sister"))
# print(soup.find_all(class_=re.compile("itl")))
# def has_six_characters(css_class):
#     return css_class is not None and len(css_class) == 6
# print(soup.find_all(class_=has_six_characters))
# css_soup = BeautifulSoup('<p class="body strikeout"></p>', features="lxml")
# print(css_soup.find_all("p", class_="strikeout"))
# print(css_soup.find_all("p", class_="body"))
# print(css_soup.find_all("p", class_="body strikeout"))
# print(css_soup.find_all("p", class_="strikeout body"))
# print(css_soup.select("p.strikeout.body"))
# print(soup.find_all("a", attrs={"class": "sister"}))


#  # # The string argument
# print(soup.find_all(string="Elsie"))
# print(soup.find_all(string=["Tillie", "Elsie", "Lacie"]))
# print(soup.find_all(string=re.compile("Dormouse")))
# def is_the_only_string_within_a_tag(s):
#     return s == s.parent.string
# print(soup.find_all(string=is_the_only_string_within_a_tag))
# print(soup.find_all("a", string="Elsie"))
# # # The string argument is new in Beautiful Soup 4.4.0. In earlier versions it was called text:
# # print(soup.find_all("a", text="Elsie"))


# # # The limit argument
# print(soup.find_all("a", limit=2))


# # # The recursive argument
# print(soup.html.find_all("title"))
# print(soup.html.find_all("title", recursive=False))


# # # Calling a tag is like calling find_all()
# print(soup.find_all("a"))
# print(soup("a"))
# print(soup.title.find_all(string=True))
# print(soup.title(string=True))

# # # find()
# print(soup.find_all("title", limit=1))
# print(soup.find("title"))
# print(soup.find("nosuchtag"))
# print(soup.head.title)
# print(soup.find("head").find("title"))
