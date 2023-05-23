from django.db import models


class Patent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False, unique=True, blank=True)
    # Углерод - Carbon
    c = models.FloatField(null=True, blank=True)
    # Хром - Chrome
    cr = models.FloatField(null=True, blank=True)
    # Кобальт - Cobalt
    co = models.FloatField(null=True, blank=True)
    # Молибден - Molybdenum
    mo = models.FloatField(null=True, blank=True)
    # Вольфрам - Wolfram
    w = models.FloatField(null=True, blank=True)
    # Титан - Titan
    ti = models.FloatField(null=True, blank=True)
    # Алюминий - Aluminum
    al = models.FloatField(null=True, blank=True)
    # Ниобий
    nb = models.FloatField(null=True, blank=True)
    # Тантал - Tantalum
    ta = models.FloatField(null=True, blank=True)
    # Бор
    b = models.FloatField(null=True, blank=True)
    # Цирконий
    zr = models.FloatField(null=True, blank=True)
    # Гафний
    hf = models.FloatField(null=True, blank=True)
    # Ванадий
    v = models.FloatField(null=True, blank=True)
    # Рений - Renius
    re = models.FloatField(null=True, blank=True)
    # Рутений
    ru = models.FloatField(null=True, blank=True)
    # Иридий
    ir = models.FloatField(null=True, blank=True)
    # Церий - Cerium
    ce = models.FloatField(null=True, blank=True)
    # Лантан - Lanthanum
    la = models.FloatField(null=True, blank=True)
    # Неодим - Neodymium
    nd = models.FloatField(null=True, blank=True)
    # Иттрий - Yttrium
    y = models.FloatField(null=True, blank=True)
    link = models.CharField(max_length=250, null=False)
    doclink = models.CharField(max_length=250, null=True, blank=True)
    class Meta:
        db_table = 'Patent'

    def __str__(self):
        return self.name
