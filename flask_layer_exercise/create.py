from app import db, Customers, Products, Orders

db.drop_all()
db.create_all()

customer_one = Customers(name = "Dave", email = "dave.tom@hotmail.com")
customer_two = Customers(name = "Tom", email = "tommo@gmail.com")

product_one = Products(name = "Laptop", price = 499.99)
product_two = Products(name = "tabletennis table", price = 125.99)

order_one = Orders(customer = customer_one, product = product_one)
order_two = Orders(customer = customer_one, product = product_two)
order_three = Orders(customer = customer_two, product = product_one)

db.session.add(customer_one)
db.session.add(customer_two)
db.session.add(product_one)
db.session.add(product_two)
db.session.add(order_one)
db.session.add(order_two)
db.session.add(order_three)
db.session.commit()