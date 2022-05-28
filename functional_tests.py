# import django
# print(django.get_version())

from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title 
# browser.quit()