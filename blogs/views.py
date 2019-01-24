from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .models import BlogModel
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def index(request):
    listings = BlogModel.objects.order_by('-created_at').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    } 
    return render(request, 'blogs/blogs.html',context)

def blog(request,blog_id):
    listing = get_object_or_404(BlogModel, pk=blog_id)
    
    context = {
        'listing':listing
    }
    return render(request, 'blogs/blog.html', context)

def search(request):
    queryset_list = BlogModel.objects.order_by('-created_at')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
    if keywords:
        queryset_list = queryset_list.filter(body__icontains=keywords)
    context = {
        'listings':queryset_list
    }
    return render(request, 'blogs/search.html',context)

def semistruc(request):
    queryset_list = BlogModel.objects.all()
    mixqur = list(queryset_list)
    json_str = serializers.serialize('json',mixqur)
    response = HttpResponse(json_str,content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=export.json'
    return response
