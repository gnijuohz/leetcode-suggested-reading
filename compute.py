"""
generate a reading list from geeksforgeeks.com for
each problems on leetcoder.com

The algorithm is based on this answer: http://stackoverflow.com/a/24129170/1062364
"""

import json
import heapq
import codecs
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

from util import save_to_json_file

SUGGESTION_COUNT = 10
result = []

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    '''remove punctuation, lowercase, stem'''
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def compute_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

with open('data/leetcode_problem_titles.json') as leetcode:
    leets = json.load(leetcode)

with open('data/geeksforgeeks_titles.json') as gfg:
    gfg_posts = json.load(gfg)

for leet_p in leets:
    item = {
        "number": leet_p["number"],
        "title": leet_p["title"],
        "url": leet_p["url"]
    }
    max_queue = []
    heapq.heapify(max_queue)
    for g_post in gfg_posts:
        val = compute_sim(leet_p["title"], g_post["title"])
        if len(max_queue) > SUGGESTION_COUNT-1:
            heapq.heappushpop(max_queue, (val, g_post["title"], g_post["url"]))
        else:
            heapq.heappush(max_queue, (val, g_post["title"], g_post["url"]))
    item["suggested"] = [
        {"title": article[1],
        "url": article[2],
        "score": article[0]} for article in sorted(max_queue, reverse=True) if article[0] > 0]
    result.append(item)

save_to_json_file(result, 'data/suggested.json')