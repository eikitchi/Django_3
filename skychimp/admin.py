from django.contrib import admin
from skychimp.models import Customer, Sending, Message, Attempt


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)


@admin.register(Sending)
class SendingAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'scheduled_time', 'frequency', 'status')
    list_filter = ('scheduled_time', 'frequency', 'status')

    def message_subject(self, obj):
        return obj.message.subject
    message_subject.short_description = 'Message Subject'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at')
    list_filter = ('created_at',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('sending_message_subject', 'sent_at', 'status', 'response')
    list_filter = ('sending__scheduled_time', 'status', 'sent_at', 'response')

    def sending_message_subject(self, obj):
        return obj.sending.message.subject
    sending_message_subject.short_description = 'Sending Message Subject'