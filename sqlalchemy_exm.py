# import sqlite3
import sqlalchemy as db

engine = db.create_engine('sqlite:///sqlalchemy.db')

connection = engine.connect()

metadata = db.MetaData()

products = db.Table('products', metadata,
                    db.Column('product_id', db.Integer, primary_key=True),
                    db.Column('product_name', db.Text),
                    db.Column('supplier_name', db.Text),
                    db.Column('price_per_tonne', db.Integer))

metadata.create_all(engine)

insertion_query = products.insert().values(
    [{"product_name": "Banana", "supplier_name": "United Bananas", "price_per_tonne": 7000},
     {"product_name": "Avocado", "supplier_name": "United Avocados", "price_per_tonne": 12000},
     {"product_name": "Tomatoes", "supplier_name": "United Tomatoes", "price_per_tonne": 3100}])

connection.execute(insertion_query)

# GET
select_all_query = db.select(products)
select_all_result = connection.execute(select_all_query)
print(select_all_result.fetchall())

select_all_query = db.select(products).where(products.columns.price_per_tonne != 12000)
select_all_result = connection.execute(select_all_query)
print(select_all_result.fetchall())

# UPDATE
update_query = db.update(products).where(products.columns.supplier_name == "United Bananas").values(
    supplier_name="Fruits&Co")
connection.execute(update_query)

select_all_query = db.select(products)
select_all_result = connection.execute(select_all_query)
print(select_all_result.fetchall())

# DELETE
delete_query = db.delete(products).where(products.columns.product_id == 3)
connection.execute(delete_query)

select_all_query = db.select(products)
select_all_result = connection.execute(select_all_query)
print(select_all_result.fetchall())
