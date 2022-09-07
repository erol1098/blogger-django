# Generated by Django 4.1.1 on 2022-09-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_slug_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='General', on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
    ]
