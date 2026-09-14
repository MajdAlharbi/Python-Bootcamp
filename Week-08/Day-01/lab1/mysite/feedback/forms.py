from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(
        choices=[("1", "Poor"), ("5", "Excellent")], required=False
    )


def clean_message(self):
    message = self.cleaned_data["message"]

    if len(message) < 20:
        raise forms.ValidationError("Message must be at least 20 characters.")

    return message
