# Generated by Django 5.1.1 on 2025-01-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_category_alter_recipe_cover_and_more'),
        ('tag', '0002_remove_tag_content_type_remove_tag_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='tag.tag'),
        ),
    ]
