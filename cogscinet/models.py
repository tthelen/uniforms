from django.db import models
from django.forms import ModelForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your models here.
class Verein(models.Model):

    MEMBER_ALREADY = 'A'
    MEMBER_NOW = 'N'
    MEMBER_LATER = 'L'

    PLAN_REDUCED = 'R'
    PLAN_NORMAL = 'N'
    PLAN_SENIOR = 'S'
    PLAN_SILVER = 'I'
    PLAN_GOLD = 'G'

    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    membership = models.CharField(max_length=1, choices=[(MEMBER_ALREADY, 'Already member' ), (MEMBER_NOW, 'New membership'), (MEMBER_LATER, 'Planned for later')])
    iban = models.CharField(max_length=32, verbose_name='IBAN')  # will be checked via special form field
    plan = models.CharField(max_length=1, choices=[(PLAN_REDUCED, 'Reduced (21€)'), (PLAN_NORMAL, 'Regular (42€)'), (PLAN_SENIOR, 'Senior (84€)'), (PLAN_SILVER, 'Company, silver member (420€)'), (PLAN_GOLD, 'Company, gold member (1.764€)')])
    extra_fee = models.IntegerField(verbose_name='Optional: Higher membership fee per year')
    suggested_name = models.CharField(max_length=128, verbose_name='Suggested name for the association')
    notes = models.TextField(blank=True)
    validation_id = models.UUIDField(editable=False)
    validated = models.BooleanField(default=False, editable=False)
    mkdate = models.DateTimeField(auto_now_add=True)


class VereinForm(ModelForm):
    class Meta:
        model = Verein
        fields = '__all__'

    def send_confirmation(self, anmeldung):
        subject = 'Please confirm your registration for F2IKW / The CogSci Network'
        html_message = render_to_string('cogscinet/confirmation_mail.html', locals())
        plain_message = strip_tags(html_message)
        sender = 'tobias.thelen@uni-osnabrueck.de'
        to = anmeldung.email
        send_mail(subject, plain_message, sender, [to], html_message=html_message, fail_silently=False)
