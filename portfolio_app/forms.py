from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "your@email.com"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 6, "placeholder": "Write your message..."}))
