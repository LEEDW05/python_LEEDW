def select(menu, menu_name):
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
    # print(order_pizza)
    return order

def money_calculater(order, pizza_menu, menu):
    tot_price = 0
    for x in order_pizza.keys():
        price = 0
        if x in pizza_menu.keys():
            price = price + (order_pizza[x] * pizza_menu[x])
        print(f'{x}({pizza_menu.get(x, 0)}원) X {order.get(x, 0)} = {price:,}원')
        tot_price = tot_price + price

    print(f'피자 전체 가격 : {tot_price}')

    return tot_price

if __name__ == "__main__":
    pizza_menu = {'페퍼로니 피자': 3000,
                  "치즈피자": 3200,
                  '콤비네이션피자': 3500,
                  '불고기피자': 3600,
                  '해산물피자': 3800}
    drink_menu = {'콜라': 1500, "사이다": 1500, "생수": 1000}

# 주문
    order_pizza = select(pizza_menu, '피자')
    print(order_pizza)
    order_drink = select(drink_menu, '음료')
    print(order_drink)

# 계산
    tot_pizza = money_calculater(order_pizza, pizza_menu, '피자')   #피자계산
    tot_drink = money_calculater(order_drink, drink_menu, '음료')   #음료계산

    print(f'전체가격 : 피자 + 음료 : {tot_pizza + tot_drink}')