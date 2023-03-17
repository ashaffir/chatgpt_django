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
            return render(request, "main/chat.html", {"response": chat_reply, "usage": usage['total_tokens']})
        except Exception as e:
            print(f"error: {e}")
            response = "error"
            chat_reply = ""
            usage = None
            return render(request, "main/chat.html")

    else:
        return render(request, "main/chat.html")