import random 

#Prints random ricky misspeak
def randomMispronunciations():
  #read misspeak file, store lines
  f = open("misspeak.txt")
  quotes = f.readlines()
  f.close()
  #get last isms from list, generate rnd, find rnd between 0 and rnd
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  randomRickyism()
  print(quotes[rnd])
  return quotes[rnd]

#Prints a random rickyism
def randomRickyism():
  #Read rickyisms file, store lines
  f = open("rickyisms.txt")
  isms = f.readlines()
  f.close()
  #get last isms from list, generate rnd, find rnd between 0 and rnd
  last = len(isms) - 1
  rnd = random.randint(0, last)
  print(isms[rnd])
  return isms[rnd]





if __name__== "__main__":
  randomMispronunciations()
