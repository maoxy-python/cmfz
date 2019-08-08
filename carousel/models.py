# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Album(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=255, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    broadcast = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    cover = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    guru_id = models.CharField(max_length=11, blank=True, null=True)
    new_img = models.ImageField(upload_to='img', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class Banner(models.Model):
    """
    轮播图
    """
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banner'


class Chapter(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    album_id = models.CharField(max_length=36, blank=True, null=True)
    audio = models.FileField(upload_to='audio', null=True, blank=True)

    class Meta:
        db_table = 'chapter'


class Counter(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    createdate = models.DateField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'counter'


class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    name = models.CharField(max_length=55, blank=True, null=True)
    userid = models.CharField(db_column='userId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    creattime = models.DateTimeField(db_column='creatTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


class Guru(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(db_column='nickName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guru'


class Menu(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    title = models.CharField(max_length=50, blank=True, null=True)
    href = models.CharField(max_length=255, blank=True, null=True)
    iconcls = models.CharField(db_column='iconCls', max_length=30, blank=True, null=True)  # Field name made lowercase.
    parentid = models.CharField(db_column='parentId', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class Permission(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    permission = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission'


class Role(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class RolePermission(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    role_id = models.CharField(max_length=255, blank=True, null=True)
    permission_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_permission'


class SubjectRole(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    subject_id = models.CharField(max_length=255, blank=True, null=True)
    role_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject_role'


class Task(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'


class User(models.Model):
    photo = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(db_column='nickName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    sign = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.IntegerField(db_column='phoneNumber', blank=True, null=True)  # Field name made lowercase.
    registtime = models.DateField(db_column='registTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


