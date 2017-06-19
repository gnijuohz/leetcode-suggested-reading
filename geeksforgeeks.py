"""
get all article titles and their urls from geeksforgeeks.org
"""
import time
import json

from tqdm import tqdm

from util import get_doc_root, save_to_json_file

def get_title(el):
    """get title and url of an article"""
    title_ele = el.cssselect('a')[0]
    url = title_ele.attrib['href']
    title = title_ele.text
    return [url, title]

def get_last_page_num():
    """get total number of pages on geeksforgeeks.com
    TODO: replace this const"""
    return 651

def save_titles_to_json(titles):
    """save titles to a json file"""
    with open('data/geeksforgeeks_titles.json', 'w') as json_file:
        json.dump(titles, json_file)

def main():
    """entry point"""
    titles = []
    last_page_num = get_last_page_num()
    for page_num in tqdm(range(last_page_num + 1)):
        url = 'http://www.geeksforgeeks.org/page/{page_num}/'.format(
            page_num=page_num)
        time.sleep(0.2)
        root = get_doc_root(url)
        for article_el in root.cssselect('h2.entry-title'):
            title_ele = article_el.cssselect('a')[0]
            title_url, title_text = get_title(title_ele)
            titles.append({
                "title": title_text,
                "url": title_url
            })
    save_to_json_file(titles[::-1], 'data/geeksforgeeks_titles.json')

main()
