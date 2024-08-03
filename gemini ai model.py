import requests

url = 'https://api.example.com/endpoint'
headers = {
    'Authorization': 'AIzaSyA0Jx5lovrPEfz7_4_fLFwP4vttlOuRmXc'  # Replace with your API key
}

try:
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print('Valid credentials. Successful connection!')
    else:
        print('Error in API call. Status code:', response.status_code)
        print('Response:', response.text)

except Exception as e:
    print('Error during API call:', e)