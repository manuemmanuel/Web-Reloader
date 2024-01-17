import requests
import time
def main():
    url = input("Enter the URL: ")
    count = int(input("How many times do you want to reload? "))
    delay = int(input("Enter the delay(s): "))
    reload_url(url, count, delay)
    
def reload_url(url, count, delay):
    try:
        for i in range(count):
            response = requests.get(url)
            print(f"Reload count: {i + 1}")
            time.sleep(delay)
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
