# Leetcode + geeksforgeeks

## Idea

This project suggests articles from geeksforgeeks.org to read for each problem on leetcode.com.

## How It Works

It works by getting a similarity score, more specifically, the cosine similarity of two titiles.

Titles from both sites are stored in the `data` directory. `suggestion.json` gives a list of suggested reading from geeksforgeeks.org for each problem on leetcode.

- run `python leetcode.py' to get problem titles from leetcode.com. You'll need to configure you name and password as well as specify the location for chrome driver.
- run `python geeksforgeeks.py` to get article titles from geeksforgeeks.org.
- run `python compute.py` to generate the suggestion list. Note this list can take a long time to run...

