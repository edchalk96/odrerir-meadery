from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from products.models import Category


class FlavourSandboxIdea(models.Model):
    title = models.CharField(max_length=200, unique=True)
    ingredients = ArrayField(models.CharField(max_length=254), blank=True, default=list)
    mead_type = models.ForeignKey(Category, on_delete=models.PROTECT)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="flavour_idea_likes", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name="user_flavour_ideas", on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    def total_likes(self):
        return self.likes.count()

# Adapted from Mimir's Index | https://github.com/edchalk96/mimirs_index/

class Comment(models.Model):
    sandbox_idea = models.ForeignKey(FlavourSandboxIdea, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    # Credit to Tom Dekan for for parent field in creating comments thread -
    # https://tomdekan.com/articles/comment-threads
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.sandbox_idea.title}"