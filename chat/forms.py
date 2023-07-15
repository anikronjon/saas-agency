from django import forms


class ChatGroup(forms.Form):
    group_name = forms.CharField(max_length=20, required=True)

    def __str__(self):
        return self.group_name
