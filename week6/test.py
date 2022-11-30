import requests
url = "https://script.google.com/macros/s/AKfycbw8YuCpkp3Cpz5WVba_LM4jOV-qpFTBISAh-ZIH7tQCgI2a1ZGmyRwD7ukHCPOISg1Y/exec"

headers = {
    'Content-Type':'application/json'
}
req = requests.post(url, headers=headers, json={"assetId":"2544539559","functions":"?"})
print(req.content)