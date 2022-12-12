# Generated by Django 4.1.3 on 2022-11-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('PN', 'Pending'), ('CD', 'Closed'), ('SD', 'Solved')], default='Pending', max_length=2),
        ),
    ]
