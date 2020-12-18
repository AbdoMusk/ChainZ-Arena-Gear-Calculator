from colorama import Fore, Back, init
init(autoreset=True)

tier = {
    1: 2000,
    2: 4000,
    3: 10000,
    4: 20000,
    5: 40000,
    6: 70000,
    7: 120000,
    8: 200000,
    9: 400000,
    10: 600000,
    11: 800000,
    12: 1000000,
    13: 1200000,
    14: 1600000,
    15: 2000000,
    16: 2500000,
}
gear_name = {
    1: "Iron",
    2: "Normal",
    3: "Great",
    4: "Excellent",
    5: "Brave",
    6: "Fearless",
    7: "Glory",
    8: "Guardian",
    9: "King's",
    10: "Demon",
    11: "Brilliant",
    12: "Judgement",
    13: "Prophecy",
    14: "Eternal",
    15: "Heaven's",
    16: "God",
}
gears_type = "Sword/Armor/Boots/Ring"

fblack = Fore.BLACK
fgreen = Fore.GREEN
fred = Fore.RED
bgreen = Back.GREEN
byellow = Back.YELLOW
bred = Back.RED

print(bgreen + fblack + "|| Welcome to ChainZ Arena Gear Forge Calculator || Made in a hurry by : someone from Morocco ||"
      "\n>>If you can Please consider contributing and make this tool more powerful by modifiying the python source code from Github"
      "\n and maybe create more ChainZ Arena Tools to help the community!<<")
print(byellow + fblack + "- How its Work:\n in-game there 16 items (Wooden gears doesn't count), type in the gear number you want to Forge/Create "
                       "as follow (count from left to right):\n (first item) \"Iron\""
                       " gears are number 1, Second gear is number 2, (last item) \"God\" gears are number 16, and so on..")
print(bred + fblack + "- To quit the program type in: exit")
while True:
    i = input("What gear you want to Forge (number): ")
    try:
        taman=0
        if i == 'exit':
            break
        elif int(i) > 1:
            for j in range(int(i)):
                j += 1
                power = (3**((int(i)+1)-j))
                divided = round(power / 3)
                taman = (tier.get(int(j))*divided)+taman
        elif int(i) == 1:
            taman = 6000

        print(fgreen+"The cost to forge %s %s from scratch is: %s Gold" % ((gear_name.get(int(i))), gears_type, taman))

        i2 = input("How many times you want this gear: ")
        if i2 != 'exit':
            print(fgreen+"Total gold you need for this Quantity is: %s Gold" % (int(i2)*taman))
        elif i2 == 'exit':
            break
    except Exception as e:
        print(fred+"ERROR! <data type is not an integer or out of range(16)>:"
                               "\n Please enter the gear number (1, 2, 3... 16) or type in \"exit\" if you want to quit the program.")