# 참고: https://cocook.tistory.com/56

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from products.models import Product, ProductImage
import json

# 테스트
'''
product = Product()

product.name = '테스트3'
product.category = '테스트'
product.pay = 10000
product.Description = '블라블라'
product.delivery = 3000
product.sale = 10
product.product_image = 'imgaes/test3.jpg'

# product.save()
'''


# 1) '노트.json' 파일을 받아서 DB에 데이터 저장하기
with open('노트.json') as f:   # json -> 파이썬 변환
   note_pdts = json.load(f)

for i in range(40):
    product = Product()

    product.name = note_pdts[i]['pdt_name']
    product.category = note_pdts[i]['pdt_category']
    product.pay = int(note_pdts[i]['pdt_pay'])
    product.Description2 = f'imgaes/note_{i}_description_0.jpg'
    product.delivery = note_pdts[i]['pdt_delivery']
    product.sale = int(note_pdts[i]['pdt_sale'])

    product.save()

    for j in range(len(note_pdts[i]['pdt_images'])):
        product_image = ProductImage()
        product_image.product = product
        product_image.image = f'imgaes/note_{i}_images_{j}.jpg'
        
        product_image.save()


# 2) '다이어리.json' 파일을 받아서 DB에 데이터 저장하기
with open('다이어리.json') as f:   # json -> 파이썬 변환
   diary_pdts = json.load(f)

for i in range(40):
    product = Product()

    product.name = diary_pdts[i]['pdt_name']
    product.category = diary_pdts[i]['pdt_category']
    product.pay = int(diary_pdts[i]['pdt_pay'])
    product.Description2 = f'imgaes/diary_{i}_description_0.jpg'
    product.delivery = diary_pdts[i]['pdt_delivery']
    product.sale = int(diary_pdts[i]['pdt_sale'])

    product.save()

    for j in range(len(diary_pdts[i]['pdt_images'])):
        product_image = ProductImage()
        product_image.product = product
        product_image.image = f'imgaes/diary_{i}_images_{j}.jpg'
        
        product_image.save()


# 3) '파일.json' 파일을 받아서 DB에 데이터 저장하기
with open('파일.json') as f:   # json -> 파이썬 변환
   file_pdts = json.load(f)

for i in range(40):
    product = Product()

    product.name = file_pdts[i]['pdt_name']
    product.category = file_pdts[i]['pdt_category']
    product.pay = int(file_pdts[i]['pdt_pay'])
    product.Description2 = f'imgaes/files_{i}_description_0.jpg'
    product.delivery = file_pdts[i]['pdt_delivery']
    product.sale = int(file_pdts[i]['pdt_sale'])

    product.save()

    for j in range(len(file_pdts[i]['pdt_images'])):
        product_image = ProductImage()
        product_image.product = product
        product_image.image = f'imgaes/files_{i}_images_{j}.jpg'
        
        product_image.save()


# 4) '필기류.json' 파일을 받아서 DB에 데이터 저장하기
with open('필기류.json') as f:   # json -> 파이썬 변환
   writing_pdts = json.load(f)

for i in range(40):
    product = Product()

    product.name = writing_pdts[i]['pdt_name']
    product.category = writing_pdts[i]['pdt_category']
    product.pay = int(writing_pdts[i]['pdt_pay'])
    product.Description2 = f'imgaes/writing_{i}_description_0.jpg'
    product.delivery = writing_pdts[i]['pdt_delivery']
    product.sale = int(writing_pdts[i]['pdt_sale'])

    product.save()

    for j in range(len(writing_pdts[i]['pdt_images'])):
        product_image = ProductImage()
        product_image.product = product
        product_image.image = f'imgaes/writing_{i}_images_{j}.jpg'
        
        product_image.save()