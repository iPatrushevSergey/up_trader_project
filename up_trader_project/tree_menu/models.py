from django.db import models


class Menu(models.Model):
    """
    Initializes the menu object.
    """
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Menu name',
    )

    class Meta:
        """
        Defines the model name in singular and plural.
        """
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self) -> str:
        """
        Displays the name of the menu when accessing an instance of the class.
        """
        return self.name


class Item(models.Model):
    """
    Initializes the menu object.
    """
    name = models.CharField(
        max_length=256,
        verbose_name='Item name',
    )
    menu = models.ForeignKey(
        Menu,
        blank=True,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Menu',
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
        return self.name
