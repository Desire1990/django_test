# Generated by Django 3.0 on 2020-04-19 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idcomplete', '0003_auto_20200418_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identitecomplete',
            name='Person',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='identiteCompletes', to='idcomplete.Person'),
        ),
    ]