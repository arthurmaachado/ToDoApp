from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarefa
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import login
# Create your views here.



class TarefaLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tarefas')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tarefas')
        return super(RegisterPage,self).get(*args,**kwargs)

class SenhaReset(FormView):
    template_name = 'base/reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('tarefas')
    redirect_authenticated_user = True



class Tarefalist(LoginRequiredMixin,ListView):
    model = Tarefa
    context_object_name = 'tarefas'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tarefas'] = context['tarefas'].filter(usuario=self.request.user)
        context['contagem'] = context['tarefas'].filter(completa=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tarefas'] = context['tarefas'].filter(titulo__icontains=search_input)
        context['search_input'] = search_input
        return context


class TarefaDetail(LoginRequiredMixin,DetailView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'base/tarefa.html'

class TarefaCreate(LoginRequiredMixin,CreateView):
    model = Tarefa
    fields = ['titulo','descriçao','completa']
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(TarefaCreate, self).form_valid(form)

class TarefaUpdate(LoginRequiredMixin,UpdateView):
    model = Tarefa
    fields = ['titulo','descriçao','completa']
    success_url = reverse_lazy('tarefas')

class TarefaDelete(LoginRequiredMixin,DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    success_url = reverse_lazy('tarefas')

