print("Always been executed")

def main():
  print("Hi... only executed when the condition is true")

if __name__ == '__main__':
  main()
else:
  print("Hi... only executed when the condition is false")