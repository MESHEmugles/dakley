from django.shortcuts import get_list_or_404

from blogstory.models import *



def category(request):
    cates = get_list_or_404(Category)
    # newly = Tutorial.objects.all().order_by('-Tutorial_id')[:3]

    context ={'cates':cates}
    return context



