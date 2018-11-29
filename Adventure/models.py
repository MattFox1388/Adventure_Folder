from django.db import models

# Create your models here.
class State(models.Model):
    title = models.CharField(max_length=30)
    storytext = models.CharField(max_length=256)
    options = models.ForeignKey('Option', blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.title, self.storytext)

class Option(models.Model):
    text = models.CharField(max_length=256)
    target_state = models.ForeignKey(State)
    current_state = models.ForeignKey(State)

    def __str__(self):
        return "%s" % self.text
