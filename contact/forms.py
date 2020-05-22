from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject"
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Leave a comment"
        }))