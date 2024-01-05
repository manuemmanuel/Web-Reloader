import requests
import time

def reload_url(url, count):
    try:
        for i in range(count):
            response = requests.get(url)
            print(f"Reload count: {i + 1}")
            time.sleep(1)
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    count = int(input("How many times do you want to reload? "))
    reload_url(url, count)
