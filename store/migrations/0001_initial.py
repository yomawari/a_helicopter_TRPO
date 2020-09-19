# Generated by Django 3.1.1 on 2020-09-19 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='events_type',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('vaule', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='payments_method',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='pesons',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('Login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
                ('reg_data', models.DateField()),
                ('id_role', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=150)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.country')),
            ],
        ),
        migrations.CreateModel(
            name='postavshik',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('addres', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.country')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('weight', models.IntegerField()),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.country')),
                ('id_events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.events')),
                ('id_postavshik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.postavshik')),
            ],
        ),
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('vaule', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('id_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_staff', to='store.pesons')),
                ('payments_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.payments_method')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='store.pesons')),
            ],
        ),
        migrations.CreateModel(
            name='shift_type',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='storage',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('date_bg', models.DateField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('pr_count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.country')),
            ],
        ),
        migrations.CreateModel(
            name='staff_timetable',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('working_day_date', models.DateField()),
                ('id_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.pesons')),
                ('id_shift_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shift_type')),
            ],
        ),
        migrations.CreateModel(
            name='sale_pos',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('id_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sale')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.events_type'),
        ),
        migrations.CreateModel(
            name='bonus_card',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=30)),
                ('count_bonus', models.IntegerField()),
                ('date_bg', models.DateTimeField()),
                ('id_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.pesons')),
            ],
        ),
    ]