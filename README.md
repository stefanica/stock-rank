# stock-rank
Tiny stock news scraper. Python script for scraping online financial newspapers and ranking a specific stock.

This script uses serper.dev API for google scrap/search and Beutiful Soup library/package for extracting the paragraphs from the google results.
For this to run on your machine (IDE or Rich Text Editor, VS Code for example) you need to instal Python (Guide: https://kinsta.com/knowledgebase/install-python/), install Python Requests (Guide: https://www.activestate.com/resources/quick-reads/how-to-pip-install-requests-python-package/), install Beautiful Soup (Guide: https://scrapeops.io/python-web-scraping-playbook/installing-beautifulsoup/) and lxml (Guide: https://lxml.de/installation.html). If you are using Visual Studio Code you need to also install the Python extension.

There are two lists: one with positive stock keywords and one with negative stock keywords. The script searches through each title, description and article text from the first 10 Google News results (you can modify yout serper.dev API to go through more than 10 result), and if it finds that the respective text contains a positive keyword it ads +10 to the stock score, if its a negative one it sutracts -10. Each article will be graded and you will also have the total score at the end. 

The score starts from 0, and theoreticaly, anything above 0 can be considered as a buy option. 