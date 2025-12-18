from rest_framework import serializers
from .models import Chat, AgentResponse

class AgentResponseSerializers(serializers.ModelSerializer):

    class Meta:
        model = AgentResponse
        fields = ["agent_name", "response"]

class ChatSerializers(serializers.ModelSerializer):
    responses = AgentResponseSerializers(many = True, read_only = True)

    class Meta:
        model = Chat
        fields = ["id", "user_message", "timestamp", "responses"]