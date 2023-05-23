from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math
import requests
import re
import numpy as np
from .dictionary import elements


# options
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('headless')
service = Service("C:\\Users\\Альберт\\Desktop\\ВКР\\application\\api\\chromedriver\\chromedriver.exe")


def process_dictionary(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, str) and value.isalpha():
            new_dict[value] = key
        else:
            new_dict[key] = value
    return new_dict


def get_links():
    driver = webdriver.Chrome(
        service=service,
        options=options)
    url = "https://yandex.ru/patents"
    try:
        driver.get(url=url)
        time.sleep(3)

        # Находим поле для ввода текста на странице Яндекс.Патенты
        search_box = driver.find_element(By.CLASS_NAME, 'input__control')

        # Вводим в поле для ввода текста поисковой запрос
        search_box.send_keys('жаропрочный сплав на основе никеля')
        # search_box.send_keys('Многокомпонентные жаропрочные никелевые сплавы')

        name_key = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div[2]/div[1]/div[7]/span/input')
        name_key.send_keys('сплав никель')
        # name_key.send_keys('сплав')

        # Нажимаем клавишу Enter для выполнения поиска
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)

        # Узнаем количество найденных ссылок
        count_of_page = int(driver.find_element(By.CLASS_NAME, 'search-summary').text.partition(':')[2].strip())

        snippet_links = []

        # Сбор всех ссылок по запросу
        for i in range(math.ceil(count_of_page / 10)):
            print(i)
            time.sleep(1)
            links = driver.find_elements(By.TAG_NAME, 'a')
            for link in links:
                if 'snippet-title' in link.get_attribute('class'):
                    snippet_links.append(link.get_attribute('href'))
            time.sleep(1)
            if i == math.ceil(count_of_page / 10) - 1:
                break
            active_button = driver.find_element(By.CLASS_NAME, 'leaf-button__active')
            next_button = active_button.find_element(By.XPATH, 'following-sibling::div')
            next_button.click()

        result_links = []
        np.savetxt('links.txt', snippet_links, fmt='%s')
        for link in snippet_links:
            driver.get(url=link)
            time.sleep(1)
            try:
                title = driver.find_element(By.TAG_NAME, 'h1')
                # if 'сплав' in title.text.lower() and 'способ' not in title.text.lower() \
                #         and 'устройство' not in title.text.lower() and 'раствор' not in title.text.lower():
                if 'сплав' in title.text.lower() and 'способ' not in title.text.lower() \
                        and 'устройство' not in title.text.lower() and 'раствор' not in title.text.lower() and \
                        'припой' not in title.text.lower():
                    last_slash_index = link.rfind("/")
                    result_string = link[last_slash_index + 1:]
                    data = {
                        'c': 0, 'cr': 0, 'co': 0, 'mo': 0, 'w': 0, 'ti': 0, 'al': 0, 'nb': 0, 'ta': 0, 'b': 0, 'zr': 0,
                        'hf': 0, 'v': 0, 're': 0, 'ru': 0, 'ir': 0, 'ce': 0, 'la': 0, 'nd': 0, 'y': 0
                    }
                    print("*"*50)
                    print(link)
                    doclink = ("https://patents.s3.yandex.net/" + result_string + '.pdf')
                    response = requests.get(doclink)
                    if response.status_code == 200:
                        data['doclink'] = doclink
                    result_links.append(link)

                    info = take_info(driver)
                    if info:
                        pattern1 = r'/([^_/]+)_\d+'
                        match = re.search(pattern1, link)
                        data['name'] = match.group(1)
                        data['link'] = link
                        count = 0
                        for element, (attr) in elements.items():
                            values = info.get(element) or info.get(element.lower())

                            if values:
                                if '-' in values:
                                    start_str, end_str = values.split('-')
                                    start = float(start_str.replace(",", "."))
                                    end = float(end_str.replace(",", "."))
                                    data[attr] = (start+end)/2
                                    count += 1
                                else:
                                    # Обработка случая, когда нет диапазона значений
                                    single_value = float(values.replace(",", "."))
                                    data[attr] = single_value
                                    count += 1
                        if count >= 4:
                            url = 'http://127.0.0.1:8000/patent'  # URL-адрес вашего POST endpoint
                            response = requests.post(url, data=data)
            except Exception as ex:
                print(ex)
                print("*"*20, ' ', link)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def take_info(driver):
    try:
        # Находим div с id='doc-abstract'. Это div с заголовком "Реферат"
        doc_abstract = driver.find_element(By.ID, 'doc-abstract')

        info = doc_abstract.find_element(By.XPATH, 'following-sibling::div').text

        # регулярное выражение для поиска названий элементов и их значений
        pattern = r"(\w+)\s?-?\s?(\d+,?\d*\s?-?\s?\d+,?\d*)"
        # pattern1 = r"(\d+,?\d*\s?-?\s?\d+,?\d*)\s?-?\s?(\w+)"

        # поиск всех совпадений по обоим паттернам в тексте
        matches = re.findall(pattern, info)
        # print(1)
        # print(matches1)
        # matches2 = re.findall(pattern1, info)
        # print(2)
        # print(matches2)
        # # поиск всех совпадений по обоим паттернам в тексте
        # matches = matches1 + matches2
        # print('all')
        # print(matches)

        # создание словаря для хранения найденных значений
        data = {}
        for match in matches:
            data[match[0]] = match[1]
        return process_dictionary(data)

    except Exception as ex:
        print(ex)
        return None
