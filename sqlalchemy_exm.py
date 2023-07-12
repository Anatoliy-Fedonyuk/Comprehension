import sqlalchemy as db

engine = db.create_engine('sqlite:///sqlalchemy.db')

connection = engine.connect()

metadata = db.MetaData()

products = db.Table('products', metadata,
                    db.Column('product_id', db.Integer, primary_key=True),
                    db.Column('product_name', db.Text),
                    db.Column('supplier_name', db.Text),
                    db.Column('price_per_tonne', db.Text))

metadata.create_all(engine)
