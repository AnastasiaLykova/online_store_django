from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    extra_context = {'title': 'Блог'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    extra_context = {'title': 'Статья'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counts += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        new_art = form.save()
        new_art.slug = slugify(new_art.title)
        new_art.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body', 'preview')

    def get_success_url(self):
        return reverse('blog:article', args=[self.object.pk])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:list')
