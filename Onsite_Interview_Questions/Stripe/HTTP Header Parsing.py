import collections
import unittest
def parse_accept_language(headers, supportedLanguagesForSever):
    res = []
    resSet = set()
    tagMap = collections.defaultdict(set)
    weightMap = collections.defaultdict(float)
    maxHeap = []
    if len(headers) == 0 or len(supportedLanguagesForSever) == 0:
        return res
    for curLang in supportedLanguagesForSever:
        curTag = curLang[:2]
        tagMap[curTag].add(curLang)
    supportedLanguagesForClient = headers.replace(' ', '').split(',')
    for curHeaderTag in supportedLanguagesForClient:
        # Get Tag Array if len(curHeaderTag) > 0
        curHeaderTagArray = curHeaderTag.split(';')
        if len(curHeaderTagArray) > 1:
            # Get Current Tag
            curTag = curHeaderTagArray[0]
            # Get Weight
            curTagWeight = float(curHeaderTagArray[1][2:])
        else:
            curTag = curHeaderTagArray[0]
            curTagWeight = 0
        
        if curTag in supportedLanguagesForSever:
            resSet.add(curTag)
            heapq.heappush(maxHeap, (-curTagWeight, curTag))
            #res.append(curLang)
        elif curTag in tagMap:
            for curLang in tagMap[curTag]:
                if curLang not in resSet:
                    resSet.add(curLang)
                    heapq.heappush(maxHeap, (-curTagWeight, curLang))
                    #res.append(s)
        elif curTag == '*':
            for curLang in supportedLanguagesForSever:
                if curLang not in resSet:
                    resSet.add(curLang)
                    heapq.heappush(maxHeap, (-curTagWeight, curLang))
    while maxHeap:
        lang = heapq.heappop(maxHeap)[1]
        res.append(lang)
    return res
                
# print('test case 1')   
# print(parse_accept_language("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"]))
# print(parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"]))
# print(parse_accept_language("en-US", ["en-US", "fr-CA"]))
# print('================================','\n')

# print('test case 2')
# print(parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"]))
# print(parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"]))
# print(parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"]))

# print('================================','\n')
# print('test case 3')
# print(parse_accept_language("en-US, *", ["en-US", "fr-CA", "fr-FR"]))
# print(parse_accept_language("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"]))

# print('================================','\n')
# print('test case 4')
# print(parse_accept_language("fr-FR;q=1, fr-CA;q=0, fr;q=0.5", ["fr-FR", "fr-CA", "fr-BG"]))
# print(parse_accept_language("fr-FR;q=1, fr-CA;q=0, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"]))
# print(parse_accept_language("en-US;q=1, en;q=0.5, *;q=0", ["en-GB", "en-US", "fr-CA", "fr-FR"]))

class TestCaseCheck(unittest.TestCase):
    def testcase_parse_header_positive_case(self):
        result = parse_accept_language("en-US, fr-CA, fr-FR",["fr-FR", "en-US"])
        self.assertEqual(result, ["en-US", "fr-FR"])
        print('TEST CASES PASSED')
    
t = TestCaseCheck()
t.testcase_parse_header_positive_case()
