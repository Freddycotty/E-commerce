import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope = 'function')
def chrome_browser_instance(request):
  
  """
  Proporcione una instancia de webdriver de selenium
  """
  
  options = Options()
  options.headless = False
  browser = webdriver.Chrome(chrome_options=options)
  yield browser
  browser.close()