from shop.models import Category


def categorys(request):
    cats = Category.objects.all()
    return {'cats': cats}
