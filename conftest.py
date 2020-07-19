import pytest
import pytest_bdd
from selenium import webdriver
import os

@pytest.fixture(scope='session')
def browser():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(ROOT_DIR, 'driver/chromedriver.exe')
    b = webdriver.Chrome(executable_path='%s' % CONFIG_PATH)
    b.implicitly_wait(10)
    yield b
    b.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")