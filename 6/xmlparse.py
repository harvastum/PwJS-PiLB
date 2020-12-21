from xml.sax import saxutils, make_parser
from xml.dom import minidom

class DiscountXML(saxutils.XMLGenerator):
    def __init__(self, *args, **kwargs):
        self.in_price = False
        super().__init__(*args, **kwargs)

    def startElement(self, name, attrs):
        saxutils.XMLGenerator.startElement(self, name, attrs)
        if name == "PRICE":
            self.in_price = True
        else:
            super().startElement(name, attrs)

    def characters(self, content):
        if self.in_price:
            self.in_price = False
            print(content)
            new_price = float(content)/2
            self._write(f'{new_price:.2f}')
        else:
            super().characters(content)
def parse_sax():
    with open('data/cd_catalog.xml', 'r', encoding='utf-8') as infile, \
         open('data/discounted_sax.xml', 'w', encoding='utf-8') as outfile:

        parser = make_parser()
        parser.setContentHandler(DiscountXML(outfile, encoding='utf-8'))
        parser.parse(infile)

def parse_dom():
    with open('data/cd_catalog.xml', 'r') as infile, \
         open('data/discounted_dom.xml', 'w', encoding='utf-8') as outfile:
        document = minidom.parse(infile)
        tags = document.getElementsByTagName("PRICE")
        for tag in tags:
            tag.firstChild.nodeValue = float(tag.firstChild.nodeValue)/2
        document.writexml(outfile)

if __name__ == "__main__":
    parse_sax()
    parse_dom()

