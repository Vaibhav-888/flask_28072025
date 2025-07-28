from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
            "name": "Chair",
            "price": 15.99
            }
        ]       
    }
]


@app.get("/") # http://127.0.0.1:8080/
def get_stores():
    return {"stores": stores}


@app.post("/store")  # http://127.0.0.1:8080/store
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201 # 201 resource created


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201 # 201 resource created
    return {"messege": "Store not found"}, 404 # 404 Store not found


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug=True)