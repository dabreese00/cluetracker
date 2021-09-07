# Generated by Django 3.2.7 on 2021-09-06 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_pass_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='games.game'),
        ),
        migrations.AlterField(
            model_name='have',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='haves', to='games.game'),
        ),
        migrations.AlterField(
            model_name='show',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='games.game'),
        ),
    ]
