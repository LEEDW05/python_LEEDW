import pizzaorder as po

pizza_menu = {'페퍼로니 피자': 3000,
              "치즈피자": 3200,
              '콤비네이션피자': 3500,
              '불고기피자': 3600,
              '해산물피자': 3800}
drink_menu = {'콜라': 1500, "사이다": 1500, "생수": 1000}

# 주문
order_pizza = po.select(pizza_menu, '피자')
print(order_pizza)
order_drink = po.select(drink_menu, '음료') 
print(order_drink)           

# 계산
tot_pizza = po.money_calculater(order_pizza, pizza_menu, '피자')   #피자계산
tot_drink = po.money_calculater(order_drink, drink_menu, '음료')   #음료계산

print(f'전체가격 : 피자 + 음료 : {tot_pizza + tot_drink}')

