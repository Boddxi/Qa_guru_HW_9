import pytest
from selene import browser


@pytest.fixture(scope="session")
def windows_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
