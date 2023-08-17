from random import sample

import django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Post
from skychimp.forms import MessageForm, SendingForm
from skychimp.models import *
from skychimp.services import send_email


class IndexView(TemplateView):
    template_name = 'skychimp/skychimp_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_sendings'] = Sending.objects.count()
        context['active_sendings'] = Sending.objects.filter(status=Sending.LAUNCHED).count()
        context['unique_customers'] = Customer.objects.filter(clients__status=Sending.LAUNCHED).distinct().count()
        all_posts = list(Post.objects.all())
        context['random_blog_posts'] = sample(all_posts, min(3, len(all_posts)))
        return context


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    extra_context = {
        'object_list': Customer.objects.all(),
        'title': 'Все клиенты'  # дополнение к статической информации
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('skychimp.view_client'):
            return queryset
        return Customer.objects.filter(created_by=self.request.user)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ('name', 'email', 'comment', 'created_by',)
    success_url = reverse_lazy('skychimp:customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ('name', 'email', 'comment', 'created_by', 'is_active',)

    def get_success_url(self):
        return reverse('skychimp:customer_view', args=[str(self.object.pk)])


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('skychimp:customer_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'message_list': Message.objects.all(),
        'title': 'Все Сообщения'  # дополнение к статической информации
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('subject', 'body',)
    success_url = reverse_lazy('skychimp:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ('subject', 'body',)

    def get_success_url(self):
        return reverse('skychimp:sending_view', args=[str(self.object.pk)])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('skychimp:message_list')


class SendingListView(LoginRequiredMixin, ListView):
    model = Sending
    extra_context = {
        'title': 'Все Рассылки'  # дополнение к статической информации
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('skychimp.view_sending'):
            return queryset
        return Sending.objects.filter(created_by=self.request.user)


class SendingDetailView(LoginRequiredMixin, DetailView):
    model = Sending


class SendingCreateView(LoginRequiredMixin, CreateView):
    model = Sending
    form_class = SendingForm
    template_name = 'skychimp/sending_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_formset'] = formset_factory(MessageForm, extra=1)  # Создаем формсет для сообщения
        return context

    def form_valid(self, form):
        message_formset = formset_factory(MessageForm, extra=1)(
            self.request.POST)  # Инициализируем формсет с данными из POST
        if message_formset.is_valid():  # Проверяем валидность формсета
            self.object = form.save(commit=False)
            self.object.created_by = self.request.user
            self.object.save()

            for message_form in message_formset:
                message = message_form.save()
                self.object.message = message

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, message_formset=message_formset))


class SendingUpdateView(LoginRequiredMixin, UpdateView):
    model = Sending
    fields = ('message', 'frequency', 'status',)

    def get_success_url(self):
        return reverse('skychimp:sending_view', args=[str(self.object.pk)])


class SendingDeleteView(LoginRequiredMixin, DeleteView):
    model = Sending
    success_url = reverse_lazy('skychimp:sending_list')


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    extra_context = {
        'object_list': Attempt.objects.all(),
        'title': 'Все Рассылки'  # дополнение к статической информации
    }


class AttemptDetailView(DetailView):
    model = Attempt


def set_is_active(request, pk):
    customer_item = get_object_or_404(Customer,
                                      pk=pk)  # get_object_or_404 ищет объект модели если не находит выводит ошибку
    if customer_item.is_active:
        customer_item.is_active = False
    else:
        customer_item.is_active = True
    customer_item.save()
    return redirect(reverse('skychimp:customer_list'))


def set_status_sending(request, pk):
    sending_item = get_object_or_404(Sending,
                                     pk=pk)  # get_object_or_404 ищет объект модели если не находит выводит ошибку
    if sending_item.status == Sending.CREATED:
        sending_item.status = Sending.COMPLETED
        sending_item.save()
    else:
        sending_item.status = Sending.CREATED
        sending_item.save()
    return redirect(reverse('skychimp:sending_list'))
