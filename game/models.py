from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


STATUS = [
    ("DUV", "Dúvida"),
    ("SUP", "Suspenso"),
    ("PRO", "Provável"),
    ("NUL", "Nulo"),
    ("CON", "Contundido")
]


class Status(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=50, choices=STATUS, default="NUL")

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


POSITIONS = [
        ('GOL', 'Goleiro'),
        ('LAT', 'Lateral'),
        ('ZAG', 'Zagueiro'),
        ('MEI', 'Meia'),
        ('ATA', 'Atacante'),
        ('TEC', 'Técnico')
    ]


class Player(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    slug = models.SlugField()
    team = models.ForeignKey(Team, verbose_name='Clube', on_delete=models.CASCADE)
    position = models.CharField(verbose_name='Posição', choices=POSITIONS, max_length=50)
    price = models.DecimalField('Preço', max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.name


class Match(models.Model):
    round = models.IntegerField('Rodada', validators=[MinValueValidator(1), MaxValueValidator(38)])
    date = models.DateTimeField('Data da Partida', auto_now=True)
    home_team = models.ForeignKey(Team, verbose_name='Time da casa', related_name='home_team', on_delete=models.CASCADE)
    guest_team = models.ForeignKey(Team, verbose_name='Time visitante',
                                   related_name='quest_team', on_delete=models.CASCADE)
    score_home = models.IntegerField()
    score_guest = models.IntegerField()

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'


# class Scouts(models.Model):
#     player = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE)
#     team = models.ForeignKey(Team, verbose_name='Time', on_delete=models.CASCADE)
#     status = models.ForeignKey(Status, verbose_name='Status',  on_delete=models.CASCADE)