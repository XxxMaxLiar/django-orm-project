import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())   # noqa: T001
    passcards = Passcard.objects.all()   # Импорт всех данных из БД
    active_passcard = Passcard.objects.filter(is_active = True)   #Сохраняем в переменную только активных пользователей
    print('Активных пропусков:', len(active_passcard))