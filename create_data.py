#!/bin/env python
import random
import mysql
from mysql.connector import Error
import math
from faker import Faker
Faker.seed(3342)

fake = Faker(locale="fr_FR")

TYPE =["mixed","women","men","kid","baby"]
STATUT = ["delivered","in_delivery","in_preparation"]



conn = mysql.connector.connect(host='localhost', database = "ali_steve",
                                user="root", password="Cledev444!")

if conn.is_connected():
    cursor = conn.cursor()
    for i in range(50):
        row = [fake.country(), fake.country_code()]
        cursor.execute('INSERT INTO `country` (label, initials) VALUES ("%s", "%s");' % (row[0], row[1]))
    conn.commit()
    select_country =("Select * from country")
    cursor.execute(select_country)
    countries = cursor.fetchall()
    print("country")
    for country in countries:
        for i in range(random.randint(5, 15)):
            initial = fake.city_suffix()
            row = [fake.city(), fake.postcode(),fake.country_code(),country[0]]
            cursor.execute('INSERT INTO `town` (label, zipCode,initials,country_id) VALUES ("%s", "%s","%s","%s");' % (row[0], row[1],row[2],row[3]))
        conn.commit()
    select_towns =("Select * from town")
    cursor.execute(select_towns)
    towns = cursor.fetchall()
    print("town")
    for town in towns:
        for i in range(random.randint(500, 1000)):
            row = [fake.street_address(), town[0]]
            cursor.execute('INSERT INTO `address` (label, town_id) VALUES ("%s", "%s");' % (row[0], row[1]))
        conn.commit()
    select_adress =("Select * from address")
    cursor.execute(select_adress)
    addresses = cursor.fetchall()
    warehouses_address_number = math.floor(len(addresses)/20)
    print("warehouse")
    for w in range(warehouses_address_number):
        row = [addresses[w][0]]
        cursor.execute('INSERT INTO `warehouse` (address_id) VALUES ("%s");' % (row[0]))
    conn.commit()
    print("addres user")
    for u in range(warehouses_address_number+1,len(addresses)):
        row = [fake.ascii_email(),fake.name(),fake.password(),fake.word().title(),fake.phone_number(),fake.date(),addresses[u][0]]
        cursor.execute('INSERT INTO `user` (email,username,password,firstname,phone_number,created_at,address_id) VALUES ("%s", "%s","%s", "%s","%s", "%s","%s");' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    conn.commit()
    print("category")
    for i in range(30):
        row = [fake.word()]
        cursor.execute('INSERT INTO `category` (label) VALUES ("%s");' % (row[0]))
    conn.commit()
    select_categories =("Select * from category")
    cursor.execute(select_categories)
    categories = cursor.fetchall()
    print("product")
    for category in categories:
        for i in range(random.randint(10, 10000)):
            row = [fake.word().title(),fake.paragraph(nb_sentences=5),random.randint(0, 150),random.choice(TYPE),fake.date(),fake.date(),category[0]]
            cursor.execute('INSERT INTO `product` (name,description,price,type,created_at,updated_at,category_id) VALUES ("%s","%s","%s","%s","%s","%s","%s");' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        conn.commit()
    select_products =("Select * from product")
    cursor.execute(select_products)
    products = cursor.fetchall()
    select_warehouses =("Select * from warehouse")
    cursor.execute(select_warehouses)
    warehouses = cursor.fetchall()
    select_users =("Select * from user")
    cursor.execute(select_users)
    users = cursor.fetchall()
    print("warehouse sproduct")
    for product in products:
        warehouse = random.choice(warehouses)
        row = [warehouse[0],product[0],random.randint(0, 1500)]
        cursor.execute('INSERT INTO `warehouse_product` (warehouse_id,product_id,stock) VALUES ("%s","%s","%s");' % (row[0],row[1],row[2]))
    print("order")
    for i in range(100000):
        row = [fake.date(),random.choice(users)[0],random.choice(STATUT)]
        cursor.execute('INSERT INTO `order` (created_at,user_id,status) VALUES ("%s","%s","%s");' % (row[0],row[1],row[2]))
        products_orders = random.choices(products, k=random.randint(1, 15))    
        order_id = cursor.lastrowid

        for product_order in products_orders:
            row = [random.randint(1, 12),order_id,product_order[0]]
            cursor.execute('INSERT INTO `order_product` (number,order_id,product_id) VALUES ("%s","%s","%s");' % (row[0],row[1],row[2]))
    conn.commit()
    print("payement")
    for user in users :
        my_bool= fake.boolean(chance_of_getting_true=15)
        if my_bool:
            row = [fake.random_number(digits=15),fake.random_number(digits=3),fake.date(),user[0]]
            cursor.execute('INSERT INTO `info_payment` (card_number,code,date_card,user_id) VALUES ("%s","%s","%s","%s");' % (row[0],row[1],row[2],row[3]))
    conn.commit()









