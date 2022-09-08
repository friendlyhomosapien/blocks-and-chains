import http.client

endpoint = '127.0.0.1'

connection = http.client.HTTPConnection(endpoint, 5000)
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()
