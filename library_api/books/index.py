import http.client

conn = http.client.HTTPSConnection("book-finder1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "13dd409807msh42364fb45e8a76ep13a2dajsn02c11fcf1bfb",
    'X-RapidAPI-Host': "book-finder1.p.rapidapi.com"
    }

conn.request("GET", "/api/search?series=Wings%20of%20fire&book_type=Fiction&lexile_min=600&lexile_max=800&results_per_page=25&page=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


