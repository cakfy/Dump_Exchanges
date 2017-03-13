import requests
res = request.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
print res.text
