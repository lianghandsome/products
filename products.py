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
print(products)

for i in products:
    print(i[0],'的價格是:',i[1])

#寫入檔案(沒有檔案，就會寫一個全新的)
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品, 價格\n')
    for i in products:
        f.write(i[0] + ',' + i[1] + '\n')