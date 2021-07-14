# Generated by Django 3.2.4 on 2021-07-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='avinash', max_length=20)),
                ('patient_name', models.CharField(max_length=30)),
                ('doctor_name', models.CharField(choices=[('Ms.Krishna', 'Ms.Krishna'), ('Ms.Bhavani', 'Ms.Bhavani'), ('Ms.Gireesha', 'Ms.Gireesha')], max_length=15)),
                ('timings', models.CharField(choices=[('10:00 A.M - 11:00 A.M', '10:00 A.M - 11:00 A.M'), ('11:00 A.M - 12:00 P.M', '11:00 A.M - 12:00 P.M'), ('2:00 P.M - 3:00 P.M', '2:00 P.M - 3:00 P.M'), ('4:00 P.M - 5:00 P.M', '4:00 P.M - 5:00 P.M'), ('5:00 P.M - 6:00 P.M', '5:00 P.M - 6:00 P.M')], max_length=30)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=10)),
                ('symptoms', models.CharField(max_length=255)),
                ('status', models.CharField(default='Pending', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=6)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
