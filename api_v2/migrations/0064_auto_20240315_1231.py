# Generated by Django 3.2.20 on 2024-03-15 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0063_auto_20240315_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatureattack',
            name='extra_damage_type',
            field=models.ForeignKey(help_text='What kind of extra damage this attack deals', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api_v2.damagetype'),
        ),
        migrations.AlterField(
            model_name='creatureattack',
            name='damage_type',
            field=models.ForeignKey(help_text='What kind of damage this attack deals', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api_v2.damagetype'),
        ),
    ]