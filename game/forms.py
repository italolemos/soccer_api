from django import forms


class PlayerChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return "{} - {}".format(obj.name, obj.team)
