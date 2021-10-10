def primary():
  f = open("quotes.txt","a")

 #Adding new quotes to the quotes.txt
  add_quotes = ["Two heads are better than one",
                "One step at a time",
                "Time waits for no man"
                ] 
  for i in add_quotes:
    f.writelines(i +"\n")
  f.close()

  f = open("quotes.txt", "r")
  quotes = f.readlines()
  #Read the last line 
  print("Last quote")
  print(quotes[-1])
  #Reading the first five lines
  print("First five lines")
  for i in range(5):

    print(i+1,quotes[i], sep=" ")


  #print the last line of a file
  #print(quotes[-1])

if __name__== "__main__":
  primary()
