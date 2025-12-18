# chat/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Chat, AgentResponse
from .services import summarizer_agent, answer_agent

class ChatAPIView(APIView):
    def post(self, request):
        message = request.data.get("message")

        if not message:
            return Response(
                {"error": "message field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        chat = Chat.objects.create(user_message=message)

        summary = summarizer_agent(message)
        answer = answer_agent(message)

        AgentResponse.objects.create(
            chat=chat,
            agent_name="summarizer",
            response=summary
        )
        AgentResponse.objects.create(
            chat=chat,
            agent_name="answer",
            response=answer
        )

        return Response({
            "user_message": message,
            "agents": {
                "summarizer": summary,
                "answer": answer
            }
        })
