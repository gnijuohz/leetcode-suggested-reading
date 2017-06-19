import json
import codecs

with codecs.open('data/suggested.json') as suggested_file:
    suggested = json.load(suggested_file)

with codecs.open('result/suggestion_list.md', 'w', 'utf-8') as suggestion_list:
    for problem in suggested:
        leet_problem = u'## [{title}]({url})({number})  \n'.format(title=problem["title"], url=problem["url"], number=problem["number"])
        suggestion_list.write(leet_problem)
        suggestions = u"  \n".join([u'- [{title}]({url})({score})'.format(title=suggestion["title"], url=suggestion["url"], score=suggestion["score"]) for suggestion in problem["suggested"]])
        suggestion_list.write(suggestions)
        suggestion_list.write("\n\n")