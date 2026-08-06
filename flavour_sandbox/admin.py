from django.contrib import admin
from .models import FlavourSandboxIdea, Comment


@admin.register(FlavourSandboxIdea)
class SandboxAdmin(admin.ModelAdmin):
    list_display = (
            'title',
            'approved',
            'total_likes',
            'author'
        )
    actions = ['approve_idea', ]

    ordering = ('likes',)

    @admin.action(
            description='Confirm and approve flavour ideas to be published to site')
    def approve_idea(self, request, queryset):
        to_approve = queryset.filter(approved=False)
        count = to_approve.count()
        to_approve.update(approved=True)
        self.message_user(request,
                          f"Successfully approved and published {count} ideas to Flavour Sandbox")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author__username', 'idea__title', 'approved',)
    list_filter = ('approved',)
    actions = ['approve_comment', ]

    @admin.action(
            description='Confirm and approve comments to be published to site')
    def approve_comment(self, request, queryset):
        to_approve = queryset.filter(approved=False)
        count = to_approve.count()
        to_approve.update(approved=True)
        self.message_user(request,
                          f"Successfully approved and published {count} comments")
