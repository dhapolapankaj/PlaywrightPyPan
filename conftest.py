import pytest
from playwright.sync_api import Playwright


@pytest.fixture(autouse=True, scope="session")
def before_after(playwright: Playwright):
    #we will have to get things ready before tests
    browser =  playwright.chromium.launch(headless=True, slow_mo=2000)
    context =  browser.new_context()
    page =  context.new_page()
    yield page
    context.close()
    browser.close()


    

