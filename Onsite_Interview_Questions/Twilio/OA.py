###1
def imageValidation(image_arr, maxSize):
    res = []
    hashMap = {'KB':int(1e3), 'MB': int(1e6), 'GB': int(1e9)}
    while image_arr:
        image_url, size = image_arr.pop(0)
        if size.lower() == 'none':
            size = hashMap['MB']
        # if int(size[:-2]) * hashMap[size[-2:].upper()] <= maxSize:
        if int(size) <= int(maxSize[:-2]) * hashMap[maxSize[-2:].upper()]:
            res.append([image_url, 'TRUE'])
        else:
            res.append([image_url, 'FALSE'])
    return res

image_arr = [['https://image/apple','32000000'],['https://image/pear','32000000'],['https://image/og','none']]
maxSize = '40MB'
print(imageValidation(image_arr, maxSize))


###2
import re
def isE164(number):
    if not number:
        return False
    token = '' if number[0] == '+' else '+' 
    number = token + number
    return re.match(r"^\+[1-9]\d{1,14}$", number)

def isWechat(number):
    if not number or len(number) < 1 or len(number) > 258:
        return False
    return re.match(r"^[a-zA-Z0-9+-_@.]*$", number)

def validatePhoneNumberFormat(address):
    if isE164(address):
        return 'SMS'
    val = address.split(":")
    if len(val) != 2:
        return 'INVALID_ADDRESS'
    provider = val[0].UPPER()
    if provider in ['WHATSAPP', 'MESSENGER'] and isE164(val[1]):
        return provider
    elif provider == 'WECHAT' and isWechat(val[1]):
        return provider
    return "INVALID_ADDRESS"  

###3 Get Author Articles
import requests
# author: epaga
def getArticleTitles(author):
    def getURL(author, pageNumber):
        return f'https://jsonmock.hackerrank.com/api/articles?author={author}&page={pageNumber}'
    response = requests.get(getURL(author,0))
    totalPages = response.json()['total_pages']
    res = []
    for page in range(1, totalPages + 1):
        url = getURL(author, page)
        response = requests.get(url)
        articles = response.json()['data']
        for article in articles:
            title, storyTitle = article['title'], article['story_title']
            if title:
                res.append(title)
            elif storyTitle:
                res.append(storyTitle)
    return res
print(getArticleTitles('epaga'))

###4

from collections import defaultdict
def countDuplicate(numbers):
    hashMap = defaultdict(int)
    cnt = 0
    for num in numbers:
        if num not in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1
    for val in hashMap.values():
        if val > 1:
            cnt += 1
    return cnt
numbers = [1,3,3,4,4,4]
print(countDuplicate(numbers))
