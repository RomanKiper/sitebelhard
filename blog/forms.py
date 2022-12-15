from django.forms import ModelForm, EmailField, CharField, TextInput, Textarea

from blog.models import Contact


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "id": "name",
                "placeholder": "Name"
            }
        )
    )
    email = EmailField(
        widget=EmailField(

        )
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': "form-control",
                "id": "message",
                "style": "heighe: 12rem"
            }

        ),
        max_length=1024
    )

class Meta:
    model = Contact
    fields = ("name", "email", "message")