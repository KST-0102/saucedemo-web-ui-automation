
from playwright.sync_api import Page, expect

import logging

logger = logging.getLogger(__name__)


# 정상 로그인 테스트
def test_login_success(page: Page):
    logger.info("정상 로그인 테스트 시작")

    # 1. 로그인 페이지 접속
    page.goto("https://www.saucedemo.com/")
    logger.info("로그인 페이지 접속 완료")

    # 2. 로그인 정보 입력
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    logger.info("로그인 정보 입력 완료")

    # 3. 로그인 버튼 클릭
    page.locator("#login-button").click()
    logger.info("로그인 버튼 클릭")

    # 4. 상품 목록 페이지 이동 확인
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    logger.info("상품 목록 페이지 이동 검증 완료")

    # 5. 상품 목록 제목 확인
    expect(page.locator(".title")).to_have_text("Products")
    logger.info("상품 목록 제목 검증 완료")

    logger.info("정상 로그인 테스트 종료")


# 잘못된 비밀번호 로그인 테스트
def test_login_failure(page: Page):
    logger.info("잘못된 비밀번호 로그인 테스트 시작")

    # 1. 로그인 페이지 접속
    page.goto("https://www.saucedemo.com/")
    logger.info("로그인 페이지 접속 완료")

    # 2. 로그인 정보 입력
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")
    logger.info("잘못된 비밀번호 입력 완료")

    # 3. 로그인 버튼 클릭
    page.locator("#login-button").click()

    # 4. 오류 메시지 확인
    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
    logger.info("잘못된 로그인 오류 메시지 검증 완료")


# 아이디 누락 테스트
def test_login_empty_username(page: Page):
    logger.info("아이디 누락 로그인 테스트 시작")

    # 1. 로그인 페이지 접속
    page.goto("https://www.saucedemo.com/")
    logger.info("로그인 페이지 접속 완료")

    # 2. 비밀번호만 입력
    page.locator("#password").fill("secret_sauce")
    logger.info("비밀번호 입력 완료")

    # 3. 로그인 버튼 클릭
    page.locator("#login-button").click()

    # 4. 오류 메시지 확인
    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username is required"
    )
    logger.info("아이디 누락 오류 메시지 검증 완료")


# 비밀번호 누락 테스트
def test_login_empty_password(page: Page):
    logger.info("비밀번호 누락 로그인 테스트 시작")

    # 1. 로그인 페이지 접속
    page.goto("https://www.saucedemo.com/")
    logger.info("로그인 페이지 접속 완료")

    # 2. 아이디만 입력
    page.locator("#user-name").fill("standard_user")
    logger.info("아이디 입력 완료")

    # 3. 로그인 버튼 클릭
    page.locator("#login-button").click()

    # 4. 오류 메시지 확인
    expect(page.locator("[data-test='error']")).to_contain_text(
        "Password is required"
    )
    logger.info("비밀번호 누락 오류 메시지 검증 완료")
