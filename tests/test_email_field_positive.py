import pytest
import conftest
from configuration import config


@pytest.mark.parametrize('email', [config.REAL_TEST_EMAIL, config.REAL_EMAIL_MIN_SYMBOLS]) # I failed to register MAX
# usrname symbols account (30), so not included it in set
def test_email_field_positive(browser_instance, navigate_login, email):
    browser_instance.get_by_label("Email or phone").click()
    browser_instance.get_by_label("Email or phone").fill(email)
    browser_instance.get_by_role("button", name="Next").click()
    browser_instance.wait_for_load_state("networkidle", timeout=200000)
    password_field = browser_instance.get_by_label("Enter your password")
    password_field.wait_for(state="visible", timeout=200000)
    assert password_field.is_visible()
    conftest.logger.info(f'Positive test - Passed')


@pytest.mark.parametrize('phone', [config.REAL_PHONE])
def test_email_field_positive_phone(browser_instance, navigate_login, phone):
    browser_instance.get_by_label("Email or phone").click()
    browser_instance.get_by_label("Email or phone").fill(phone)
    browser_instance.get_by_role("button", name="Next").click()
    browser_instance.wait_for_load_state("networkidle", timeout=200000)
    browser_instance.get_by_role("button", name="Next").click()
    browser_instance.wait_for_load_state("networkidle", timeout=200000)
    button = browser_instance.locator('xpath=//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/button/span')
    button.wait_for(state="visible", timeout=200000)
    assert button.is_visible()
    conftest.logger.info(f'Positive test - Passed')
