from ..serializers import PatentSerializer
from ..models import Patent
from ..scrapping import take_all_links
from django.db import IntegrityError


class PatentService:
    def get_all_patents(self) -> PatentSerializer:
        result = Patent.objects.all()
        return PatentSerializer(result, many=True)

    def add_patent(self, patent: PatentSerializer) -> None:
        patent_data = patent.data
        patent_name = patent_data.get('name')
        defaults = {
            'c': patent_data.get('c'),
            'cr': patent_data.get('cr'),
            'co': patent_data.get('co'),
            'mo': patent_data.get('mo'),
            'w': patent_data.get('w'),
            'ti': patent_data.get('ti'),
            'al': patent_data.get('al'),
            'nb': patent_data.get('nb'),
            'ta': patent_data.get('ta'),
            'b': patent_data.get('b'),
            'zr': patent_data.get('zr'),
            'hf': patent_data.get('hf'),
            'v': patent_data.get('v'),
            're': patent_data.get('re'),
            'ru': patent_data.get('ru'),
            'ir': patent_data.get('ir'),
            'ce': patent_data.get('ce'),
            'la': patent_data.get('la'),
            'nd': patent_data.get('nd'),
            'y': patent_data.get('y'),
            'link': patent_data.get('link'),
            'doclink': patent_data.get('doclink'),
        }

        try:
            patent_obj, created = Patent.objects.get_or_create(name=patent_name, defaults=defaults)

            if not created:
                # Обновляем значения полей при конфликте
                for key, value in defaults.items():
                    setattr(patent_obj, key, value)
                patent_obj.save()
        except IntegrityError:
            # Обработка ошибки уникального ограничения
            existing_patent = Patent.objects.get(name=patent_name)
            for key, value in defaults.items():
                setattr(existing_patent, key, value)
            existing_patent.save()

    def parse_new_patents(self) -> PatentSerializer:
        result = take_all_links.get_links()
        return PatentSerializer(result, many=True)
