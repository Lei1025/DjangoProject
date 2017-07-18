from django import forms
from myapp.models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model= Topic
        fields = {"subject","intro_course","time","avg_age"}
        widgets = {"time":forms.RadioSelect()}
        labels = {"intro_course":'This should be an introductory level course',"time":u'Preferred Time','avg_age':u'What is your age?'}

class InterestForm(forms.Form):
    interest = forms.TypedChoiceField(widget=forms.RadioSelect,choices=((1,'Yes'),(0,"No")))
    age = forms.IntegerField(label='Age',initial=20)
    comment = forms.CharField(widget=forms.Textarea(),label='Additional Comments',required=False,)
