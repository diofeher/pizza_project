# CREATE
curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/pizzas/ -d "name=Pepperoni"

curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/orders/ -d "description=Chocolate border&pizza=1&customer_name=Dio&customer_address=Rua Major Jader, 50"

# LIST
curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/orders/

# UPDATE ORDER
curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/orders/1/ -d "customer_name=MoBerries" -X PATCH

# DELETE ORDER
curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/orders/1/ -X DELETE