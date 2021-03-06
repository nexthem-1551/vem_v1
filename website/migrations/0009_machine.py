# Generated by Django 2.1.7 on 2019-03-31 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190331_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=60)),
                ('m_image', models.ImageField(blank=True, default='defImages/defMachine.jpeg', upload_to='images/machines/')),
                ('m_upload_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('m_verified', models.BooleanField(blank=True, default=False, null=True)),
                ('m_avail', models.BooleanField(blank=True, default=False, null=True)),
                ('m_subtype', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('m_location', models.CharField(max_length=1000)),
                ('m_brand', models.CharField(blank=True, max_length=50, null=True)),
                ('m_manufacturing_year', models.CharField(blank=True, max_length=15, null=True)),
                ('m_size', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True)),
                ('m_travel_length', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True)),
                ('m_accuracy', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=10, null=True)),
                ('m_spindle_rpm', models.IntegerField(blank=True, default=0, null=True)),
                ('m_tonnage', models.FloatField(blank=True, default=0, null=True)),
                ('m_ra_value', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True)),
                ('m_current_rating', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True)),
                ('m_tie_bar', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True)),
                ('m_shot_weight', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
