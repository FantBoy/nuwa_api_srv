from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    purview = models.IntegerField()
    modify_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta():
        # abstract = True
        db_table = 't_person'

class ProgrameGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=64)
    desc = models.CharField(max_length=1024)
    modify_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta():
        db_table = 't_programe_group'

class Device(models.Model):
    STATUS_CHOICE = (
        (0, 'offline'),
        (1, 'online'),
        (-1, 'error')

    )
    id = models.IntegerField(primary_key=True)
    device_name = models.CharField(max_length=64)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(ProgrameGroup, on_delete=models.CASCADE)
    device_ip = models.CharField(max_length=16)
    status = models.IntegerField(choices=STATUS_CHOICE)
    desc = models.CharField(max_length=1024)
    modify_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta():
        db_table = 't_device_list'

class PackageType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta():
        db_table = 't_package_type'


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    package_name = models.CharField(max_length=64)
    package_type = models.ForeignKey(PackageType, on_delete=models.CASCADE)
    package_owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1024)
    modify_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta():
        db_table = 't_package_list'

class PackageVersion(models.Model):
    id = models.IntegerField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    version = models.CharField(max_length=16)
    modify_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    desc = models.CharField(max_length=1024)

    class Meta():
        db_table = 't_package_version'

