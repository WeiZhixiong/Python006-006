from django.db import models


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    # ¶©µ¥½ð¶î
    amount = models.PositiveIntegerField()
    is_cancel = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<order_id:{self.order_id};amount:{self.amount}>'
