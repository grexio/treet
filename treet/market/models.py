from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Treet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User)
    video = models.CharField(verbose_name="Youtube Video ID", max_length=20)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TreetPurchase(models.Model):
    STATES = (
        ('PEND', 'Pending'),
        ('ACPT', 'Accepted'),
        ('RJCT', 'Rejected'),
        ('CNCL', 'Cancelled'),
        ('CMPL', 'Completed'),
        ('FAIL', 'Failed')
    )

    treet = models.ForeignKey(Treet)
    purchaser = models.ForeignKey(User, related_name="purchaser")
    seller = models.ForeignKey(User, related_name="seller")
    purchased_on = models.DateTimeField(auto_now_add=True)
    resolved_on = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=10, choices=STATES)

    def __str__(self):
        return self.treet.title


@python_2_unicode_compatible
class TreetReview(models.Model):
    title = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comments = models.TextField()
    user = models.ForeignKey(User)
    treet_purchase = models.OneToOneField(TreetPurchase)

    def __str__(self):
        return title
