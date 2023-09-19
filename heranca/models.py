from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

def validate_image_ratio(image):
    img = Image.open(image)
    width, height = img.size
    if width / height != 16 / 9:
        raise ValidationError("A proporção da imagem deve ser 16:9.")


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Posts/cover/%Y/%m/%d/', blank=True, null=True)
    description = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)
    likes_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.description


    def like(self, user):
        if user not in self.likes.all():
            self.likes.add(user)
            self.is_liked = True
            self.likes_count += 1
            
        else:
            self.likes.remove(user)
            self.is_liked = False
            self.likes_count -= 1
        self.save()


class New(models.Model):
    titulo = models.CharField(_("Titulo"), max_length=200)
    conteudo = models.TextField(_("Conteudo"), )
    image = models.ImageField(upload_to='News/cover/%Y/%m/%d/', blank=True, null=True)
    is_public = models.BooleanField(default=True)


    def __str__(self):
        return self.titulo


class Dict_letter(models.Model):
    letter = models.AutoField(primary_key=True)
    letter_char = models.CharField(_("Letter Char"), max_length=1)
    alphabetical_order = models.IntegerField(_("Alphabetical Order"), default=0, blank=True)
    
    def get_words(self):
        return self.dict_indigenou_set.all()
    
    def __str__(self):
        return self.letter_char
    class Meta:
        ordering = ['letter_char']

class Dict_indigenou(models.Model):
    name = models.CharField(_("Name"), max_length=40)
    description = models.CharField(_("Description"), max_length=740)
    letter = models.ForeignKey(Dict_letter, on_delete=models.CASCADE)
    alphabetical_order = models.IntegerField(_("Alphabetical Order"), default=0, blank=True)
   

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


  