import requests
import time
import random

def reload_url(url, count, min_delay, max_delay):
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    ]
    
    try:
        for i in range(count):
            headers = {'User-Agent': random.choice(user_agents)}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"Reload count: {i + 1}, Status code: {response.status_code}, Request was successful")
            else:
                print(f"Reload count: {i + 1}, Status code: {response.status_code}, Request failed")
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    count = int(input("How many times do you want to reload? "))
    min_delay = int(input("Enter the minimum delay (seconds): "))
    max_delay = int(input("Enter the maximum delay (seconds): "))
    reload_url(url, count, min_delay, max_delay)
