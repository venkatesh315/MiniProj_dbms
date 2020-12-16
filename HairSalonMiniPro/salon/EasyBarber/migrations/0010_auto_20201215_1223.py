# Generated by Django 3.0.4 on 2020-12-15 06:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('EasyBarber', '0009_auto_20201208_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('cust_name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])),
                ('comment', models.TextField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='emp_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_emp', to='EasyBarber.Shop_Barber', to_field='emp_name'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='shop_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_shop', to='EasyBarber.Shop_Owner', to_field='shop_name'),
        ),
        migrations.AlterField(
            model_name='shop_barber',
            name='shop_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sb_address', to='EasyBarber.Shop_Owner', to_field='shop_address'),
        ),
        migrations.AlterField(
            model_name='shop_barber',
            name='shop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sb_shop', to='EasyBarber.Shop_Owner', to_field='shop_name'),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='app_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rev_no', to='EasyBarber.Appointment'),
        ),
        migrations.AddField(
            model_name='review',
            name='emp_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rev_emp', to='EasyBarber.Shop_Barber', to_field='emp_name'),
        ),
        migrations.AddField(
            model_name='review',
            name='shop_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rev_shop', to='EasyBarber.Shop_Owner', to_field='shop_name'),
        ),
    ]