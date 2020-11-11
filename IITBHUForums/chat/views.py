from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView
from .forms import ComposeForm
from .models import Thread, ChatMessage


class ThreadView(LoginRequiredMixin, FormMixin, DetailView):
    template_name = 'thread.html'
    form_class = ComposeForm

    def get_success_url(self):
        return '/chat/' + self.kwargs.get("username")
    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username  = self.kwargs.get("username")
        obj, created    = Thread.objects.get_or_new(self.request.user, other_username)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        thread = self.get_object()
        user = self.request.user
        message = form.cleaned_data.get("message")
        ChatMessage.objects.create(user=user, thread=thread, message=message)
        return super().form_valid(form)

def chatroom(request):
    list_of_users = []
    for x in Thread.objects.by_user(request.user):
        if x.first != request.user:
            list_of_users.append([x.first,Thread.objects.get_or_new(x.first,x.second)[0]])
        else:
            list_of_users.append([x.second,Thread.objects.get_or_new(x.first,x.second)[0]])
        print(list_of_users[-1])
    return render(request,'chatroom.html', {'list' : list_of_users})