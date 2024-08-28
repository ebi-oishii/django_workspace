from django.db import models
from category.models import Category
from accounts.models import User
import uuid
# Create your models here.

class Transaction(models.Model):
    class Meta:
        db_table = 'transaction'
    
    transaction_id = models.UUIDField(verbose_name="取引Id", default=uuid.uuid4, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField(verbose_name = "取引名", null = True, blank = True)
    amount = models.IntegerField(verbose_name = "金額")
    register_time = models.DateTimeField(verbose_name = "登録日時", auto_now_add = True)
    update_time = models.DateTimeField(verbose_time = "更新日時", auto_now=True)
    remark = models.TextField(verbose_name = "備考", blank = True, null = True)