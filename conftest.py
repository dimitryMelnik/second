import logging
import pytest


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/logtest.txt"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
URL = "https://accounts.google.com/"
REAL_TEST_EMAIL = "checking.point.test@gmail.com"
REAL_PW = "wordpassS2!"


@pytest.fixture(scope='function')
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context()
    page = context.new_page()
    yield page


@pytest.fixture(scope='function')
def navigate_login(browser_instance):
    browser_instance.goto(URL)
    browser_instance.wait_for_load_state("networkidle")
    logger.info(f'reached login screen')
    yield browser_instance
    browser_instance.close()
    logger.info('Browser closed')

