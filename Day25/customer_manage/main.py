# Customer 테스트
from customer_class import Customer, GoldCustomer, VIPCustomer

# Customer 객체(인스턴스) 생성
c1 = Customer(101, "흥부")
c2 = Customer(102, "놀부")
gold1 = GoldCustomer(201, "콩쥐")
gold2 = GoldCustomer(202, "팥쥐")
vip1 = VIPCustomer(301, "심청", 777)
vip2 = VIPCustomer(302, "심봉사", 888)

# 상품 구매
price1 = 10000
price2 = 20000
c1.calc_price(price1)
c2.calc_price(price2)
gold1.calc_price(price1)
gold2.calc_price(price2)
vip1.calc_price(price1)
vip2.calc_price(price2)

# 고객 정보를 출력
c1.showInfo()
c2.showInfo()
gold1.showInfo()
gold2.showInfo()
vip1.showInfo()
vip2.showInfo()