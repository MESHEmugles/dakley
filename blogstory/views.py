from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q


from taggit.models import Tag
from hitcount.utils import get_ip

from .models import *
from myblog.views import Global
from .address import Address

# Create your views here.

def like(request):
    if request.POST.get('action') == 'post':
        
        ############# Get the page value or rasie not found error ######################
        post = get_object_or_404(Tutorial, Tutorial_id = int(request.POST.get('post_id')))

        ################ get the ip of the anonymous user #####################
        ip = get_ip(request)

        liking ='' # giving initial content here

        #################   Retrieve or create the address object for the current IP Address ##################
        current, created = Global.ip.get_or_create(ip=ip)

        ############### If the anonymous ip already liked the page ##############
        if post.like.filter(id=current.pk).exists():
            post.like.remove(current)
            post.like_count -= 1
            liking =post.like_count
            post.save()
        else:
            post.like.add(current)
            post.like_count += 1
            liking = post.like_count
            post.save()
        
        return JsonResponse ({'liking':liking})