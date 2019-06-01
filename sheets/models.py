from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Sheet(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=20, allow_unicode=True, unique=True)
    batch = models.CharField(max_length=20)
    problems_added = models.PositiveIntegerField(default=4, null=False)
    cut_off = models.PositiveIntegerField(default=0, null=False)
    cut_off_date = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(User, through='SheetMember')

    def __str__(self):
        return self.name + " ( " + str(self.batch) + " )"

    def get_absolute_url(self):
        return reverse('sheets:activity', kwargs={'slug': self.slug})
        return reverse('home')

    # incomplete
    class Meta:
        pass
        # ordering = ['']

class SheetMember(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name='memberships')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sheet')
    solve_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.member.username + ": " + self.sheet.name

    class Meta:
        unique_together = ['sheet', 'member']
