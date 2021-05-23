from django.shortcuts import render, redirect, HttpResponse
from .models import Articles,Comments,Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .forms import ArticleForm, AuthUserForm, RegisterUserForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from hitcount.views import HitCountDetailView
from django.template import Context, Template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.base import View




def oferta(request):
    return render(request, 'oferta.html')


class GenreYear:
    def get_genres(self):
        return Category.objects.all()

class CategoryViewSet(View,GenreYear):

    def get(self, request, pk):

        get_genres = Category.objects.all()
        forum_list = Articles.objects.all()
        posts = Articles.objects.filter(category__id = pk)
        menu = Category.objects.all()

        return render(request, 'home.html', {'posts':posts, 'menu':menu, 'get_genres': get_genres, 'forum_list':forum_list} )



class IndexList(View):

    def get(self,request):
        category = Category.objects.all()
        context = {"category": category}
        return render(request, 'ind.html', context)





class HomeListView(ListView, GenreYear ):
    model = Articles
    template_name = 'index.html'
    context_object_name = 'list_articles'
    queryset = Articles.objects.filter(ok=True)
    paginate_by = 4




class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)



class HomeDetailView(CustomSuccessMessageMixin, FormMixin, HitCountDetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'get_article'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан, ожидайте модерации'
    count_hit = True

    def get_success_url(self, **kwargs):

        return reverse_lazy('detail_page', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def update_comment_status(request, pk, type):
    item = Comments.objects.get(pk=pk)
    if request.user != item.article.author:
        return HttpResponse('deny')

    if type == 'public':
        import operator
        item.status = operator.not_(item.status)
        item.save()
        template = 'comment_item.html'
        context = {'item':item, 'status_comment':'Комментарий опубликован'}
        return render(request,template,context)
    elif type == 'delete':
        item.delete()
        return HttpResponse('''

        <div class="alert alert-success">
        Комментарий удален
        </div>
        ''')


    return HttpResponse('1')


class ArticleCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Articles.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)




class ArticleUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Articles
    template_name = 'edit_page.html'
    success_url = reverse_lazy('post_author')
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

class Search(ListView):

    def get_queryset(self):
        return Articles.objects.filter(name__icontains=self.request.GET.get("q"))


    context_object_name = 'a'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'

        return context


def post_author(request):
    post = Articles.objects.filter(author__id = request.user.id)
    return render(request, 'homes.html', {'post':post})
