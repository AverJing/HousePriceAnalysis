from django.db import models

# Create your models here.
class User(models.Model):
    '''用户注册登录'''
    gender = {
        ('male',"男"),
        ('female',"女"),
    }
    #用户名，必填，最长不超过128个字符，唯一即不能有相同姓名
    name = models.CharField(max_length=128,unique=True)
    #密码，必填，最长不超过256个字符
    password = models.CharField(max_length=256)
    #邮箱 使用Django内置的邮箱类型，并且唯一
    email = models.EmailField(unique=True)
    #性别 只有男女
    sex = models.CharField(max_length=32,choices=gender,default="男")
    #注册时间
    c_time = models.DateTimeField(auto_now_add=True)

    # 人性化显示对象信息
    def __str__(self):
        return self.name

    #元数据里定义用户按创建时间的反序排列，即最近的最先显示
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"