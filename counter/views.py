from django.shortcuts import render

# Create your views here.
def home(request):
    text = ""

    return render(request, "index.html", {'text': text})

def result(request):
    text = request.GET["text"].split()
    a = len(request.GET["text"])
    b = 0
    for i in text:
        b += len(i)
    return render(request, "index.html", {'text': text, 'a': a, 'b': b})