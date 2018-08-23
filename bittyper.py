#!/usr/bin/env python3

import random
import sys
import time
import threading
import os


def playerStats():
	playerStats.playerMoney = 0
	

def currentInv():
	currentInv.pocketcalc = 0
	currentInv.telephone = 0
	currentInv.graphicscard = 0
	currentInv.advancedGraphicscard = 0
	currentInv.miningcard = 0
	currentInv.advancedMiningcard = 0
	currentInv.supercomputer = 0
	currentInv.quantumcomputer = 0
	currentInv.gigaquantum = 0
	

def printcurrentInv():
	print(
" Pocket Calculator:",currentInv.pocketcalc,"\n",
"Telephone:",currentInv.telephone, "\n",
"Graphics card:",currentInv.graphicscard, "\n",
"Advanced graphics card:",currentInv.advancedGraphicscard, "\n",
"Mining card:",currentInv.miningcard, "\n",
"Advanced mining card:",currentInv.advancedMiningcard, "\n",
"Supercomputer:",currentInv.supercomputer, "\n",
"Quantumcomputer:",currentInv.quantumcomputer, "\n",
"Gigaquantum:",currentInv.gigaquantum, "\n" "\n" "\n",
"Hash speed:",gameCycle.collection,"btc/s" "\n" "\n"
	)
	
def gameCycle():
	while True:
		#print("mining..")
		#make a random range btc/s
		#make it constantly harded to mine!
		gameCycle.pocketcalc = (currentInv.pocketcalc * 0.001)
		gameCycle.telephone = (currentInv.telephone * 0.005)
		gameCycle.graphicscard = (currentInv.graphicscard * 0.01)
		gameCycle.advancedGraphicscard = (currentInv.advancedGraphicscard * 0.02)
		gameCycle.miningcard = (currentInv.miningcard * 0.05)
		gameCycle.advancedMiningcard = (currentInv.advancedMiningcard * 0.1)
		gameCycle.supercomputer = (currentInv.supercomputer * 0.2)
		gameCycle.quantumcomputer = (currentInv.quantumcomputer * 0.5)
		gameCycle.gigaquantum = (currentInv.gigaquantum * 1)
		
		
		gameCycle.collection = (gameCycle.pocketcalc + gameCycle.telephone +
		 gameCycle.graphicscard + gameCycle.advancedGraphicscard +
		  gameCycle.miningcard + gameCycle.advancedMiningcard +
		   gameCycle.supercomputer + gameCycle.quantumcomputer +
		    gameCycle.gigaquantum)
		setattr(bitcoinWallet, "wallet", (bitcoinWallet.wallet + gameCycle.collection))
		
		time.sleep(1)
		#print("Current bitcoins:", bitcoinWallet.wallet)
		
def bitcoinWallet():
	bitcoinWallet.wallet = 0
	bitcoinWallet.Price = 10
	
def bitcoinMarket():
	print(bitcoinWallet.Price)
	pm = playerStats.playerMoney
	bwp = bitcoinWallet.Price
	bww = bitcoinWallet.wallet
	
	playerI = input("Do you want to sell all your bitcoin? (y)es or (n)o \n:") #option to just sell some
	if playerI == "y":
		cashToPay = (bwp * bww)
		setattr(playerStats, "playerMoney", (pm + cashToPay))
		setattr(bitcoinWallet, "wallet", 0)
	else:
		pass
	
def bitcoinPrice():
	while True:
		bp = bitcoinWallet.Price
		
		marketSwitch = random.randint(1,6)
		
		time.sleep(1)
		
		if marketSwitch == 1:
			newPrice = (bp + (random.randint(1,2) * 3.5))
			setattr(bitcoinWallet, "Price", newPrice)
			time.sleep(random.randint(1,5))
			#print(newPrice)	
		elif marketSwitch == 2:
			newPrice = (bp + (random.randint(1,3) * 4.5))
			setattr(bitcoinWallet, "Price", newPrice)
			time.sleep(random.randint(1,5))
			#print(newPrice)	
		elif marketSwitch == 3:
			newPrice = (bp + (random.randint(1,5) * 7.5))
			setattr(bitcoinWallet, "Price", newPrice)
			time.sleep(random.randint(1,5))
			#print(newPrice)	
		elif marketSwitch == 4:
			newPrice = (bp - (random.randint(1,2) * 3.5))
			setattr(bitcoinWallet, "Price", newPrice)
			time.sleep(random.randint(1,5))
			#print(newPrice)	
		elif marketSwitch == 5:
			newPrice = (bp - (random.randint(1,3) * 4.5))
			setattr(bitcoinWallet, "Price", newPrice)
			time.sleep(random.randint(1,3))
			#print(newPrice)	
		else:
			newPrice = (bp + (random.randint(1,5) * 5.5))
			setattr(bitcoinWallet, "Price", newPrice)
			time.sleep(random.randint(1,3))
			#print(newPrice)	
			
	
def moneyPass():
	newCash = playerStats.playerMoney + 1
	setattr(playerStats, "playerMoney", newCash)

def buy(first, second):
	productChoice = first
	minimumPrice = second
	invNow = getattr(currentInv, productChoice)
	currentCash = playerStats.playerMoney
	if currentCash >= minimumPrice:
		setattr(playerStats, "playerMoney", (currentCash - minimumPrice))
		setattr(currentInv, productChoice, (invNow + 1))
	else: 
		print("You dont have enough cash, you can be(g).")


def gameStart():
	while True:
		key = "d"
		if key != "d":
			exit()
		else:
			defaultMenu()


def defaultMenu():
	playerChoice = input("(b)uy equipment, (w)allet, (m)arket, be(g), (i)nventory, (h)elp or (q)uit\n:")
	if playerChoice == "b":
		playerBuyOptions()
	elif playerChoice == "w":
		print("Current cash:", playerStats.playerMoney)
		print("Current bitcoins:", bitcoinWallet.wallet)
		print("Current price for bitcoin:", bitcoinWallet.Price)
	elif playerChoice == "m":
		bitcoinMarket()
	elif playerChoice == "h":
		print("Coming soon")
	elif playerChoice == "q":
		os._exit(0)
	elif playerChoice == "g":
		moneyPass()
	elif playerChoice == "i":
		printcurrentInv()
	else:
		print("Please put in a valid option.")

#supersell (sell all bitcoins) also new menu, make * the amnmount mined * constant make it harder to mine.
def playerBuyOptions():
	
	playerInput = input("What mining equipment do you want to buy?: \n\n\
k: pocketcalculator \nl: telephone \nm: graphicscard\nn: advanced graphicscard\n\
b: miningcard\nv: advanced miningcard\nc: supercomputer\nx: quantumcomputer\nz: gigaquantum\n:")
		
	if playerInput == "k":
		buy("pocketcalc", 10)
	elif playerInput == "l":
		buy("telephone", 200)
	elif playerInput == "m":
		buy("graphicscard", 1000)
	elif playerInput == "n":
		buy("advancedGraphicscard", 2500)
	elif playerInput == "b":
		buy("miningcard", 10000)
	elif playerInput == "v":
		buy("advancedMiningcard", 40000)
	elif playerInput == "c":
		buy("supercomputer", 100000)
	elif playerInput == "x":
		buy("quantumcomputer", 250000)
	elif playerInput == "z":
		buy("gigaquantum", 500000)
	else:
		print("Type a valid option.")
	
playerStats()	
currentInv()
bitcoinWallet()

game = threading.Thread(name="gamemenu", target=gameStart, daemon=True)
gamec = threading.Thread(name="gameCycle", target=gameCycle, daemon=True)
bitmark = threading.Thread(name="bitcoinmarket", target=bitcoinPrice, daemon=True)

game.start()
gamec.start()
bitmark.start()

game.join()
gamec.join()
bitmark.join()


