# 這是第二次作業
## 作業二程式碼

## 請將以下網址的json,儲存為aqi.json檔


url = '	https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
## 將位址使用requests.get 賦值response

res:Response = requests.get(url=url)
## 使用model requests的內建功能

with open("aqi2.csv", 'wb') as fd:
    for chunk in res.iter_content(chunk_size=128):
        fd.write(chunk)

作業程式連結：[lession3.ipynb] (https://github.com/joechen1973/joechen_window/blob/main/homework/Issues%236/lession3.ipynb)