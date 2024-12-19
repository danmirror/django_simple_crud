from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    old = forms.IntegerField()
    number = forms.IntegerField()

    def print_user(self):
        print(f"name {self.cleaned_data['name']}, old {self.cleaned_data['old']}, number {self.cleaned_data['number']}")