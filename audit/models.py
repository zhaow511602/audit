from django.db import models
from django.contrib.auth.models import User


class IDC(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name


class Host(models.Model):
    """主机表，所有主机信息"""
    hostname = models.CharField(max_length=32, unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    port= models.IntegerField(default=22)
    # host_user = models.ManyToManyField("HostUser")
    idc = models.ForeignKey("IDC")
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return "%s-%s" %(self.hostname, self.ip_addr)


class HostGroup(models.Model):
    """主机组"""
    name = models.CharField(max_length=32, unique=True)
    host_user_binds = models.ManyToManyField("HostUserBind")

    def __str__(self):
        return self.name

class HostUser(models.Model):
    """存储远程用户主机信息"""
    auth_type_choices = ((1,"ssh_password"),(2,"ssh_key"))
    auth_type = models.SmallIntegerField(choices=auth_type_choices)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return "%s-%s-%s" %(self.get_auth_type_display(),self.username,self.password)

    class Meta:
        unique_together = ('username','password')


class HostUserBind(models.Model):
    """绑定主机和用户表"""
    host = models.ForeignKey("Host")
    host_user = models.ForeignKey("HostUser")
    def __str__(self):
        return "%s-%s"%(self.host, self.host_user)

    class Meta:
        unique_together = ("host","host_user")


class AuditLog(models.Model):
    """审计日志"""


class Account(models.Model):
    """堡垒机账号
    1、扩展
    2、继承
    """
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64)
    host = models.ManyToManyField("HostUserBind", null=True,blank=True)
    host_group = models.ManyToManyField("HostGroup",null=True,blank=True)




