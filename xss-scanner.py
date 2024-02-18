import base64

import requests
from bs4 import BeautifulSoup

from urllib.parse import urlparse, parse_qs



def fetch_input_tags(url, cookies, headers):
    # HTTP 요청을 보내고 응답을 받음
    response = requests.get(url, cookies=cookies, headers=headers)

    # 응답으로부터 HTML을 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 모든 <input> 태그를 찾음
    input_tags = soup.find_all('input')

    # 찾은 <input> 태그들을 출력
    for tag in input_tags:
        print(tag)


def parse_cookies(cookie_string):
    cookies = {}
    for cookie in cookie_string.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value
    return cookies


def parse_headers(header_string):
    headers = {}
    for line in header_string.strip().split('\n'):
        key, value = line.split(': ', 1)
        headers[key] = value
    return headers

# 헤더 문자열
# header_string = """
# Sec-Ch-Ua: "Chromium";v="121", "Not A(Brand";v="99"
# Sec-Ch-Ua-Mobile: ?0
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36
# Sec-Ch-Ua-Platform: "Windows"
# Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: no-cors
# Sec-Fetch-Dest: image
# Referer: https://www.codeit.kr/subscription/payment?chargeTerm=asd%22%3E
# Accept-Encoding: gzip, deflate, br
# Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
# Priority: u=2, i
# """


def parse_http_request(request_string):
    # 요청 문자열을 줄바꿈으로 분리
    lines = request_string.strip().split('\n')
    # 첫 줄에서 메서드, 경로, HTTP 버전 추출
    method, path, http_version = lines[0].split(' ')

    # 헤더와 쿠키를 저장할 딕셔너리 초기화
    headers = {}
    cookies = {}

    # 헤더 시작 지점부터 쿠키를 제외한 헤더 파싱
    for line in lines[1:]:
        if line.startswith('Cookie:'):
            # 쿠키 문자열 추출 및 파싱
            cookie_string = line[len('Cookie: '):]
            for cookie in cookie_string.split('; '):
                key, value = cookie.split('=', 1)
                cookies[key] = value
        else:
            # 일반 헤더 파싱
            key, value = line.split(': ', 1)
            headers[key] = value

    return method, path, http_version, headers, cookies


# # 전체 HTTP 요청 문자열

#
# # 함수 호출 및 결과 출력
# method, path, http_version, headers, cookies = parse_http_request(request_string)
# print("Method:", method)
# print("Path:", path)
# print("HTTP Version:", http_version)
# print("Headers:", headers)
# print("Cookies:", cookies)


def send_request(method, path, headers, cookies, base_url="http://www.codeit.kr"):
    # 전체 URL 구성
    url = base_url + path

    # requests의 메서드를 동적으로 호출하기 위한 준비
    method_function = getattr(requests, method.lower(), None)

    # 지원하지 않는 메서드인 경우 예외 처리
    if not method_function:
        raise ValueError(f"Unsupported method: {method}")

    # 요청 보내기
    response = method_function(url, headers=headers, cookies=cookies)

    # 응답 반환
    return response


# # 예제 사용
# response = send_request(method, path, headers, cookies)
#
# # 응답 내용 출력
# print(response.status_code)
# print(response.headers)
# print(response.text)
#
#
# # 사용 예시
# url = "http://example.com"  # 실제 요청을 보낼 URL
# cookies = {'session': '123456789'}  # 필요한 쿠키, 실제 값으로 변경해야 함
# headers = {'User-Agent': 'Mozilla/5.0'}  # 필요한 헤더, 실제 값으로 변경해야 함
#
# # 함수 호출
# fetch_input_tags(url, cookies, headers)

def param_test(path):
    print(path)
    tmp_path = path.split('?')
    if len(tmp_path) < 2:
        print("no param")
    elif tmp_path[1] == '':
        print("no param")
    # hash??

    get_param = tmp_path[1].split('&')
    print(get_param)
    param_dict = {}
    for p in get_param:
        # param에 =이 들어가 있을 경우
        param_dict[p.split('=')[0]] = p.split('=')[1]
    print(param_dict)






if __name__=="__main__":
    print("[+]")
    request_string = """
GET /search/all?adQuery=asd%22%3E&cardDiscount=true&maxPrice=1234&minPrice=123&origQuery=asd%22%3E&pagingIndex=1&pagingSize=40&productSet=checkout&query=asd%20%3E&sort=rel&timestamp=&viewType=list HTTP/2
Host: search.shopping.naver.com
Cookie: NNB=GFLW4UF4CD6GI; SHP_BUCKET_ID=4; naverfinancial_CID=0b20f1c30bbf459daa8ec70ce946f1b8; _ga_Q7G1QTKPGB=GS1.1.1697853130.1.1.1697856542.0.0.0; _ga_EFBDNNF91G=GS1.1.1698763767.2.1.1698765728.0.0.0; _ga=GA1.1.1248901520.1697298436; _ga_3X9JZ731KT=GS1.1.1698765730.2.1.1698766083.0.0.0; _fwb=136wmsgNtQ8JkguavMAONN1.1708146675522; market_tooltip_EMART_EVERYDAY=true; spage_uid=
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="121", "Not A(Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Arch: ""
Sec-Ch-Ua-Platform: "Windows"
Sec-Ch-Ua-Platform-Version: ""
Sec-Ch-Ua-Model: ""
Sec-Ch-Ua-Bitness: ""
Sec-Ch-Ua-Wow64: ?0
Sec-Ch-Ua-Full-Version-List: 
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Priority: u=0, i


    """
    # print(request_string)
    base_url = ''
    method, path, http_version, headers, cookies = parse_http_request(request_string)
    # print(method, path, http_version, headers, cookies)
    if base_url == '':
        base_url = 'https://'+headers['Host']
    url = base_url+path
    # print(url)

    # urlparse를 사용하여 URL 파싱
    parsed_url = urlparse(path)
    test = param_test(path)

    # # parse_qs를 사용하여 쿼리 파라미터를 딕셔너리로 변환
    # query_params = parse_qs(parsed_url.query)
    # # print(query_params)
    #
    # res = send_request(method, path, headers, cookies, base_url)
    # # print(res.text)
    # soup = BeautifulSoup(res.text, 'html.parser')
    #
    # # 모든 <input> 태그를 찾음
    # input_tags = soup.find_all('input')
    #
    # # 찾은 <input> 태그들을 출력
    # for tag in input_tags:
    #     print(tag)