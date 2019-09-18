from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models
import requests

BASE_CRAIGSLIST_URL = "https://charlotte.craigslist.org/d/apts-housing-for-rent/search/apa"
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get("search")
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features="html.parser")
    post_title = soup.find_all("a", {"class": "result-title"})
    print(post_title)
    frontend = {
        "search": search,
    }
    return render(request, "pages/new_search.html", frontend)