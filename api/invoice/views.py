from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.http.response import JsonResponse
import requests
from django.urls import reverse
from django.contrib import messages

from .models import Payment
# Create your views here.

default_payment = {
    "status": "new",
    "price_currency": "USD",
    "price_amount": "1.00",
    "receive_currency": "EUR",
    #"receive_amount": "",
    "order_id": "111",
    #"payment_url": "https://sandbox.coingate.com/pay/",
    "token": "fzWr8vzbSRNJq2MCxux2iw9-DMtjWXkxZMvhxmn6" #fzWr8vzbSRNJq2MCxux2iw9-DMtjWXkxZMvhxmn6   cSX-bZbWyDyhrSaWD868NZzVwt95_dy1rR-DsCof
}


class LookingForward(ListView):

    model = Payment
    template_name = "looking_forward.html"
    ordering = "-created_at"
    context_object_name = "payments"


class AjaxResponseView(View):

    def dispatch(self, request, *args, **kwargs):
        return self.render_to_ajax_response(request, *args, **kwargs)

    def get_data(self, request, *args, **kwargs):
        context = {}
        return context

    def render_to_ajax_response(self, request, *args, **kwargs):
        return JsonResponse(self.get_data(request, *args, **kwargs))


class PaymentAjaxView(AjaxResponseView):

    def get_data(self, request, *args, **kwargs):
        payment = Payment.objects.create(**default_payment)
        payment.save()
        print(payment.pk)
        context = payment.invoice_json()
        headers = {"Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Token fzWr8vzbSRNJq2MCxux2iw9-DMtjWXkxZMvhxmn6"}
        r = requests.post("https://api-sandbox.coingate.com/v2/orders/", data=context, headers=headers)
        if r.status_code:
            data = payment.remove_no_necessary_response_data(r.json())
            pay = Payment.objects.filter(pk=payment.id).update(**data)
            print(payment.id)
            try:
                p = Payment.objects.get(pk=payment.id)
                context = p.as_json()
            except Exception as exc:
                print("Can't get payment by id", exc)
        return context


class PaymentAjaxSuccessView(View):

    def dispatch(self, request, *args, **kwargs):
        print("any data?",request.POST, request.GET, args, kwargs)
        payments = Payment.objects.filter(status="new") 
        headers = {"Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Token fzWr8vzbSRNJq2MCxux2iw9-DMtjWXkxZMvhxmn6"}
        for payment in payments:
            r = requests.post("https://api.coingate.com/v2/orders/{}/checkout"\
                .format(payment.order_id), data={"pay_currency": "BTC"} ,headers=headers)
            if r.status_code:
                data = payment.remove_no_necessary_response_data(r.json())
                Payment.objects.filter(pk=payment.pk).update(**data)
                p = Payment.objects.get(pk=payment.pk)
                context = p.as_json()
        #messages.success(request, "Success payment!")
        return redirect(reverse("looking-forward"))

