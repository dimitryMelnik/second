import re

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.google.com/")
    page.wait_for_load_state("networkidle")
    page.get_by_label("Email or phone").click()
    page.get_by_label("Email or phone").fill("dmitrymelnik1988@gmail.com")
    page.get_by_role("button", name="Next").click()
    page.wait_for_load_state("networkidle")
    page.get_by_label("Enter your password").click()
    page.get_by_label("Enter your password").fill("wordpassS1!")
    page.get_by_role("button", name="Next").click()
    page.wait_for_load_state("networkidle")
    # page.pause()
    # page.get_by_role("button", name="Done").click()
    # page.goto("https://myaccount.google.com/")

    print("ok")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)