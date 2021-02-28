import json

from xml.etree.ElementTree import (Element,
                                   SubElement,
                                   ElementTree)
from uuid import uuid4

root = Element('bakings')
data = {}

def make_node(root, name, value):
    node = SubElement(root, name.replace(' ', '_'))
    if isinstance(value, (list, dict)):
        make_nodes(value, node)
    else:
        node.text = str(value)

def make_nodes(data, root):
    if isinstance(data, list):
        for data_element in data:
            name = f'id_{uuid4().time_low}'
            make_node(root, name, data_element)

    else:
        for k, v in data.items():
            make_node(root, k, v)



with open('dataj.json', 'r') as json_file:
    data = json.loads(json_file.read())


make_nodes(data, root)
tree = ElementTree(root)


tree.write('test.xml', xml_declaration=True, short_empty_elements=True)



