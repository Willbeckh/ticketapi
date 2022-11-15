from django.db import models
import uuid
from django.contrib.auth.models import User

# ticket id generator method
def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]

# Create your models here.
class Ticket(models.Model):
    """This class represents the ticket object."""
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """tickect string identifier."""
        return f"{self.title} - {self.ticket_id}"
    
    def save(self, *args, **kwargs):
        """Saves the tickect.
        
        Keyword arguments:
        ticket_id -- unique identifier key
        Return: a ticket with a universal unique identifier.
        """
        if len(self.ticket_id.strip(" "))== 0:
            self.ticket_id = generate_ticket_id()
            
        super(Ticket, self).save(*args, **kwargs) # calls the django save method

    class Meta:
        ordering = ["-created_at"]
        
        
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name