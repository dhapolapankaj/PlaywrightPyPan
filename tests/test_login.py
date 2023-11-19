from playwright.sync_api import Page
import data.config as config
import data.locators as repo


def test_load_login_page(page: Page):
    page.goto(config.globalData['environment']['url'])


    assert page.title() == "Swag Labs"

    page.locator(repo.pages["loginpage"]["username_textbox"]).fill(config.globalData['environment']['userid'])
    page.locator(repo.pages["loginpage"]["password_textbox"]).fill(config.globalData['environment']['password'])
    page.locator(repo.pages["loginpage"]["login_button"]).click()

    assert page.title() == "Swag Labs"


