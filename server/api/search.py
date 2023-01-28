# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# # Initilize the driver
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-blink-features=AutomationControlled')
# driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub", options=options)

# # Xpath for the search items on Google
# SEARCH_ITEM_XPATH = "//div[@class='yuRUbf']/a"


# def get_search_items(search_string: str, num_items: int = 1) -> list:
#     """Gets the html elements from Google browser.
#     :Args:
#         - search_string: The string to search for.
#         - num_items: The number of items to return.
#     :Returns:
#         - items: The html elements of the search items.
#     """
#     search_string = search_string.replace(" ", "+")
#     driver.get(f"https://www.google.com/search?q={search_string}")
#     items = driver.find_elements(by=By.XPATH, value=SEARCH_ITEM_XPATH)

#     return items[:num_items]

# def get_search_titles(items: list) -> list:
#     """Gets the titles from the html elements.
#     :Args:
#         - items: The html elements of the search items.
#     :Returns:
#         - titles: The titles of the search items.
#     """
#     titles = [item.text for item in items]
#     return titles

# def get_urls(items: list) -> list:
#     """Gets the urls from the html elements.
#     :Args:
#         - items: The html elements of the search items.
#     :Returns:
#         - urls: The urls of the search items.
#     """
#     urls = [item.get_attribute("href") for item in items]
#     return urls
