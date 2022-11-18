from django.shortcuts import render


def main(request):
    context = {"msg": "Rekruto! Давай дружить!"}
    if "name" in request.GET and "message" in request.GET:
        name = request.GET.get("name")
        message = request.GET.get("message")
        context["msg"] = f"Hello {name}! {message}!"
    return render(request, "main.html", context=context)
