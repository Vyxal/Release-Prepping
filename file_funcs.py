import sys
import ast
import requests

if __name__ == "__main__":
  print("sys.argv is ", sys.argv)
  files = eval(sys.argv[1])
  directory = sys.argv[2]

  for file in files:
    res = requests.get("https://vyxal.github.io/Vyxal/" + file)
    javascript = res.text
    with open(directory + "/src/" + file, "w") as file:
      file.write(javascript)
