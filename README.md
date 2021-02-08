# newsapp-django
This is a simple django newsapp that demonstrates how to utilise the News API (https://newsapi.org/).

### Getting Started
You will need the following dependencies to run this app.
1. **Python installed.** https://docs.djangoproject.com/en/3.1/topics/install/#install-python and https://www.python.org/downloads/ I have tested it with Python 3.9, though you should be able to run it with an older version of Python.
2. **Django installed.** You can install that from the Django project https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release
3. **News API API key** You will need to sign up for a free API key from News API (https://newsapi.org) (which is free for a month).

### Clone this into your working environment:
1. Clone this repo `git clone https://github.com/vulongtran/newsapp-django.git`.
2. Change directory to this repo using `cd newsapp-django`.
3. Install the newsapi module which is a dependency for this to work. `pip install newsapi-python`.
4. Add your News API key to this line `newsapi = NewsApiClient(api_key='NEWSAPI_API_KEY')` to the `views.py` file which is located in the `newsapp-django>financialnewsapp>views.py` folder.
5. Run the django application, by using this command `python manage.py runserver`.
6. Open this link in your preferred web browser (http://127.0.0.1:8000/).
 
### Bash commands for you to download and run this:
To install this example Django application, run the following commands in your preferred Terminal, Powershell or Git Bash:
```bash
git clone https://github.com/vulongtran/newsapp-django.git
cd newsapp-django
pip install newsapi-python
run `python manage.py runserver`
```
Open this link in your preferred web browser (http://127.0.0.1:8000/) 

### Notes:
Make sure you update the API key in the views.py file which is located in the newsapp-django>financialnewsapp>views.py folder. You will need to go to (https://newsapi.org) to create a free API key (which is free for a month).

As it will give you this error message if you do not have added in the API key or need a valid API key:
`newsapi.newsapi_exception.NewsAPIException: {'status': 'error', 'code': 'apiKeyInvalid', 'message': 'Your API key is invalid or incorrect. Check your key, or go to https://newsapi.org to create a free API key.'}`.
