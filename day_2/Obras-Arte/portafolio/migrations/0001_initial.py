# Generated by Django 4.0.6 on 2022-07-19 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exposicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('place', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uri', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ObrasArte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('multimedia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.multimedia')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('exposicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.exposicion')),
            ],
        ),
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('obrasarte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.obrasarte')),
            ],
        ),
        migrations.AddField(
            model_name='obrasarte',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.tipo'),
        ),
        migrations.AddField(
            model_name='exposicion',
            name='Portafolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.portafolio'),
        ),
        migrations.CreateModel(
            name='Author_ObrasArte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.author')),
                ('obrasarte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.obrasarte')),
            ],
        ),
    ]
