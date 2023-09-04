from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name=_("persian name"), max_length=200)
    en_name = models.CharField(verbose_name=_("english name"), max_length=200)
    description = models.TextField(verbose_name=_("Description"))   
    category = models.ForeignKey("Category",
                               verbose_name=_("Category"),
                               on_delete=models.PROTECT,
                               )   
    def __str__(self):
        return f"{self.id}{self.name}"
    

class Category(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length = 50)
    slug = models.SlugField(verbose_name=_("slug"),unique=True, db_index=True)
    description = models.TextField(verbose_name=_("Description"))
    icon = models.ImageField(verbose_name=_("Icon"), upload_to = "category_images", null=True, blank=True)
    image = models.ImageField(verbose_name=_("Image"), upload_to = "category_images", null=True, blank=True)
    parent = models.ForeignKey("self",
                               verbose_name=_("Parent Category"),
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True
                               )   

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self) -> str:
        return self.slug


class Comment(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=150)
    text = models.TextField(verbose_name=_("Text"))
    product = models.ForeignKey("Product",
                                 verbose_name=_("Product"),
                                 on_delete=models.CASCADE
                                 )
    rate = models.PositiveSmallIntegerField(verbose_name=_("rate"))
    user_email = models.EmailField(verbose_name=_("email"),max_length=250)

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return f'commnet on{self.products.name}'
    

class Image(models.Model):
    name = models.CharField(verbose_name=_("name"),max_length=50)
    alt = models.CharField(verbose_name=_("Alternative Text"),max_length=100)
    product = models.ForeignKey("Product",
                                 verbose_name=_("IMAGE"),
                                on_delete=models.CASCADE)    
    IMAGE = models.ImageField(verbose_name=_("Image"), upload_to='products')
    is_default = models,models.BooleanField(verbose_name=_("Is default image?"), default=False)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(verbose_name=_("Question"))
    user_email = models.EmailField(verbose_name=_(""), max_length=254)
    producst = models.ForeignKey("Product",
                                 verbose_name=_("Product"),
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.text
 

class Answer(models.Model):
    text = models.TextField(verbose_name=_("Answer"))
    question = models.ForeignKey("Question",
                                 verbose_name=_("Products"),
                                 on_delete=models.CASCADE)
    
    

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return self.text 
    

class ProductOption(models.Model):
    producst = models.ForeignKey("Product",
                                 verbose_name=_("Product"),
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("Name"),max_length=200)
    value = models.CharField(verbose_name=_("Value"),max_length=200)
    

    class Meta:
        verbose_name = _("Product_Option")
        verbose_name_plural = _("Product_Options")

    def __str__(self):
        return f'{self.producst.name}{self.name}'

    
class ProductsPrice(models.Model):
    producst = models.ForeignKey("Product",
                                 verbose_name=_("Product"),
                                 on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField(verbose_name=_("Price"))
    create_at = models.DateTimeField(
        verbose_name=_("create at"), auto_now=False, auto_now_add=True)
    update_at =models.DateTimeField(
        verbose_name=_("apdate at"), auto_now=True,)

    class Meta:
        verbose_name = _("ProductsPrice")
        verbose_name_plural = _("ProductsPrices")

    def __str__(self):
        return self.name
