from django.db import models


class Item(models.Model):
    """
    Initializes the menu object.
    """
    is_menu = models.BooleanField(
        verbose_name='Menu or not',
        default=False,
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Item name',
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='Item slug',
    )
    menu = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='childrens',
        on_delete=models.CASCADE,
    )

    class Meta:
        """
        Defines the model name in singular and plural.
        """
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self) -> str:
        """
        Displays the name of the menu when accessing an instance of the class.
        """
        return self.title
