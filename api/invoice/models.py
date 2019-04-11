from django.db import models

# Create your models here.

class Payment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    status = models.CharField(max_length=50)
    price_currency = models.CharField(max_length=10)
    price_amount = models.DecimalField(max_digits=20000, decimal_places=2)
    receive_currency = models.CharField(max_length=10, blank=True)
    receive_amount = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    order_id = models.IntegerField()
    success_url = models.CharField(max_length=200, default="http://127.0.0.1:8000/success/")
    cancel_url = models.CharField(max_length=200, default="http://127.0.0.1:8000/")
    payment_url = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    message = models.CharField(max_length=200, blank=True)
    reason = models.CharField(max_length=200, blank=True)
    errors = models.CharField(max_length=2000, blank=True)

    def str(self):
        return "Payment #{} with status {}".format(self.id, self.status)

    def as_json(self):
        context = {}
        for key, value in self.__dict__.items():
            if key != "_state":
                context[key] = value
        return context

    def invoice_json(self):
        context = {}
        keys = [
            "order_id", "price_amount", "price_currency",
            "receive_currency", "success_url", "cancel_url",
            "token", "id"
        ]
        for key, value in self.__dict__.items():
            if key in keys:
                context[key] = value
        return context

    def remove_no_necessary_response_data(self, json):
        context = {}
        for key,value in json.items():
            if key in self.__dict__.keys():
                context[key] = value
        return context

