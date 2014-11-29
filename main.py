import wikipedia,webbrowser

def getPage():
    wikipage = wikipedia.random(1)
    wikiload = wikipedia.page(wikipage)
    userchoice = input("Would you like to read about {} (Y/N/Q)".format(wikipage))
    if(userchoice == "Y" or userchoice == "y"):
        print("\nSummary:\n--------\n" + wikipedia.summary(wikipage))
        wikiopen = input("\nOpen Wiki page in browser? (Y/N)")
        if(wikiopen == "Y" or wikiopen == "y"):
            webbrowser.open(wikiload.url,new=2)
        else:
            getPage()
        exit(0)
    elif(userchoice == "q" or userchoice == "Q"):
        exit(0)
    else:
        getPage()

getPage()
