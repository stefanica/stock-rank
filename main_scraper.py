import requests
import json
from bs4 import BeautifulSoup

#list of positive keywords
positives = ["gain", "gained", "jumo", "is up", "are up", "rebounded", "surged", "surpass", "exceed", "growth", "upswing", "gains", "rise", "soars"
             "profit", "dividend", "earnings", "bullish", "uptrend", "expansion", "innovation", "success", "prosperity", 
             "appreciation", "opportunity", "asset appreciation", "value investing", "blue-chip stocks", "long-term investment", 
             "capital gains", "stock market rally", "market upswing", "financial stability", "economic growth", 
             "robust performance", "market resilience", "positive outlook", "strong fundamentals", "rising stock prices", 
             "high returns", "market optimism", "stock buybacks", "dividend yield", "shareholder value", "market expansion", 
             "capital appreciation", "market recovery", "solid performance", "earnings growth", "positive sentiment", 
             "investment gains", "market strength", "stable market conditions", "positive trends", "wealth creation", 
             "market prosperity", "value appreciation", "market confidence", "winning stocks", "investment success", 
             "positive momentum", "market gains", "resilient economy"]
#list of negative keywords
negatives = ["losses", "is down", "are down", "issue", "trouble", "losing", "bankruptcy", "collapes", "volatile", "volatility", "fraud", 
             "turmoil", "bubble", "scandal", "fraud", "scam", "lawsuit", "investigation", "Ponzi scheme", "crisis", "collapse", 
             "crash", "downturn", "recession", "bear market", "short selling", "insider trading", "volatility", "default", 
             "delisting", "SEC investigation", "bubble", "economic crisis", "market manipulation", "penny stocks", 
             "pump and dump", "overvalued", "overbought", "debt", "dividend cut", "regulatory issues", "downgrade", 
             "stock fraud", "market correction", "stock bubble", "financial scandal", "margin call", "market turmoil", 
             "earnings miss", "credit downgrade", "accounting fraud", "underperforming", "stock scam", "market uncertainty", 
             "stock manipulation", "market risk", "global economic downturn", "stock volatility", "debt", "economic downturn", 
             "market crash", "financial instability", "overleveraged", "commodity collapse", "missed"]

#gets the all the article text inside p element
def article_text(url: str):
  single_url = url
  # Send a GET request to the URL
  response_url = requests.get(single_url)
  all_text = ""
  # Check if the request was successful (status code 200)
  if response_url.status_code == 200:
      # SLOWER METHOD: Parse the HTML content of the page
      #soup = BeautifulSoup(response_url.text, 'html.parser')

      # FASTER METHOD: Parse the HTML content of the page using the lxml parser
      soup = BeautifulSoup(response_url.text, 'lxml')

      # Find all <p> elements and extract the text
      all_paragraphs = soup.find_all('p')
      # Print the text inside each <p> element
      
      for paragraph in all_paragraphs:
          #print(paragraph.get_text())
          all_text += paragraph.get_text()
  else:
      print(f"Failed to retrieve the webpage. Status code: {response_url.status_code}")
      #pass
  return all_text

#returns a grade for a text string (title, description or artcile body) based on the positives and negatives lists
def string_ranker(all_text: str):
  grade = 0
  for word in positives:
      if word in all_text:
          grade += 10

  for word in negatives:
      if word in all_text:
          grade -= 10
  return grade
  

#searching google using serper.dev API
url = "https://google.serper.dev/news"
payload = json.dumps({
   #### IMPORTANT #### 
   #This is the keyword used for searching on Google. You can also replace the stock name with the company name.
  "q": "apple"
})
headers = {
   #replace this API key with yout own after creating an account on serper.dev (it's free for 2500 entries)
  'X-API-KEY': 'd6af99fb79e24bbc97112f2ed39b430e02eee497',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)

#creating a json based on the response
#json_data = response.json()
#json_data = json.loads(response.text)

json_data = None
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON
    json_response = response.json()
    json_data = json_response
    # Now you can work with the JSON data
else:
    print(f"Failed to make the POST request. Status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging purposes

#create a list of dictionaries with all the articles with title, snippet, url and rank.
articles_list = []
total_rank = 0
for item in json_data['news']:
    dictionary = {}
    dictionary["title"] = item["title"]
    dictionary["snippet"] = item["snippet"]
    dictionary["link"] = item["link"]
    article_rank = string_ranker(item["title"]) + string_ranker(item["snippet"]) + string_ranker(article_text(item["link"]))
    total_rank += article_rank
    dictionary["rank"] = article_rank
    articles_list.append(dictionary)

#Prints the resualts and the total final Stock Rank
for article in articles_list:
  for key, value in article.items():
    print(value)
  print(" ")
print(f"Total Rank: {total_rank}")