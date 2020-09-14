import requests
import json
import sys

def exchange(base,target):
  try:
    response = requests.get("https://api.exchangeratesapi.io/latest?symbols=" + target + "&base=" + base)
    response.raise_for_status()
    # print(response.status_code)
    print("\n" + json.loads(response.text)["date"] + "\n" + base + "=>" + target + ":",str(json.loads(response.text)["rates"][target]))
  except requests.exceptions.RequestException as e:
    print("\n" +"入力内容に誤りがあります(正しい通貨コードを入力してください): " + "\n" + base + "または" + target + "に対応した通貨はありませんでした。")

def getRates():
  base = "USD"
  target = "JPY"
  if len(sys.argv) == 2:
    target = str(sys.argv[1]).upper()
    exchange(base,target)
  elif len(sys.argv) > 2:
    base = str(sys.argv[1]).upper()
    for i,targets in enumerate(sys.argv):
      if i < 2:
        continue
      exchange(base,str(targets).upper())
  else:
    exchange(base,target)

getRates()

sys.exit(0)