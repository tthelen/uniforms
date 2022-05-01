from django.db import models
from django.forms import ModelForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your models here.
class Schnupperanmeldung(models.Model):
    FOOD_VEGAN = 'VE'
    FOOD_VEGETARIAN = 'VT'
    FOOD_OMNIVORE = 'OV'

    PROGRAM_BACHELOR = 'BA'
    PROGRAM_MASTER = 'MA'

    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    program = models.CharField(max_length=2, choices=[(PROGRAM_BACHELOR, 'Bachelor Cognitive Science'), (PROGRAM_MASTER, 'Master Cognitive Science')])
    accomodation = models.BooleanField()
    food = models.CharField(max_length=2, blank=True, choices=[(FOOD_VEGAN, 'vegan'), (FOOD_VEGETARIAN, 'vegetarian'), (FOOD_OMNIVORE, 'omnivore')])
    notes = models.TextField(blank=True)
    validation_id = models.UUIDField(editable=False)
    validated = models.BooleanField(default=False, editable=False)
    mkdate = models.DateTimeField(auto_now_add=True)


class SchnupperanmeldungForm(ModelForm):
    class Meta:
        model = Schnupperanmeldung
        fields = '__all__'

    def send_confirmation(self, anmeldung):
        subject = 'Please confirm your registration for Schnupperstudium 2022'
        html_message = render_to_string('schnupper/confirmation_mail.html', locals())
        plain_message = strip_tags(html_message)
        sender = 'tobias.thelen@uni-osnabrueck.de'
        to = anmeldung.email
        send_mail(subject, plain_message, sender, [to], html_message=html_message, fail_silently=False)
