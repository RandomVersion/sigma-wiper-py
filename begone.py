import os, sys, webbrowser

sigmaDataDir = "~/.minecraft/sigma"
sigma5datadir = "~/.minecraft/sigma5"
sigmajellodatadir = "~/.minecraft/jello"
sigmaCapitalizedDataDir = "~/.minecraft/Sigma"
SigmaVerDir = "~/.minecraft/versions/Sigma"
Sigma5VerDir = "~/.minecraft/versions/Sigma5"
jellolauncher = "~/.minecraft/SigmaJelloPrelauncher.jar"

def remove():
	os.remove(sigmaDataDir)
	os.remove(sigma5datadir)
	os.remove(sigmajellodatadir)
	os.remove(sigmaCapitalizedDataDir)
	os.remove(SigmaVerDir)
	os.remove(Sigma5VerDir)
	os.remove(jellolauncher)

def test():
	print("\nCurrently selected directories")
	print(sigmaDataDir)
	print(sigma5datadir)
	print(sigmajellodatadir)
	print(sigmaCapitalizedDataDir)
	print(Sigma5VerDir)
	print(SigmaVerDir)
	print(jellolauncher)

def main():
	print("Select an option:")
	print("[1]	Delete sigma")
	print("[2]	Star the project")
	print("[3]	Exit")
	print("[4]	Test")

	i = input("> ")
	if i == "1":
		remove()
	elif i == "2":
		webbrowser.open('https://github.com/RandomVersion/sigma-wiper-py/', new=2)
	elif i == "3":
		exit()
	elif i == "4":
		test()

main()