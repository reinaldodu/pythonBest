import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print (r.status_code)
    # print (r.text)
    categorias = r.json()
    print(categorias)
    for categoria in categorias:
        print(categoria['name'])