import sys
import json
import requests

if __name__ == "__main__":
  files = eval(sys.argv[1])
  print(files)
  directory = sys.argv[2]

  for file in files:
    res = requests.get("https://vyxal.github.io/Vyxal/" + file)
    javascript = res.text
    with open(directory + "/src/" + file, "w") as file:
      file.write(javascript)
