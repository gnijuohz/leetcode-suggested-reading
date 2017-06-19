"""
this script fetch titles from leetcode.com and geeksforgeeks.com and
provide a reading list from geeksforgeeks.com for each problem on leetcode.com
"""

import os
import re
import time
import json
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from settings import username, password, chrome_driver_location
from util import save_to_json_file

def setup_driver():
    """set up chrome driver"""
    os.environ["webdriver.chrome.driver"] = chrome_driver_location
    driver = webdriver.Chrome(chrome_driver_location)
    driver.set_window_size(1280, 800)
    return driver

def login_leetcode(driver):
    """ login leetcode with username and password"""
    login_url = "https://leetcode.com/accounts/login/"
    name_field_id = "id_login"
    password_field_id = "id_password"
    login_button_selector = 'button.btn-primary'
    driver.get(login_url)
    time.sleep(2)
    username_ele = driver.find_element_by_id(name_field_id)
    password_ele = driver.find_element_by_id(password_field_id)
    username_ele.send_keys(username)
    password_ele.send_keys(password)
    driver.find_element_by_css_selector(login_button_selector).click()

def get_problem_detail(tr):
    problems_nodes = tr.find_elements_by_xpath('.//td')
    problem_parts = [item.text.strip() for item in problems_nodes if item.text.strip()]
    if not problem_parts:
        return None
    number, title = problem_parts[:2]
    if title.endswith('New'):
        title = re.sub(' New$', '', title)
    url = problems_nodes[2].find_elements_by_xpath('.//a')[0].get_attribute('href')
    return [number, title, url]

def get_all_titles(driver):
    """get all titles of the problems"""
    titles = []
    problem_list_url = "https://leetcode.com/problemset/algorithms/"
    time.sleep(2)
    driver.get(problem_list_url)
    time.sleep(2)
    select = Select(driver.find_element_by_css_selector(".reactable-pagination select.form-control"))
    select.select_by_index(3)
    time.sleep(2)
    ps = driver.find_elements_by_css_selector('tbody.reactable-data')
    for tbl in ps:
        for tr in tqdm(tbl.find_elements_by_xpath('.//tr')):
            problem_detail = get_problem_detail(tr)
            if not problem_detail:
                continue
            number, title, url = problem_detail
            titles.append({
                "number": number,
                "title": title,
                "url": url
            })
    return titles

def main():
    """entry point"""
    driver = setup_driver()
    login_leetcode(driver)
    titles = get_all_titles(driver)
    save_to_json_file(titles, 'data/leetcode_problem_titles.json')
    driver.quit()

if __name__ == "__main__":
    main()