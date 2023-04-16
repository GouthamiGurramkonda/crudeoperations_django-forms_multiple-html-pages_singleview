from django.shortcuts import render
from django.http import HttpResponse
from app.models import*

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        
        return HttpResponse('data is submeeted')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        Email=request.POST['Email']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,Email=Email)[0]
        WO.save()
        return HttpResponse('webpage insertion is done')
    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    LOW=Webpage.objects.all()
    d={'name':LOW}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get(name=name)
        AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('access record insertion is done')
    

    return render(request,'insert_accessrecord.html',d)



def retrieve_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve_data.html',d)



def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)



def radiobuttun(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'radiobuttun.html',d)