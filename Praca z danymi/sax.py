#!/usr/bin/python3

import xml.sax

'''

Parser SAX pozwala tylko na odczyt plików xml

'''


class BookHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.author = ""
        self.title = ""
        self.genre = ""
        self.price = ""
        self.publish_date = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "book":
            print('####Book####')
            book_id = attributes['id']
            print(f"\tId: {book_id}")


    def endElement(self, tag):
        if self.CurrentData == "author":
            print(f"\tAuthor: {self.author}")
        elif self.CurrentData == "title":
            print(f"\tTitle: {self.title}")
        elif self.CurrentData == "genre":
            print(f"\tGenre: {self.genre}")
        elif self.CurrentData == "price":
            print(f"\tPrice: {self.price}")
        elif self.CurrentData == "publish_date":
            print(f"\tPublish_date: {self.publish_date}")
        elif self.CurrentData == "description":
            print(f"\tDescription: {self.description}")
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "genre":
            self.genre = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData == "publish_date":
            self.publish_date = content
        elif self.CurrentData == "description":
            self.description = content

    def setDocumentLocator(self, locator):
        pass


def main():
    Handler = BookHandler()
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(Handler)
    parser.parse('sample_xml.xml')

if __name__ == '__main__':
    main()
