from django.shortcuts import render,get_object_or_404
from . models import CategoryProduct,Product 
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    popular_products = Product.objects.order_by('-click_count')[:6]
    return render(request,'products/index.html',{'popular_products':popular_products})



def catalog(request):
    products = Product.objects.all()
    categories = CategoryProduct.objects.all()
    per_page = 12
    paginator = Paginator(products, per_page)
    page_number = request.GET.get('page')


    # Проверяем, что page_number не равен None, и преобразуем его в целое число
    if page_number:
        try:
            page_number = int(page_number) # Преобразуем в int, чтобы избежать PageNotAnInteger
        except ValueError:

            page_number = 1  # Если не удалось преобразовать в int, возвращаем первую страницу
    else:
        page_number = 1  # Если page не передан, возвращаем первую страницу


    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
    }

    return render(request, 'products/catalog.html', context)


def product_detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    product.click_count+=1
    product.save()
    return render(request,"products/product_detail.html",{"product":product})

def category(request, category_id):
    """Отображает товары из выбранной категории."""

    current_category = get_object_or_404(CategoryProduct, pk=category_id)  # Получаем объект категории

    product_category = Product.objects.filter(category=current_category)  # Фильтруем товары по категории

    context = {
        'category': current_category,
        'products': product_category,  # Передаем список товаров в шаблон
    }

    return render(request, "products/onecategoryonly.html", context)


