from django.db import models
from django.urls import reverse

class Post(models.Model):   #extends islemi yapildi.
    title = models.CharField(max_length=120, verbose_name='Baslik')   #Char Field icin mutlaka max lenght belirtilmeli
    content = models.TextField(verbose_name='Icerik')
    publishing_date = models.DateTimeField(verbose_name='Yayinlanma Tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'postId': self.id})
        #return "/post/detail/{}".format(self.id)

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})

    class Meta:
        ordering = ['-publishing_date','id']