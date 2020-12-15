#!/usr/bin/python3

import xml.dom.minidom

# class BookHandler(xml.sax.handler.ContentHandler):
#
#     def __init__(self):
#         self.CurrentData = ""
#         self.author = ""
#         self.title = ""
#         self.genre = ""
#         self.price = ""
#         self.publish_date = ""
#         self.description = ""
#
#     def startElement(self, tag, attributes):
#         self.CurrentData = tag
#         if tag == "book":
#             print('####Book####')
#             book_id = attributes['id']
#             print(f"\tId: {book_id}")
#
#
#     def endElement(self, tag):
#         if self.CurrentData == "author":
#             print(f"\tAuthor: {self.author}")
#         elif self.CurrentData == "title":
#             print(f"\tTitle: {self.title}")
#         elif self.CurrentData == "genre":
#             print(f"\tGenre: {self.genre}")
#         elif self.CurrentData == "price":
#             print(f"\tPrice: {self.price}")
#         elif self.CurrentData == "publish_date":
#             print(f"\tPublish_date: {self.publish_date}")
#         elif self.CurrentData == "description":
#             print(f"\tDescription: {self.description}")
#         self.CurrentData = ""
#
#     def characters(self, content):
#         if self.CurrentData == "author":
#             self.author = content
#         elif self.CurrentData == "title":
#             self.title = content
#         elif self.CurrentData == "genre":
#             self.genre = content
#         elif self.CurrentData == "price":
#             self.price = content
#         elif self.CurrentData == "publish_date":
#             self.publish_date = content
#         elif self.CurrentData == "description":
#             self.description = content
#
#     def setDocumentLocator(self, locator):
#         pass

def print_books_in_catalog(collection):

    books = collection.getElementsByTagName('book')

    for book in books:
        print("####Book####")
        if book.hasAttribute('id'):
            print(f"Id: {book.getAttribute('id')}")

        if book.getElementsByTagName('author'):
            author = book.getElementsByTagName('author')[0]
            print(f"Author: {author.childNodes[0].data}")

        if book.getElementsByTagName('title'):
            title = book.getElementsByTagName('title')[0]
            print(f"Title: {title.childNodes[0].data}")

        if book.getElementsByTagName('price'):
            price = book.getElementsByTagName('price')[0]
            print(f"Price: {price.childNodes[0].data}")

        if book.getElementsByTagName('publish_date'):
            date = book.getElementsByTagName('publish_date')[0]
            print(f"Publish date: {date.childNodes[0].data}")

        if book.getElementsByTagName('description'):
            description = book.getElementsByTagName('description')[0]
            print(f"Description: {description.childNodes[0].data}")

def make_discount(collection, discount_percent):



    books = collection.getElementsByTagName('book')

    for book in books:

        if book.getElementsByTagName('price'):
            price = book.getElementsByTagName('price')[0]
            price.childNodes[0].data = str((1.0 - discount_percent/100) * float(price.childNodes[0].data))
            print(f"Price: {price.childNodes[0].data}")


def main():

    DOMTree = xml.dom.minidom.parse('sample_xml.xml')
    collection = DOMTree.documentElement

    print_books_in_catalog(collection)
    make_discount(collection, 50)
    print_books_in_catalog(collection)

    with open('output_xml.xml', 'w') as file:
        DOMTree.writexml(file)

if __name__ == '__main__':
    main()
