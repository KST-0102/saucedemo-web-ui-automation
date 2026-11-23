import pytest
import logging

logger = logging.getLogger(__name__)


# 상품 1개 장바구니 추가
def test_add_single_product(logged_in_page):
    # 1. 로그인
    page = logged_in_page
    logger.info("단일 상품 장바구니 추가 테스트 시작")

    # 2. 첫 번째 상품 추가
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    logger.info("Sauce Labs Backpack 상품 추가")

    # 3. 장바구니 수량 확인
    cart_badge = page.locator(".shopping_cart_badge")

    assert cart_badge.inner_text() == "1"
    logger.info("장바구니 상품 수량 1개 확인 완료")


# 상품 2개 장바구니 추가
def test_add_multiple_products(logged_in_page):
    # 1. 로그인
    page = logged_in_page
    logger.info("복수 상품 장바구니 추가 테스트 시작")

    # 2. 서로 다른 상품 2개 추가
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    logger.info("Sauce Labs Backpack 및 Bike Light 상품 추가")

    # 3. 장바구니 수량 확인
    cart_badge = page.locator(".shopping_cart_badge")

    assert cart_badge.inner_text() == "2"
    logger.info("장바구니 상품 수량 2개 확인 완료")


# 장바구니에서 상품 삭제
def test_remove_product_from_cart(logged_in_page):
    # 1. 로그인
    page = logged_in_page
    logger.info("장바구니 상품 삭제 테스트 시작")

    # 2. 상품 추가
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    logger.info("Sauce Labs Backpack 상품 추가")

    # 3. 장바구니 진입
    page.locator(".shopping_cart_link").click()
    logger.info("장바구니 페이지 진입")

    # 4. 상품 삭제
    page.locator("#remove-sauce-labs-backpack").click()
    logger.info("Sauce Labs Backpack 상품 삭제")

    # 5. 장바구니 상품이 없는지 확인
    cart_items = page.locator(".cart_item")

    assert cart_items.count() == 0
    logger.info("장바구니 상품 삭제 확인 완료")

    # 6. 장바구니 수량 표시도 사라졌는지 확인
    assert page.locator(".shopping_cart_badge").count() == 0
    logger.info("장바구니 수량 표시 제거 확인 완료")


# 장바구니 상품 정보 확인
def test_cart_product_information(logged_in_page):
    # 1. 로그인
    page = logged_in_page
    logger.info("장바구니 상품 정보 확인 테스트 시작")

    # 2. 상품 추가
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    logger.info("Sauce Labs Backpack 상품 추가")

    # 3. 장바구니 진입
    page.locator(".shopping_cart_link").click()
    logger.info("장바구니 페이지 진입")

    # 4. 상품명 확인
    product_name = page.locator(".cart_item .inventory_item_name").inner_text()

    # 5. 상품 가격 확인
    product_price = page.locator(".cart_item .inventory_item_price").inner_text()

    assert product_name == "Sauce Labs Backpack"
    assert product_price == "$29.99"

    logger.info(
        f"상품 정보 확인 완료 - 상품명: {product_name}, 가격: {product_price}"
    )
