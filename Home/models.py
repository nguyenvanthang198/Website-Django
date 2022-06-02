import random
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now as djnow


# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    title = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    url = models.CharField(max_length=1024,
                           null=True,
                           blank=True)

    parent_menu = models.ForeignKey("self",
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)
    icon = models.ImageField(max_length=4096,
                             null=True,
                             blank=True)
    ico_class = models.CharField(max_length=1024,
                                 null=True,
                                 blank=True)

    css_class = models.CharField(max_length=1024,
                                 null=True,
                                 blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        if self.parent_menu is None:
            return str(self.name)
        else:
            return str("[%s] %s" % (self.parent_menu.name, self.name))

    def admin_name(self):
        if self.parent_menu is None:
            return str(self.name)
        else:
            return str("[%s] %s" % (self.parent_menu.name, self.name))

    def sub_menus(self):
        result = Menu.objects.filter(parent_menu=self).order_by('order')
        if len(result) == 0:
            return None
        else:
            return result

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)
    #
    # def ll_str(self):
    #     result = "Test"
    #     if self.name != "" and self.name is not None:
    #         result = self.name
    #     return result


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# upload_storage = FileSystemStorage(location=settings.MEDIA_ROOT, base_url='/media')
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))


from datetime import datetime
import os


def _upload_to(instance, filename):
    result = os.path.join(instance._meta.app_label, instance.__class__.__name__, datetime.today().strftime("%Y/%m/%d"),
                          filename)
    print('result = %s' % result)
    return result


class UserProfile(models.Model):
    choice_gender = (
        ('Not known', 'Not known'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not applicable', 'Not applicable')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    avatar = models.ImageField(null=True,
                               blank=True,
                               upload_to=_upload_to
                               )
    gender = models.CharField(null=True,
                              max_length=1024,
                              choices=choice_gender,
                              default='Not known')
    date_of_birth = models.DateField(null=True,
                                     blank=True)
    phone = models.CharField(max_length=45,
                             null=True,
                             blank=True)
    biography = models.TextField(null=True,
                                 blank=True)
    email = models.EmailField(max_length=255,
                              null=True,
                              blank=True)
    created_at = models.DateTimeField(default=djnow,
                                      null=False)
    updated_at = models.DateTimeField(default=djnow,
                                      null=False)

    def __str__(self):
        return str(self.name)

