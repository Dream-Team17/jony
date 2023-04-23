from django import forms


class AnnouncementCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, min_length=5, max_length=255, label='Введите объявление')


class GroupCreateForm(forms.Form):
    title = forms.CharField(label='Название группы')

