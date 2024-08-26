from django.shortcuts import render,get_object_or_404,redirect

from django.contrib.auth.decorators import login_required,permission_required

from .models import Article

from .forms import ArticleForm


from django .core.paginator import Paginator

def list_article(request):
    
    articles = Article.objects.all()
    
    paginator = Paginator(articles,10)
    page = request.GET.get('page')
    articles_page =paginator.get_page(page)
    
    return render(request,'blog/list_article.html',{'articles':articles_page})
    
    
def detail_article(request,article_id):
    
    article = get_object_or_404(Article,pk =article_id)
    
    return render(request,'blog/detail_article.html',{'article':article})


@login_required
def creer_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('detail_article', article_id=article.id)
    else:
        form = ArticleForm()
    
    return render(request, 'blog/creer_article.html', {'form': form})




@login_required

def modifier_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('detail_article', article_id=article_id)
    else:
        form = ArticleForm(instance=article)
        
    return render(request, 'blog/modifier_article.html', {'form': form})

@login_required
def supprimer_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    
    if request.method == 'POST':
        article.delete()
        return redirect('list_article')
    
    return render(request, 'blog/supprimer_article.html', {'article': article})




            
            


# Create your views here.
