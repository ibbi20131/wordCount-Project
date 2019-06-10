from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html", {"intro":"I will count your words"})

def gay(request):
    return HttpResponse("<h1>I'm not you are</h1>")

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word]=1
    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {"fulltext":fulltext, "count":len(wordlist), "sortedWords":sortedWords})
