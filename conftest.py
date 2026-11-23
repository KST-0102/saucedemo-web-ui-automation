
import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture
def logged_in_page(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.wait_for_url("**/inventory.html")

    return page


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)