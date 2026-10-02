from django.shortcuts import render
from .forms import RegistrationForm, MAJORS, PROGRAMMING_LANGUAGES, CLASS_STANDING
# Create your views here.

def register(request):
    if (request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            majorDict = dict(MAJORS)
            # progDict = dict(PROGRAMMING_LANGUAGES)
            classDict = dict(CLASS_STANDING)
            studentName = form.cleaned_data["studentName"]
            studentId = form.cleaned_data["studentId"]
            major = majorDict[form.cleaned_data["major"]]
            classStanding = classDict[form.cleaned_data["classStanding"]]
            progLangs = form.cleaned_data["progLangs"]
            expectedGradYear = form.cleaned_data["expectedGradYear"]
            comments = form.cleaned_data["comments"]
            return render(request, "results.html", {
                "studentName": studentName,
                "studentId": studentId,
                "major": major,
                "classStanding": classStanding,
                "progLangs": progLangs,
                "expectedGradYear": expectedGradYear,
                "comments": comments
            })
    else:
        form = RegistrationForm()
    return render(request,"register.html",{"form":form})