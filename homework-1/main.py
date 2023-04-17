"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
from os import path
from os import listdir


def change_ap(word: str) -> str:
    """
    Функция для изменения типа кавычек в названии, для формирования корректного SQL-запроса
    """
    if word.count("'") == 0:
        return word
    return word.replace("'", '"')


data_files = listdir('north_data')

for file in data_files:
    with open(path.join('north_data', file), encoding='utf-8', newline='') as csv_file:
        tmp = file.split('.')[0]
        locals()[tmp] = []
        for row in csv.DictReader(csv_file):
            locals()[tmp].append(row)

orders_data = orders_data
customers_data = customers_data
employees_data = employees_data

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="4444"
) as conn:
    with conn.cursor() as cur:
        for i, employee in enumerate(employees_data):
            name, last_name, title, birthday, notes = employee.values()
            cur.execute(f"INSERT INTO employees VALUES "
                        f"({i+1}, '{name}', '{last_name}', '{title}', '{birthday}', '{notes}');")

    with conn.cursor() as cur:
        for customer in customers_data:
            id_customer, company_name, contact_name = customer.values()
            cur.execute(f"INSERT INTO customers VALUES "
                        f"('{id_customer}', '{change_ap(company_name)}', '{contact_name}');")

    with conn.cursor() as cur:
        for order in orders_data:
            order_id, id_customer, employee_id, order_date, ship_city = order.values()
            cur.execute(f"INSERT INTO orders VALUES "
                        f"({int(order_id)}, '{id_customer}', {int(employee_id)}, '{order_date}', '{ship_city}');")

conn.close()




