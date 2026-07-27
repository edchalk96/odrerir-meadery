from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import FlavourSandboxIdea, Comment


def sandbox_list(request):
    """ View to display all, approved, sandbox idea posts and sorting """
    ideas = FlavourSandboxIdea.objects.filter(approved=True)

    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'likes':
                sortkey = 'like_count'
                ideas = ideas.annotate(like_count=Count("likes"))
            elif sortkey == "created_on":
                sortkey = "created_on"

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            ideas = ideas.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(ideas, 12) # Show 12 products per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'ideas': page_obj,
        'sandbox_list': page_obj,
        "current_sorting": current_sorting,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "sort": sort,
        "direction": direction,
    }

    return render(request, 'flavour_sandbox/flavour_sandbox.html', context)

def idea_detail(request, idea_id):    
    """ A view to show individual idea details """

    idea = get_object_or_404(FlavourSandboxIdea, pk=idea_id)

    context = {
        'idea': idea,
    }

    return render(request, 'flavour_sandbox/idea_detail.html', context)


def like_idea(request, pk):
    """ A view to enable users to like another users idea"""

    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Please log in or sign up to vote on flavour ideas!')
        return redirect("account_login")

    idea = get_object_or_404(FlavourSandboxIdea, pk=pk)

    if idea.likes.filter(id=request.user.id).exists():
        idea.likes.remove(request.user)
    else:
        idea.likes.add(request.user)

    return redirect(request.META.get("HTTP_REFERER", "sandbox_list"))