cost_f , cost_v, price = map(int, input().split())

if price <= cost_v:
     print('-1')
else:
    print(cost_f//(price-cost_v) +1)