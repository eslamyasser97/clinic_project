from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
# Create your models here.

TYPE_OF_CITY=(
    ('alex',"الاسكندريه"),
    ('cairo', "القاهره"),
    ('matroh', "مطروح"),
    ('aswan', "اسوان"),

)

class clinic(models.Model):
    admin = models.ForeignKey(User, related_name='clinc_admin', on_delete=models.CASCADE)
    name = models.CharField(_(': الاسم'), max_length=50)
    type_of_city = models.CharField(_('المحافظه'), choices=TYPE_OF_CITY,max_length=15)
    services = models.CharField(_('الخدمات المقدمه'),max_length=4000)
    subtitle = models.CharField(_(': نبذه عن العياده'),max_length=1000,blank=True,null=True)
    telephone = models.CharField(_('رقم الهاتف'),max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(_(': الصوره الخاصه بالعياده'),upload_to='clinic',blank=True,null=True)
    works_hour = models.IntegerField(_(': ساعات العمل اليوميه'))
    facebook = models.CharField(_(': لينك صفحه الفيسبوك'),max_length=40,blank=True,null=True)
    twitter = models.CharField(_(': لينك تويتر '), max_length=40,blank=True,null=True)
    email = models.EmailField(_(': الايميل:'), max_length=40,blank=True,null=True)
    slug = models.SlugField(blank=True, null=True)
    #location


    class Meta:
        verbose_name = _("clinic")
        verbose_name_plural = _("clinics")

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(clinic,self).save(*args, **kwargs) ## override of save method

 ##function to create user with clinic dynamic only create user

#def create_clinic(sender, **kwargs):
 #   if kwargs['created']:
  #      clinic.objects.create(user=kwargs['instance'])

#post_save.connect(create_clinic , sender=User)

class apply(models.Model):
    clinic = models.ForeignKey(clinic, related_name='apply_clinic', on_delete=models.CASCADE)
    name = models.CharField(_(': الاسم'), max_length=50)
    telephone = models.CharField(_(': التليفون:'), max_length=50,blank=True,null=True)
    ssid = models.ImageField(_('صوره البطاقه'),upload_to='apply')
    email = models.CharField(_('الايميل'),max_length=2000)
    apply_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



