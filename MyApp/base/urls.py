from django.urls import path
from .views import Tarefalist, TarefaDetail, TarefaCreate, TarefaUpdate, TarefaDelete, TarefaLoginView, RegisterPage, SenhaReset
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TarefaLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view() , name='register'),
    path('reset/',SenhaReset.as_view() , name='reset'),
    path('',Tarefalist.as_view(), name='tarefas'),
    path('tarefa/<int:pk>/',TarefaDetail.as_view(),name='tarefa'),
    path('tarefa-create/', TarefaCreate.as_view(), name='tarefa-create'),
    path('tarefa-update/<int:pk>', TarefaUpdate.as_view(), name='tarefa-update'),
    path('tarefa-delete/<int:pk>', TarefaDelete.as_view(), name='tarefa-delete'),
]