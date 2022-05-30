from django.db import models
from django.utils.timezone import now as djnow


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


class Category(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


class Status(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


class Author(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


class Post(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    image01 = models.ImageField(null=True,
                                blank=True)
    image01_thumbnail = models.ImageField(null=True,
                                          blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    is_published = models.BooleanField(default=False)
    status = models.ForeignKey(Status,
                               null=True,
                               on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    content = models.TextField(max_length=50000,
                               null=True,
                               blank=True)
    post_author = models.ForeignKey(Author,
                                    null=True,
                                    on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=djnow,
                                        null=False)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


class CommentPerson(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


class Comment(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    content = models.TextField(max_length=50000,
                               null=True,
                               blank=True)
    post = models.ForeignKey(Post,
                             null=True,
                             on_delete=models.CASCADE)
    author = models.ForeignKey(CommentPerson,
                               null=True,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


class Reaction(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    desc = models.TextField(max_length=50000,
                            null=True,
                            blank=True)
    post = models.ForeignKey(Post,
                             null=True,
                             on_delete=models.CASCADE)
    author = models.ForeignKey(CommentPerson,
                               null=True,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result
