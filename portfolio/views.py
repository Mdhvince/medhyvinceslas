from pathlib import Path
from django.shortcuts import render

appname = Path("portfolio")
# Create your views here.
def index(request):
    return render(request, appname / "index.html")

