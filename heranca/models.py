from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError

def validate_image_ratio(image):
    img = Image.open(image)
    width, height = img.size
    if width / height != 16 / 9:
        raise ValidationError("A proporção da imagem deve ser 16:9.")

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    image = models.ImageField(upload_to='News/cover/%Y/%m/%d/', blank=True, null=True)
    is_public = models.BooleanField(default=True)


    def __str__(self):
        return self.titulo


class Dict_letter(models.Model):
    letter = models.AutoField(primary_key=True)
    letter_char = models.CharField(max_length=1)
    alphabetical_order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.letter_char
    class Meta:
            ordering = ['alphabetical_order']

class Dict_indigenous(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=140)
    letter = models.ForeignKey(Dict_letter, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.letter_char

  