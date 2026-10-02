from django import forms

MAJORS =[
    ("SDEV","Software Development"),
    ("CS","Computer Science"),
    ("GDEV","Game Development"),     
         ]
CLASS_STANDING=[
    ("FR","Freshman"),
    ("SM","Sophmore"),
    ("JR","Junior"),
    ("SR","Senior"),
]
PROGRAMMING_LANGUAGES=[
    ("C","C"),
    ("C#","C#"),
    ("Py","Python"),
    ("HTML","HTML"),
    ("JS","Java Script"),
    ("CSS","Cascading Style Sheets"),
    ("Java","Java"),
    ("SQL","SQL"),
]
class RegistrationForm(forms.Form):
    studentName = forms.CharField(max_length=100)
    studentId = forms.CharField(max_length=10)
    major = forms.ChoiceField(choices=MAJORS, widget=forms.Select())
    classStanding = forms.ChoiceField(choices=CLASS_STANDING,widget=forms.RadioSelect())
    progLangs = forms.MultipleChoiceField(choices=PROGRAMMING_LANGUAGES,widget=forms.CheckboxSelectMultiple())
    expectedGradYear = forms.IntegerField(widget=forms.NumberInput())
    comments = forms.CharField(max_length=1000,widget=forms.Textarea)