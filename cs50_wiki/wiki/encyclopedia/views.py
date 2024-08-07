from django.shortcuts import render
import markdown
from . import util
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


def convert_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else: 
        return markdowner.convert(content)




def entry(request, title):
    html_content = convert_to_html(title)
    if html_content is None:
        return render(request,"encyclopedia/204.html")
    else: 
        return render(request,"encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        } )





def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })





def search(request):
    if request.method == "POST":
        user_input = request.POST.get("q")
        content = convert_to_html(user_input)

        if content is not None:
            return HttpResponseRedirect(reverse("entry", kwargs={"title": user_input}))
        
        
        
        else:
            all_entries = util.list_entries()
            entry_reccomendation = []

            for entry in all_entries:

                if user_input.lower() in entry.lower():
                    entry_reccomendation.append(entry)
                
            return render(request, "encyclopedia/search.html", {
                "reccomendation": entry_reccomendation
            } )
        
    
def add(request):
    if request.method == "POST":
        if request.POST.get("textarea_title") in util.list_entries():
            input_title = request.POST.get("textarea_title")
            return render(request,"encyclopedia/alreadyexists.html", {
                "title": input_title
            })

        else:
            title = request.POST.get("textarea_title")
            content = request.POST.get("textarea_content")
            list_entries = util.list_entries()

        util.save_entry(title, content)
    
    return render(request, 'encyclopedia/add_entry.html')






