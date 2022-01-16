g = [{"id": 1, "purchased_date": "2022-01-14T13:56:23.781Z", "item": "Headache pills", "item_category": "Medicine", "quantity": 5, "price": 3}, {"id": 2, "purchased_date": "2022-01-14T13:57:54.230Z", "item": "Headache pills", "item_category": "Medicine", "quantity": 1, "price": 4}, {"id": 3, "purchased_date": "2022-01-15T06:00:01.371Z", "item": "Saridon", "item_category": "Medicine", "quantity": 2, "price": 4}, {"id": 4, "purchased_date": "2022-01-15T06:02:15.032Z", "item": "Saridon", "item_category": "Medicine", "quantity": 2, "price": 4}, {"id": 5, "purchased_date": "2022-01-15T06:11:53.791Z", "item": "Saridon", "item_category": "Medicine", "quantity": 3, "price": 2}, {"id": 6, "purchased_date": "2022-01-15T06:15:06.673Z", "item": "Saridon", "item_category": "Medicine", "quantity": 3, "price": 8}, {"id": 7, "purchased_date": "2022-01-15T06:18:32.789Z", "item": "Saridon", "item_category": "Medicine", "quantity": 4, "price": 8}, {"id": 8, "purchased_date": "2022-01-14T18:30:00Z", "item": "Saridon", "item_category": "Medicine", "quantity": 3, "price": 6}, {"id": 9, "purchased_date": "2022-01-15T06:25:51.189Z", "item": "Saridon", "item_category": "Medicine", "quantity": 4, "price": 8}, {"id": 10, "purchased_date": "2022-01-15T06:32:59.293Z", "item": "Saridon", "item_category": "Medicine", "quantity": 2, "price": 5}, {"id": 11, "purchased_date": "2022-01-15T06:35:05.168Z", "item": "Saridon", "item_category": "Medicine", "quantity": 2, "price": 8}, {"id": 12, "purchased_date": "2022-01-15T06:38:21.502Z", "item": "dsds", "item_category": "ds", "quantity": 3, "price": 3}]
from functools import reduce

# g = [{
#     "item": "Headache pills",
#     "itemCategory": "Medicine",
#     "quantity": 5,
#     "price": 50
# },
#     {
#         "item": "Sandwich",
#         "itemCategory": "Food",
#         "quantity": 2,
#         "price": 200
#     },
#     {
#         "item": "Perfume",
#         "itemCategory": "Imported",
#         "quantity": 1,
#         "price": 4000
#     },
#     {
#         "item": "Black Swan",
#         "itemCategory": "Book",
#         "quantity": 1,
#         "price": 300
#     }
# ]

tax = {'Medicine': 5, 'Food': 5, 'music': 3, 'Total': 5, 'Imported': 18}


def get_amount(key, value):
    print("float(value * (1 + float(tax.get(key, 0) / 100)) ",float(value * (1 + float(tax.get(key, 0) / 100))))
    return float(value * (1 + float(tax.get(key, 0) / 100)))


# total = sum(map(lambda x: , g))
print("Before sum   ",sum(map(lambda x:x.get('price',0),g)))
# print(get_amount('imported', 3000))


def generate_bill():
    for i in g:
        i['final_price'] = get_amount(i.get('item_category', 0), i['price'])
    return g


total = sum(map(lambda x: x.get('final_price'), generate_bill()))
print(" total:  ",total)
print(int(total) >= 2000)
total = get_amount('Total', total) if int(total) >= 10 else total
g.append({'total': total})
print(g)

# print(generate_bill())

# g.clear()
