from django.shortcuts import get_object_or_404, redirect, render
from gnu.forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    return redirect('gnu:list')

def list(request):
    latest_articles = Article.objects.order_by('-id')[:5]
    context = {'latest_articles': latest_articles}
    return render(request, 'gnu/list.html', context)

def read(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'gnu/read.html', {'article': article})

def form(request):
    return render(request, 'gnu/form.html', {'w': ''})

# def add(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)    
#         if form.is_valid():
#             article = form.save()
#             article.save()
#             return redirect('gnu:read', article_id=article.id)
#     # return render(request, 'gnu/form.html')

def edit(request, article_id):
    if article_id is not None:
        article = get_object_or_404(Article, id=article_id)
        return render(request, 'gnu/form.html', {'w': 'u', 'article': article})

def update(request):
    if request.method == 'POST':
        w = request.POST['w']
        if w == '':
            form = ArticleForm(request.POST)    
            if form.is_valid():
                article = form.save()
                article.save()
                return redirect('gnu:read', article_id=article.id)
        elif w == 'u':
            article_id = request.POST['id']
            # article = get_object_or_404(Article, id=id)
            article = Article.objects.get(id=article_id)
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                article.save()
                return redirect('gnu:read', article_id=article.id)
        else:
            pass # w error
    return redirect('gnu:list')

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('gnu:list')