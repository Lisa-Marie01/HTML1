# https://fastapi.tiangolo.com/
#importieren FastAPI aus Namespace fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List
import uuid 
# im Items Basemodel

class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    total_price: Optional[float] = None
    price: float
    tax: float
    amount: int

items=[]

#Objekt namens myApp erstellen, basierend auf der Klasse FastAPI(ohne Anpassungen)
myApp = FastAPI()

def find_item(id):
    for item in items:
        if id == item.id:
            return item
    return None 

def replace_item(patched_item:Item):
    for index, item in enumerate(items):
        print("patched item id:  ", patched_item.id)
        print("Item id:  ", item.id)
        if (patched_item.id == item.id):
            print("match")
            items[index] = patched_item
            return items[index]
    return None


#Root-route
@myApp.get('/')
def read_root():
    return("pullerparty")

#joke-route
@myApp.get("/jokes")
def read_jokes():
    return("witzig")

#lisas-route
@myApp.get("/lisa")
def read_lisa():
    return("waaaaaaaaaaaaaasssssssssssssssuuuuuuuuuuuuuuuuuuuuuuuuuuuuuup")

@myApp.put("/item")
def put_item(item: Item):
    item.total_price = (item.price * (item.tax / 100)) + item.price
    item.id = uuid.uuid4()
    items.append(item)
    return item

@myApp.get("/items")
def get_items()->List[Item]:  
    return items

@myApp.delete("/item")
def delete_item(itemid):
    item_to_delete = find_item(itemid)
    if (item_to_delete):
        items.remove(item_to_delete)

@myApp.patch("/item")
def put_item(patched_item:Item):
    return replace_item(patched_item)

#main Funktion = Einstiegspunkt/entry point
def main():
    #webserver importieren (uvicorn)
    import uvicorn
    #webserver ausführen
    uvicorn.run(app=myApp,host="localhost",port=8000)
    print ("Hello Friends, main()")

if __name__ == "__main__":
    main()
