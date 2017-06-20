# Leetcode + geeksforgeeks

## What it Does

This project suggests articles from geeksforgeeks.org to read for each problem on leetcode.com.

## How it Works

It works by getting a similarity score, more specifically, the cosine similarity of two titiles.

Titles from both sites are stored in the `data` directory in json format. `suggestion.json` gives a list of suggested reading from geeksforgeeks.org for each problem on leetcode.

`gen_md` uses `suggestion.json` to generate `suggestion_list.md` in the `result` directory, and `suggestion_list.pdf` is generated via `pandoc` from the markdown file.

If you want to run the scripts yourself...

- run `python leetcode.py' to get problem titles from leetcode.com. You'll need to configure you name and password as well as specify the location for chrome driver.
- run `python geeksforgeeks.py` to get article titles from geeksforgeeks.org.
- run `python compute.py` to generate the suggestion list. This script can take a *long* time to run...

## You may also like...

Like this?** You may like [Leetcoder](https://itunes.apple.com/us/app/leetcoder/id1069760709?mt=8) too!