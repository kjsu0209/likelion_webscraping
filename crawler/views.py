from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def main(request):
    info_url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2723064500'

    return render(request, 'home.html')

def parse(request):
    url = request.POST['parse_url']
   
    return render(request, 'parse.html')
