import random
import time

class Input:
    def __init__(self):
        self.length = 0

    def getAccountName(self):
        self.accountName = str(input("Bitte gebe den Accountname an: "))

    def getLength(self):
        print("Mindestlänge ist 4 Zeichen und Maximallänge ist 256 Zeichen")
        self.length = int(input("Bitte geben Sie die Länge des Passwortes ein: "))
        self.checkLength()
    
    def checkLength(self):
        if self.length < 4:
            print("\nDie eingegebene Länge war zu kurz.\n")
            self.getLength()
        elif self.length > 256:
            print("\nDie eingegebene Länge war zu lang.\n")
            self.getLength()

    def resetAll(self):
        self.length = 0
        self.accountName = ""

class PwdGen:
    def __init__(self):
        self.lettersBig = ["A","B","C","D","E","F","G","H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.lettersSmall = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.nummbers = ["0","1","2","3","4","5","6","7","8","9"]
        self.specialChars = ["!",'"',"§","$","%","&","/","(",")","=","?","{","}","[","]","<",">","+","*","#"]
        self.passwd = ""
        self.dateiName = "Passwd.txt"

    def genPasswd(self,length):
        self.length = length

        for i in range (0,self.length):
            self.charType = random.choice([1,2,3,4])
            if self.charType == 1:
                self.passwd += random.choice(self.lettersBig)
            elif self.charType == 2:
                self.passwd += random.choice(self.lettersSmall)
            elif self.charType == 3:
                self.passwd += random.choice(self.nummbers)
            elif self.charType == 4:
                self.passwd += random.choice(self.specialChars)
        
        self.checkPasswd()
        
    def checkPasswd(self):
        self.charNummberes = 0
        self.charLettersBig  = 0
        self.charLettersSmall = 0
        self.charSpecial = 0
        
        for i in range (0, len(self.passwd)):
            for a in self.lettersBig:
                self.charLettersBig += self.passwd[i].count(a) 
            for b in self.lettersSmall:
                self.charLettersSmall += self.passwd[i].count(b)
            for c in self.nummbers:
                self.charNummberes += self.passwd[i].count(c)
            for d in self.specialChars: 
                self.charSpecial += self.passwd[i].count(d)
        
        if self.charNummberes >= 1 and self.charLettersBig >= 1 and self.charLettersSmall >= 1 and self.charSpecial >= 1:
            print(f"Passwort: {self.passwd}\nIhr Passwort enthält: Nummern: {self.charNummberes}, Großbuchstaben: {self.charLettersBig}, Kleinbuchstaben: {self.charLettersSmall}, Spezialzeichen: {self.charSpecial}")
        
        elif self.charNummberes == 0 or self.charLettersSmall == 0 or self.charLettersBig == 0 or self.charSpecial == 0:
            self.passwd = ""
            self.genPasswd(self.length)
       
    def writeFile(self,logTime,accountName):
        self.accountName = accountName
        self.logTime = logTime

        self.datei = open(self.dateiName,"a")
        self.datei.write(f"Erstellt am: {self.logTime}\nAccountname: {self.accountName}\nPasswort: {self.passwd}\nIhr Passwort enthält: {self.charNummberes} Nummer(n), {self.charLettersBig} Großbuchstabe(n), {self.charLettersSmall} Kleinbuchstabe(n), {self.charSpecial} Spezialzeichen")
        self.datei.write("\r\n")
        self.datei.close()
    
    def resetAll(self):
        self.passwd = ""
        self.charNummberes = 0
        self.charLettersBig  = 0
        self.charLettersSmall = 0
        self.charSpecial = 0

class Controller:
    def __init__(self):
        self.gen = PwdGen()
        self.input = Input()
        self.done = False

    def run(self):
        self.startTime = time.strftime("%d.%m.%Y, %H:%M:%S")
        self.input.getAccountName()
        self.input.getLength()
        self.gen.genPasswd(self.input.length)
        self.gen.writeFile(logTime = self.startTime, accountName = self.input.accountName)

    def loop(self):
        self.run()
        while not self.done:
            self.restart = str(input("Noch ein Passwort generieren? y/n: "))
            if self.restart == "y" or self.restart == "Y" or self.restart == "Yes" or self.restart == "Ja" or self.restart == "ja" or self.restart == "yes":
                self.gen.resetAll()
                self.input.resetAll()
                self.run()
            elif self.restart == "n" or self.restart == "N" or self.restart == "Nein" or self.restart == "nein" or self.restart == "No" or self.restart == "no":
                print("Bye!")
                self.done = True

if __name__ == '__main__': 
    main = Controller()
    main.loop()