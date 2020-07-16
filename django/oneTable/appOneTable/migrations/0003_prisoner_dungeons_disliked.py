# Generated by Django 2.2 on 2020-03-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOneTable', '0002_prisoner'),
    ]

    operations = [
        migrations.AddField(
            model_name='prisoner',
            name='dungeons_disliked',
            field=models.ManyToManyField(related_name='prisoners_that_dislike', to='appOneTable.Dungeon'),
        ),
    ]