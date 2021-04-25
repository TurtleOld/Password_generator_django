from django.shortcuts import render
import random
import string


# Create your views here.


def pass_gen(request):
    digits = string.digits
    letters = string.ascii_letters
    punctuation = string.punctuation
    # chars = letters + digits + punctuation
    password = ''
    len_pass = 15
    if request.method == "POST":
        len_pass = int(request.POST["length_password"])
        if len_pass < 65:
            if request.POST.get("sym_numbers") == "Digits":
                chars = digits
                for item in range(len_pass):
                    password += random.choice(chars)
    data = {"password": password, "len_pass": len_pass}

    return render(request, "index.html", context=data)


