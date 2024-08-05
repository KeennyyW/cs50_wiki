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







# class SearchForm(forms.Form):




def search(request):
    if request.method == "POST":
        user_input = request.GET.get("q")

        if util.get_entry(user_input) is not None:
            return HttpResponseRedirect(reverse("search", kwargs={"title": user_input}))
    
        else:
            render(request, "encyclopedia/204.html")
    else:
        render(request, "encyclopedia/204.html")




#        return HttpResponseRedirect(reverse("search", args=[title]))
 #   else:
  #      return render(request, "encyclopedia/search.html", {
   #         "entries": [entry for entry in util.list_entries() if title in entry]
    #    })




        


