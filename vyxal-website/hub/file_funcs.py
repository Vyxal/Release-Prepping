import sys
import requests

if __name__ == "__main__":
  files = sys.argv[1].split(" !! ")
  directory = sys.argv[2]

  for file in files:
    res = requests.get("https://vyxal.github.io/Vyxal/" + file)
    javascript = res.text
    with open(directory + "/src/" + file, "w") as file:
      file.write(javascript)
