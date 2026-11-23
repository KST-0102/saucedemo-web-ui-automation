
from playwright.sync_api import expect
from decimal import Decimal

import logging

logger = logging.getLogger(__name__)


# 결제 성공 테스트
def test_checkout_success(logged_in_page):
    page = logged_in_page
    logger.info("결제 성공 테스트 시작")

    # 1. 상품을 장바구니에 추가
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    logger.info("Sauce Labs Backpack 상품 추가")

    # 2. 장바구니 이동
    page.locator(".shopping_cart_link").click()
    logger.info("장바구니 페이지 진입")

    # 3. Checkout 클릭
    page.locator("#checkout").click()
    logger.info("결제 정보 입력 페이지 진입")

    # 4. 주문자 정보 입력
    page.locator("#first-name").fill("QA")
    page.locator("#last-name").fill("Tester")
    page.locator("#postal-code").fill("12345")
    logger.info("주문자 정보 입력 완료")

    # 5. Continue 클릭
    page.locator("#continue").click()

    # 6. 주문 요약 정보 확인
    product_name = page.locator(
        ".cart_item .inventory_item_name"
    ).inner_text()

    assert product_name == "Sauce Labs Backpack"
    logger.info("주문 상품명 확인 완료: %s", product_name)

    # 7. 상품 금액 확인
    subtotal = page.locator(".summary_subtotal_label").inner_text()
    tax = page.locator(".summary_tax_label").inner_text()
    total = page.locator(".summary_total_label").inner_text()

    subtotal_value = Decimal(subtotal.replace("Item total: $", ""))
    tax_value = Decimal(tax.replace("Tax: $", ""))
    total_value = Decimal(total.replace("Total: $", ""))

    assert subtotal_value + tax_value == total_value
    logger.info(
        "주문 금액 검증 완료 - 소계: %s, 세금: %s, 총액: %s",
        subtotal_value, tax_value, total_value
    )

    # 8. 주문 완료
    page.locator("#finish").click()
    logger.info("주문 완료 버튼 클릭")

    # 9. 주문 완료 메시지 확인
    complete_message = page.locator(".complete-header").inner_text()

    assert complete_message == "Thank you for your order!"
    logger.info("주문 완료 메시지 확인: %s", complete_message)


# 이름 누락 테스트
def test_checkout_empty_first_name(logged_in_page):
    page = logged_in_page
    logger.info("주문자 이름 누락 테스트 시작")

    # 1. 상품 추가 및 장바구니 이동
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    # 2. 이름을 입력하지 않고 나머지 정보만 입력
    page.locator("#last-name").fill("Tester")
    page.locator("#postal-code").fill("12345")

    # 3. Continue 클릭
    page.locator("#continue").click()

    # 4. 오류 메시지 검증
    error_message = page.locator("[data-test='error']")

    expect(error_message).to_have_text(
        "Error: First Name is required"
    )
    logger.info("이름 누락 오류 메시지 확인 완료")


# 성 누락 테스트
def test_checkout_empty_last_name(logged_in_page):
    page = logged_in_page
    logger.info("주문자 성 누락 테스트 시작")

    # 1. 상품 추가 및 장바구니 이동
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    # 2. 성을 입력하지 않고 나머지 정보만 입력
    page.locator("#first-name").fill("QA")
    page.locator("#postal-code").fill("12345")

    # 3. Continue 클릭
    page.locator("#continue").click()

    # 4. 오류 메시지 검증
    error_message = page.locator("[data-test='error']")

    expect(error_message).to_have_text(
        "Error: Last Name is required"
    )
    logger.info("성 누락 오류 메시지 확인 완료")


# 우편 번호 누락 테스트
def test_checkout_empty_postal_code(logged_in_page):
    page = logged_in_page
    logger.info("우편번호 누락 테스트 시작")

    # 1. 상품 추가 및 장바구니 이동
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    # 2. 우편번호를 입력하지 않고 나머지 정보만 입력
    page.locator("#first-name").fill("QA")
    page.locator("#last-name").fill("Tester")

    # 3. Continue 클릭
    page.locator("#continue").click()

    # 4. 오류 메시지 검증
    error_message = page.locator("[data-test='error']")

    expect(error_message).to_have_text(
        "Error: Postal Code is required"
    )
    logger.info("우편번호 누락 오류 메시지 확인 완료")


# 숫자가 아닌 우편번호 입력 관찰 테스트
def test_checkout_accepts_non_numeric_postal_code(logged_in_page):
    page = logged_in_page
    logger.info("비숫자 우편번호 입력 관찰 테스트 시작")

    # 1. 상품 추가 및 장바구니 이동
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    # 2. 숫자가 아닌 우편번호 입력
    page.locator("#first-name").fill("QA")
    page.locator("#last-name").fill("Tester")
    page.locator("#postal-code").fill("ABC@@@")

    # 3. Continue 클릭
    page.locator("#continue").click()

    # 4. 주문 요약 화면으로 이동하는지 확인
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )
    logger.info("비숫자 우편번호 입력 후 주문 요약 화면 이동 확인")

# 관찰 테스트:
# 숫자가 아닌 우편번호를 입력해도 다음 결제 단계로 이동하는 것을 확인한다.
# 해당 동작의 정상 여부는 별도 요구사항 확인이 필요하다.


# 여러 상품의 주문 금액 합계 검증
def test_checkout_multiple_products_total(logged_in_page):
    page = logged_in_page
    logger.info("복수 상품 주문 금액 검증 테스트 시작")

    # 1. 상품 2개 추가
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    logger.info("Sauce Labs Backpack 및 Bike Light 상품 추가")

    # 2. 장바구니 이동
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()
    logger.info("주문자 정보 입력 페이지 진입")

    # 3. 주문자 정보 입력
    page.locator("#first-name").fill("QA")
    page.locator("#last-name").fill("Tester")
    page.locator("#postal-code").fill("12345")
    page.locator("#continue").click()

    # 4. 주문 요약 화면 확인
    expect(page.locator(".title")).to_have_text(
        "Checkout: Overview"
    )
    logger.info("주문 요약 화면 진입 확인")

    # 5. 화면에서 상품별 가격 가져오기
    prices = page.locator(
        ".cart_item .inventory_item_price"
    ).all_text_contents()

    price_values = [
        Decimal(price.replace("$", ""))
        for price in prices
    ]

    # 6. 화면에 표시된 소계 가져오기
    subtotal = page.locator(
        ".summary_subtotal_label"
    ).inner_text()

    subtotal_value = Decimal(
        subtotal.replace("Item total: $", "")
    )

    # 7. 실제 상품 가격 합산
    actual_subtotal = sum(price_values)

    # 8. 상품 가격 합계와 화면 소계 비교
    assert len(price_values) == 2
    assert actual_subtotal == subtotal_value

    # 9. 사전에 정의한 기대 금액과 비교
    expected_subtotal = Decimal("39.98")
    assert actual_subtotal == expected_subtotal

    logger.info(
        "주문 금액 검증 완료 - 상품 가격 합계: %s, 화면 소계: %s",
        actual_subtotal, subtotal_value
    )


# 주문 완료 후 장바구니 초기화 테스트
def test_cart_empty_after_checkout(logged_in_page):
    page = logged_in_page
    logger.info("주문 완료 후 장바구니 초기화 테스트 시작")

    # 1. 상품 추가
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    logger.info("Sauce Labs Backpack 상품 추가")

    # 2. 장바구니 이동
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    # 3. 주문자 정보 입력
    page.locator("#first-name").fill("QA")
    page.locator("#last-name").fill("Tester")
    page.locator("#postal-code").fill("12345")

    # 4. 주문 요약 화면 이동
    page.locator("#continue").click()
    logger.info("주문 요약 화면 진입")

    # 5. 주문 완료
    page.locator("#finish").click()

    # 6. 주문 완료 메시지 확인
    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )
    logger.info("주문 완료 메시지 확인")

    # 7. 장바구니 이동
    page.locator(".shopping_cart_link").click()

    # 8. 장바구니 상품이 없는지 확인
    expect(page.locator(".cart_item")).to_have_count(0)
    logger.info("주문 완료 후 장바구니 상품 제거 확인")

    # 9. 장바구니 수량 표시가 없는지 확인
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)
    logger.info("장바구니 수량 표시 제거 확인")
