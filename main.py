import requests
import time

def get_data_sync(urls):
    st = time.time()
    json_array = []
    x = 0
    for url in urls:
        x += 1
        json_array.append(requests.get(url).json())
        print(x)
    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 3
print(get_data_sync(urls))