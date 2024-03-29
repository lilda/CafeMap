# Generated by Django 2.1.7 on 2019-09-22 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_auto_20190922_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review_Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='cafe.Review')),
            ],
        ),
        migrations.CreateModel(
            name='Review_Unlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Unlike', to='cafe.Review')),
            ],
        ),
        migrations.RenameModel(
            old_name='Like',
            new_name='Cafe_Like',
        ),
        migrations.RenameModel(
            old_name='Unlike',
            new_name='Cafe_Unlike',
        ),
    ]
