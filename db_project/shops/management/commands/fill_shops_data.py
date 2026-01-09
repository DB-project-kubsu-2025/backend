# management/commands/seed_products.py
import random
from uuid import uuid4
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from shops.models import Product, ProductUnit, ProductCategory


class Command(BaseCommand):
    help = 'Заполняет таблицу продуктов тестовыми данными'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Начинаем заполнение таблицы продуктов...')
        self.create_products()
        self.stdout.write(self.style.SUCCESS('Таблица продуктов успешно заполнена!'))

    def create_products(self):
        units = list(ProductUnit.objects.all())
        categories = list(ProductCategory.objects.all())

        products_data = [
            # Молочные продукты
            {
                'name': 'Молоко 2.5% пастеризованное',
                'description': 'Свежее пастеризованное молоко высшего сорта',
                'expiration_days': 5,
                'producer_name': 'Молочный комбинат "Вкуснотеево"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'В пластиковой бутылке 1л, жирность 2.5%',
                'unit': 'Литр',
                'category': 'Молочные продукты и яйца'
            },
            {
                'name': 'Сметана 15%',
                'description': 'Натуральная сметана',
                'expiration_days': 7,
                'producer_name': 'Молочный комбинат "Домик в деревне"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'В пластиковом стаканчике 400г',
                'unit': 'Грамм',
                'category': 'Молочные продукты и яйца'
            },
            {
                'name': 'Творог 9%',
                'description': 'Творог мягкий зерненый',
                'expiration_days': 5,
                'producer_name': 'Творожный завод "Простоквашино"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'В вакуумной упаковке 200г',
                'unit': 'Грамм',
                'category': 'Молочные продукты и яйца'
            },
            {
                'name': 'Сыр Российский',
                'description': 'Твердый сыр 45% жирности',
                'expiration_days': 30,
                'producer_name': 'Сыродельный комбинат "Сырный край"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'В вакуумной упаковке, нарезка 300г',
                'unit': 'Грамм',
                'category': 'Молочные продукты и яйца'
            },

            # Мясные продукты
            {
                'name': 'Колбаса Докторская',
                'description': 'Вареная колбаса высшего сорта',
                'expiration_days': 15,
                'producer_name': 'Мясокомбинат "Микоян"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'В натуральной оболочке, 500г',
                'unit': 'Грамм',
                'category': 'Мясо и мясные продукты'
            },
            {
                'name': 'Куриное филе',
                'description': 'Охлажденное куриное филе',
                'expiration_days': 3,
                'producer_name': 'Птицефабрика "Челябинская"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Вакуумная упаковка 1кг',
                'unit': 'Килограмм',
                'category': 'Мясо и мясные продукты'
            },
            {
                'name': 'Свиная вырезка',
                'description': 'Охлажденная свиная вырезка',
                'expiration_days': 4,
                'producer_name': 'Мясокомбинат "Останкино"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Вакуумная упаковка 800г',
                'unit': 'Грамм',
                'category': 'Мясо и мясные продукты'
            },

            # Овощи и фрукты
            {
                'name': 'Яблоки Голден',
                'description': 'Свежие яблоки сорта Голден',
                'expiration_days': 20,
                'producer_name': 'Фруктовый сад "Краснодарский"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Упаковка сетка 1кг',
                'unit': 'Килограмм',
                'category': 'Овощи и фрукты'
            },
            {
                'name': 'Картофель молодой',
                'description': 'Молодой картофель мытый',
                'expiration_days': 30,
                'producer_name': 'Сельхозпредприятие "Белая дача"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Сетка 2кг',
                'unit': 'Килограмм',
                'category': 'Овощи и фрукты'
            },
            {
                'name': 'Помидоры черри',
                'description': 'Помидоры черри на ветке',
                'expiration_days': 10,
                'producer_name': 'Тепличный комплекс "Московский"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Лоток 250г',
                'unit': 'Грамм',
                'category': 'Овощи и фрукты'
            },

            # Бакалея
            {
                'name': 'Гречневая крупа',
                'description': 'Гречневая крупа ядрица',
                'expiration_days': 365,
                'producer_name': 'Крупяной завод "Алтай"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Бумажный пакет 900г',
                'unit': 'Грамм',
                'category': 'Бакалея'
            },
            {
                'name': 'Сахар-песок',
                'description': 'Сахар-песок рафинированный',
                'expiration_days': 730,
                'producer_name': 'Сахарный завод "Русский сахар"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Бумажный пакет 1кг',
                'unit': 'Килограмм',
                'category': 'Бакалея'
            },
            {
                'name': 'Макароны рожки',
                'description': 'Макаронные изделия из твердых сортов пшеницы',
                'expiration_days': 180,
                'producer_name': 'Макаронная фабрика "Макфа"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Бумажная пачка 450г',
                'unit': 'Грамм',
                'category': 'Бакалея'
            },

            # Напитки
            {
                'name': 'Вода минеральная газированная',
                'description': 'Природная минеральная вода',
                'expiration_days': 365,
                'producer_name': 'Водный источник "Ессентуки"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Пластиковая бутылка 1.5л',
                'unit': 'Литр',
                'category': 'Напитки'
            },
            {
                'name': 'Сок апельсиновый',
                'description': 'Сок прямого отжима',
                'expiration_days': 90,
                'producer_name': 'Соковый завод "Добрый"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Тетрапак 1л',
                'unit': 'Литр',
                'category': 'Напитки'
            },

            # Кондитерские изделия
            {
                'name': 'Шоколад молочный',
                'description': 'Молочный шоколад с фундуком',
                'expiration_days': 180,
                'producer_name': 'Кондитерская фабрика "Красный Октябрь"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Плитка 100г',
                'unit': 'Грамм',
                'category': 'Кондитерские изделия'
            },
            {
                'name': 'Печенье овсяное',
                'description': 'Овсяное печенье с изюмом',
                'expiration_days': 60,
                'producer_name': 'Кондитерская фабрика "Большевик"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Картонная коробка 300г',
                'unit': 'Грамм',
                'category': 'Кондитерские изделия'
            },

            # Замороженные продукты
            {
                'name': 'Блинчики с творогом',
                'description': 'Замороженные блинчики с творожной начинкой',
                'expiration_days': 90,
                'producer_name': 'Завод замороженных продуктов "Хладокомбинат"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Пакет 500г, 8 шт',
                'unit': 'Грамм',
                'category': 'Замороженные продукты'
            },
            {
                'name': 'Овощная смесь',
                'description': 'Смесь замороженных овощей',
                'expiration_days': 180,
                'producer_name': 'Овощная база "Морозко"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Пакет 400г',
                'unit': 'Грамм',
                'category': 'Замороженные продукты'
            },

            # Хлеб и выпечка
            {
                'name': 'Хлеб пшеничный нарезной',
                'description': 'Свежий пшеничный хлеб',
                'expiration_days': 3,
                'producer_name': 'Хлебозавод №1',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Буханка 500г',
                'unit': 'Грамм',
                'category': 'Хлеб и выпечка'
            },
            {
                'name': 'Батон нарезной',
                'description': 'Пшеничный батон',
                'expiration_days': 2,
                'producer_name': 'Хлебозавод "Каравай"',
                'producer_code': uuid4(),
                'country_name': 'Россия',
                'additional_info': 'Буханка 350г',
                'unit': 'Грамм',
                'category': 'Хлеб и выпечка'
            },
        ]

        created_count = 0
        for data in products_data:
            try:
                unit = ProductUnit.objects.get(name=data.pop('unit'))
                category = ProductCategory.objects.get(name=data.pop('category'))

                product, created = Product.objects.get_or_create(
                    name=data['name'],
                    defaults={
                        'unit': unit,
                        'category': category,
                        **data
                    }
                )

                if created:
                    created_count += 1

            except (ProductUnit.DoesNotExist, ProductCategory.DoesNotExist) as e:
                self.stdout.write(self.style.WARNING(f'Пропускаем продукт {data["name"]}: {e}'))
                continue

        self.stdout.write(f'✅ Создано {created_count} продуктов из {len(products_data)}')