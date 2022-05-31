from django.db import models
from django.forms import ModelForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

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
    PLAN_INDIVIDUAL = 'L'

    company = models.CharField(max_length=128, blank=True, verbose_name="Company name (if registering as a company member)")
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    membership = models.CharField(max_length=1, choices=[(MEMBER_ALREADY, 'I am a member of F2IKW and want to stay a member.' ), (MEMBER_NOW, 'I want to become a member now (binding) and I\'ll be able to join the hybrid meeting on July, 13th, 18:00'), (MEMBER_LATER, 'I plan to become a member later (not binding, but we will remind you)')])
    plan = models.CharField(max_length=1, choices=[(PLAN_REDUCED, 'Reduced (21€)'), (PLAN_NORMAL, 'Regular (42€)'),
                                                   (PLAN_SENIOR, 'Senior (84€)'), (PLAN_SILVER, 'Company, silver member (420€)'),
                                                   (PLAN_GOLD, 'Company, gold member (42 * 42€ = 1.764€)'), (PLAN_INDIVIDUAL, 'Individual amount > 84€ for individuals, > 1764€ for companys, given below)')],
                            verbose_name="Membership type (non-binding, has to be declared after final decision on fees)")
    # iban = models.CharField(max_length=32, verbose_name='IBAN (only if you become a member now')  # will be checked via special form field
    extra_fee = models.IntegerField(verbose_name='Optional: Higher membership fee per year', blank=True, null=True)
    suggested_name = models.CharField(max_length=128, verbose_name='Suggested name for the association (examples suggested so far: "Coxi Club" or "CogSci Network"', blank=True)
    privacy = models.BooleanField(verbose_name="I agree to the data privacy declaration as given below")
    notes = models.TextField(blank=True)
    validation_id = models.UUIDField(editable=False)
    validated = models.BooleanField(default=False, editable=False)
    mkdate = models.DateTimeField(auto_now_add=True)

    def fee(self):
        if self.plan == Verein.PLAN_REDUCED: return 21
        if self.plan == Verein.PLAN_NORMAL: return 42
        if self.plan == Verein.PLAN_SENIOR: return 84
        if self.plan == Verein.PLAN_SILVER: return 420
        if self.plan == Verein.PLAN_GOLD: return 1764
        if self.plan == Verein.PLAN_INDIVIDUAL:
            return self.extra_fee

class VereinForm(ModelForm):
    class Meta:
        model = Verein
        fields = '__all__'

    def clean_privacy(self):
        privacy = self.cleaned_data['privacy']
        if not privacy:
            raise ValidationError("Please agree to the data privacy declaration.")
        return privacy

    def send_confirmation(self, anmeldung):
        subject = 'Please confirm your commitment for F2IKW / The CogSci Network'
        html_message = render_to_string('cogscinet/confirmation_mail.html', locals())
        plain_message = strip_tags(html_message)
        sender = '"F2IKW e.V. (Tobias Thelen)" <tobias.thelen@uni-osnabrueck.de>'
        to = anmeldung.email
        send_mail(subject, plain_message, sender, [to], html_message=html_message, fail_silently=False)
