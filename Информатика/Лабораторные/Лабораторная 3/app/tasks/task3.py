import re
import requests

def solve(string):
    """ 466730 % 8 = 2 =>
    Вливаемся в роль фрилансера! Нужно найти (распарсить) цену валюты Bitcoin
    используя регулярные выражения для частного сайта заказчика. 
    """
    # Курс биткоина
    current_bitcoin_price = 6432191
    
    pattern1 = r"Bitcoin.*?₽([\d,]+(?:\.\d+)?)\s*RUB"
    matches1 = re.findall(pattern1, string)

    pattern2 = r'^\d{1,3}(?:,\d{3})*(?:\.\d+)?$'
    matches2 = [number for number in matches1 if re.match(pattern2, number)]

    prices = [float(price.replace(',', '')) for price in matches2]
    
    most_suitable_price = prices[0]
    index = 0
    for i in range(len(prices)):
        if abs(prices[i] - current_bitcoin_price) < abs(most_suitable_price - current_bitcoin_price):
            most_suitable_price = prices[i]
            index = i

    return matches2[index]
