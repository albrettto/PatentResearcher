from rest_framework import serializers


class PatentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    # Углерод - Carbon
    c = serializers.FloatField(required=False)
    # Хром - Chrome
    cr = serializers.FloatField(required=False)
    # Кобальт - Cobalt
    co = serializers.FloatField(required=False)
    # Молибден - Molybdenum
    mo = serializers.FloatField(required=False)
    # Вольфрам - Wolfram
    w = serializers.FloatField(required=False)
    # Титан - Titan
    ti = serializers.FloatField(required=False)
    # Алюминий - Aluminum
    al = serializers.FloatField(required=False)
    # Ниобий
    nb = serializers.FloatField(required=False)
    # Тантал - Tantalum
    ta = serializers.FloatField(required=False)
    # Бор
    b = serializers.FloatField(required=False)
    # Цирконий
    zr = serializers.FloatField(required=False)
    # Гафний
    hf = serializers.FloatField(required=False)
    # Ванадий
    v = serializers.FloatField(required=False)
    # Рений - Renius
    re = serializers.FloatField(required=False)
    # Рутений
    ru = serializers.FloatField(required=False)
    # Иридий
    ir = serializers.FloatField(required=False)
    # Церий - Cerium
    ce = serializers.FloatField(required=False)
    # Лантан - Lanthanum
    la = serializers.FloatField(required=False)
    # Неодим - Neodymium
    nd = serializers.FloatField(required=False)
    # Иттрий - Yttrium
    y = serializers.FloatField(required=False)
    link = serializers.CharField()
    doclink = serializers.CharField(required=False)
