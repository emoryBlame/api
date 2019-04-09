from django.shortcuts import render
from django.views.generic import ListView, View
from django.http.response import JsonResponse


from .models import Payment
# Create your views here.

default_payment = {
    "status": "new",
    "price_currency": "USD",
    "price_amount": "0.02",
    "receive_currency": "EUR",
    #"receive_amount": "",
    "order_id": "111",
    #"payment_url": "https://sandbox.coingate.com/pay/",
    "token": "cSX-bZbWyDyhrSaWD868NZzVwt95_dy1rR-DsCof"
}


class LookingForward(ListView):

    model = Payment
    template_name = "looking_forward.html"
    ordering = "-created_at"

    # def get_context_data(self, *args, **kwargs):
    #     context = self.get_context_data(*args, **kwargs)
    #     current_payment = self.model.objects.create(**default_payment)
    #     current_payment.payment_url += str
    #     context["new"] = current_payment
    #     current_payment["payment_url"] += 


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
        #payment.
        context = {"payment": payment.invoice_json()}
        return context
