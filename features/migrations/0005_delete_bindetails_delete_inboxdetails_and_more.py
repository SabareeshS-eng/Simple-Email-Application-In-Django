# Generated by Django 4.0.3 on 2022-04-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_alter_bindetails_from_id_alter_inboxdetails_from_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BinDetails',
        ),
        migrations.DeleteModel(
            name='InboxDetails',
        ),
        migrations.DeleteModel(
            name='JunkDetails',
        ),
        migrations.DeleteModel(
            name='SentDetails',
        ),
    ]
