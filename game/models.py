from django.db import models


class Position(models.Model):
    name = models.CharField(verbose_name='Posição', max_length=50)
    abbreviation = models.CharField(verbose_name='Abreviação', max_length=3)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Posição'
        verbose_name_plural = 'Posições'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=50)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    abbreviation = models.CharField(verbose_name='Abreviação', max_length=3)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Clube'
        verbose_name_plural = 'Clubes'

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    slug = models.SlugField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Clube')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Posição')
    price = models.DecimalField('Preço', max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.name
