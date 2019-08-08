# Generated by Django 2.0.7 on 2019-07-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('broadcast', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('brief', models.CharField(blank=True, max_length=255, null=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('cover', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('insert_img', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('guru_id', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('album_id', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'chapter',
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('createdate', models.DateField(blank=True, db_column='createDate', null=True)),
                ('userid', models.IntegerField(blank=True, db_column='userID', null=True)),
                ('taskid', models.IntegerField(blank=True, db_column='taskId', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'counter',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=55, null=True)),
                ('userid', models.CharField(blank=True, db_column='userId', max_length=32, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('creattime', models.DateTimeField(blank=True, db_column='creatTime', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('nickname', models.CharField(blank=True, db_column='nickName', max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'guru',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('href', models.CharField(blank=True, max_length=255, null=True)),
                ('iconcls', models.CharField(blank=True, db_column='iconCls', max_length=30, null=True)),
                ('parentid', models.CharField(blank=True, db_column='parentId', max_length=32, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('permission', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('role_id', models.CharField(blank=True, max_length=255, null=True)),
                ('permission_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'role_permission',
            },
        ),
        migrations.CreateModel(
            name='SubjectRole',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('subject_id', models.CharField(blank=True, max_length=255, null=True)),
                ('role_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'subject_role',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('createdate', models.DateTimeField(blank=True, db_column='createDate', null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('userid', models.IntegerField(blank=True, db_column='userId', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('nickname', models.CharField(blank=True, db_column='nickName', max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('salt', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('sign', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('phonenumber', models.IntegerField(blank=True, db_column='phoneNumber', null=True)),
                ('registtime', models.DateField(blank=True, db_column='registTime', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('url_pic', models.ImageField(blank=True, null=True, upload_to='img')),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'banner',
            },
        ),
    ]