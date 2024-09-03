from bs4 import BeautifulSoup
from bs4.builder import builder_registry
from bs4 import CData

# parser used the default variable used
html = "html.parser"
lxml = "lxml"
lxmlX = "lxml-xml"
xml = "xml"
html5 = "html5lib"

# with open("index.html") as fp:
#     soup = BeautifulSoup(fp, html)

soup = BeautifulSoup("<html>data</html>", html)
# print(BeautifulSoup("Sacr&eacute; bleu!", html5).prettify())

# Tag
soup = BeautifulSoup('<b  id="boldest">Extremely bold</b>', html)
tag = soup.b
# print(type(tag))


# Name
tag.name = "blockquote"
# print(tag)
# print(tag["id"])


# Attributes
# print(tag["id"])
# print(tag.attrs)

tag["id"] = "verybold"
tag["another-attribute"] = 1
# print(tag)

del tag["id"]
del tag["another-attribute"]
# print(tag)
# print(tag["id"])
# print(tag.get("id"))


# Multi-valued attributes
css_soup = BeautifulSoup('<p class="body"></p>', html)
# print(css_soup.p["class"])
css_soup = BeautifulSoup('<p class="body strikeout"></p>', html)
# print(css_soup.p["class"])

id_soup = BeautifulSoup('<p id="my id"></p>', html)
# print(id_soup.p["id"])

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', html)
# print(rel_soup.a["rel"])
rel_soup.a["rel"] = ["index", "contents"]
# print(rel_soup.p)

no_list_soup = BeautifulSoup(
    '<p class="body strikeout"></p>', html, multi_valued_attributes=None
)
# print(no_list_soup.p["class"])

# print(id_soup.p.get_attribute_list("id"))

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', xml)
# print(xml_soup.p["class"])

# print(builder_registry.lookup(html).DEFAULT_CDATA_LIST_ATTRIBUTES)


# NavigableString

# print(tag.string)
# print(type(tag.string))

unicode_string = str(tag.string)
# print(unicode_string)
# print(type(unicode_string))

tag.string.replace_with("No longer bold")
# print(tag)


# BeautifulSoup
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", xml)
footer = BeautifulSoup("<footer>Here's the footer</footer>", xml)
# print(doc.find(string="INSERT FOOTER HERE").replace_with(footer))
# print(doc)
# print(soup.name)


# Comments and other special strings

soup = BeautifulSoup("<b><!--Hey, buddy. Want to buy a used parser?--></b>", html)
comment = soup.b.string
# print(type(comment))
# print(comment)
# print(soup.b.prettify())


cdata = CData("A CDATA block")
comment.replace_with(cdata)
# print(soup.b.prettify())
