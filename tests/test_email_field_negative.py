import pytest
import conftest
from configuration import config


@pytest.mark.parametrize('email, error_message', config.NEGATIVE_EMAILS)
def test_email_field_negative(browser_instance, navigate_login, email, error_message):
    browser_instance.get_by_label("Email or phone").click()
    browser_instance.get_by_label("Email or phone").fill(email)
    browser_instance.get_by_role("button", name="Next").click()
    browser_instance.wait_for_load_state("networkidle", timeout=200000)
    actual_error_message_element = browser_instance.locator("xpath=//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div["
                                                            "1]/form/span/section/div/div/div[1]/div/div[2]/div[2]/div")
    actual_error_message = actual_error_message_element.text_content()
    assert actual_error_message == error_message, f"Expected '{error_message}', but got '{actual_error_message}'"
    conftest.logger.info(f'Negative test - Passed')
