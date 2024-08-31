import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os

import config
from selene_in_action import utils

from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "udid": "emulator-5554",
        "appWaitActivity": "org.wikipedia.*",
        "app": "/Users/Workstation/PycharmProjects/qa_guru_lesson_20_mobile_automation_v2/resources/app-alpha-universal-release.apk"
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://127.0.0.1:4723',
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    # session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    # utils.allure.attach_bstack_video(session_id)


