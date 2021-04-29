from django.db import models

mobiles_color = [
    ('white', 'White'),
    ('black', 'Black'),
    ('gold', 'Gold'),
    ('silver', 'Silver'),
    ('blue', 'Blue'),
]

class Mobile(models.Model):

    brand_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='نام برند')
    brand_nationality = models.CharField(max_length=20, null=False, blank=False, verbose_name='ملیت برند')
    model = models.CharField(max_length=20, unique=True, verbose_name='مدل گوشی')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    color = models.CharField(max_length=10, choices=mobiles_color, verbose_name='رنگ')
    resulation = models.FloatField(verbose_name='سایز صفحه نمایش')
    is_available = models.BooleanField(default=False, verbose_name='وضعیت موجودی')
    manufacturer = models.CharField(max_length=20, verbose_name='کشور سازنده')

    class Meta:
        verbose_name = 'موبایل'
        verbose_name_plural = 'موبایل ها'

    def __str__(self):
        return self.model
