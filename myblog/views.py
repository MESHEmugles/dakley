from datetime import datetime, date
from dataclasses import dataclass
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q


from taggit.models import Tag
from hitcount.utils import get_ip
# from hitcount.models import HitCount
# from hitcount.views import HitCountMixin, HitCountDetailView, _update_hit_count
# from hitcount.utils import get_hitcount_model


from .models import *
from blogstory.address import *
from .forms import TutorialCommentForm
from blogstory.models import *

# Create your views here.

@dataclass
class Global:
    hom = Home.objects.all()
    tut = Tutorial.objects.all()
    tutnum = TutorialNumber.objects.all()
    tutcom = TutorialComment.objects.all()
    cat = Category.objects.all()
    abt = AboutMe.objects.all()
    ip = Address.objects.all()

def index(request):
    url = request.META.get('HTTP_REFERER')
    home = Global.hom.get()
    tuto = Global.tut
    com = TutorialComment()
    # comment =com.comment.coun
    cates = Global.cat

    context= {
        'home':home,
        'tuto':tuto,
        'cates':cates,
        # 'comment':comment,
    }

    return render (request, 'home/index.html', context)


def all_stories(request, tag_slug=None, category_slug = None):
    cate = Global.tut
    

    # # ############## PAGINATION #####################
    pag = Paginator(cate,2)
    page_number = request.GET.get('page',all)
    all_stories= pag.get_page(page_number)

    # # ############## PAGINATION END #####################



    # # ############## TAGS #####################
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_stories = Global.tut.filter(tags__in=[tag])

    # # ############## TAGS END #####################


    # # ############## CATEGORY #####################
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        all_stories = Global.tut.filter(category=category)
    # ############## CATEGORY END #####################


    context= {
        'all_stories':all_stories,
        'cate':cate,
    }


    return render (request, 'pages/all_stories.html', context)

def details(request, id,slug):
    detail = Tutorial.objects.get(pk=id)
    abtme = Global.abt.get()
    
    #################### PAGINATION ##########################
    next_ln = Global.tutnum.filter(pk__gt =detail.pk).order_by('id').first()
    previous_ln = Global.tutnum.filter(pk__lt =detail.pk).order_by('id').last()
    #################### PAGINATION END ##########################


    newly = Global.tut.order_by('-Tutorial_id')[:3]

    # ############## NUMBER_OF_COUNTS ###########################

    # context = {}
    # hit_count = HitCount.objects.get_for_object(Tutorial.objects.get(pk=id))
    # hits = hit_count.hits
    # hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    # hit_count_response =HitCountDetailView.hit_count(request, hit_count)
    # if hit_count_response.hit_counted:
    #     hits = hits + 1
    #     hitcontext['hit_counted'] = hit_count_response.hit_counted
    #     hitcontext['hit_message'] = hit_count_response.hit_message
    #     hitcontext['total_hits'] = hits
    
    # ############## NUMBER_OF_COUNTS ENDS ###########################


    # ############## COMMENT #####################
    tutocom = Global.tutcom.filter(comment_tuto= id)
    com = Global.tutcom
    number_of_comments = Global.tutcom.filter(comment_tuto=id).count()
    if int(number_of_comments) > 0:
        newcom = Tutorial(Tutorial_id= id)
        newcom.no_of_comments += number_of_comments
        print(number_of_comments)
    else:
        newcom = Tutorial(Tutorial_id= id)
        newcom.no_of_comments = 0
    comment = TutorialCommentForm(instance=Global.tut.get(pk=id))
    if request.method == 'POST':
        comment = TutorialCommentForm(request.POST, instance=Global.tut.get(pk=id))
        if comment.is_valid():
            comment.save(commit=False)
            c= TutorialComment(comment_tuto =Global.tut.get(pk=id), 
                               name=comment.cleaned_data['name'], 
                               email=comment.cleaned_data['email'], 
                               comment=comment.cleaned_data['comment'], 
                               created=datetime.now() 
            )
            c.save()
            return redirect('myblog:details', detail.pk, detail.slug )
    else:
        comment= TutorialCommentForm()
            
    # ############## COMMENT END #####################

    return render (request, 'pages/details.html', {'detail':detail,'next_ln':next_ln,
    'previous_ln':previous_ln, 'newly':newly,
    'comment':comment,'tutocom':tutocom,'com':com,'abtme':abtme,'number_of_comments':number_of_comments})

def searched(request):
    if request.method == 'POST':
        searched = request.POST['itemsearch']
        search = Global.tut.filter(
            Q(Q(title__icontains=searched) | 
            Q(description__icontains=searched) | 
            Q(category__name__icontains=searched))
        )
    else:
        search = Global.tut

    context={
        'search':search,
    }
    return render(request, 'pages/search.html', context)

