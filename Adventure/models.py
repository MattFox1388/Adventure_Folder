from django.db import models

# Create your models here.


class Option(models.Model):
    text = models.CharField(max_length=256)
    target_state = models.ForeignKey('State', on_delete=models.CASCADE, related_name="state_target")
    current_state = models.ForeignKey('State', on_delete=models.CASCADE, related_name="state_current", null=True)

    def __str__(self):
        return "%s" % self.text


class State(models.Model):
    title = models.CharField(max_length=30)
    storytext = models.CharField(max_length=256)
    options = models.ManyToManyField(Option)

    def __str__(self):
        return "%s %s" % (self.title, self.storytext)
