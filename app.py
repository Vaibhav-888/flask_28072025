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


@app.get("/") # endpoint: http://127.0.0.1:8080/
def get_stores():
    return {"stores": stores}


@app.post("/store")  # endpoint: http://127.0.0.1:8080/store
def create_store():
    """Create stores"""
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201 # 201 resource created



@app.post("/store/<string:name>/item") # endpoint: http://127.0.0.1:8080/My%Store/item
def create_item(name):
    """Create item in a store"""
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201 # 201 resource created
    return {"messege": "Store not found"}, 404 # 404 Store not found


# get stores and items that initially created.

@app.get("/store")
def get_store_data():
    """get a store data"""
    for store in stores:
        return {"store": store}
        
@app.get("/store/<string:name>") # endpoint: http://127.0.0.1:8080/My%Store
def get_store(name):
    """Get a Store"""
    for store in stores:
        if store["name"] == name:
            return store
    return {"messege": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    """Get items from a particular store"""
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"messege": "items not found"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug=True)