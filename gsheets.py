# Librería para conectar con Google Spreadsheets
import requests
import time

def report(code,success):
    date = time.strftime("%c")
    url = "https://script.google.com/macros/s/AKfycbwI1RbJdElFFRl8FbYlDd0M7DuztFdCUAB8WSmjyZT-mS1zdvMI/exec?date="+str(date)+"&code="+str(code)+"&success="+str(success)
    response = requests.get(url)
    return response
