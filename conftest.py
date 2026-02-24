import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox"
    )

@pytest.fixture(scope="class")
def driver(request):
    browser = request.config.getoption("browser").lower()

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.set_capability("acceptInsecureCerts", True)
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--dns-prefetch-disable")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False })
        # add other chrome options here...
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        # add other firefox options here...
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    else:
        raise ValueError(f"Browser '{browser}' is not supported")

    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield driver  # till here executes with functions execution
    driver.quit() # it will run after yield meaning functions which has the fixture executes first