products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('商品價格:')
    #p = []
    #p.append(name)
    #p.append(price)
    
    #p = [name, price]
    
    products.append([name, price])
print(products[0][0])