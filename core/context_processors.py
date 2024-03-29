from core.models import User, IpManagerDb
from products.models import Categories


def push_categories(request):
    categories = Categories.objects.all()
    context = {
        "categories": categories
    }
    return context


def site_views(request):
    views = IpManagerDb.objects.count()
    print(views)
    return {"views": views}


def check_login(request):
    username = request.user
    if str(username) != "AnonymousUser":
        status_logged = True
    else:
        status_logged = False
    context = {
        "customer_username": username,
        "status_logged": status_logged
    }
    return context
