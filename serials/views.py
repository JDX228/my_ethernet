from django.shortcuts import render, redirect
from .models import Serial
from operator import itemgetter


def get_fresh_serials(request):
    serials_list = list(
        Serial.objects.filter(_is_expired=False).values(
            "title", "img", "data", "serial_and_season", "episode", "id"
        )
    )
    return render(request, "serials/serials.html", {"serials_list": serials_list})


def hidden_serial(request, pk):
    Serial.hidden(pk)
    return redirect("serials:serials")


def del_serial(request, pk):
    Serial.d_serial(pk)
    return redirect("serials:serials")
