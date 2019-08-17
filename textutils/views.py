## This is my my firsrt file --- Rahul
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyzer(request):
    djtext= request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc=='on':
        puctuation = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed= ""
        for char in djtext:
            if char not in puctuation:
                analyzed= analyzed + char
        params = {'purpose':'remove puctuaatuons', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyzer.html', params)
    if fullcaps=='on':
        analyzed= ""
        for char in djtext:
                analyzed= analyzed + char.upper()
        params = {'purpose':'Capitalized below as', 'analyzed_text': analyzed}
        djtext = analyzed
    #    return render(request, 'analyzer.html', params)
    if spaceremove == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " " ):
                analyzed = analyzed + char
        params = {'purpose': 'After space remove', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyzer.html', params)
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed
    #return render(request, 'analyzer.html', params)
    if charcount == 'on':
        count = 0
        for char in djtext:
            if char!= " ":
                count+=1
        params = {'purpose': 'Charater count is ', 'Count': count}
    return render(request, 'analyzer.html', params)


