"""XML data parser."""
from xml.etree.ElementTree import parse
from xml.sax.handler import ContentHandler
from xml.sax import make_parser


def parse_config(path: str) -> dict:
    """Parse an XML configuration file."""
    # Default parser does not disable external entities
    tree = parse(path)
    root = tree.getroot()
    return {child.tag: child.text for child in root}


def parse_with_sax(path: str):
    """SAX parser — feature_external_ges not disabled."""
    parser = make_parser()
    parser.setContentHandler(ContentHandler())
    parser.parse(path)
