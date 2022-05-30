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
