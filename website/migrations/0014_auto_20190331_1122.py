# Generated by Django 2.1.7 on 2019-03-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20190331_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='m_shot_weight',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True),
        ),
    ]
