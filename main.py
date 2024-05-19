import requests
import psycopg2
url = f'https://dummyjson.com/products/'

r = requests.get(url)
print(r.status_code, r.text)

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='jasur',
                        host='localhost',
                        port=5432)

def create_table():
    create_table_products_query = """create table products(
            id serial primary key ,
            title varchar(255) ,
            description text ,
            price int,
            discountPercentage float,
            rating float ,
            stock int,
            brand varchar(255),
            category varchar(200),
            thumbnail varchar(255),
            images jsonb
    );"""

    cur = conn.cursor()
    cur.execute(create_table_products_query)
    conn.commit()
def inser_into():
    insert_into_query = """insert into products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail,images)

        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);

    """

    for product in r.json()['products']:
        cur = conn.cursor()
        cur.execute(insert_into_query,)
        product['title'], product['description'], product['price'], product['discountPercentage'],
        product['rating'],
        product['stock'], product['brand'], product['category'], product['thumbnail'], str(product['images'])
        conn.commit()

def named_taple():
    from collections import namedtuple

    Product = namedtuple('Product', ['name', 'image','price'])
    product1 = Product('iphone x','image1',10000)
    product2=Product('samsung a32','image2',2000)
    product3=Product('redmo note11','image3',4000)
    return print(Product._fields)
def named_tuble_kayse():
    from collections import namedtuple
    Person = namedtuple('Person', 'name age email', defaults=[20,'john@gmail.com'])
    jasur=Person('jasur')
    print(Person.name)
    print(Person.age)
    print(Person.email)
    anna = Person('Anna', 24, 'anna@gmail.com')
    john = Person('John')
    print(john)
    print(Person._fields)
    anna.name = 'Jake'
    print(anna[1])
    jane=anna._replace(name='anjilina')
    print(jane.name)
    john = Person._make(data)
    print(john)



#har bir funksiyani chaqirish orqali ishlatamiz
named_tuble_kayse()
named_taple()
create_table()
inser_into()




