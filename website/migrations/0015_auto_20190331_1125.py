# Generated by Django 2.1.7 on 2019-03-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20190331_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='m_accuracy',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True),
        ),
    ]
