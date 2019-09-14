# Generated by Django 2.1.1 on 2019-05-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afectiuni', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultatieMedicala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosnsultatieMedicala', models.CharField(blank=True, max_length=100, null=True)),
                ('cosnsultatieControl', models.BooleanField(default=False)),
                ('afectiune', models.ForeignKey(on_delete='cascade', to='afectiuni.Afectiuni')),
            ],
        ),
        migrations.RemoveField(
            model_name='bazatratament',
            name='cosnsultatieMedicala',
        ),
    ]
