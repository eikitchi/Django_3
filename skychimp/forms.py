from django import forms
from skychimp.models import Message, Sending


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']


class SendingForm(forms.ModelForm):
    class Meta:
        model = Sending
        fields = ['message', 'frequency', 'status', 'scheduled_time', 'start_date', 'end_date']
