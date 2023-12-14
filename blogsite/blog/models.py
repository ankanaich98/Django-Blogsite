from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default_post.png', upload_to='post_pictures', validators=[FileExtensionValidator(['png','jpg'])])
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()

    def __str__(self) -> str:
        return self.title

class PostSection(models.Model):
    content = models.TextField()
    image = models.ImageField(default='default_post.png', upload_to='post_pictures', validators=[FileExtensionValidator(['png','jpg'])])
    post_model = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Section {self.pk}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content