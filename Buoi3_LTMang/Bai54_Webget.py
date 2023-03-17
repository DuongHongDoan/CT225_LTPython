import http.client as httplib

httpconn = httplib.HTTPConnection("172.18.54.56", 80)

httpconn.request("GET", "/index.html")
resp = httpconn.getresponse()
if resp.status == 200:
    resp_data = resp.read()
    print(resp_data.decode('ascii'))
httpconn.close()