# Generated by Django 2.1.7 on 2019-09-17 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='like',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='cafe.Cafe'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='cafe.Cafe'),
        ),
        migrations.AlterField(
            model_name='unlike',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Unlike', to='cafe.Cafe'),
        ),
        migrations.AlterField(
            model_name='unlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Unlike', to=settings.AUTH_USER_MODEL),
        ),
    ]