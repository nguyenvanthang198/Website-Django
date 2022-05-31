from django.db import models
from django.utils.timezone import now as djnow


# Create your models here.

class ContactContent(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    subject = models.CharField(max_length=1024,
                               null=True,
                               blank=True)
    content = models.TextField(max_length=50000,
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

class ContactPerson(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    title = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    email = models.CharField(max_length=1024,
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


class EmailTemplate(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    title = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    subject_pattern = models.ForeignKey(ContactPerson,
                                       null=True,
                                       on_delete=models.CASCADE)
    content_pattern = models.ForeignKey(ContactContent,
                                       null=True,
                                       on_delete=models.CASCADE)
    type = models.CharField(max_length=1024,
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


class ContactMessage(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    email = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    subject = models.CharField(max_length=1024,
                               null=True,
                               blank=True)
    content = models.TextField(max_length=5000,
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


class CompanyEmail(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    title = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    value = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    icon = models.ImageField(max_length=4096,
                             null=True,
                             blank=True)
    is_default = models.BooleanField(default=False, )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)




class CompanyPhone(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    title = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    value = models.CharField(max_length=1024,
                             null=True,
                             blank=True)

    icon = models.ImageField(max_length=4096,
                             null=True,
                             blank=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)


class CompanyAddress(models.Model):
    name = models.CharField(max_length=1024,
                            null=True,
                            blank=True)
    title = models.CharField(max_length=1024,
                             null=True,
                             blank=True)
    value = models.CharField(max_length=1024,
                             null=True,
                             blank=True)

    icon = models.ImageField(max_length=4096,
                             null=True,
                             blank=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        super().save(*args, **kwargs)