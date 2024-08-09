from django.shortcuts import render
import markdown
from . import util
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import random


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
        message = "Page not found"
        return render(request,"encyclopedia/204.html", {
            "content": message
        })
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
            title_add = request.POST.get("textarea_title")
            content_add = request.POST.get("textarea_content")
            list_entries = util.list_entries()

            #if not title and not content:
              #  message = "Title or content has not been set"
             #   return render(request, "encyclopedia/204.html", {
              #      "content": message
               # })

            util.save_entry(title_add, content_add)
    
    return render(request, 'encyclopedia/add_entry.html')


def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("new_textarea_content")

        
        
     
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit_page.html", {
        "link": title,
        "content": content  
    })  



def rand(request):
    list = util.list_entries()
    random_entry = random.choice(list)
    random_content = convert_to_html(random_entry)
    title = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {
        "content": random_content,
        "title": title
    } )







# save entry function and redirect to index.html (path="")





    