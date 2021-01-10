# Generated by Django 3.1.5 on 2021-01-10 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.location')),
            ],
        ),
    ]
