import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('商品價格:')
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for i in products:
        print(i[0],'的價格是:',i[1])

#寫入檔案(沒有檔案，就會寫一個全新的)
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品, 價格\n')
        for i in products:
            f.write(i[0] + ',' + i[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案在不在
        print('yeah! 找到檔案')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()