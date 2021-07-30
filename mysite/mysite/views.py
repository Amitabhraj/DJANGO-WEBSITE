# I have created this file - Amitabh
from django.http import HttpResponse
from django.shortcuts import render


def Amitabh(request):
    return render(request, 'index.html')


def analyz(request):
    #take text
    dj= request.POST.get('text','default')
    
    
    #check checkbox value
    remove_punc= request.POST.get('removepunc','off')
    upper= request.POST.get('upper','off')
    newline= request.POST.get('newline','off')
    spaceRemover= request.POST.get('ExtraSpaceRemover','off')
    charcount= request.POST.get('CharacterCount','off')




    #Check which checkbox is on
    if remove_punc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in dj:
            if char not in punctuations:
                analyzed= analyzed+char
                
        params={"analyze_text":analyzed}
        dj = analyzed




    if(upper=="on"):
        analyzed=""
        for char in dj:
            analyzed=analyzed+char.upper()
            
        params={"analyze_text":analyzed}
        dj = analyzed




    if(newline=="on"):
        analyzed=""
        for char in dj:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
                
        params={"analyze_text":analyzed}
        dj = analyzed



    if(spaceRemover=="on"):
        analyzed=""
        for index, char in enumerate(dj):
            if dj[index]==" " and dj[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
                 
        params={"analyze_text":analyzed}



    if(charcount=="on"):
        analyzed=""
        for index, char in enumerate(dj):
            if dj[index]==" ":
                pass
            else:
                analyzed=analyzed+char
                anal=(len(analyzed))
        params={"char":"Character Count:-","analyze_text":anal,}
        dj=analyzed
        
        
        

    if(remove_punc != "on" and newline !="on" and spaceRemover!="on" and upper!="on" and charcount!="on"):
        return HttpResponse("<h1>please select any operation and try again</h1>")



    return render(request, 'analyze.html', params)

