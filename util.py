"""
util functions
"""
import json

import requests
from lxml import etree

def get_doc_root(url):
    """parse html at url"""
    r = requests.get(url)
    html_text = r.text
    my_parser = etree.HTMLParser(encoding='utf-8')
    root = etree.HTML(html_text, parser=my_parser)
    return root

def save_to_json_file(py_obj, filename):
    """save titles to a json file"""
    with open(filename, 'w') as json_file:
        json.dump(py_obj, json_file)
