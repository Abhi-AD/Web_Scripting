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
from bs4 import BeautifulSoup

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
def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")


print(soup.find_all(has_class_but_no_id))
