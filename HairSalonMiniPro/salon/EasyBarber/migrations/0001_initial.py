# Generated by Django 3.0.4 on 2020-11-29 18:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('app_no', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('service_type', models.CharField(choices=[('Shop', 'shop'), ('Home', 'home')], max_length=4)),
                ('service_category', models.CharField(choices=[('Haircut', 'haircut'), ('Massage', 'massage'), ('Hair Colour', 'hair colour'), ('Shave', 'shave'), ('Facial', 'facial')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=50, unique=True)),
                ('cust_email', models.EmailField(max_length=50, unique=True)),
                ('cust_phone', models.IntegerField()),
                ('cust_address', models.TextField(max_length=100)),
                ('cust_gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Owner',
            fields=[
                ('own_id', models.IntegerField(primary_key=True, serialize=False)),
                ('own_name', models.CharField(max_length=50)),
                ('own_email', models.EmailField(max_length=50)),
                ('own_phone', models.IntegerField()),
                ('shop_name', models.CharField(max_length=50, unique=True)),
                ('shop_address', models.TextField(max_length=100, unique=True)),
                ('own_gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Barber',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50, unique=True)),
                ('emp_email', models.EmailField(max_length=50)),
                ('emp_phone', models.IntegerField()),
                ('emp_gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=6)),
                ('shop_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='EasyBarber.Shop_Owner', to_field='shop_address')),
                ('shop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='EasyBarber.Shop_Owner', to_field='shop_name')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])),
                ('comment', models.TextField(max_length=300)),
                ('app_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EasyBarber.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_id', models.CharField(blank=True, default=uuid.uuid4, max_length=15, unique=True)),
                ('amt', models.IntegerField()),
                ('app_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EasyBarber.Appointment')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='cust_email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='EasyBarber.Customer', to_field='cust_email'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='cust_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='EasyBarber.Customer', to_field='cust_name'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='emp_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='EasyBarber.Shop_Barber', to_field='emp_name'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='shop_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='EasyBarber.Shop_Owner', to_field='shop_name'),
        ),
    ]
