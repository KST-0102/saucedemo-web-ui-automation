
import logging
from decimal import Decimal

logger = logging.getLogger(__name__)


# 상품명 오름차순 테스트
def test_sort_name_ascending(logged_in_page):
    page = logged_in_page
    logger.info("상품명 오름차순 정렬 테스트 시작")

    # 1. A to Z 선택
    page.locator(".product_sort_container").select_option("az")
    logger.info("상품명 A to Z 정렬 옵션 선택")

    # 2. 화면에 표시된 상품명 수집
    actual_names = page.locator(
        ".inventory_item_name"
    ).all_text_contents()

    # 3. 기대 결과 생성
    expected_names = sorted(actual_names)

    # 4. 정렬 결과 검증
    assert actual_names == expected_names
    logger.info("상품명 오름차순 정렬 검증 완료")


# 상품명 내림차순 테스트
def test_sort_name_descending(logged_in_page):
    page = logged_in_page
    logger.info("상품명 내림차순 정렬 테스트 시작")

    # 1. Z to A 선택
    page.locator(".product_sort_container").select_option("za")
    logger.info("상품명 Z to A 정렬 옵션 선택")

    # 2. 화면에 표시된 상품명 수집
    actual_names = page.locator(
        ".inventory_item_name"
    ).all_text_contents()

    # 3. 기대 결과 생성
    expected_names = sorted(actual_names, reverse=True)

    # 4. 정렬 결과 검증
    assert actual_names == expected_names
    logger.info("상품명 내림차순 정렬 검증 완료")


# 가격 오름차순 테스트
def test_sort_price_ascending(logged_in_page):
    page = logged_in_page
    logger.info("가격 오름차순 정렬 테스트 시작")

    # 1. Low to High 선택
    page.locator(".product_sort_container").select_option("lohi")
    logger.info("가격 Low to High 정렬 옵션 선택")

    # 2. 화면에 표시된 가격 수집
    actual_prices = page.locator(
        ".inventory_item_price"
    ).all_text_contents()

    # 3. 문자열 가격을 Decimal로 변환
    actual_prices = [
        Decimal(price.replace("$", ""))
        for price in actual_prices
    ]

    # 4. 기대 결과 생성
    expected_prices = sorted(actual_prices)

    # 5. 정렬 결과 검증
    assert actual_prices == expected_prices
    logger.info("가격 오름차순 정렬 검증 완료")


# 가격 내림차순 테스트
def test_sort_price_descending(logged_in_page):
    page = logged_in_page
    logger.info("가격 내림차순 정렬 테스트 시작")

    # 1. High to Low 선택
    page.locator(".product_sort_container").select_option("hilo")
    logger.info("가격 High to Low 정렬 옵션 선택")

    # 2. 화면에 표시된 가격 수집
    actual_prices = page.locator(
        ".inventory_item_price"
    ).all_text_contents()

    # 3. 문자열 가격을 Decimal로 변환
    actual_prices = [
        Decimal(price.replace("$", ""))
        for price in actual_prices
    ]

    # 4. 기대 결과 생성
    expected_prices = sorted(actual_prices, reverse=True)

    # 5. 정렬 결과 검증
    assert actual_prices == expected_prices
    logger.info("가격 내림차순 정렬 검증 완료")


# HTML 내 정렬 옵션의 text와 value 확인 (학습용)
def test_check_sort_options(logged_in_page):
    page = logged_in_page

    options = page.locator(
        ".product_sort_container option"
    ).evaluate_all(
        """elements => elements.map(e => ({
            text: e.textContent,
            value: e.value
        }))"""
    )

    print(options)
