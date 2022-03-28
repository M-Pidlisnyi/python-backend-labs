from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    category = models.CharField('Category', max_length=255, help_text="Max 255 characters length")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Article category"
    
class Article(models.Model):
    title = models.CharField("Title", max_length=127, help_text="Max 127 characters length")
    descrition = models.CharField("Article description", 
                                   max_length=512, blank=True, null=True)

    publication_date = models.DateField("Date of publication", default=timezone.now())
    slug = models.SlugField("Slug", unique_for_date='publication_date')

    main_page = models.BooleanField("Main page", default=False, help_text="Show on main page")

    category = models.ForeignKey(Category, related_name="news",
                                verbose_name="Category", on_delete=models.CASCADE)
    objects = models.Manager()

    def  str (self): 
        return self.title

    def get_absolute_url(self):
        try: 
            url = reverse("news-detail", 
                            kwargs={
                                'year': self.publication_date.strftime("%Y"),
                                'month': self.publication_date.strftime("%m"),
                                'day': self.publication_date.strftime("%d"),
                                'slug': self.slug})
        except: 
            url = '/'
    
        return url
    
    class Meta:
        ordering = ['-publication_date']
        verbose_name = "Article"
        verbose_name_plural = "Aticles"


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name="Article", 
                                related_name="images", on_delete=models.CASCADE)
    
    image = models.ImageField("Image", upload_to="images")
    title = models.CharField("Title", max_length=255, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]
    
    class Meta:
        verbose_name = "Image for Article"
        verbose_name_plural = "Images for Articles"
    


