from django.db import models
from django.conf import settings
import random
import string
# Create your models here.
SHORTCODE_MAX=getattr(settings,"SHORTCODE_MAX",20)
SHORTCODE_MAN=getattr(settings,"SHORTCODE_MAN",8)
SHORTCODE_MAX=settings.SHORTCODE_MAX
def code_generator(size=SHORTCODE_MAN, chars=string.ascii_lowercase + string.digits):
    new_code =''
    for i in range(size):
        new_code=random.choice(chars)
    return ''.join(random.choice(chars) for i in range(size))
def create_shortcode(instance,size=SHORTCODE_MAN):
    new_code =code_generator(size=size)
    mURL=instance.__class__
    qs_exists=mURL.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code

class URLManager(models.Manager):
    def all(self,*args, **kwargs):
        qs_main = super(URLManager,self).all(*args, **kwargs)
        qs=qs_main.filter(active=True)
        return qs
    def refresh_shortcode(self,items=None):
        qs=URL.objects.filter(id__gte=1)
        if items is not None and isinstance(items,int):
            qs =qs.order_by('-id')[:items]
        for q in qs:
            q.shortcode =create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class URL(models.Model):
    url=models.URLField(max_length=100)
    shortcode=models.CharField(max_length=20,unique=True,blank=True, null=True)
    updated=models.DateTimeField(auto_now=True,null=True, blank=True)
    timestap=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    # empty_datetime=models.DateTimeField(auto_now=False,auto_now_add=False,null=True, blank=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        # ordering ='-id'
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
    
    # def save(self,*args, **kwargs):
    #     if self.shortcode == None or self.shortcode == "" :
    #         self.shortcode = code_generator(self)
    #     else:
    #         self.shortcode = code_generator(self)
    #     super(URL,self).save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(URL, self).save(*args, **kwargs)

    
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
