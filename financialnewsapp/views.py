from django.shortcuts import render
from django.shortcuts import render
from newsapi import NewsApiClient
import json
# Initializing this django app with a https://newsapi.org/ api key which newsapi offers for one month free to test with. 
newsapi = NewsApiClient(api_key='NEWSAPI_API_KEY')
all_articles = newsapi.get_everything(q='bitcoin',sources='yahoo,the-verge,cnbc,bbc-news',
language='en',sort_by='relevancy')

# loading all_articles as json
new = json.dumps(all_articles)
# This will allow us to create creat dictionary from the json which will make easier for us to use the data
data = json.loads(new)
def index(request):
    return render(request,'news/index.html',{'data':data})
