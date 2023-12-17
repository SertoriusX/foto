from django.shortcuts import render,get_object_or_404
from .models import  cards_s,Category,card_detail
from django.core.paginator import Paginator

# Create your views here.
def cards(request,*args,**kwargs):
     
    category = request.GET.get('category')

    if category == None  :
        cards = cards_s.objects.filter(is_published=True)
    else:
        cards = cards_s.objects.filter(category__name=category)
    search=''
    if request.GET.get('search'):
        search =request.GET.get('search')
        cards =cards_s.objects.filter(name__icontains=search)

    paginator = Paginator(cards, 16)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    cards = paginator.get_page(page_number)
    categories = Category.objects.all()
    ctx ={
        'categories': categories,
        'cards': cards,
       
    }
    return render(request, 'app/home.html',ctx)


def detail(request,card_id,*args,**kwargs):
    card = get_object_or_404(cards_s,id=card_id)
    return render(request,'app/detail.html',{'cards':card}) 
