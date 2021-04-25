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
    chars = []
    if request.method == "POST":
        len_pass = int(request.POST["length_password"])
        if 65 > len_pass > 0:
            if request.POST.get("sym_numbers") == "Digits":
                chars = digits
            if request.POST.get("sym_letters") == "Letters":
                chars = letters
            if request.POST.get("sym_punctuation") == "Punctuation":
                chars = punctuation
            if request.POST.get("sym_letters") == "Letters" and request.POST.get("sym_numbers") == "Digits":
                chars = letters + digits
            if request.POST.get("sym_letters") == "Letters" and request.POST.get("sym_punctuation") == "Punctuation":
                chars = letters + punctuation
            if request.POST.get("sym_numbers") == "Digits" and request.POST.get("sym_punctuation") == "Punctuation":
                chars = punctuation + digits
            if request.POST.get("sym_letters") == "Letters" and request.POST.get("sym_numbers") == "Digits" and \
                    request.POST.get("sym_punctuation") == "Punctuation":
                chars = letters + digits + punctuation
            for _ in range(len_pass):
                password += random.choice(chars)
    data = {"password": password, "len_pass": len_pass}

    return render(request, "index.html", context=data)


