import logging
import os
import time
import pytest
from configuration import config
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("../pythonProject/logs/logtest.txt"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context()
    page = context.new_page()
    yield page


@pytest.fixture(scope='function')
def navigate_login(browser_instance):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            browser_instance.goto(config.URL)
            break
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retrying
                continue
            else:
                raise e
    browser_instance.wait_for_load_state("networkidle")
    logger.info(f'reached login screen')
    yield browser_instance

    # Cleanup code to close the browser after the test finishes
    browser_instance.close()
    logger.info('Browser closed')


@pytest.fixture(scope='function')
def navigate_password_field(browser_instance):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            browser_instance.goto(config.URL)
            break
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retrying
                continue
            else:
                raise e
    browser_instance.wait_for_load_state("networkidle")
    logger.info(f'reached login screen')
    browser_instance.get_by_label("Email or phone").click()
    browser_instance.get_by_label("Email or phone").fill(config.REAL_TEST_EMAIL)
    browser_instance.get_by_role("button", name="Next").click()
    browser_instance.wait_for_load_state("networkidle", timeout=200000)
    password_field = browser_instance.get_by_label("Enter your password")
    password_field.wait_for(state="visible", timeout=200000)
    yield browser_instance

    # Cleanup code to close the browser after the test finishes
    browser_instance.close()
    logger.info('Browser closed')
