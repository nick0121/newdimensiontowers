
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from towers.forms import SearchForm
from .models import Products
from .models import Images
from .forms import ContactForm



############################################################# INDEX VIEWS ############################################
def index(request):
    products = Products.objects.all()

    context = {
        "products": products,
    }

    return render(request, "pages/index.html", context)


############################################################# ABOUT VIEWS ############################################
def about(request):
    return render(request, "pages/about.html")


############################################################# CONTACT VIEWS ############################################
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        #####SET UP EMAIL HERE
        # message = request.POST.get("message")
        message = "this is a test email"
        toEmail = "owner@vankoindustries.com"
        fromEmail = settings.EMAIL_HOST_USER

        if form.is_valid():

            form.save()

                        # send mail
            send_mail(
                "new mail from website",
                message,
                fromEmail,
                [toEmail,],
                fail_silently=True,
            )

            form = ContactForm()
            messages.success(request, "Thanks!! Someone will contact you soon")
            return HttpResponseRedirect(reverse("contact"))

    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, "pages/contact.html", context)


############################################################# ACCESSORIES VIEWS ############################################
def accessories(request):

    products = Products.objects.all()

    context = {
        "products": products,
    }

    return render(request, "pages/accessories.html", context)


def accessory(request, query):

    products = Products.objects.filter(category=query)

    context = {"products": products}

    return render(request, "pages/accessories.html", context)


def accessory_product(request, category, product_id):

    product = Products.objects.filter(slug=product_id)
    product_id = product[0].id

    images = Images.objects.filter(product_id=product_id)

    context = {
        "product": product,
        "images": images,
    }

    return render(request, "pages/product.html", context)


############################################################# BIMINIS VIEWS ############################################
def biminis(request):
    # products = Products.objects.filter(images__manufacturer="ndt")

    form = SearchForm()

    context = {
        "form": form,
    }

    return render(request, "pages/biminis.html", context)


############################################################# INSTALLATION VIEWS ############################################
def installation(request):
    return render(request, "pages/installation.html")


############################################################# FAQ VIEWS ############################################
def faq(request):
    return render(request, "pages/faq.html")


############################################################# FAQ VIEWS ############################################
def orders(request):
    return render(request, "pages/orders.html")


######################################################## product views #########################################
def product(request):

    ## Add products from models

    return render(request, "pages/product.html")
