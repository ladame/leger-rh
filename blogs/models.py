from django.db import models

# Create your models here.
class myBlogs(models.Model):
	title = models.CharField(max_length=200,blank=False,null=False,verbose_name='Titre de l’actualité')
	body = models.TextField(max_length=1000,blank=False,null=False,verbose_name='Contenu de l’actualité')
	gambar = models.ImageField(null=False,blank=False,upload_to="blogs_img",verbose_name='Image pour les nouvelles')
	created_at = models.DateField(null=True,blank=True,auto_now_add=True,verbose_name='Date de création')
	active = models.BooleanField(default=True,null=False,blank=False,verbose_name='Cochez pour afficher')

	def __str__(self):
		return "%s - %s"%(self.title,self.created_at)

	class Meta:
		ordering=['-id']
		unique_together =['title','body']