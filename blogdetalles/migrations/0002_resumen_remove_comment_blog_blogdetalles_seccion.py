# Generated by Django 4.2.2 on 2023-07-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdetalles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to='imagen_resumen')),
                ('contenido', models.TextField()),
                ('dato_extra1', models.CharField(max_length=50)),
                ('dato_extra2', models.CharField(max_length=50)),
                ('dato_extra3', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.AddField(
            model_name='blogdetalles',
            name='seccion',
            field=models.CharField(default='anime', max_length=100),
        ),
    ]