items=[
    {
        'marca':'Toyota',
        'modelo':2010
    },
    {
        'marca':'Renault',
        'modelo':2020
    },
    {
        'marca':'BMW',
        'modelo':2000
    },
]
modelos=list(map(lambda item:item['modelo'],items))
print(modelos)

