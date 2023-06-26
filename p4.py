import re
import requests

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

while True:
    response = requests.get(base_url)
    information = response.text
    number_match = re.search(r'and the next nothing is (\d+)', information)

    if number_match:
        number = int(number_match.group(1))
        next_number = str(number)  # Divide the number by 2
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_number}"
        response = requests.get(url)
        print(f"URL: {url} - Response: {response.text}")

        # Update the base_url for the next iteration
        base_url = url
    elif information == "Yes. Divide by two and keep going.":
        next_number = str(int(base_url.split("=")[-1]) // 2)
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_number}"
        response = requests.get(url)
        print(f"URL: {url} - Response: {response.text}")

        # Update the base_url for the next iteration
        base_url = url
    else:
        print("No number found in the response.")
        break
