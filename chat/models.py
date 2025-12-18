from django.db import models

# Create your models here.

class Chat(models.Model):
    user_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_message[:50]
    
class AgentResponse(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="responses")
    agent_name = models.CharField(max_length=50)
    response = models.TextField()

    def __str__(self):
        return f"{self.agent_name} respnse"

