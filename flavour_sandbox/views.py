from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, IdeaForm
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

    queryset = FlavourSandboxIdea.objects.filter(approved=True)
    idea = get_object_or_404(queryset, pk=idea_id)
    comments = idea.comments.all().order_by("-created_on")
    comment_count = idea.comments.filter(approved=True, parent__isnull=True).count()

    comment_form = CommentForm()
    edit_idea_form = IdeaForm(instance=idea)

    if request.method == "POST":

        if "submit_comment" in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.idea = idea

                parent_id = request.POST.get("parent_id")
                if parent_id:
                    comment.parent = Comment.objects.get(id=parent_id)
                comment.save()

                messages.add_message(request, messages.SUCCESS, "Your comment has been submitted and is awaiting approval.")
                return redirect("idea_detail", idea_id)

        if "submit_edit_idea" in request.POST:
            edit_idea_form = IdeaForm(data=request.POST, instance=idea, files=request.FILES)
            if edit_idea_form.is_valid():
                idea = edit_idea_form.save(commit=False)
                idea.status = 0
                idea.save()
                edit_idea_form.save_m2m()
                messages.add_message(request, messages.SUCCESS, "Your Flavour Sandbox post has been edited and is waiting approval")
                return redirect("sandbox")

    context = {
        'idea': idea,
        'comments': comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "edit_idea_form": edit_idea_form
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


def comment_edit(request, idea_id, comment_id):
    """
    View to enable users to edit their own comments
    """

    if request.method == "POST":
        queryset = FlavourSandboxIdea.objects.filter(status=1)
        idea = get_object_or_404(queryset, idea_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.idea = idea
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated! Pending approval.')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return redirect("idea_detail", idea_id)


def comment_delete(request, idea_id, comment_id):
    """
    View to enable users to delete their own comments
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return redirect("idea_detail", idea_id)