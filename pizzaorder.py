def select(menu,menu_name):
    order = {}
    print(f'\n***** {menu_name}목록 *****')
    for name, price in menu.items():
        print(f'{name} ({price})원')
    
    while True:
        p_name = input(f'주문할 {menu_name}을 입력하십시오(종료: exit)>>>  ')
        if p_name == '0':
           pass
        elif p_name in menu:
            count = int(input('수량을 입력하십시오'))
            order[p_name] = count
            print('주문 완료!')
        elif p_name == 'exit':
            break

    return order

    
if __name__=="__mian__":
    pizza_menu = {'페퍼로니 피자':3000,
                  "치즈피자":3200,
                  '콤비네이션피자':3500,
                  '불고기피자':3600,
                  '해산물피자':3800}
    drink_menu = {'콜라':1500, "사이다":1500, "생수":1000}
    
    order_pizza = select(pizza_menu, '피자')
    print(order_pizza)
    order_drink = select(pizza_menu, '음료')
    print(order_drink)

