# 배송비 계산하기
# uniprice : 상품 가격,  quantity : 수량
# 조건 - 주문 상품 가격이 20,0000원 미만이면 배송비(2,500원) 포함, 아니면 무료 배송

def price(uniprice, quantity):
    delivery_fee = 2500     # 배송비
    price = uniprice * quantity     # 상품 가격은 상품 가격 * 수량
    if price < 20000:
        price += delivery_fee
        return price
    else:
        return price

p1 = price(15000, 2)    # 15,000원짜리 2개 구매
p2 = price(5000, 3)     # 5,000원짜리 3개 구
print("상품 가격 1은 " + format(p1, ',d') + "원 입니다.")
print("상품 가격 2은 " + format(p2, ',d') + "원 입니다.")


