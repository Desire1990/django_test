from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Person(models.Model):
	user              = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar            = models.ImageField(null=True, blank=True,upload_to="image/")
	Prenom            = models.CharField(max_length = 50)
	Nom               = models.CharField(max_length = 50)
	NomPere           = models.CharField(max_length = 20)
	NomMere           = models.CharField(max_length = 20)
	colline           = models.CharField(max_length = 20)
	commune_natal     = models.CharField(max_length = 20)
	province_natal    = models.CharField(max_length = 20)
	anneeDeNaissance  = models.CharField(max_length = 20)
	nationalite       = models.CharField(max_length = 20)
	etatCivil         = models.CharField(max_length = 20)
	profession        = models.CharField(max_length = 20)
	numberId          = models.CharField(max_length = 20)
	date_delivrated   = models.DateField()


	def __str__(self):
		return ("{0} {1}".format(self.Nom, self.Prenom))





class Province(models.Model):
	name     = models.CharField(max_length = 20)
	govner   = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Commune(models.Model):
	# province        = models.ForeignKey(Province, on_delete=models.CASCADE)
	name            = models.CharField(max_length = 30)
	administrator   = models.CharField(max_length = 30)

	def __str__(self):
		return self.name
	

class Zone(models.Model):
	# commune         = models.ForeignKey(Commune, on_delete=models.CASCADE)
	name            = models.CharField(max_length = 30)
	chefZoneLeader  = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Quarter(models.Model):
	# zone           = models.ForeignKey(Zone, on_delete=models.CASCADE)
	name           = models.CharField(max_length = 30)
	chefQuarter    = models.CharField(max_length = 30)

	def __str__(self):
		return self.name



class IdentiteComplete(models.Model):
	user              = models.OneToOneField(User, 
											on_delete=models.CASCADE,
											default = False, 
											related_name='users')
	Person            = models.ForeignKey(Person, 
											on_delete=models.CASCADE,
											default = False,
											related_name = 'identiteCompletes')
	province          = models.ForeignKey(Province, on_delete=models.CASCADE)
	commune           = models.ForeignKey(Commune, on_delete=models.CASCADE)
	zone              = models.ForeignKey(Zone, on_delete=models.CASCADE)
	quarter           = models.ForeignKey(Quarter, on_delete = models.CASCADE)
	attestionId       = models.CharField(max_length = 30)
	date              = models.DateField()


	
	def __str__(self):
		return self.user.username
