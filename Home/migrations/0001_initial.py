# Generated by Django 3.2.9 on 2022-04-22 10:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('url', models.CharField(blank=True, max_length=1024, null=True)),
                ('icon', models.ImageField(blank=True, max_length=4096, null=True, upload_to='')),
                ('ico_class', models.CharField(blank=True, max_length=1024, null=True)),
                ('css_class', models.CharField(blank=True, max_length=1024, null=True)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.menu')),
            ],
        ),
    ]