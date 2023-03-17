from django.shortcuts import render

from .chat import get_response

def chat(request):
    if request.method == "POST":
        message = request.POST.get("message")
        print(f"message: {request.POST.get('message')}")
        try:
            response = get_response(message)
            chat_reply = response.choices[0]["message"]["content"]
            usage = response["usage"]
            print(f"{response}")
        except Exception as e:
            response = "error"
            print(f"error: {e}")
        return render(request, "main/chat.html", {"response": chat_reply, "usage": usage['total_tokens']})
    else:
        return render(request, "main/chat.html")