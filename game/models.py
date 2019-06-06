import re

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, **extra_fields):

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), is_staff=is_staff, is_active=True)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True, help_text=_(
        'Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[
        validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])

    first_name = models.CharField(_('first name'), max_length=30)

    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('e-mail address'), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can loginto this admin site.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


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


class UserTeam(models.Model):
    owner = models.OneToOneField(get_user_model(), verbose_name='Cartoleiro', on_delete=models.CASCADE)
    team_name = models.CharField('Nome do Time', max_length=100)
    club_fan = models.ForeignKey(Team, verbose_name='Time do Coração', on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player2')
    player3 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player3')
    player4 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player4')
    player5 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player5')
    player6 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player6')
    player7 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player7')
    player8 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player8')
    player9 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player9')
    player10 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player10')
    player11 = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE, related_name='player11')
    coach = models.ForeignKey(Player, verbose_name='Técnico', on_delete=models.CASCADE, related_name='coach')

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.team_name


# class Scouts(models.Model):
#     player = models.ForeignKey(Player, verbose_name='Jogador', on_delete=models.CASCADE)
#     team = models.ForeignKey(Team, verbose_name='Time', on_delete=models.CASCADE)
#     status = models.ForeignKey(Status, verbose_name='Status',  on_delete=models.CASCADE)

