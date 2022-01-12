from django.shortcuts import render
from website.models import Article

# Create your views here.


def index(request):
    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, 'index.html', context)
def ravaror(request):
    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, 'components/statichtml/ravaror.html', context)
def forex(request):
    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, 'components/statichtml/forex.html', context)
def krypto(request):
    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, 'components/statichtml/krypto.html', context)
def cfdHandel(request):
    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, 'components/statichtml/cfdHandel.html', context)  
def dayTrading(request):
    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, 'components/statichtml/dayTrading.html', context) 
def brokers(request):
    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, 'components/statichtml/brokers.html', context)

def articles(request):
    articles = Article.objects.all().order_by('-created_at')
    context = {
        'articles':articles,
    }
    return render(request, 'components/statichtml/articles.html', context)

def articleDetail(request, slug):
    article = Article.objects.get(slug=slug)
    template = ''
    if(article.category == 'B'):
        template = 'components/generic/brokerdetail.html'
    elif(article.category == 'G'):
        template = 'components/generic/guestPost.html'
    else:
        template = 'components/generic/articleDetail.html'

    brokers = Article.objects.filter(category='B')
    guestPosts = Article.objects.filter(category='G').order_by('-created_at')[:3]
    context = {
        'article':article,
        'brokers':brokers,
        'guestPosts':guestPosts,
    }
    return render(request, template, context)    
