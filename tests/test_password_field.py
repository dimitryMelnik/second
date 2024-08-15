import pytest
import conftest
from configuration import config


def test_password_field_positive(browser_instance, navigate_password_field):
    browser_instance.get_by_label("Enter your password").click()
    browser_instance.get_by_label("Enter your password").fill(config.REAL_PW)
    browser_instance.get_by_role("button", name="Next").click()
    browser_instance.wait_for_load_state("networkidle", timeout=100000)
    assert browser_instance.get_by_role("heading", name="Welcome, Check Point").is_visible(), "Failed to login"
    conftest.logger.info(f'Positive test - Passed')


@pytest.mark.parametrize('password', config.WRONG_PW)
def test_password_field_negative(browser_instance, navigate_password_field, password):
    browser_instance.get_by_label("Enter your password").click()
    browser_instance.get_by_label("Enter your password").fill(password)
    browser_instance.get_by_role("button", name="Next").click()
    browser_instance.wait_for_load_state("networkidle", timeout=100000)
    assert browser_instance.get_by_text("Wrong password. Try again or").is_visible(), "Failed to login"
    conftest.logger.info(f'Positive test - Passed')

