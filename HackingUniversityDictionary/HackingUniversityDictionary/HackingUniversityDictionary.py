
def main():
 albums ={"Milkduds":2, "Herald Gene":1, "The 7750's":3, "The Beatles":4,"Snoop Dog":4}
# Variables in quotes and the value after the colon. ! Like our own little database! 

 albums["Milkduds"]+=1 #new album

 albums["The 7750's"] = 2 #Only had 2

 albums.update({"Diamond Dozens":1}) #New album purchased.

 del albums["Herald Gene"] # I sold one away I did not like it

 print("These are the ablums I own!")

 print(albums)

main()
