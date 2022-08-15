import emoji
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class EmojiCollection():
  def __init__(self):

    options = Options()
    # TODO this can't be OS specific
    # options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"
    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    self.driver = webdriver.Chrome(options=options)
    self.driver.get("https://emojipedia.org")
    # accepts cookies
    acceptCookies = WebDriverWait(
      self.driver,
      30).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()
    
  def searchEngineReturned(self):
    #click onto the link of the first emoji
    clickFirstEmoji = WebDriverWait(self.driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[@class='container']/div[@class='content']/ol/*[1]/h2/a"))).click()
  def getEmoji(self):
    try:
      nameOfEmoji = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "span.shortcode"))).text
      return emoji.emojize(nameOfEmoji)
    except selenium.common.exceptions.TimeOutException:
      tmp = emoji.emojize(":red_heart:")
      return tmp
  #enter the requested emoji to the search engine
  def search(self, emoji):
    #type a key word to the search engine
    element = self.driver.find_element(By.ID, "id_q")
    element.send_keys(emoji)
    #the search engine starts searching
    element.send_keys(Keys.RETURN)
    self.searchEngineReturned()
    return self.getEmoji()

  def quit(self):
    self.driver.quit()

