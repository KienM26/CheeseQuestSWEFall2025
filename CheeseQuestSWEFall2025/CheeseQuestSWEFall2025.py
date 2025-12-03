# Cheese Quest: The Plight of Kashkaval
# Edited by: 
# Gage Halpin, Kien Ma, Christina Kuo, Liam Casey, Sean Reynolds

# Original Author: Evan Quan Oct. 17, 2016
# Single-player text based adventure game
# Save the world from the Cheese Mage!

# Sean Reynolds - Updated code to work under PEP 8 Convention Standards
#                 Removed redundant parentheses

# imports
import random, os, getpass

# === KEEP THESE VARIABLES (Your game uses them) ===
VERSION = "1.4.3"
DATE = "October 17, 2016"

# === ADD THIS LINE (Required for Inventory to work) ===
player_name = "Hero"

# Inventory
class Inventory(object):
        def __init__(self, name = "room", gold = 0, letter = 0, key = 0, key_skeleton = 0, pickaxe = 0, shrubbery = 0, funnel_cake = 0, half_funnel_cake = 0, foot = 0, porridge = 0, bowl = 0, lantern = 0, oil = 0, pie = 0, coal = 0, biscuit = 0, hook = 0, staff = 0, ticket = 0, potato = 0, bandage = 0, journal = 0, book = 0, brie = 0, munster = 0, stilton = 0, swiss = 0, wensleydale = 0, potion = 0, flask = 0, stone = 0, bird = 0, note = 0, memo = 0, note_1 = 0, note_2 = 0, note_3 = 0, note_4 = 0):
            self.name = name
            self.gold = gold
            self.goldDescription = "The edges are worn down from handling."
            self.letter = letter
            self.letterDescription = "Made out of old parchment, the message on it is written in ink."
            self.letterRead = "It reads:\n\nTo " + str(player_name) + ",\n\nA certain Eden Von Roquefort has set up residence NORTH of MOUNT MAGNA. While he purports to be a lowly cheese mage, reliable sources claim him to be the demon lord, Vesh'kathal the Deceiver, a shapeshifter infamous of manipulating the minds and bending the wills of others. Legend tells of a saviour, deemed the Monterey Messiah, who will save all of Kashkaval from his wickedness. It has be brought to my attention that you are that saviour that the legends speak of. While I have very important matters to attend to, the best I can do is help instruct you in how to defeat this demon lord:\n\nFIRST, you must acquire the staff from the Garrotxian temple NORTHEAST of this town, for it is the only weapon capable of defeating such a powerful demon.\n\nNEXT, once you have the staff, go NORTH through the MINES of MOUNT MAGNA and find him at his house on the other end.\n\nFINALLY, kill Roquefort and Kashkaval will be saved from his wrath.\n\nI know this is probably a lot to digest at once, but you are our only hope. I fear in your attempt to complete this task, Vesh'kathal will attempt to thwart you. He may attempt to contact and manipulate you, or have his minions work to stop you. Whatever he does, you must persevere.\n\nMay you be blessed,\n\nThe last prophet of Garrotxa"
            self.key = key
            self.keyDescription = "The key to your jail cell."
            self.key_skeleton = key_skeleton
            self.key_skeleton_description = "The head is a skull with glowing purple eyes."
            self.pickaxe = pickaxe
            self.pickaxeDescription = "A sturdy tool useful for mining."
            self.shrubbery = shrubbery
            self.shrubberyDescription = "It's a very nice shrubbery, and not too expensive."
            self.funnel_cake = funnel_cake
            self.funnel_cake_description = "It's covered in powdered sugar. Mmmmm... and still warm."
            self.half_funnel_cake = half_funnel_cake
            self.half_funnel_cake_description = "Ew. You can see the bite marks."
            self.foot = foot
            self.footDescription = "A prominent symbol of RNGesus, the ancient god of gambling, luck, and salt."
            self.porridge = porridge
            self.porridgeDescription = "Bland prison food. Makes you consider if eating this everyday was the real punishment."
            self.bowl = bowl
            self.bowlDescription = "Small and dented. Made of out of tin."
            self.lantern = lantern
            self.lanternDescription = "Perfect for lighting dark areas."
            self.oil = oil
            self.oilDescription = "Perfect for things that are perfect for lighting dark areas."
            self.pie = pie
            self.pieDescription = "Hardy and delicious. Just looking at it makes you hungry."
            self.biscuit = biscuit
            self.biscuitDescription = "Harder than a brick and probably just as tasty."
            self.hook = hook
            self.hookDescription = "Just having one makes you feel like a secret agent."
            self.staff = staff
            self.staffDescription = "Elaboratedly designed and encrusted with sapphires, this staff holds unspeakable power."
            self.ticket = ticket
            self.ticketDescription = "The number 77 is written on it."
            self.coal = coal
            self.coalDescription = "A valuable fuel source for a variety of uses."
            self.potato = potato
            self.potatoDescription = "It looks rotten and covered in ash. You probably shouldn't eat it."
            self.bandage = bandage
            self.bandageDescription = "Good for healing wounds."
            self.journal = journal
            self.journalDescription = "The cover is leather-bound. The whatever text there was along the spine is worn off."
            self.book = book
            self.bookDescription = "The cover is entirely black, made out of a material unbeknownst to you. It is heavier than it looks."
            self.brie = brie
            self.brieDescription = "Soft and creamy."
            self.munster = munster
            self.munsterDescription = "Milky white."
            self.stilton = stilton
            self.stiltonDescription = "Hard, with blue veins."
            self.swiss = swiss
            self.swissDescription = "It has more holes than the plot to the story of this game."
            self.wensleydale = wensleydale
            self.wensleydaleDescription = "Crumbly and a bit dry."
            self.potion = potion
            self.potionDescription = "The fluid is red, bubbling, and and foggy. Looks completely safe to drink."
            self.flask = flask
            self.flaskDescription = "It's empty."
            self.stone = stone
            self.stoneDescription = "It glows a pulsing red as if it were alive. It also seems to produces its own heat."
            self.bird = bird
            self.birdDescription = "It's crudely carved to look like a raven."
            self.note = note
            self.noteDescription = "Some numbers are written on the small slip of paper."
            self.note_1 = note_1
            self.note_2 = note_2
            self.note_3 = note_3
            self.note_4 = note_4
            self.noteRead = "It reads: \"If you must enter, bring a LIGHT SOURCE to keep the creature away. It won't work forever, but it will give you some time. The vault code is %s%s%s%s.\"" % (note_1,note_2,note_3,note_4)
            self.memo = memo
            self.memoDescription = "The edges are burnt and the parchment is covered in ash."
            self.memoRead = "It reads:\n\n\"To whoever is still alive,\n\nBy the time you read this, I will probably be dead. After I learned I could say \"EYIK VO'HOLLOM\" to enter the obisdian hemispheres, I came here from Airedale through one of them in order to help look for survivors up North. The demons went from farm to farm, burning all the crops down, and got me before I could escape. If you are to save this world from demon-kind, you must vanquish them with the staff of Garrotxa back in my home town. It is our only hope.\""
            # "It reads:\n\nTo whoever is still alive,\n\nBy the time you read this, I will probably be dead. It turns out POTATOES, of all things, are the Ozkavosh's greatest WEAKNESS. After I learned I could say \"EYIK VO'HOLLOM\" to enter the obisdian hemispheres, I came here from Airedale through one in order to get as many potatoes as I could find. The demons went from farm to farm, burning all the crops down, and got me before I could escape. If you are to save this world from demon-kind, you must vanquish them with a potato. Either that, or get hold of the staff of Garrotxa back in my town."
        def item_types(self):
            type_count = 0
            if self.gold:
                type_count += 1
            if self.letter:
                type_count += 1
            if self.key:
                type_count += 1
            if self.key_skeleton:
                type_count += 1
            if self.pickaxe:
                type_count += 1
            if self.shrubbery:
                type_count += 1
            if self.funnel_cake:
                type_count += 1
            if self.half_funnel_cake:
                type_count += 1
            if self.foot:
                type_count += 1
            if self.porridge:
                type_count += 1
            if self.bowl:
                type_count += 1
            if self.lantern:
                type_count += 1
            if self.oil:
                type_count += 1
            if self.pie:
                type_count += 1
            if self.biscuit:
                type_count += 1
            if self.hook:
                type_count += 1
            if self.staff:
                type_count += 1
            if self.ticket:
                type_count += 1
            if self.coal:
                type_count += 1
            if self.potato:
                type_count += 1
            if self.bandage:
                type_count += 1
            if self.journal:
                type_count += 1
            if self.book:
                type_count += 1
            if self.brie:
                type_count += 1
            if self.munster:
                type_count += 1
            if self.stilton:
                type_count += 1
            if self.swiss:
                type_count += 1
            if self.wensleydale:
                type_count += 1
            if self.potion:
                type_count += 1
            if self.flask:
                type_count += 1
            if self.stone:
                type_count += 1
            if self.bird:
                type_count += 1
            if self.note:
                type_count += 1
            if self.memo:
                type_count += 1
            return type_count
        def examine_inventory(self, option, room_current):
            # Quantity and Description
            # Inventory
            if option == "inventory":
                if not self.item_types():
                    print("You have nothing.")
                else:
                    print("You have:")
                    if self.bandage == 1:
                        print("    a bandage")
                    elif self.bandage > 1:
                        print("   ",self.bandage,"bandages")
                    if self.porridge:
                        print("    a bowl of porridge")
                    if self.bowl:
                        print("    a bowl")
                    if self.pie == 1:
                        print("    a chicken pot pie")
                    elif self.pie > 1:
                        print("   ",self.pie,"chicken pot pies")
                    if self.stone:
                        print("    a dragonstone")
                    if self.flask == 1:
                        print("    a flask")
                    elif self.flask > 1:
                        print("   ",self.flask,"flasks")
                    if self.funnel_cake == 1:
                        print("    a funnel cake")
                    elif self.funnel_cake > 1:
                        print("   ",self.funnel_cake,"funnel cakes")
                    if self.gold:
                        print("   ",self.gold,"gold")
                    if self.hook == 1:
                        print("    a grappling hook")
                    elif self.hook > 1:
                        print("   ",self.hook,"grappling hooks")
                    if self.half_funnel_cake == 1:
                        print("    a half-eaten funnel cake")
                    elif self.half_funnel_cake > 1:
                        print("   ",self.half_funnel_cake,"half-eaten funnel cakes")
                    if self.biscuit == 1:
                        print("    a hardtack biscuit")
                    elif self.biscuit > 1:
                        print("   ",self.biscuit,"hardtack biscuits")
                    if self.journal == 1:
                        print("    a journal")
                    elif self.journal > 1:
                        print("   ",self.journal,"journals")
                    if self.key:
                        print("    a key")
                    if self.key_skeleton:
                        print("    the key of Ahm'domosh")
                    if self.lantern == 1:
                        print("    a lantern")
                    elif self.lantern > 1:
                        print("   ",self.lantern,"lanterns")
                    if self.letter:
                        print("    a letter")
                    if self.foot == 1:
                        print("    a lucky rabbit foot")
                    elif self.foot > 1:
                        print("   ",self.foot,"lucky rabbit feet")
                    if self.memo:
                        print("    a memo")
                    if self.book == 1:
                        print("    a mysterious book")
                    elif self.book > 1:
                        print("   ",self.book,"mysterious books")
                    if self.note:
                        print("    a note")
                    if self.pickaxe == 1:
                        print("    a pickaxe")
                    elif self.pickaxe > 1:
                        print("   ",self.pickaxe,"pickaxes")
                    if self.coal == 1:
                        print("    a piece of coal")
                    elif self.coal > 1:
                        print("   ",self.coal,"pieces of coal")
                    if self.potato:
                        print("    a rotten potato")
                    if self.potion == 1:
                        print("    a potion of rejuvination")
                    elif self.potion > 1:
                        print("   ",self.potion,"potions of rejuvination")
                    if self.ticket:
                        print("    a raffle ticket")
                    if self.shrubbery == 1:
                        print("    a shrubbery")
                    elif self.shrubbery > 1:
                        print("   ",self.shrubbery,"shrubberies")
                    if self.brie:
                        print("    a slice of brie cheese")
                    if self.munster:
                        print("    a slice of munster cheese")
                    if self.stilton:
                        print("    a slice of stilton cheese")
                    if self.swiss:
                        print("    a slice of swiss cheese")
                    if self.wensleydale:
                        print("    a slice of wensleydale cheese")
                    if self.staff:
                        print("    the staff of Garrotxa")
                    if self.oil == 1:
                        print("    a vial of lantern oil")
                    elif self.oil > 1:
                        print("   ",self.oil,"vials of lantern oil")
                    if self.bird:
                        print("    a wooden bird")
            # Individual items
            elif option == "gold" and (self.gold or room_current.gold):
                print(self.goldDescription)
            elif option == "letter" and (self.letter or room_current.letter):
                    print(self.letterDescription)
            elif option == "key" and (self.key or room_current.key):
                print(self.keyDescription)
            elif option == "key of Ahm'domosh" and (self.key_skeleton or room_current.key_skeleton):
                print(self.key_skeleton_description)
            elif option == "pickaxe" and (self.pickaxe or room_current.pickaxe):
                print(self.pickaxeDescription)
            elif option == "shrubbery" and (self.shrubbery or room_current.shrubbery):
                print(self.shrubberyDescription)
            elif option == "funnelCake" and (self.funnel_cake or room_current.funnel_cake):
                print(self.funnel_cake_description)
            elif option == "half-eaten funnel cake" and (self.half_funnel_cake or room_current.half_funnel_cake):
                print(self.half_funnel_cake_description)
            elif option == "lucky rabbit foot" and (self.foot or room_current.foot):
                print(self.footDescription)
            elif option == "bowl of porridge" and (self.porridge or room_current.porridge):
                print(self.porridgeDescription)
            elif option == "bowl" and (self.bowl or room_current.bowl):
                print(self.bowlDescription)
            elif option == "lantern" and (self.lantern or room_current.lantern):
                print(self.lanternDescription)
            elif option == "vial of oil lantern" and (self.oil or room_current.oil):
                print(self.oilDescription)
            elif option == "chicken pot pie" and (self.pie or room_current.pie):
                print(self.pieDescription)
            elif option == "hardtack biscuit" and (self.biscuit or room_current.biscuit):
                print(self.biscuitDescription)
            elif option == "grappling hook" and (self.hook or room_current.hook):
                print(self.hookDescription)
            elif option == "staff of Garrotxa" and (self.staff or room_current.staff):
                print(self.staffDescription)
            elif option == "raffle ticket" and (self.ticket or room_current.ticket):
                print(self.ticketDescription)
            elif option == "piece of coal" and (self.coal or room_current.coal):
                print(self.coalDescription)
            elif option == "potato" and (self.potato or room_current.potato):
                print(self.potatoDescription)
            elif option == "bandage" and (self.bandage or room_current.bandage):
                print(self.bandageDescription)
            elif option == "journal" and (self.journal or room_current.journal):
                print(self.journalDescription)
            elif option == "book" and (self.book or room_current.book):
                print(self.bookDescription)
            elif option == "brie" and (self.brie or room_current.brie):
                print(self.brieDescription)
            elif option == "slice of munster cheese" and (self.munster or room_current.munster):
                print(self.munsterDescription)
            elif option == "slice of stilton cheese" and (self.stilton or room_current.stilton):
                print(self.stiltonDescription)
            elif option == "slice of swiss cheese" and (self.swiss or room_current.swiss):
                print(self.swissDescription)
            elif option == "slice of wensleydale cheese" and (self.wensleydale or room_current.wensleydale):
                print(self.wensleydaleDescription)
            elif option == "potion or rejuvination" and (self.potion or room_current.potion):
                print(self.potionDescription)
            elif option == "flask" and (self.flask or room_current.flask):
                print(self.flaskDescription)
            elif option == "dragonstone" and (self.stone or room_current.stone):
                print(self.stoneDescription)
            elif option == "wooden bird" and (self.bird or room_current.bird):
                print(self.birdDescription)
            elif option == "note" and (self.note or room_current.note):
                print(self.noteDescription)
            elif option == "memo" and (self.memo or room_current.memo):
                print(self.memoDescription)
            else:
                if option == "gold":
                    print("There is no gold here to examine.")
                else:
                    print("There is no",option,"here to examine.")

# Multiple imports for an import name detected, deep source
# #_______Libraries_______________________________________________________________
# import random,os,getpass
# playerName = "Hero"

# Resize command line window to appropriate size
# col is width
# lines is buffer height
os.system('mode con: cols=200')
#_______Constants_______________________________________________________________
# Debug mode password
PASSWORD = "mwop"
# Stats
HUNGER_MAX = 80
HUNGER_START = 5
HUNGER_DEBUG = HUNGER_MAX
HEALTH_MAX = 7
HUNGER_DARKNESS = 30
# How many turns until death that warning messages appear
HUNGER_WARNING = 15
# Food Hunger Values
HUNGER_PORRIDGE = HUNGER_MAX
HUNGER_FUNNELCAKE = 20 # 2 hunger/gold
HUNGER_HALFFUNNELCAKE = HUNGER_FUNNELCAKE / 2
HUNGER_PIE = 70 # 3.5 hunger/gold
HUNGER_BISCUIT = 30
HUNGER_POTION = 125 # 5 hunger/gold, or 12.5 hunger/gold if refill
HUNGER_CHEESE = 10

# Lantern oil turn duration
OIL_DURATION = 30
# Ball of light duration
LIGHT_DURATION = OIL_DURATION * 2
# Prices
# Buy
PRICE_BUY_PICKAXE = 20
PRICE_BUY_FUNNELCAKE = 5
PRICE_BUY_FOOT = 30
PRICE_BUY_LANTERN = 30
PRICE_BUY_OIL = 5
PRICE_BUY_PIE = 20
PRICE_BUY_HOOK = 400
PRICE_BUY_BANDAGE = 10
PRICE_BUY_TICKET = 20
PRICE_BUY_POTION = 25
PRICE_REFILL_POTION = 10
# Sell
PRICE_SELL_COAL = 25
PRICE_SELL_STONE = 300
# LAKE
LAKE_GOLD_REWARD = 241
LAKE_PIE_REWARD = 1
# MOUNT ENTRANCE
LOOT_ENTRANCE_COAL = 3
LOOT_ENTRANCE_NOTE = 1
# CAVERN
# Coal Mine
COAL_MIN = 6
COAL_MAX = 9
PICKAXE_BREAK_CHANCE = 1
RUBBLE_FALL_CHANCE = 1
# Creature
CREATURE_ROAM_MIN = 22
CREATURE_ROAM_MAX = 32
CREATURE_CHASE_MIN = 16
CREATURE_CHASE_MAX = 22
# Cave Treasure chest gold reward
# Should offset most of equipment prices
CHEST_REWARD = 324
# Dead body loot
LOOT_A_GOLD = 187
LOOT_A_OIL = 2
LOOT_B_GOLD = 96
LOOT_B_JOURNAL = 1
LOOT_C_PICKAXE = 1
LOOT_C_OIL = 2

# DARKNESS
DARKNESS_DURATION = 3

# LAIR
# How many turns it takes to break rubble
RUBBLE_DURABILITY = 2
LOOT_MID_BISCUIT = 1
LOOT_MID_BANDAGE = 2
LOOT_WEST_GOLD = 42
LOOT_WEST_BISCUIT = 2
LOOT_HOLE_OIL = 1
# creatureLairChaseCounter
# Determines how many turns before creature kills you after waking
LAIR_CHASE_DURATION = 5

# BRIDGE
# Troll Gold needed to pass at roomBridge
TROLL_GOAL = 1500
# Value multiplier compared to giving gold
TROLL_FUNNELCAKE_MULTIPLIER = PRICE_BUY_FUNNELCAKE * 2
TROLL_HALFFUNNELCAKE_MULTIPLIER = PRICE_BUY_FUNNELCAKE

# COURTYARD
LOOT_GATE_GOLD = 16
LOOT_S_GOLD = 7

# CARNIVAL
# Shell Game gold inventory at roomCarnivalShellGame
# Sybil goes out of business and shuts down tent if gold reaches 0.
SHELL_GOLD = 300
# Win multiplier in roomShellGame
SHELL_REWARD_MULTIPLIER = 2
# Percent added win chance for gambling per lucky rabbit foot
LUCKY_FOOT_MODIFIER = 100
# Funnel Cake limit
# Vendor can't sell anymore funnel cakes if you've reached limit
FUNNELCAKE_LIMIT = 50
# Raffle ticket reimbursement
#   How many turns raffle ticket can be exchanged at roomCarnival
RAFFLE_TIMER = 5
# Raffle ticket reward
RAFFLE_COMPENSATION = 200

# HOUSE
DIAL_START = "GREEN"
DIAL_ANSWER = "RED"
LEVER_START = "FORWARD"
LEVER_ANSWER = "BACKWARDS"

# Non-resetable varaibles
#   Caries on between lives
# Total game counters
# Continue between playthroughs of a single sitting'
## Testing out for duplicate strings here
# Sean Reynolds - Removed extra turnCounter initializations
turn_counter_total = 0
deaths_total = 0
# Ozkavosh spells
spell_learn = 0
spell_unlock = 0
spell_persuade = 0
spell_jump = 0
spell_light = 0
spell_heal = 0
spell_feed = 0
spell_kill = 0
spell_killself = 0
word_darkness = 0
word_reign = 0
word_stop = 0
word_servant = 0
word_mirror = 0
word_dominion = 0
word_curse = 0
spell_oblivion = 0

# Player name
# playerName = False



#_______Functions_______________________________________________________________

def demon_words():
    global spell_learn, spell_unlock, spell_persuade, spell_jump, spell_light
    global spell_heal, spell_feed, spell_kill, spell_killself, spell_oblivion
    global word_darkness, word_reign, word_stop, word_servant, word_mirror
    global word_dominion, word_curse

    # Dictionaries describing all words
    spells = {
        "Ozh ensh": (spell_learn, "I learn - Translates the meaning and effects of words from Ozkavosh."),
        "Ozh vo'ses sa": (spell_unlock, "I unlock this - Opens any lock."),
        "Izh vo'poz": (spell_persuade, "You have no power - Persuades those blocking the way."),
        "Ozh sol fek": (spell_killself, "My life ends - Kills self."),
        "Ozh thok alatho": (spell_jump, "I move forward - Crosses large gaps."),
        "Ozh groth sol": (spell_light, "I open the light - Creates a glowing ball that illuminates your surroundings."),
        "Eyik vo'hollom": (spell_oblivion, "Behold oblivion - Opens obsidian hemispheres."),
        "Ozh vo'irush": (spell_heal, "I am without illness - Mends all wounds and illnesses."),
        "Ozh gluth nith": (spell_feed, "I consume the Earth - Satisfies all hunger."),
        "Ozh gluth izh sol": (spell_kill, "I consume your soul - Kills your enemies.")
    }

    words = {
        "Omoz gloth izh - Darkness welcomes you.": word_darkness,
        "Izh tal el ozh icha rek'tal - Talk and I will mirror.": word_mirror,
        "Ahm'domosh - Highest dominion.": word_dominion,
        "Ozkavosh icha domosh sa nith - Demon-kind shall reign upon this land.": word_reign,
        "Izh icha vo'fek ozh domosh - You will not stop my reign.": word_stop,
        "Ahm'fol - Servant of Vesh'arkosh.": word_servant,
        "Sof izh - Curse you.": word_curse
    }

    # Unknown versions of non-spells (slight spelling differences preserved)
    unknown_words = {
        "Omoz gloth izh": word_darkness,
        "Izh tal et ozh icha rek'tal": word_mirror,
        "Ahm'domosh": word_dominion,
        "Ozkavosh icha domosh sa nith": word_reign,
        "Izh icha vo'fek ozh domosh": word_stop,
        "Ahm'fol": word_servant,
        "Sof izh": word_curse
    }

    # Check if nothing at all is known
    all_values = [
        spell_learn, spell_unlock, spell_persuade, spell_jump, spell_light,
        spell_heal, spell_feed, spell_kill, spell_killself, spell_oblivion,
        word_darkness, word_reign, word_stop, word_servant, word_mirror,
        word_dominion, word_curse
    ]

    if not any(all_values):
        print("You do not know any words in Ozhkavosh.")
        return

    # Known spells (status = 2)
    known_spells = {k: v for k, v in spells.items() if v[0] == 2}
    if known_spells:
        print("Spells:")
        for phrase, (status, desc) in known_spells.items():
            print(f"    {phrase}")
            print(f"\t{desc}")

    # Known non-spells (status = 2)
    known_words = {k: v for k, v in words.items() if v == 2}
    if known_words:
        print("Non-spells:")
        for line in known_words.keys():
            print(f"    {line}")

    # Unknown words (status = 1)
    unknown_items = {}

    # Unknown spells
    for phrase, (status, _) in spells.items():
        if status == 1:
            unknown_items[phrase] = True

    # Unknown non-spells
    for phrase, value in unknown_words.items():
        if value == 1:
            unknown_items[phrase] = True

    if unknown_items:
        print("Unknown:")
        for phrase in unknown_items.keys():
            print(f"    {phrase}")

def shortcuts():
    print("l - Look")
    print("x - Examine")
    print("i - Inventory")
    print("h - Examine Hunger")
    print("o - Current Objective")
    print("z - Wait")
    print("g - Again (Repeat previous action)")
    print("\nMovement:")
    print("n - Go North")
    print("e - Go East")
    print("w - Go West")
    print("s - Go South")
    print("u - Go Up")
    print("d - Go Down")


def reverse(option):
    output_list = []
    for character in option:
        output_list.insert(0,character)
    output_string = "".join(output_list)
    return output_string

def reverse_cap(option):
    return reverse(option)[0].upper() + reverse(option)[1:].lower()

# Main Menu
# Splash Screen
# All credit goes to:
#   http://www.chris.com/ascii/index.php?art=art%20and%20design/borders
#   http://patorjk.com/software/taag/
#
def menu():
    print("                                                                              .---.")
    print("                                                                             /  .  \ ")
    print("                    WELCOME TO...                                           |\_/|   |")
    print("                                                                            |   |  /|")
    print("  .-------------------------------------------------------------------------------' |")
    print(" /  .-.     _____  _   _  _____ _____ _____ _____   _____ _   _ _____ _____ _____   |")
    print("|  /   \   /  __ \| | | ||  ___|  ___/  ___|  ___| |  _  | | | |  ___/  ___|_   _|  |")
    print("| |\_.  |  | /  \/| |_| || |__ | |__ \ `--.| |__   | | | | | | | |__ \ `--.  | |    |")
    print("|\|  | /|  | |    |  _  ||  __||  __| `--. \  __|  | | | | | | |  __| `--. \ | |    |")
    print("| `---' |  | \__/\| | | || |___| |___/\__/ / |___  \ \/' / |_| | |___/\__/ / | |    |")
    print("|       |   \____/\_| |_/\____/\____/\____/\____/   \_/\_\\\___/\____/\____/  \_/    |")
    print("|       |         _____  _           ___  _  _        _    _           __           |")
    print("|       |        |_   _|| |_   ___  | _ \| |(_) __ _ | |_ | |_   ___  / _|          |")
    print("|       |          | |  | ' \ / -_) |  _/| || |/ _` || ' \|  _| / _ \|  _|          |")
    print("|       |          |_|  |_||_|\___| |_|  |_||_|\__, ||_||_|\__| \___/|_|            |")
    print("|       |              _  __           _     _ |___/               _                |")
    print("|       |             | |/ / __ _  ___| |_  | |__ __ _ __ __ __ _ | |               |")
    print("|       |             | ' < / _` |(_-<| ' \ | / // _` |\ V // _` || |               |")
    print("|       |             |_|\_\\\__,_|/__/|_||_||_\_\\\__,_| \_/ \__,_||_|               |")
    print("|       |                                                                          /")
    print("|       |-------------------------------------------------------------------------'")
    print("\       |" )
    print(" \     /                          A Text Adventure Game")
    print("  `---'")
    print()
    print("    1. Start Game        2. How to Play        3. About this Game        4. Quit")
    choice_made = False
    while not choice_made:
        option = input("\n\n\n\n> ").lower()
        if option in ("1","1.","start","start game","1. start game"):
            option = 1
            choice_made = True
        elif option in ("2","2.","how to play","2. how to play"):
            print("Type in commands to do stuff. See what works and what doesn't.")
            print("\nExample:")
            print("\n> get a 4.0 GPA")
            print("You cannot get that.")
            print("\n> drink eggnog")
            print("You drink the eggnog. It's like Christmas morning!")
            print("\n> give catnip to kitten")
            print("You give the catnip to the kitten, making it go crazy.")
            print("\n\n\nBesides that, there are some basic shortcut commands.\n")
            shortcuts()
            print("\nYou can recall these shortcuts in-game at any time by typing in \"help\".")
            # print("\n\n\nAlso, it's recommended to play in fullscreen.")
        elif option in ("3","3.","about","about game","about this game"):
            print("Version " + VERSION + "\n")
            print("Cheese Quest: The Plight of Kashkaval was developed by Evan Quan starting",DATE,"because he was bored and had a lot of free time.")
            # print("Cheese Quest: The Plight of Kashkaval was developed by Evan Quan from on Oct. 17, 2016 to " + DATE + ". The original motivation behind the game's creation was to complete an assignment for CPSC 231 (found here: http://pages.cpsc.ucalgary.ca/~tamj/2016/231F/assignments/assignment2/index.htm). It draws inspiration from a variety of other works including:\n    - Terry Jones' and Terry Gilliam's movie, \"Monty Python and the Holy Grail.\" (1975)\n    - Douglas Adams' and Steve Meretzky's text adventure game, \"Hitchhicker's Guide to the Galaxy.\" (1984)\n    - Irrational Games' first-person shooter, \"Bioshock\" (2007)\n    - Frictional Game's survival horror game, \"Amnesia: The Dark Descent.\" (2010)\n    - Bethesda Game Studio's open world RPG, \"The Elder Scrolls V: Skyrim.\" (2011)\n    - Blizzard's online CCG \"Heartstone.\" (2014)")
        elif option in ("4","4.","quit","4. quit","q"):
            option = 4
            choice_made = True
        elif option == "debug":
            password = getpass.getpass("Debug mode password: ").lower()
            if password == PASSWORD:# <= OH HI THERE. IF YOU CAN READ THIS, THIS IS THE PASSWORD TO DEBUG MODE
                choice_made = True
            else:
                print("Incorrect.")
        else:
            print("Select 1, 2, 3, or 4.")
    if option == 1:
        in_game(False)
    elif option == 4:
        print("Okay. Bye!")
    elif option == "debug":
        print("Type !debug to see all the debug commands.")
        in_game(True)
    else:
        print("Uh oh. You broke the game. :(")

# Repeat
def repeat():
    choice_made = False
    debug = False
    while not choice_made:
        option = input("What would you like to do?\n    1. Play Again\n    2. Return to Main Menu\n    3. Quit\n> ").lower()
        if option in ("1","play","play again"):
            choice_made = True
        elif option in ("2","return","menu","main menu","return to main menu"):
            choice_made = True
        elif option in ("3","quit","q"):
            choice_made = True
        elif option == "debug":
            password = getpass.getpass("Debug mode password: ").lower()
            if password == PASSWORD: # <= OH HI THERE. IF YOU CAN READ THIS, THIS IS THE PASSWORD TO DEBUG MODE
                choice_made = True
                debug = True
            else:
                print("Incorrect.")
        else:
            print("Select 1, 2, or 3.")
    if option in ("1","play","play again"):
        in_game(debug)
    elif option in ("2","return","menu","main menu","return to main menu"):
        menu()
    elif option in ("3","quit","q"):
        print("Okay. Bye!")
    elif debug:
        in_game(debug)
# In Game
def in_game(debug):
    global deaths_total,turn_counter_total,spell_learn,spell_unlock,spell_persuade,spell_jump,spell_light,spell_heal,spell_feed,spell_kill,spell_killself,spell_oblivion,word_darkness,word_reign,word_stop,word_servant,word_mirror,word_dominion,word_curse,player_name
    # Resetable constant/variables

    # Vault Answers
    vault_answer_1 = random.randint(0,9)
    vault_answer_2 = random.randint(0,9)
    vault_answer_3 = random.randint(0,9)
    vault_answer_4 = random.randint(0,9)

    # Vault Initial
    vault_initial_1 = random.randint(0,9)
    vault_initial_2 = random.randint(0,9)
    vault_initial_3 = random.randint(0,9)
    vault_initial_4 = random.randint(0,9)
    same = random.randint(1,4)
    # Two vault values are randomly set to the correct answer already
    if same == 1:
        vault_initial_1 = vault_answer_1
        vault_initial_3 = vault_answer_3
        while vault_initial_2 == vault_answer_2 or vault_initial_4 == vault_answer_4:
            vault_initial_2 = random.randint(0,9)
            vault_initial_4 = random.randint(0,9)
    elif same == 2:
        vault_initial_2 = vault_answer_2
        vault_initial_4 = vault_answer_4
        while vault_initial_1 == vault_answer_1 or vault_initial_3 == vault_answer_3:
            vault_initial_1 = random.randint(0,9)
            vault_initial_3 = random.randint(0,9)
    elif same == 3:
        vault_initial_1 = vault_answer_1
        vault_initial_4 = vault_answer_4
        while vault_initial_2 == vault_answer_2 or vault_initial_3 == vault_answer_3:
            vault_initial_2 = random.randint(0,9)
            vault_initial_3 = random.randint(0,9)
    elif same == 4:
        vault_initial_2 = vault_answer_2
        vault_initial_3 = vault_answer_3
        while vault_initial_1 == vault_answer_1 or vault_initial_4 == vault_answer_4:
            vault_initial_1 = random.randint(0,9)
            vault_initial_4 = random.randint(0,9)
#_______Player Information______________________________________________________
# Information about Player
    #_______Class Initialization - Objects - Reset
    # Stats
    class Stat(object):
        # def __init__(self, hunger = HUNGER_START, health = HEALTH_MAX, shield = 0, objectiveMain = 0, objectiveSecondary = [0], objectiveSecondaryBlock = [0]): 
        # Was changed due to dangerous default arg
        def __init__(self, hunger = HUNGER_START, health = HEALTH_MAX, shield = 0, objective_main = 0, objective_secondary = None, objective_secondary_block = None):
            if objective_secondary is None:
                objective_secondary = [0]
            if objective_secondary_block is None:
                objective_secondary_block = [0]
            self.hunger = hunger
            self.health = health
            self.healthmax = HEALTH_MAX
            self.shield = shield
            self.objective_main = objective_main
            self.objective_secondary = objective_secondary
            self.objective_secondary_block = objective_secondary_block
        def examine_hunger(self):
            if self.hunger <= 1:
                print("You are about to die from starvation.")
            elif self.hunger <= 3:
                print("You feel extremely hungry.")
            elif self.hunger <= 6:
                print("You feel very hungry.")
            elif self.hunger <= 9:
                print("You feel quite hungry.")
            elif self.hunger <= 20:
                print("You feel moderately hungry.")
            elif self.hunger <= 30:
                print("You feel a bit hungry.")
            elif self.hunger <= HUNGER_MAX:
                print("You feel satisfied.")
            else:
                print("\nYou feel full.")
        def examine_health(self):
            if self.health == 7:
                print("You are healthy.")
            elif self.health in range(2,7):
                print("You're bleeding out.")
            elif self.health == 1:
                print("You are about to die from your wounds.")
        def lower_hunger(self):
                self.hunger -= 1
        def lower_health(self):
            if self.shield:
                print("The effects of the potion of rejuvination protect you from harm.")
            else:
                self.health -= 1
        def lower_shield(self):
            if self.shield:
                self.shield -= 1
                if self.shield == 1:
                    print("\nYou feel the protective power of the potion of rejuvination dissipate.")
        def set_objective_main(self,option):
            if option > self.objective_main:
                self.objective_main = option
        def add_objective_secondary(self,option):
            if option not in self.objective_secondary_block:
                self.remove_objective_secondary.append(option)
                self.objective_secondary_block.append(option)
        def remove_objective_secondary(self,option):
            self.objective_secondary_block.append(option)
            if option in self.remove_objective_secondary:
                self.remove_objective_secondary.remove(option)
        def print_objective(self):
            # Main goal
            print("Main Objective:",end = "\n    - ")
            if self.objective_main == 0:
                print("Escape the jail cell")
            elif self.objective_main == 1:
                print("Get the staff of Garrotxa from the Temple of Garrotxa")
            elif self.objective_main == 2:
                print("Go through Mount Magna Mine to reach Eden von Roquefort's house")
            elif self.objective_main == 3:
                print("Get inside of Eden von Roquefort's house")
            elif self.objective_main == 4:
                print("Kill Eden von Roquefort")
            elif self.objective_main == 5:
                print("Kill Vesh'kathal the Deceiver")
            # Immediate problems to solve
            print("\nSecondary Objective:")
            if 0 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Have enough food to stay alive")
            if 1 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Find enough money to stay alive")
            if 2 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Buy a raffle ticket from the Wonderful Wheel of Mystery")
            if 3 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Give the raffle ticket to the spokesperson to get reimbursed")
            if 4 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Give the shrubbery to the guard at the town gate")
            if 5 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Get enough gold/funnel cakes to bypass the troll at the bridge")
                print("        - ",end="")
                print("Mine coal in Mount Magna")
                print("        - ",end="")
                print("Explore Mount Magna")
                print("        - ",end="")
                print("Complete tasks for people around Airedale")
                print("        - ",end="")
                print("Play Sybil's Shell Game at the Carnival")
            if 6 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Give the dragonstone to Tim the Enchanter")
            if 7 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Give the wooden bird to the stranger at the lake")
            if 8 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Learn the spell from the stone tablet at the lake")
            if 9 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Open the lockbox at the lake")
            if 10 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Unlock the vault door at the Mount Magna Mine entrance")
            if 11 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Find a way to get across the crevasse to reach the treasure chest in Mount Magna Mine")
            if 12 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Open the treasure chest in Mount Magna Mine")
            if 13 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Find a way to get through the rubble blocking the Temple of Garrotxa entrance")
            if 14 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Solve the ghostly figure's riddle")
            if 15 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Get past the black knight")
            if 16 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Escape the creature's lair")
            if 17 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Find a way to get into Eden von Roquefort's house without using spells")
            if 18 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Go into the obsidian hemisphere")
            if 19 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Solve the puzzle of the gargoyle")
            if 20 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Solve the puzzle of the coloured rooms")
            if 21 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Solve the puzzle to get through the metal door")
            if 22 in self.remove_objective_secondary:
                print("    - ",end="")
                print("Alternatively, give the staff of Garrotxa to Eden von Roquefort")


    ## good place to start making methods for repeated code
    
    #______Rooms____________________________________________________
    # Room information
    #	 Description
    #	 Adjacent Rooms
    #	 Check Adjacent Rooms
    #	 Items Present

    # Room
    # Sean Reynolds - Changed Room __init__ to have all proper variables types in place when called from Initialization
    class Room(object):
        def __init__(self, name = "name", gold = 0, letter = 0, key = 0, key_skeleton  = 0, pickaxe = 0, shrubbery = 0, funnel_cake = 0, half_funnel_cake = 0, foot = 0, porridge = 0, bowl = 0, lantern = 0, oil = 0, pie = 0, biscuit = 0, hook = 0, staff = 0, ticket = 0, coal = 0, potato = 0, bandage = 0, journal = 0, book = 0, brie = 0, munster = 0, stilton = 0, swiss = 0, wensleydale = 0, potion = 0, flask = 0, stone = 0, bird = 0, note = 0, memo = 0,
                     north: str | bool | None = False, north_blocked: bool = False, north_blocked_reason: str | bool | None = False,
                     east: str | bool | None = False, east_blocked: bool = False, east_blocked_reason: str | bool | None = False,
                     south: str | bool | None = False, south_blocked: bool = False, south_blocked_reason: str | bool | None= False,
                     west: str | bool | None = False, west_blocked: bool = False, west_blocked_reason: str | bool | None = False,
                     up: str | bool | None = False, up_blocked: bool = False, up_blocked_reason: str | bool | None = False,
                     down: str | bool | None = False, down_blocked: bool = False, down_blocked_reason: str | bool | None = False,
                     bet_made = False, counter_ans_1 = 0, counter_ans_2 = 0, counter_ans_3 = 0, counter_ans_4 = 0, counter_1 = 0, counter_2 = 0, counter_3 = 0, counter_4 = 0, character_dead = True, item_found = False, first_time = True, is_bet = False, is_buy = False, is_crevasse = False, is_give = False, is_mine = False, is_fill = False, is_sell = False):
            # Items
            self.name = name
            self.gold = gold
            self.letter = letter
            self.key = key
            self.key_skeleton = key_skeleton
            self.pickaxe = pickaxe
            self.shrubbery = shrubbery
            self.funnel_cake = funnel_cake
            self.half_funnel_cake = half_funnel_cake
            self.foot = foot
            self.porridge = porridge
            self.bowl = bowl
            self.lantern = lantern
            self.oil = oil
            self.pie = pie
            self.biscuit = biscuit
            self.hook = hook
            self.staff = staff
            self.ticket = ticket
            self.coal = coal
            self.potato = potato
            self.bandage = bandage
            self.journal = journal
            self.book = book
            self.brie = brie
            self.munster = munster
            self.stilton = stilton
            self.swiss = swiss
            self.wensleydale = wensleydale
            self.potion = potion
            self.flask = flask
            self.stone = stone
            self.bird = bird
            self.note = note
            self.memo = memo
            # Check Adjacent Rooms
            self.north = north
            self.north_blocked = north_blocked
            self.north_blocked_reason = north_blocked_reason
            self.east = east
            self.east_blocked = east_blocked
            self.east_blocked_reason = east_blocked_reason
            self.south = south
            self.south_blocked = south_blocked
            self.south_blocked_reason = south_blocked_reason
            self.west = west
            self.west_blocked = west_blocked
            self.west_blocked_reason = west_blocked_reason
            self.up = up
            self.up_blocked = up_blocked
            self.up_blocked_reason = up_blocked_reason
            self.down = down
            self.down_blocked = down_blocked
            self.down_blocked_reason = down_blocked_reason
            # Check if bet made
            # Applies only to betting rooms
            self.bet_made = bet_made
            # Room specific integer values
            # roomJailCorridor vault code
            # roomCarnival raffle return duration
            # roomCave coalmines coal amount
            self.counter_ans_1 = counter_ans_1
            self.counter_ans_2 = counter_ans_2
            self.counter_ans_3 = counter_ans_3
            self.counter_ans_4 = counter_ans_4
            self.counter_1 = counter_1
            self.counter_2 = counter_2
            self.counter_3 = counter_3
            self.counter_4 = counter_4
            # Troll dead
            # Applies only to roomBridge
            self.character_dead = character_dead
            # Item found
            # If action is done in room, item appears. If action is done again, more items do not appear.
            self.item_found = item_found
            # First time
            # Only applies to first time entering a room
            self.first_time = first_time
            # Room Type
            self.is_bet = is_bet
            self.is_buy = is_buy
            self.is_crevasse = is_crevasse
            self.is_give = is_give
            self.is_mine = is_mine
            self.is_fill = is_fill
            self.is_sell = is_sell
        # Description
        def description(self):
            print("\nRoom Name\n\nDescription placeholder.\n")
            # Adjacent Rooms
            print("North is north room.")
            print("East is east room.")
            print("South is south room.")
            print("West is west room.")
        def item_types(self):
            type_count = 0
            if self.gold:
                type_count += 1
            if self.letter:
                type_count += 1
            if self.key:
                type_count += 1
            if self.key_skeleton:
                type_count += 1
            if self.pickaxe:
                type_count += 1
            if self.shrubbery:
                type_count += 1
            if self.funnel_cake:
                type_count += 1
            if self.half_funnel_cake:
                type_count += 1
            if self.foot:
                type_count += 1
            if self.porridge:
                type_count += 1
            if self.bowl:
                type_count += 1
            if self.lantern:
                type_count += 1
            if self.oil:
                type_count += 1
            if self.pie:
                type_count += 1
            if self.biscuit:
                type_count += 1
            if self.hook:
                type_count += 1
            if self.staff:
                type_count += 1
            if self.ticket:
                type_count += 1
            if self.coal:
                type_count += 1
            if self.potato:
                type_count += 1
            if self.bandage:
                type_count += 1
            if self.journal:
                type_count += 1
            if self.book:
                type_count += 1
            if self.brie:
                type_count += 1
            if self.munster:
                type_count += 1
            if self.stilton:
                type_count += 1
            if self.swiss:
                type_count += 1
            if self.wensleydale:
                type_count += 1
            if self.potion:
                type_count += 1
            if self.flask:
                type_count += 1
            if self.stone:
                type_count += 1
            if self.bird:
                type_count += 1
            if self.note:
                type_count += 1
            if self.memo:
                type_count += 1
            return type_count
        def items_present(self):
            # Items Present
            if self.item_types():
                if self.item_types() > 1:
                    print("\nThere are some items here:")
                else:
                    print("\nThere is an item here:")
            if self.bandage == 1:
                print("    a bandage")
            elif self.bandage > 1:
                print("   ",self.bandage,"bandages")
            if self.porridge:
                print("    a bowl of porridge")
            if self.bowl:
                print("    a bowl")
            if self.pie == 1:
                print("    a chicken pot pie")
            elif self.pie > 1:
                print("   ",self.pie,"chicken pot pies")
            if self.stone:
                print("    a dragonstone")
            if self.flask == 1:
                print("    a flask")
            elif self.flask > 1:
                print("   ",self.flask,"flasks")
            if self.funnel_cake == 1:
                print("    a funnel cake")
            elif self.funnel_cake > 1:
                print("   ",self.funnel_cake,"funnel cakes")
            if self.gold:
                print("   ",self.gold,"gold")
            if self.hook == 1:
                print("    a grappling hook")
            elif self.hook > 1:
                print("   ",self.hook,"grappling hooks")
            if self.half_funnel_cake == 1:
                print("    a half-eaten funnel cake")
            elif self.half_funnel_cake > 1:
                print("   ",self.half_funnel_cake,"half-eaten funnel cakes")
            if self.biscuit == 1:
                print("    a hardtack biscuit")
            elif self.biscuit > 1:
                print("   ",self.biscuit,"hardtack biscuits")
            elif self.journal == 1:
                print("    a journal")
            elif self.journal > 1:
                print("   ",self.journal,"journals")
            if self.key:
                print("    a key")
            if self.key_skeleton:
                print("    the key of Ahm'domosh")
            if self.lantern == 1:
                print("    a lantern")
            elif self.lantern > 1:
                print("   ",self.lantern,"lanterns")
            if self.letter:
                print("    a letter")
            if self.foot == 1:
                print("    a lucky rabbit foot")
            elif self.foot > 1:
                print("   ",self.foot,"lucky rabbit feet")
            if self.memo:
                print("    a memo")
            if self.book == 1:
                print("    a mysterious book")
            elif self.book > 1:
                print("   ",self.book,"mysterious books")
            if self.note:
                print("    a note")
            if self.pickaxe == 1:
                print("    a pickaxe")
            elif self.pickaxe > 1:
                print("   ",self.pickaxe,"pickaxes")
            if self.coal == 1:
                print("    a piece of coal")
            elif self.coal > 1:
                print("   ",self.coal,"pieces of coal")
            if self.potato:
                print("    a rotten potato")
            if self.potion == 1:
                print("    a potion of rejuvination")
            elif self.potion > 1:
                print("   ",self.potion,"potions of rejuvination")
            if self.ticket:
                print("    a raffle ticket")
            if self.shrubbery == 1:
                print("    a shrubbery")
            elif self.shrubbery > 1:
                print("   ",self.shrubbery,"shrubberies")
            if self.brie:
                print("    a slice of brie cheese")
            if self.munster:
                print("    a slice of munster cheese")
            if self.stilton:
                print("    a slice of stilton cheese")
            if self.swiss:
                print("    a slice of swiss cheese")
            if self.wensleydale:
                print("    a slice of wensleydale cheese")
            if self.staff:
                print("    the staff of Garrotxa")
            if self.oil == 1:
                print("    a vial of lantern oil")
            elif self.oil > 1:
                print("   ",self.oil,"vials of lantern oil")
            elif self.bird:
                print("    a wooden bird")

    #Very good place to use a method again lol
    #_______Jail____________________________________________________________________
    # Cell
    class ClassJailCell(Room):
        # Description
        def description(self):
            print("\nJail Cell\n\nThere are stone walls enclosed around you.\nThere is a solid metal door with a small slit at eye-level peering into the corridor.\nThere is a HAYSTACK here.\n")
            # Adjacent Rooms
            print("    East is the corridor.")
    # Corridor
    class ClassJailCorridor(Room):
        # Description
        def description(self):
            print("\nCorridor\n\nJail cells line the the hallway on both sides.\n")
            # Adjacent Rooms
            print("    North is the antechamber.")
            print("    West is is your jail cell.")
    # Antechamber
    class ClassJailAntechamber(Room):
        def description(self):
            print("\nAntechamber\n\nThe stone walls are close together, leaving just enough room for you to stand in.\n")
            print("    Down is the foyer.")
            print("    South is the corridor.")
    # Foyer
    class ClassJailFoyer(Room):
        # Description
        def description(self):
            print("\nFoyer\n\nThe place is rather cozy and well-lit. Definitely a contrast from all those years in your cell.\n")
            # Adjacent Rooms
            print("    Up is the antechamber.")
            print("    East is the hallway.")
            print("    West is outside.")
    # Hallway
    class ClassJailHallway(Room):
        # Description
        def description(self):
            print("\nHallway\n\nLight from outside pears in from the Northern windows. This is the first time you've felt sunlight in ages.\n")
            # Adjacent Rooms
            print("    East to the break room.")
            print("    West is inside the jail.")
    # Break Room
    class ClassJailBreakRoom(Room):
        # Description
        def description(self):
            print("\nBreak Room\n\nThere's some comfortable chairs and tables scattered around the room.\n")
            # Adjacent Rooms
            print("    West is the hallway.")
            print("    South is the washroom.")
    # Entrance
    class ClassJailEntrance(Room):
        # Description
        def description(self):
            if self.first_time:
                first_time = "Finally, outside! This is the first time you've felt sunlight in ages. "
            else:
                first_time = ""
            print("\nJail Entrance\n\n%sA wall surrounds the prison from all sides, with a gate leading north.\n" % first_time)
            # Adjacent Rooms
            print("    East is the foyer.")
            print("    West is the courtyard.")
    #_______Town____________________________________________________________________
    # Courtyard
    class ClassCourtyardNorth(Room):
        # Description
        def description(self):
            if self.first_time:
                first_time = "A young urchin boy rings a bell, yelling \"Come one, come all, to the WONDERFUL WHEEL OF MYSTERY! Short on cash? Want to get rich quick? Spin the wheel and test your luck! Only at the AIREDALE CARNIVAL!\""
            elif room_carnival_wheel_game.character_dead:
                first_time = ""
            else:
                first_time = "A young urchin boy rings a bell, yelling \"The WONDERFUL WHEEL OF MYSTERY will be announcing the winner soon! Get your TICKET while you can!\""
            print("\nNorth Courtyard\n\nA crowd of people fill the streets.\nVarious buildings surround the courtyard from every angle.\n" + first_time + "\n")
            # Adjacent Rooms
            print("    North is the town gate.")
            print("    East is the general store.")
            print("    West is the carnival grounds.")
            print("    South is the south courtyard.")
    class ClassCourtyardSouth(Room):
        # Description
        def description(self):
            print("\nSouth Courtyard\n\nA large elegant fountain rests in the centre, surrounded by busy people minding their own business.\n")
            # Adjacent Rooms
            print("    North is the north courtyard.")
            print("    East is the jail entrance.")
            print("    West is the blacksmith.")
            print("    South is the alchemist's hut.")
    # Blacksmith
    class ClassBlacksmith(Room):
        # Description
        def description(self):
            print("\nBlacksmith\n")
            if self.character_dead:
                print("There is a charred body here.\nAn open furnace lights up the place and several tools lay on an adjacent table.")
            else:
                print("A man in an apron rests at stand near the entrance.\nBehind him, an open furnace lights up the place and several of his tools lay on an adjacent table.")
                if self.first_time:
                    print("\"You new here mate? Don't recognize the face. Buy anything here you'd like. Ever since the incident at the MOUNT MAGNA MINE, I've been running low on COAL to keep my furnace going. However, if you've got the guts to go up there, I'd be willing to buy any off from you.\"")
                else:
                    print("\"Y'here to buy anything? If not, I'd be willin' to buy any COAL off you. In times like these, I could always use some more fuel for my fire.\"")
                print("\nGoods available to buy:\n    Pickaxe (%s gold)\n    Grappling Hook (%s gold)" % (PRICE_BUY_PICKAXE,PRICE_BUY_HOOK))
                print("\nGoods available to sell:\n    Coal (%s gold)" % PRICE_SELL_COAL)
            if self.is_buy:
                print("\nYou have",inv.gold,"gold.")
                if inv.coal > 1:
                    print("You have",inv.coal,"pieces of coal.")
                elif inv.coal:
                    print("You have",inv.coal,"piece of coal.")
            # Adjacent Rooms
            print("\n    East is the courtyard.")
    # Alchemist
    class ClassAlchemist(Room):
        def description(self):
            print("\nAlchemist's Hut\n")
            if self.character_dead:
                dead = "The dead body of Tim the Enchanter is here."
            else:
                dead = "An old man, wearing black robes and a leather cap with goat horns wanders around from shelf to shelf, examining various strange ingredients."
            if self.first_time:
                first_time = "\"Sorry, the shop is closed. I ran out of crushed dragonstone powder, a very rare and expensive ingredient necessary for all my potions. If you could find me a DRAGONSTONE, I would be willing to buy it off from you, and I'll be able to start up my business again. How does %s gold sound? Oh, I almost forgot to introduce myself. I'm Tim. Tim the Enchanter.\"" % PRICE_SELL_STONE
            else:
                if self.is_buy:
                    first_time = "\"Come on in. The fire's roaring. Business has been going great since you got me that dragonstone. What can I get for you?\""
                else:
                    first_time = "\"Hello again. I'm still empty on crushed dragonstone powder so I won't be able to make any potions. If you have a dragonstone, the offer is still on.\""
            if self.is_buy:
                buy = "filled with a bubbling, red liquid, rests above hot coals."
            else:
                buy = "rests above an fire, filled only with water."
            print("A large, cast-iron cauldron " + buy + "\n" + dead + " \n" + first_time)
            if self.is_buy: # and self.isFill:
                outofstock = ""
            else:
                outofstock = " [OUT OF STOCK]"
            if not self.character_dead:
                print("\nGoods available to buy:\n    Potion of rejuvination (%s gold)%s" % (PRICE_BUY_POTION,outofstock))
                print("\nGoods available to fill:\n    Flask (%s gold)%s" % (PRICE_REFILL_POTION,outofstock))
            if self.is_sell:
                print("\nGoods available to sell:\n    Dragonstone (%s gold)" % PRICE_SELL_STONE)
            if self.is_buy:
                print("\nYou have",inv.gold,"gold.")
            print("\n    North is the courtyard.")
    # Town Gate
    class ClassGate(Room):
        # Description
        def description(self):
            if self.north_blocked:
                if self.first_time:
                    first_time = "\"Hey you there!\" says one of the guards as he approachs you. He looks around cautiously before lowering his voice.\n\"I recognize you! You were locked up years ago, you rat! I'd call for more guards to take you back to your cell, but I need something. You're a good thief and I'm sure you have a good eye.\nA while back, I lost a SHRUBBERY somewhere in this town.\nRetrieve it for me: one that looks nice and not too expensive, and I'll let you through the gate.\""
                else:
                    first_time = "\"Don't think you can get pass the gate until I get that SHRUBBERY. Try any funny business and I'll send you back to your cell.\""
            else:
                first_time = "He recognizes you and opens it."
            print("\nTown Gate\n\nA guard stands at the gate.", first_time)
            # Adjacent Rooms
            print("\n    North is a pathway.")
            print("    South is the courtyard.")
    # General Store
    class ClassGeneralStore(Room):
        # Description
        def description(self):
            print("\nGeneral Store\n")
            if self.character_dead:
                print("There is a charred body on the floor.")
            else:
                if self.first_time:
                    welcome = "Welcome to my shop, little human. I have goods. You have money. We make deal."
                else:
                    welcome = "I see you have returned little human. Welcome back."
                print("The shopkeeper welcomes you in the his store. \"%s\"" % welcome)
                print("\nGoods available to buy:\n    Lucky Rabbit Foot (%s gold)\n    Lantern (%s gold)\n    Vial of Lantern Oil (%s gold)\n    Bandage (%s gold)" % (PRICE_BUY_FOOT,PRICE_BUY_LANTERN,PRICE_BUY_OIL,PRICE_BUY_BANDAGE))
            if self.is_buy:
                print("\nYou have",inv.gold,"gold.")
            # Adjacent Rooms
            print("\n    West is the courtyard.")
    # Carnival
    class ClassCarnival(Room):
        # Description
        def description(self):
            if self.south_blocked:
                s_closed = "Closed: Out of Business"
            else:
                s_closed = "Sybil\'s Shell Game"
            if self.west_blocked:
                w_closed = "FRAUD"
            else:
                w_closed = "Mystery"
            print("\nCarnival Grounds\n\nFestival lights are strung above, with colourful banners swaying in the wind.\nA large party of adults and children alike fill the carnival grounds, bustling about from tent to tent.")
            if self.is_give:
                print("The spokesperson is sitting outside at a table with two guards.\nA crowd of people surround her, GIVING her their raffle tickets.")
            print('\n    North is a tent labelled, "Funnel Cakes Galore."')
            print("    East is the courtyard.")
            print('    West is a tent labelled, "The Wonderful Wheel of %s."' % w_closed)
            print('    South is a tent labelled, "%s."' % s_closed)
    # Carnival Shell Game
    class ClassCarnivalShellGame(Room):
        def description(self):
            print("\nSybil\'s Shell Game")
            if self.is_bet:
                print("\nInside the tent is an old woman hunched at a small, fragile wooden table.")
                if self.bet_made:
                    print("\nShe is waiting for you to chose a shell.")
                else:
                    print('With only one eye, she turns to you and begins to chant.\n"Hear ye, hear ye! BET if you wish some GOLD out of glee! Test your LUCK with a guess from these shells three! Double your money if you win, you shall see!"')
            elif not self.character_dead:
                print("\nSybil is packing her stuff to leave the carnival.")
            else:
                print("\n    Inside the tent is a charred body on the ground, behind a fragile wooden table.")
            if self.is_bet:
                print("\nYou have",inv.gold,"gold.")
            print("\n    North is the carnival grounds.")
    # Carnival Food
    class ClassCarnivalFood(Room):
        # Description
        def description(self):

            print("\nFunnel Cakes Galore\n")
            if self.character_dead:
                
                print("There is a charred body here, lying by a stovetop.")
            else:
                if inv_food.funnel_cake <= 0:
                    menu = "\nGoods available to buy:\n    Chicken pot pie (%i gold)" % PRICE_BUY_PIE
                else:
                    menu = "\nGoods available to buy:\n    Funnel cake (%i gold)\n    Chicken pot pie (%i gold)" % (PRICE_BUY_FUNNELCAKE,PRICE_BUY_PIE)
                print("\nInside the tent is an older overweight vendor at a stovetop, cooking up funnel cakes.")
                if self.first_time:
                    print('\n"Funnel cakes! Get your funnel cakes here!" he shouts with joy. "Enjoying the carnival so far? What better way to brighten your day with some freshly fried funnel cakes at Funnel Cakes Galore! Oh, we also sell pies here too, but no one these days are looking to buy pies at a carnival.')
                else:
                    if inv_food.funnel_cake > 0:
                        if inv_food.funnel_cake < FUNNELCAKE_LIMIT / 2:
                            print("\n\"Oh look, it's you again. You seem to be really liking those funnel cakes. You know, I only have so much batter for today. I didn't really expect you to buy so many.\"")
                        elif inv_food.funnel_cake < FUNNELCAKE_LIMIT:
                            print("\n\"You're here to buy more funnel cakes? They're delicious, I know!\"")
                        else:
                            print("\n\"Good seeing you again. Change your mind of buying some mighty fine funnel cakes?\"")
                    else:
                        print("\n\"I'm all out of funnel cake batter. You can still buy some pies if you want.\"")
            print(menu)
            if self.is_buy:
                print("\nYou have",inv.gold,"gold.")
            print("\n    South is the carnival grounds.")
    class ClassCarnivalWheelGame(Room):
        # Description
        def description(self):
            print("\nWonderful Wheel of Mystery\n\nInside the tent is a large elevated platform.\nDisplayed in the centre is a large wheel with various numbers on it.")
            if self.character_dead:
                print("The rest of the place is empty.")
            else:
                if self.first_time:
                    first_time = "Get your tickets here. Only %s gold each. Winner gets 100,000 gold and their own personal yacht. We'll be drawing today's winner in just a couple of minutes! Last chance to get your tickets!" % PRICE_BUY_TICKET
                else:
                    first_time = "Last chance to get your tickets. Today's winner will be announced soon!"
                print("A large crowd of people are all gathered around it, waving bags of gold in their hands. A man with a top hat, is collecting gold from the people nearest to him as he hands out raffle tickets in return. \"%s\"" % first_time)
                print("\nGoods available to buy:\n    Raffle ticket (%i gold)" % PRICE_BUY_TICKET)
            if self.is_buy:
                print("\nYou have",inv.gold,"gold.")
            print("\n    East is the carnival grounds.")

    #_______Outside____________________________________________________________________
    # Road
    class ClassRoadSouth(Room):
        def description(self):
            print("\nRoad\n\nThe gravel path extends out into the forest. Pine trees hug the path closely on both ends.")
            print("\n    North is a crossroads.")
            print("    South is the town gate.")
    class ClassRoadMid(Room):
        def description(self):
            if self.item_found:
                north_d = "Mount Magna."
                east_d = "Temple of Garrotxa."
                west_d = "Lake Laguiole."
            else:
                north_d = "a road."
                east_d = "a road."
                west_d = "a road."
            print("\nCrossroads\n\nFour paths meet here. There is a SIGN you can READ here.")
            print("\n    North is",north_d)
            print("    East is",east_d)
            print("    West is",west_d)
            print("    South is the town of Airedale.")
    class ClassRoadNorth(Room):
        def description(self):
            print("\nRoad\n\nThe gravel path extends out into the forest. Pine trees hug the path closely on both ends.")
            print("\n    North is Mount Magna.")
            print("    South is a crossroads.")
    class ClassRoadEast(Room):
        def description(self):
            print("\nRoad\n\nThe gravel path extends out into the forest. Pine trees hug the path closely on both ends.")
            print("\n    East is is a bridge.")
            print("    West is a crossroads.")
    class ClassRoadWest(Room):
        def description(self):
            print("\nRoad\n\nThe gravel path extends out into the forest. Pine trees hug the path closely on both ends.")
            print("\n    East is a crossroads.")
            print("    West is a lake.")
    class ClassRoadCorner(Room):
        def description(self):
            if not self.character_dead and self.counter_1:
                black_knight = " A knight, outfitted in black platemetal armour and equipped with a large broadsword stands in the way. He stands quietly."
            else:
                black_knight = ""
            print("\nRoad\n\nThe gravel path extends out into the forest. Pine trees hug the path closely on both ends.%s" % black_knight)
            print("\n    North is a temple.")
            print("    East is an opening in the forest.")
            print("    West is a bridge.")
    class ClassForest(Room):
        def description(self):
            if self.east_blocked:
                blocked = " The surface has no distinguishing features."
            else:
                blocked = " An opening leads inside."
            print("\nForest\n\nIn the middle of the foliage is a large obsidian hemisphere.%s\n" % blocked)
            print("    West is a road.")
            if not self.east_blocked:
                print("    East is inside the obsidian hemisphere.")
    # Lake
    class ClassLake(Room):
        def description(self):
            if self.first_time:
                first_time = "A stranger lies by the shoreline.\n\"Hey you there! I lost my precious WOODEN BIRD in the MOUNT MAGNA MINE before it was locked down. If you could somehow get in there and GIVE me my bird back, I will surely make it worth your while. Please, I beg of you!\""
            elif self.character_dead:
                first_time = "A dead body lies by the shoreline."
            elif not self.is_give:
                first_time = "A stranger lies by the shoreline, happy to have his wooden bird back."
            else:
                first_time = "A stranger lies by the shoreline. \"Are you back with my WOODEN BIRD from MOUNT MAGNA? I'll make it worth your while.\""
            print("\nLake Laguiole\n\nThe sun shimmers off the lake's surface.\nThere is a LOCKBOX here.\nThere is a STONE TABLET you can READ here.\n" + first_time)
            print("\n    East is the crossroads.")
    # Woods
    class ClassShrineSouth(Room):
        def description(self):
            if self.first_time and room_shrine_north.first_time:
                first_time = " A voice echoes within the chamber, \"Omoz... gloth... izh...\""
            else:
                first_time = ""
            print("\nSouth Shrine\n\nSteps lead down to a circular pit, shallowly filled with water.\nAround the edges of the room, floating candles dimly light the area.\nAlong the North wall is a MYSTICAL PORTAL." + first_time + "\n")
            print("    North is through the portal.")
            print("    West is outside.")
    # Bridge
    class ClassBridge(Room):
        def description(self):
            print("\nBridge\n\nThe wooden bridge stretches across a river.",end = " ")
            if self.first_time:
                first_time = "He notices you, and says \"Bridge is home of Ugg. Ugg want funnel cakes. Ugg need gold to buy funnel cakes. Ugg no let you pass unless you GIVE Ugg GOLD or FUNNEL CAKES.\nUgg need %s gold to be happy.\nIf you give Ugg funnel cakes, that will be like giving Ugg %s gold each because it take a lot of work for Ugg to go buy funnel cakes.\"" % (TROLL_GOAL - inv_troll.gold,TROLL_FUNNELCAKE_MULTIPLIER)
            else:
                first_time = "He reminds you, \"Ugg need %s GOLD before you can pass. You can GIVE Ugg FUNNEL CAKES too, which count as %s gold each.\"" % (TROLL_GOAL - inv_troll.gold,TROLL_FUNNELCAKE_MULTIPLIER)
            if self.east_blocked:
                print("There is a troll standing on it, blocking the way. %s" % first_time)
            elif not self.character_dead:
                print("The troll is happily sitting under the bridge, excited to see how many funnel cakes he can buy.")
            else:
                print("The body of the troll lays on the bridge, leaving some room to step over and across the other side.")
            if self.east_blocked:
                print("\nYou have",inv.gold,"gold.")
                if inv.funnel_cake > 1:
                    print("You have",inv.funnel_cake,"funnel cakes.")
                elif inv.funnel_cake:
                    print("You have",inv.funnel_cake,"funnel cake.")
            print("\n    East is the crossroads.")
            print("    West is a road.")

    # Temple
    class ClassTempleEntrance(Room):
        def description(self):
            if self.north_blocked:
                rubble = ", blocked by RUBBLE"
            else:
                rubble = ""
            print("\nTemple Entrance\n\nWhite marble pillars support the temple roof, which is embellished with gold.\nA large stairway leads up towards the doorway entering the temple.\nA hedge surrounds the temple from the back and sides.\n")
            print("    North is inside the temple%s." % rubble)
            print("    South is a road.")
    class ClassTempleInside(Room):
        def description(self):
            print("\nTemple\n\nA velvet carpet extends from the entrance to a pedestal in the center of the room.\nAt the back is a large statue of the goddess, Garrotxa, overlooking the room.\nThree MURALS you can READ with embroided text are laid out, spanning across the West, North, and East walls.\n")
            print("    Down is the antechamber.")
            print("    South is outside.")
    class ClassTempleBasement(Room):
        def description(self):
            if self.staff:
                staffpresent = "A gem-encrusted staff rests on a stand atop it."
            else:
                staffpresent = "An empty stand sits on top of it."
            if not self.character_dead:
                if self.first_time:
                    first_time = "A ghostly figure stands in the way.\nIt says, \"The staff of Garrotxa stands before you. Only those who can answer my riddle are worthy to take it.\"\nIt pauses to speak again.\"%s\"" % self.counter_1
                else:
                    first_time = "A ghostly figure stands in the way.\nIt repeats the riddle, \"%s\"" % self.counter_1
            else:
                first_time = ""
            print("\nInner Sanctum\n\nTorches line the walls of a stone hallway.\nAt the end sits a pedestal. " + staffpresent + "\n" + first_time)
            print("\n    Up is the ground floor.")

    #_______The Cavern______________________________________________________________
    # Entrance
    # debug cave names
    class ClassMountEntrance(Room):
        def description(self):
            print("\nCoal Mine Entrance\n\nMount Magna towers above, casting a shadow onto the land below.\nThere is a DEAD BODY here.\nThere is a SIGN you can READ here.\nThere is a vault door North, with a combination lock.\nFour large dials, each set to a number from 0 to 9 are displayed on the vault.\n\nThe first dial reads %i.\nThe second dial reads %i.\nThe third dial reads %i.\nThe fourth dial reads %i.\n" % (self.counter_1, self.counter_2, self.counter_3, self.counter_4))
            print("    North is inside the mine.")
            print("    South is the crossroads.")
    # 1
    class ClassCave1M(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    South is outside.")
    # 2
    class ClassCave2M(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    West is an opening.")
            print("    South is an opening.")
    class ClassCave2Mr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    West is an opening.")
    class ClassCave2Lm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.\n")
            print("    North is an opening.")
            print("    East is an opening.")
            print("    West is an opening.")
    class ClassCave2Llm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.\nThere is a DEAD BODY here.")
            print("\n    North is an opening.")
            print("    East is an opening.")
    # 3
    class ClassCave3MCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veinss lined along the cavern wall.")
            print("\n    North is an opening.")
    class ClassCave3Mr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    East is an opening.")
            print("    South is an opening.")
    class ClassCave3MrrCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veins lined along the cavern wall.")
            print("\n    West is an opening.")
    class ClassCave3LmCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veins lined along the cavern wall.")
            print("\n    South is an opening.")
    class ClassCave3LlmCrevasse(Room):
        def description(self):
            if self.west_blocked:
                hook = ""
            else:
                hook = " with a grappling hook spanning across it"
            print("\nCavern\n\nCold stone surrounds you in every direction.\nYou can see a TREASURE CHEST to the West.")
            print("\n    North is an opening.")
            print("    West is a crevasse%s." % hook)
            print("    South is an opening.")
    class ClassCave3LllmTreasureCrevasse(Room):
        def description(self):
            if self.east_blocked:
                hook = ""
            else:
                hook = " with a grappling hook spanning across it"
            if self.item_found:
                chest = "n open"
            else:
                if self.counter_1:
                    chest = " closed"
                else:
                    chest = " locked"
            print("\nCavern\n\nCold stone surrounds you in every direction.\nThere is a%s TREASURE CHEST here." % chest)
            print("\n    East is a crevasse%s." % hook)
    # 4
    class ClassCave4M(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    East is an opening.")
            print("    West is an opening.")
            print("    South is an opening.")
    class ClassCave4Mr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.\nThere is some strange TEXT on written on one of the walls.\n")
            print("    West is an opening.")
            print("    South is an opening.")
    class ClassCave4Lm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.\n")
            print("    North is an opening.")
            print("    East is an opening.")
            print("    West is an opening.")
    class ClassCave4Llm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    East is an opening.")
            print("    South is an opening.")
    # 5
    class ClassCave5M(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    East is an opening.")
            print("    South is an opening.")
    class ClassCave5MrCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veins lined along the cavern wall.")
            print("\n    West is an opening.")
    class ClassCave5LmCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veins lined along the cavern wall.")
            print("\n    South is an opening.")
    class ClassCave5Llm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    West is an opening.")
            print("    South is an opening.")
    class ClassCave5Lllm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    East is an opening.")
    # 6
    class ClassCave6M(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.\nThere is a DEAD BODY here.")
            print("\n    South is an opening.")
            print("    East is an opening.")
    class ClassCave6Mr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    West is an opening.")
    class ClassCave6LmCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veins lined along the cavern wall.")
            print("\n    North is an opening.")
    class ClassCave6LlmCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veins lined along the cavern wall.")
            print("\n    West is an opening.")
    class ClassCave6Lllm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.\nThere is a DEAD BODY here.")
            print("\n    North is an opening.")
            print("    East is an opening.")
            print("    South is an opening.")
    # 7
    class ClassCave7M(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    West is an opening.")
    class ClassCave7Mr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    West is an opening.")
            print("    South is an opening.")
    class ClassCave7Lm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    West is an opening.")
            print("    South is an opening.")
    class ClassCave7Llm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    East is an opening.")
            print("    West is an opening.")
    class ClassCave7Lllm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    South is an opening.")
    # 8
    class ClassCave8MrCrevasse(Room):
        def description(self):
            if self.north_blocked:
                hook = ""
            else:
                hook = " with a grappling hook spanning across it"
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is a crevasse%s." % hook)
            print("    South is an opening.")
    class ClassCave8LlmCoalmine(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            if self.counter_1:
                print("There are COAL veins lined along the cavern wall.")
            print("\n    South is an opening.")
    # 9
    # Creature cannot naturally spawn here.
    # If creature chase, then creature retreats (cannot pass crevasse)
    class ClassCave9MrCrevasse(Room):
        def description(self):
            if self.north_blocked:
                rubble = "The tunnel has collapsed North.\n"
            else:
                rubble = "\n"
            if self.south_blocked:
                hook = ""
            else:
                hook = " with a grappling hook spanning across it"
            print("\nCavern\n\nCold stone surrounds you in every direction.",rubble)
            if not self.north_blocked:
                print("    North is an opening.")
            print("    South is a crevasse%s." % hook)
    # 10
    # Chase rooms after crossing crevasse
    class ClassCave10Mr(Room):
        def description(self):
            if self.south_blocked:
                rubble = ", blocked by RUBBLE"
            else:
                rubble = ""
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    West is an opening.")
            print("    South is an opening%s." % rubble)
    class ClassCave10Mrr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    West is an opening.")
    class ClassCave10M(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    East is an opening.")
            print("    West is an opening.")
    class ClassCave10Mrrr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    West is an opening.")
    class ClassCave10Lm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    East is an opening.")
    # 11
    class ClassCave11Lm(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    South is an opening.")
    class ClassCave11Mrrr(Room):
        def description(self):
            print("\nCavern\n\nCold stone surrounds you in every direction.")
            print("\n    North is an opening.")
            print("    South is an opening.")
    # Darkness
    class ClassDarkness(Room):
        def description(self):
            print("\nDarkness\n\nYou feel nothing.")
    # Lair
    # Have lots of stuff to examine
    #   Shrine to Vesh'kathal
    #   markings on wall?
    class ClassLairMid(Room): # body here with lantern oil, biscuits
        def description(self):
            print("\nLair\n\nAn obsidian fountain sits in the centre, spewing a mysterious purple fluid.\nFour gargoyle statues from the corners of the room look inward towards the fountain, perched upon stone pedestals.\nYour BACKPACK and the CREATURE are visible within the rubble.\nThere is a DEAD BODY here.") # contains biscuits to prevent starve (hunger set low after waking up)
            print("\n    East is a doorway.") # leads to exit
            print("    West is a doorway.") # leads to drop puzzle and supplies in more bodies (include bandage for escape hit, pick for mining rock, more food for after escape)
            print("South is an opening, blocked by RUBBLE.")
    class ClassLairEast(Room):
        def description(self):
            if self.north_blocked:
                rubble = ", blocked by RUBBLE. Light from the outside peers through the cracks"
            else:
                rubble = ""
            if self.first_time:
                eyes = "closed"
            else:
                eyes = "open"
            print("\nLair\n\nStrange TEXT is etched across the walls. A single gargoyle statue is perched on a pedestal. Its eyes are %s." % eyes)
            print("\n    North is an opening%s." % rubble)
            print("    West is a doorway.")
    class ClassLairWest(Room): # body here with bandages, lantern
        def description(self):
            print("\nLair\n\nA skeleton lies on an elongated table, stained with old blood.")
            print("\n    East is a doorway.")
            print("    South is a small opening.")
    class ClassLairHole(Room): # get pickaxe here, only if carrying 1 thing in travel both ways
        def description(self):
            print("\nLair\n\nCold stone surrounds you in every direction. The space is extremely cramped.\nThere is a DEAD BODY here.\n")
            print("    North is a small opening.")
    # Fermiere
    class ClassRoad2South(Room):
        def description(self):
            print("\nRoad\n\nThe dirt path extends out on the field. The shadow of Mount Magna towers from the south.\n")
            print("    North is a crossroads.")
            print("    South is inside the mine.")
    class ClassRoad2Mid(Room):
        def description(self):
            if self.item_found:
                north_d = "the House of Roquefort."
                west_d = "Fermiere Farm."
                south_d = "Mount Magna."
            else:
                north_d = "a road."
                west_d = "a road."
                south_d = "a road."
            print("\nCrossroads\n\nThe paths meet here. There is a SIGN you can READ here.\n")
            print("    North is",north_d)
            print("    East is a field.")
            print("    West is",west_d)
            print("    South is",south_d)
    class ClassFarm(Room): # Get potato
        def description(self):
            print("\nFarm\n\nThe entire field is barren and the soil is mixed with ash and dead crops.\n")
            print("    East is a crossroads.")
            print("    West is a barn.")
    class ClassBarn(Room):
        def description(self):
            print("\nBarn\n\nThe entire interior is empty as as the walls are all burnt.\nThe roof is entirely removed, and part of the second floor, allowing the sun to light up the area.\nThere is some WRITING on a wall you can READ.\n")
            print("    Up is the second floor.")
            print("    East is a farm.")
    class ClassBarnUp(Room):
        def description(self):
            print("\nBarn\n\nSeveral stacks of hay are lined across the wall.\nA table and chair stand at the far end.\nThere is a DEAD BODY here.\n")
            print("    Down is the ground floor.")
    class ClassHouseGate(Room):
        def description(self):
            if self.north_blocked:
                lock = " locked"
            else:
                lock = "n unlocked"
            print("\nGate\n\nThe path leads to a%s gate with a large stone wall surrounding the house inside.\nThere is a METAL PLAQUE you can READ just above the gate.\n" % lock)
            print("    North is the entrance.")
            print("    South is the crossroads.")
    class ClassField(Room):
        def description(self):
            if self.east_blocked:
                blocked = "The surface has no distinguishing features."
            else:
                blocked = "An opening leads inside."
            print("\nRoad\n\nIn the middle of the field is large obsidian hemisphere. %s\n" % blocked)
            if not self.east_blocked:
                print("    East is inside the obsidian hemisphere.")
            print("    West is the crossroads.")
    class ClassShrineNorth(Room):
        def description(self):
            if self.first_time and room_shrine_south.first_time:
                first_time = " A pedestal emerges from the water as a voice echoes within the chamber, \"Omoz... gloth... izh...\""
            else:
                if self.book:
                    bookpresent = " with a mysterious book"
                else:
                    bookpresent = ""
                first_time = " A pedestal is here%s." % bookpresent
            print("\nNorth Shrine\n\nSteps lead down to a circular pit, shallowly filled with water.\nAround the edges of the room, floating candles dimly light the area.\nAlong the South wall is a MYSTICAL PORTAL." + first_time + "\n")
            print("    West is outside.")
            print("    South is through the portal.")
    # House
    class ClassHouseEntrance(Room):
        def description(self):
            print("\nEntrance\n\nStairs lead up to a tall door bordered by cobblestones.\n")
            print("    North is inside the house.")
            print("    South is the gate.")
    class ClassHouseFoyer(Room):
        def description(self):
            if self.north_blocked:
                lock = " locked"
            else:
                lock = "n unlocked"
            print("\nFoyer\n\nVelet carpet covers the floor as a large, glass chandilier crowned with lights hangs above.\nSeveral busts and paintings line the walls.\nThere is a%s rectangular metal door leading north.\n" % lock)
            print("    North is the hallway.")
            print("    East is the pantry.")
            print("    West is the kitchen.")
    class ClassHouseKitchen(Room):
        def description(self):
            print("\nKitchen\n\nSeveral complicated gadgets sit on the countertops.\nThere is a LEVER here that can be set in a forward or backwards position.\nIt is currently set to the %s position.\n" % self.counter_1)
            print("    East is the foyer.")
    class ClassHousePantry(Room):
        def description(self):
            print("\nPantry\n\nThere are several cabinets containing various cheeses.\nOn the wall is a DIAL with 3 settings: blue, red, and green.\nIt is currently set to %s.\n" % self.counter_1)
            print("    West is the foyer.")
    class ClassHouseHallway(Room): # East and West blocked
        def description(self):
            print("\nHallway\n\nThe velvet carpet extends out in the hallway.\n")
            print("    North is the office.")
            print("    East is the library.")
            print("    West is the bedroom.")
            print("    South is the foyer.")
    class ClassHouseOffice(Room): # End game
        def description(self):
            if self.first_time: ##continue revamp
                first_time = "The door locks behind you. \"The assassin has overcome my final defense, and now he's come to murder me. Tell me, what would a lowly rat from the prisons of Airedale want in killing me? Are you an agent of the Ozkavosh?\"\nAn old bearded man wearing tattered rags, sits at the desk at the far end of the room, facing the North wall. He gets up from his chair and turns around to see you.\n\"What did they offer you for your nefarious task? Untold riches? Rule over Airedale? They will not hold their end of the deal! GIVE me the staff and together we can rid the world of demon-kind.\"\nEden Von Roquefort walks towards you with open hands. \"It is not too late top stop what you are doing.\""
                # firsttime = "The door locks behind you. \"The assassin has overcome my final defense, and now he's come to murder me. Tell me, what would a lowly rat from the prisons of Airedale want in killing me?\" An old bearded man wearing tattered rags, sits at the desk at the far end of the room, facing the North wall. He gets up from his chair and turns around to see you. \"So you are the one sent to kill me? Not what I expected. Then again, appearances don't mean much in times like these. It took me a while to figure out what was going on. You are an agent of the Ozkavosh, here to kill me like they've done the rest of this land. A vesh'raheen would not do, so they would need someone with a history of breaking and entering to reach me. What better choice than a criminal from the Airedale prisons? It is not too late to stop what you are doing.\" Eden Von Roquefort walks towards you with open hands. \"Give me the staff, and together we can rid the world of demon-kind.\""
            elif self.character_dead:
                first_time = "There is a desk at the far back of the room. The body of Eden Von Roquefort lays on the floor."
            else:
                first_time = "There is a desk at the far back of the room. Eden Von Roquefort is here."
            print("\nOffice\n\n" + first_time + "\n")
            print("    South is the hallway.")
    # Mysterious book
    class ClassBookAnimal(Room):
        def description (self):
            if self.book:
                bookpresent = " with a mysterious book on it"
            else:
                bookpresent = ""
            print("\nBlack room\n\nThere are four totems in each direction of the room. Behind each totem is a statue of an animal. In the centre is a pedestal%s.\n" % bookpresent)
            if self.counter_1 == 1:
                north = "Fox"
            elif self.counter_1 == 2:
                north = "Owl"
            elif self.counter_1 == 3:
                north = "Lion"
            elif self.counter_1 == 4:
                north = "Moose"
            if self.counter_2 == 1:
                east = "Fox"
            elif self.counter_2 == 2:
                east = "Owl"
            elif self.counter_2 == 3:
                east = "Lion"
            elif self.counter_2 == 4:
                east = "Moose"
            if self.counter_3 == 1:
                south = "Fox"
            elif self.counter_3 == 2:
                south = "Owl"
            elif self.counter_3 == 3:
                south = "Lion"
            elif self.counter_3 == 4:
                south = "Moose"
            if self.counter_4 == 1:
                west = "Fox"
            elif self.counter_4 == 2:
                west = "Owl"
            elif self.counter_4 == 3:
                west = "Lion"
            elif self.counter_4 == 4:
                west = "Moose"
            print("    North totem animal:",north)
            print("    East totem animal:",east)
            print("    West totem animal:",west)
            print("    South totem animal:",south)
    class ClassBookMirror(Room):
        def description (self):
            if self.book:
                bookpresent = " with a mysterious book on it"
            else:
                bookpresent = ""
            if self.counter_1:
                light = " A ball of light floats in the room."
            else:
                light = ""
            if self.item_found:
                item_found = " There is a pedestal here%s." % bookpresent
            else:
                item_found = ""
            if self.character_dead:
                gargoyle = "pile of stone dust is spread across the floor"
            else:
                gargoyle = "gargoyle statue sits in the centre"
            print("\nBlack room\n\nA %s.\nOn the wall behind it is some TEXT.\n%s%s" % (gargoyle,item_found,light))
    class ClassBook31(Room):
        def description (self):
            print("\nRed room\n\nThere is a statue of a tortoise here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook32(Room):
        def description (self):
            print("\nGreen room\n\nThere is a statue of a vulture here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook33(Room):
        def description (self):
            print("\nPurple room\n\nThere is a statue of a goat here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook34(Room):
        def description (self):
            print("\nOrange room\n\nThere is a statue of a cow here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook35(Room):
        def description (self):
            print("\nYellow room\n\nThere is a statue of a wolf here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook36(Room):
        def description (self):
            print("\nBlue room\n\nThere is a statue of a boar here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook37(Room):
        def description (self):
            print("\nWhite room\n\nThere is a statue of a bear here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook38(Room):
        def description(self):
            print("\nGrey room\n\nThere is a statue of a snake here.\n")
            print("    North is a doorway.")
            print("    East is a doorway.")
            print("    West is a doorway.")
            print("    South is a doorway.")
    class ClassBook3End(Room):
        def description (self):
            if self.book:
                bookpresent = " with a mysterious book on it"
            else:
                bookpresent = ""
            print("\nBlack room\n\nThere is a pedestal here%s.\n" % bookpresent)
            print("    East is a doorway.")
            print("    West is a doorway.")

    #_______Class Initialization - Objects - Before game
    # Sean Reynolds (PyC) - Removed Duplicate Initiailizations
    # debug inventory
    debug_inv = Inventory(gold = 100000, pickaxe = 1, lantern = 1, oil = 10000, pie = 30000, coal = 100000, foot = 100, funnel_cake = 50, half_funnel_cake = 50, hook = 10, staff = 1, ticket = 1, bandage = 100, journal = 1, book = 1, potato = 1, stone = 1, note = 1, bird = 1, memo = 1, potion = 100, flask = 100, key_skeleton = 1, note_1 = vault_answer_1, note_2 = vault_answer_2, note_3 = vault_answer_3, note_4 = vault_answer_4)
    #____________ Room Init
    # Jail
    room_jail_cell = ClassJailCell(name = "jail cell", porridge = 1, east = "roomJailCorridor", east_blocked = True, east_blocked_reason = "The cell door is locked.")
    room_jail_corridor = ClassJailCorridor(name = "corridor", north = "roomJailAntechamber", west = "roomJailCell", west_blocked = False, west_blocked_reason = "The cell door is locked.")
    room_jail_antechamber = ClassJailAntechamber(name = "antechamber", south = "roomJailCorridor", down = "roomJailFoyer")
    room_jail_foyer = ClassJailFoyer(name = "foyer", east = "roomJailHallway", west = "roomJailEntrance", up = "roomJailAntechamber")
    room_jail_hallway = ClassJailHallway(name = "hallway", east = "roomJailBreakRoom", west = "roomJailFoyer")
    room_jail_break_room = ClassJailBreakRoom()
    room_jail_entrance = ClassJailEntrance(name = "jail entrance", east = "roomJailFoyer", west = "roomCourtyardSouth", shrubbery = 1)
    # Town
    room_courtyard_north = ClassCourtyardNorth(name = "north courtyard", north = "roomGate", east = "roomGeneralStore", south = "roomCourtyardSouth", west = "roomCarnival", character_dead = False)
    room_courtyard_south = ClassCourtyardSouth(name = "south courtyard", gold = LOOT_S_GOLD, north = "roomCourtyardNorth", east = "roomJailEntrance", west = "roomBlacksmith", south = "roomAlchemist", character_dead = False)
    room_blacksmith = ClassBlacksmith(name = "blacksmith", east = "roomCourtyardSouth", character_dead = False, is_buy = True, is_sell = True)
    room_alchemist = ClassAlchemist(name = "alchemist's hut", north = "roomCourtyardSouth", character_dead = False, is_sell = True)
    # Carnival
    room_carnival = ClassCarnival(name = "carnival", half_funnel_cake = 1, north = "roomCarnivalFood", east = "roomCourtyardNorth", south = "roomCarnivalShellGame", south_blocked_reason = "The tent is closed.", west = "roomCarnivalWheelGame", west_blocked_reason = "The tent is closed.", character_dead = False)
    room_carnival_food = ClassCarnivalFood(name = "funnel cakes galore", south = "roomCarnival", character_dead = False, is_buy = True)
    room_carnival_shell_game = ClassCarnivalShellGame(name = "sybil\'s shell game", north = "roomCarnival", character_dead = False, is_bet = True)
    room_carnival_wheel_game = ClassCarnivalWheelGame(east = "roomCarnival", character_dead = False, is_buy = True)
    room_gate = ClassGate(name = "town gate", gold = LOOT_GATE_GOLD, north = "roomRoadMid", north_blocked = True, north_blocked_reason = "The guard prevents you from leaving the town.", south = "roomCourtyardNorth", character_dead = False, is_give = True)
    room_general_store = ClassGeneralStore(name = "general store", west = "roomCourtyardNorth", character_dead = False, is_buy = True)
    # Outside
    # Road
    room_road_south = ClassRoadSouth(name = "road", north = "roomRoadMid", east_blocked = True, east_blocked_reason = "The foliage is too thick to traverse.", west_blocked = True, west_blocked_reason = "The foliage is too thick to traverse.", south = "roomGate")
    room_road_mid = ClassRoadMid(name = "crossroads", north = "roomMountEntrance", east = "roomBridge", south = "roomGate", west = "roomLake")
    room_road_north = ClassRoadNorth(name = "road", north = "roomMountEntrance", east_blocked = True, east_blocked_reason = "The foliage is too thick to traverse.", south = "roomRoadMid", west_blocked = True, west_blocked_reason = "The foliage is too thick to traverse.")
    room_road_east = ClassRoadEast(name = "road", north_blocked = True, north_blocked_reason = "The foliage is too thick to traverse.", east = "roomBridge", west = "roomRoadMid", south_blocked = True, south_blocked_reason = "The foliage is too thick to traverse.")
    room_road_west = ClassRoadWest(name = "road", north_blocked = True, north_blocked_reason = "The foliage is too thick to traverse.", east = "roomRoadMid", west = "roomLake", south_blocked = True, south_blocked_reason = "The foliage is too thick to traverse.")
    room_road_corner = ClassRoadCorner(name = "road", north = "roomTempleEntrance", east = "roomForest", west = "roomBridge", west_blocked_reason = "The black knight stands in the way. He declares, \"None shall pass.\"", south_blocked = True, south_blocked_reason = "The foliage is too thick to traverse.")
    room_forest = ClassForest(name = "forest", north_blocked = True, north_blocked_reason = "The foliage is too thick to traverse.", east = "roomShrineSouth", east_blocked = True, east_blocked_reason = "The foliage is too thick to traverse.", west = "roomRoadCorner", south_blocked = True, south_blocked_reason = "The foliage is too thick to traverse.")
    # Lake
    room_lake = ClassLake(name = "lake laguiole", north_blocked = True, north_blocked_reason = "The foliage is too thick to traverse.", east = "roomRoadMid", south_blocked = True, south_blocked_reason = "The foliage is too thick to traverse.", west_blocked = True, west_blocked_reason = "The foliage is too thick to traverse.", character_dead = False, is_give = True)
    # Bridge
    room_bridge = ClassBridge(name = "bridge", east = "roomRoadCorner", east_blocked = True, east_blocked_reason = "The troll is stopping you from crossing.", west = "roomRoadMid", character_dead = False, is_give = True)
    # Temple
    room_temple_entrance = ClassTempleEntrance(name = "temple entrance", north = "roomTempleInside", north_blocked = True, north_blocked_reason = "Rubble is blocking the way.", south = "roomRoadCorner", counter_1 = RUBBLE_DURABILITY, is_mine = True)
    room_temple_inside = ClassTempleInside(name = "temple", south = "roomTempleEntrance", down = "roomTempleBasement")
    room_temple_basement = ClassTempleBasement(name = "inner sanctum", up = "roomTempleInside", character_dead = False, staff = 1)
    # Cave
    room_mount_entrance = ClassMountEntrance(name = "coal mine entrance", north = "roomCave_1_m", north_blocked = True, north_blocked_reason = "The vault door is locked.", east_blocked = True, east_blocked_reason = "The foliage is too thick to traverse.", south = "roomRoadMid", west_blocked = True, west_blocked_reason = "The foliage is too thick to traverse.", counter_ans_1 = vault_answer_1, counter_ans_2 = vault_answer_2, counter_ans_3 = vault_answer_3, counter_ans_4 = vault_answer_4, counter_1 = vault_initial_1, counter_2 = vault_initial_2, counter_3 = vault_initial_3, counter_4 = vault_initial_4)
    # 1
    room_cave_1_m = ClassCave1M(name = "cavern", north = "roomCave_2_m", south = "roomMountEntrance")
    # 2
    room_cave_2_m = ClassCave2M(name = "cavern", east = "roomCave_2_mr", south = "roomCave_1_m", west = "roomCave_2_lm")
    room_cave_2_mr = ClassCave2Mr(name = "cavern", north = "roomCave_3_mr", west = "roomCave_2_m", bird = 1)
    room_cave_2_lm = ClassCave2Lm(name = "cavern", north = "roomCave_3_lm_coalmine", east = "roomCave_2_m", west = "roomCave_2_llm")
    room_cave_2_llm = ClassCave2Llm(name = "cavern", north = "roomCave_3_llm_crevasse", east = "roomCave_2_lm")
    # 3
    room_cave_3_m_coalmine = ClassCave3MCoalmine(name = "cavern", north = "roomCave_4_m", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    room_cave_3_mr = ClassCave3Mr(name = "cavern", north = "roomCave_4_mr", east = "roomCave_3_mrr_coalmine", south = "roomCave_2_mr", counter_1 = random.randint(COAL_MIN,COAL_MAX))
    room_cave_3_mrr_coalmine = ClassCave3MrrCoalmine(name = "cavern", west = "roomCave_3_mr", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    room_cave_3_lm_coalmine = ClassCave3LmCoalmine(name = "cavern", south = "roomCave_2_lm", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    room_cave_3_llm_crevasse = ClassCave3LlmCrevasse(name = "cavern", north = "roomCave_4_llm", south = "roomCave_2_llm", west = "roomCave__3_lllm_treasure_crevasse", west_blocked = True, west_blocked_reason = "The crevasse is too large to walk across.", is_crevasse = True)
    room_cave_3_lllm_treasure_crevasse = ClassCave3LllmTreasureCrevasse(name = "cavern", east = "roomCave_3_llm_crevasse", east_blocked = True, east_blocked_reason = "The crevasse is too large to walk across.", is_crevasse = True)
    # 4
    room_cave_4_m = ClassCave4M(name = "cavern", north = "roomCave_5_m", east = "roomCave_4_mr", south = "roomCave_3_m_coalmine", west = "roomCave_4_lm")
    room_cave_4_mr = ClassCave4Mr(name = "cavern", south = "roomCave_3_mr", west = "roomCave_4_m")
    room_cave_4_lm = ClassCave4Lm(name = "cavern", north = "roomCave_5_lm_coalmine", east = "roomCave_4_m", west = "roomCave_4_llm")
    room_cave_4_llm = ClassCave4Llm(name = "cavern", north = "roomCave_5_llm", east = "roomCave_4_lm", south = "roomCave_3_llm_crevasse")
    # 5
    room_cave_5_m = ClassCave5M(name = "cavern", north = "roomCave_6_m", east = "roomCave_5_mr_coalmine", south = "roomCave_4_m")
    room_cave_5_mr_coalmine = ClassCave5MrCoalmine(name = "cavern", west = "roomCave_5_m", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    room_cave_5_lm_coalmine = ClassCave5LmCoalmine(name = "cavern", south = "roomCave_4_lm", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    room_cave_5_llm = ClassCave5Llm(name = "cavern", east = "roomCave_5_lm_coalmine", south = "roomCave_4_llm", west = "roomCave_5_lllm")
    room_cave_5_lllm = ClassCave5Lllm(name = "cavern", north = "roomCave_6_lllm", east = "roomCave_5_llm")
    # 6
    room_cave_6_m = ClassCave6M(name = "cavern", east = "roomCave_6_mr", south = "roomCave_5_m")
    room_cave_6_mr = ClassCave6Mr(name = "cavern", north = "roomCave_7_mr", west = "roomCave_6_m")
    room_cave_6_lm_coalmine = ClassCave6LmCoalmine(name = "cavern", north = "roomCave_7_lm", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    room_cave_6_llm_coalmine = ClassCave6LlmCoalmine(name = "cavern", west = "roomCave_6_lllm", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    room_cave_6_lllm = ClassCave6Lllm(name = "cavern", north = "roomCave_7_lllm", east = "roomCave_6_llm_coalmine", south = "roomCave_5_lllm")
    # 7
    room_cave_7_m = ClassCave7M(name = "cavern", east = "roomCave_7_mr", west = "roomCave_7_lm")
    room_cave_7_mr = ClassCave7Mr(name = "cavern", north = "roomCave_8_mr_crevasse", south = "roomCave_6_mr", west = "roomCave_7_m")
    room_cave_7_lm = ClassCave7Lm(name = "cavern", east = "roomCave_7_m", south = "roomCave_6_lm_coalmine", west = "roomCave_7_llm")
    room_cave_7_llm = ClassCave7Llm(name = "cavern", north = "roomCave_8_llm_coalmine", east = "roomCave_7_lm", west = "roomCave_7_lllm")
    room_cave_7_lllm = ClassCave7Lllm(name = "cavern", east = "roomCave_7_llm", south = "roomCave_6_lllm")
    # 8
    room_cave_8_mr_crevasse = ClassCave8MrCrevasse(name = "cavern", north = "roomCave_9_mr_crevasse", north_blocked = True, north_blocked_reason = "The crevasse is too large to walk across.", south = "roomCave_7_mr", is_crevasse = True)
    room_cave_8_llm_coalmine = ClassCave8LlmCoalmine(name = "cavern", south = "roomCave_7_llm", counter_1 = random.randint(COAL_MIN,COAL_MAX), is_mine = True)
    # 9
    room_cave_9_mr_crevasse = ClassCave9MrCrevasse(name = "cavern", north = "roomCave__10_mr", south = "roomCave_8_mr_crevasse", south_blocked = True, south_blocked_reason = "The crevasse is too large to walk across.",  is_crevasse = True)
    # 10
    room_cave__10_m = ClassCave10M(name = "cavern", east = "roomCave__10_mr", west = "roomCave__10_lm")
    room_cave__10_mr = ClassCave10Mr(name = "cavern", east = "roomCave__10_mrr", south = "roomCave_9_mr_crevasse", south_blocked = True, south_blocked_reason = "Rubble is blocking the way.", west = "roomCave__10_m", counter_1 = RUBBLE_DURABILITY, is_mine = True)
    room_cave__10_mrr = ClassCave10Mrr(name = "cavern", east = "roomCave__10_mrrr", west = "roomCave__10_mr")
    room_cave__10_mrrr = ClassCave10Mrrr(name = "cavern", north = "roomCave__11_mrrr", west = "roomCave__10_mrr")
    room_cave__10_lm = ClassCave10Lm(name = "cavern", north = "roomCave__11_lm", east = "roomCave__10_m")
    # 11
    room_cave__11_mrrr = ClassCave11Mrrr(name = "cavern", north = "roomDarkness", south = "roomCave__10_mrrr")
    room_cave__11_lm = ClassCave11Lm(name = "cavern", north = "roomDarkness", south = "roomCave__10_lm")
    # Darkness
    room_darkness = ClassDarkness(name = "darkness")
    # Lair
    room_lair_mid = ClassLairMid(name = "lair", east = "roomLairEast", west = "roomLairWest", south_blocked = True, south_blocked_reason = "Rubble is blocking the way.", counter_1 = 5, is_mine = True)
    room_lair_east = ClassLairEast(name = "lair", north = "roomRoad2South", north_blocked = True, north_blocked_reason = "Rubble is blocking the way.", west = "roomLairMid", counter_1 = RUBBLE_DURABILITY, is_mine = True)
    room_lair_west = ClassLairWest(name = "lair", east = "roomLairMid", south = "roomLairHole", south_blocked_reason = "You are carrying too much to fit through the opening.", gold = LOOT_WEST_GOLD, biscuit = LOOT_WEST_BISCUIT)
    room_lair_hole = ClassLairHole(name = "lair", north = "roomLairWest", north_blocked_reason = "You are carrying too much to fit through the opening.", lantern = 1)
    # Field
    room_road_2_south = ClassRoad2South(name = "road", north = "roomRoad2Mid", south = "roomLairEast")
    room_road_2_mid = ClassRoad2Mid(name = "crossroad", north = "roomHouseGate", east = "roomField", south = "roomRoad2South", west = "roomFarm")
    room_house_gate = ClassHouseGate(name = "road", south = "roomRoad2Mid", north = "roomHouseEntrance", north_blocked = True, north_blocked_reason = "The gate is locked.")
    room_farm = ClassFarm(name = "farm", east = "roomRoad2Mid", west = "roomBarn", potato = 1)
    room_barn = ClassBarn(name = "barn", east = "roomFarm", up = "roomBarnUp")
    room_barn_up = ClassBarnUp(name = "barn", down = "roomBarn")
    room_field = ClassField(name = "road", east = "roomShrineNorth", east_blocked = True, east_blocked_reason = "You cannot go East.", west = "roomRoad2Mid")
    # Shrines
    room_shrine_north = ClassShrineNorth(name = "north shrine", west = "roomField", south = "roomShrineSouth", book = 1)
    room_shrine_south = ClassShrineSouth(name = "south shrine", north = "roomShrineNorth", west = "roomForest")
    # House
    room_house_entrance = ClassHouseEntrance(name = "entrance", north = "roomHouseFoyer", north_blocked = True, north_blocked_reason = "The door is locked.", south = "roomHouseGate")
    room_house_foyer = ClassHouseFoyer(name = "foyer", north = "roomHouseHallway", north_blocked = True, north_blocked_reason = "The door is locked.", east = "roomHousePantry", south = "roomHouseEntrance", west = "roomHouseKitchen")
    room_house_kitchen = ClassHouseKitchen(name = "kitchen", east = "roomHouseFoyer", counter_1 = LEVER_START)
    room_house_pantry = ClassHousePantry(name = "pantry", west = "roomHouseFoyer", brie = 1, munster = 1, stilton = 1, swiss = 1, wensleydale = 1, counter_1 = DIAL_START)
    room_house_hallway = ClassHouseHallway(name = "hallway", north = "roomHouseOffice", east_blocked = True, east_blocked_reason = "The door is locked.", south = "roomHouseFoyer", west_blocked = True, west_blocked_reason = "The door is locked.")
    room_house_office = ClassHouseOffice(name = "office", south = "roomHouseHallway", south_blocked = True, south_blocked_reason = "The door is locked.", character_dead = False, is_give = True)
    # Mysterious book
    # Puzzle 1 - Animal Totems
    room_book_animal = ClassBookAnimal(name = "black room")
    # Puzzle 2 - Mirror player
    room_book_mirror = ClassBookMirror(name = "black room", character_dead = False)
    # Puzzle 3 - Movement
    room_book_3_1 = ClassBook31(name = "red room", north = "roomBook_3_5", east = "roomBook_3_3", south = "roomBook_3_4", west = "roomBook_3_2")
    room_book_3_2 = ClassBook32(name = "green room", north = "roomBook_3_3", east = "roomBook_3_1", south = "roomBook_3_5", west = "roomBook_3_3")
    room_book_3_3 = ClassBook33(name = "purple room", north = "roomBook_3_8", east = "roomBook_3_2", south = "roomBook_3_4", west = "roomBook_3_1")
    room_book_3_4 = ClassBook34(name = "orange room", north = "roomBook_3_1", east = "roomBook_3_5", south = "roomBook_3_7", west = "roomBook_3_6")
    room_book_3_5 = ClassBook35(name = "yellow room", north = "roomBook_3_2",  east = "roomBook_3_6", south = "roomBook_3_1", west = "roomBook_3_4")
    room_book_3_6 = ClassBook36(name = "blue room", north = "roomBook_3_7", east = "roomBook_3_4", south = "roomBook_3_8", west = "roomBook_3_5")
    room_book_3_7 = ClassBook37(name = "white room", north = "roomBook_3_4", east = "roomBook_3_8", south = "roomBook_3_6", west = "roomBook_3_End")
    room_book_3_8 = ClassBook38(name = "grey room", north = "roomBook_3_6", east = "roomBook_3_End", south = "roomBook_3_3", west = "roomBook_3_7")
    room_book_3_end = ClassBook3End(name = "black room", east = "roomBook_3_7", west = "roomBook_3_8", key_skeleton = 1, book = 1)

    #_______Stat Init
    stat = Stat()

    #_______Inventory init
    if player_name:
        inv = Inventory(key = 1,porridge = 1,letter = 1)
        room_jail_cell.porridge = 0
    else:
        inv = Inventory(note_1 = vault_answer_1, note_2 = vault_answer_2, note_3 = vault_answer_3, note_4 = vault_answer_4)
    # roomBridge troll
    inv_troll = Inventory()
    # roomGate guard
    inv_gate = Inventory()
    # roomCarnivalShellGame
    inv_shell = Inventory(gold = SHELL_GOLD)
    # roomCarnival
    inv_spokesperson = Inventory()
    # roomCarnivalFood
    inv_food = Inventory(funnel_cake = FUNNELCAKE_LIMIT)


#_______Variables Init
    # Random
    riddle = random.randint(1,4)
    if riddle == 1:
        riddle = "I don't have eyes, but once I did see. I don't have thoughts, but now I'm empty. What am I?"
        riddle_answer = ["skull","a skull"]
    elif riddle == 2:
        riddle = "The poor have me. The rich need me. If you eat me, you will die. What am I?"
        riddle_answer = ["nothing","no thing","nada"]
    elif riddle == 3:
        riddle = "You will always find me in the past. I can be created in the present, But the future can never taint me. What am I?"
        riddle_answer = ["history","the history","recorded history"]
    elif riddle == 4:
        riddle = "The more there is of me, the less you see. What am I?"
        riddle_answer = ["darkness","dark","the dark","the darkness","blackness","fog","the fog"]
    room_temple_basement.counter_ans_1 = riddle_answer
    room_temple_basement.counter_1 = riddle

    end_game = False
    change_room = False
    # Starting room
    # Default: roomJailCell
    if debug:
        room_id = "roomTempleInside"
        room_current = room_temple_inside
    else:
        room_id = "roomJailCell"
        room_current = room_jail_cell
    direction = False
    just_entered = False
    ask_name = False
    jail_guards = False
    jail_guard_counter = 3
    creature_roam = False
    creature_chase = 0
    creature_roam_counter = random.randint(CREATURE_ROAM_MIN,CREATURE_ROAM_MAX)
    creature_chase_counter = random.randint(CREATURE_CHASE_MIN,CREATURE_CHASE_MAX)
    creature_lair_chase = False
    creature_lair_chase_counter = LAIR_CHASE_DURATION
    silenced = False
    # End Game
    win = False
    # Does not count as turn
    not_turn = True
    # Counters
    turn_counter = 0
    guard_counter = 0
    light_counter = 0
    oil_counter = 0
    # Default first option to prevent "again" crash on first turn
    option_last = "invalid"
#_______Start of Game text____________________________________________________________
# Current room information
    room_current.description()
    room_current.items_present()
    if inv.item_types():
        print()
        inv.examine_inventory("inventory",room_current)
# Hunger
    stat.lower_shield()
    if stat.hunger <= 0:
        end_game = True
    elif stat.hunger <= 15:
        print()
        stat.examine_hunger()
# Health
    if stat.health in range(1,stat.healthmax):
        stat.lower_health()
        print()
        stat.examine_health()
    if stat.health <= 0:
        end_game = True
# Oil warning
    if inv.lantern > 0 or room_current.lantern > 0:
        if oil_counter in range(3,5):
            print("\nYour lantern flickers.")
        elif oil_counter == 2:
            print("\nYour lantern is about to run out of oil.")
        elif oil_counter == 1:
            print("\nYour lantern has ran out of oil.")

#_______End Game_________________________________________________________________
# Loops until the game ends
# Game loop start
    while not end_game:
#_______User input______________________________________________________________
        option = input("\n\n\n\n> ").lower()
        if option not in ("again","do it again","do again","g"):
            option_last = option
#_______Start of turn___________________________________________________________
        # Set last room
        room_id_last = room_id
        room_current_last = room_current
        not_turn = False
        message = False
#_______Free Space Decisions____________________________________________________
# Can be made in free space
# Commands

        # Repeat last option
        if option in ("again","do it again","do again","g"):
            option = option_last
        #Quit game
        if option in ("quit","quit game","end game","die","kill self","suicide", "commit suicide","end my life","end my suffering","throw in the towel","give up","give up on life","exit game"):
            end_game = True
        # debug commands
        elif option == "!debug" and debug:
            print("!stat - Prints player stats")
            print("!turn - Prints number of turns")
            print("!unblock - Unblocks all directions")
            print("!block - Blocks all directions")
            print("!characterdead - makes roomCurrent.characterDead = True")
            print("!silence - Toggles silence")
            print("!inv - Gives debug inventory")
            print("!spells - Prints status of all Ozkavosh spells and words")
            print("!learn - Learns all Ozkavosh spells and words")
            not_turn = True
        elif option == "!stat" and debug:
            print("Name:",player_name)
            print("Hunger:",stat.hunger)
            print("Health:",stat.health)
            print("oilCounter:",oil_counter)
            print("inv.item_types():",inv.item_types())
            print("turnCounter:",turn_counter)
            not_turn = True
        elif option == "!turn" and debug:
            print("The turncounter is %s." % turn_counter)
            not_turn = True
        elif option == "!unblock" and debug:
            if room_current.north_blocked:
                room_current.north_blocked = False
            elif room_current.east_blocked:
                print("East is now unblocked.")
                room_current.east_blocked = False
            elif room_current.south_blocked:
                print("South is now unblocked.")
                room_current.south_blocked = False
            elif room_current.west_blocked:
                print("west is now unblocked.")
                room_current.west_blocked = False
            not_turn = True

        elif option == "!block" and debug:
            if room_current.north_blocked_reason and room_current.north:
                room_current.north_blocked = True
                print("North is now blocked.")
            if room_current.east_blocked_reason and room_current.east:
                room_current.east_blocked = True
                print("East is now blocked.")
            if room_current.south_blocked_reason and room_current.south:
                room_current.south_blocked = True
                print("South is now blocked.")
            if room_current.west_blocked_reason and room_current.west:
                room_current.west_blocked = True
                print("West is now blocked.")
            not_turn = True

        elif option == "!characterdead" and debug:
            room_current.character_dead = True
            print("characterDead is True")
            not_turn = True
        elif option == "!oilcounter" and debug:
            print(oil_counter)
            not_turn = True
        elif option in ("!health","!hp") and debug:
            print("Health:",stat.health)
            not_turn = True
        elif option in ("!hunger","!h") and debug:
            print("Hunger:",stat.hunger)
            not_turn = True
        elif option == "!name" and debug:
            print("Name:",player_name)
            not_turn = True
        elif option == "!room" and debug:
            print("roomID:",room_id)
            print("roomID_Last:",room_id_last)
            print("North room:",room_current.north)
            print("	North room blocked:",room_current.north_blocked)
            print("	North room blocked reason:",room_current.north_blocked_reason)
            print("East room:",room_current.east)
            print("	East room blocked:",room_current.east_blocked)
            print("	East room blocked reason:",room_current.east_blocked_reason)
            print("South room:",room_current.south)
            print("	South room blocked:",room_current.south_blocked)
            print("	South room blocked reason:",room_current.south_blocked_reason)
            print("West room:",room_current.west)
            print("	West room blocked:",room_current.west_blocked)
            print("	West room blocked reason:",room_current.west_blocked_reason)
            print("counter_1:",room_current.counter_1)
            print("counter_2:",room_current.counter_2)
            print("counter_3:",room_current.counter_3)
            print("counter_4:",room_current.counter_4)
            print("isBuy:",room_current.is_buy)
            print("isBet:",room_current.is_bet)
            print("isCrevasse:",room_current.is_crevasse)
            print("isGive:",room_current.is_give)
            print("isMine:",room_current.is_mine)
            print("isSell:",room_current.is_sell)
            print("itemFound:",room_current.item_found)
            print("characterDead:",room_current.character_dead)
            print("creatureRoam:",creature_roam)
            print("	creatureRoamCounter:",creature_roam_counter)
            print("creatureChase:",creature_chase)
            print("	creatureChaseCounter:",creature_chase_counter)
            not_turn = True
        elif option == "!silence" and debug:
            if silenced:
                silenced = False
                print("Silenced: False")
            else:
                silenced = True
                print("Silenced: True")
            not_turn = True
        elif option == "!inv" and debug:
            inv = debug_inv
            stat.health = HEALTH_MAX
            stat.hunger = HUNGER_DEBUG
            print("Debug inventory given.")
            not_turn = True
        elif option == "!spells" and debug:
            print("spell_learn is:",spell_learn)
            print("spell_unlock is:",spell_unlock)
            print("spell_persuade is:",spell_persuade)
            print("spell_jump is:",spell_jump)
            print("spell_light is:",spell_light)
            print("spell_heal is:",spell_heal)
            print("spell_feed is:",spell_feed)
            print("spell_kill is:",spell_kill)
            print("spell_killself is:",spell_killself)
            print("word_darkness is:",word_darkness)
            print("word_reign is:",word_reign)
            print("word_stop is:",word_stop)
            print("word_servant is:",word_servant)
            print("word_mirror is:",word_mirror)
            print("word_dominion is:",word_dominion)
            print("word_curse is:",word_curse)
            not_turn = True
        elif option == "!learn" and debug:
            print("All Ozkavosh spells and words learned.")
            spell_learn = 2
            spell_unlock = 2
            spell_persuade = 2
            spell_jump = 2
            spell_light = 2
            spell_heal = 2
            spell_feed = 2
            spell_kill = 2
            spell_killself = 2
            word_darkness = 2
            word_reign = 2
            word_stop = 2
            word_servant = 2
            word_mirror = 2
            word_dominion = 2
            word_curse = 2
            spell_oblivion = 2
            not_turn = True
        # Examine
        # Inventory
        # Objects in inventory
        # Room
        elif option.startswith("examine") or option.startswith("x") or option in ("inventory","inv","i","l","spells","spellbook","words","demon words","ozkavosh","ozkavosh words","hunger","health","hp","stat","stats","self","help","shortcut","shortcuts","h","current objective","objective","o") or option.startswith("look"):
            if option.startswith("examine") or option.startswith("look") or option.startswith("x"):
                if option.startswith("x"):
                    option = option[2:]
                elif option.startswith("examine the"):
                    option = option[12:]
                elif option.startswith("examine a"):
                    option = option[10:]
                elif option.startswith("examine"):
                    option = option[8:]
                elif option.startswith("look at"):
                    option = option[8:]
                elif option.startswith("look"):
                    option = option[5:]
            # Nothing
            if option == "":
                print("Examine what?")
                option = False
                not_turn = True
            # Shortcut help
            if option in ("commands","shortcut","shortcuts","help"):
                print("\nShortcut commands:")
                shortcuts()
                option = False
                not_turn = True
            # Examine room
            elif option in ("look","l"):
                room_current.description()
                room_current.items_present()
                option = False
                not_turn = True
            # Examine spells
            elif option in ("spells","spellbook","words","demon words","ozkavosh","ozkavosh words"):
                demon_words()
                option = False
                not_turn = True
            if option:
                # Stats
                if option in ("hunger","h"):
                    stat.examine_hunger()
                    print("You need to eat something in",stat.hunger,"turns.")
                    not_turn = True
                elif option in ("health","hp"):
                    stat.examine_health()
                   # if stat.health != HEALTH_MAX:
                        #print("You need to heal your wounds in",stat.health,"turns.")
                    if stat.health < HEALTH_MAX:
                         print(f"You need to heal your wounds in {stat.health} turns.")
                    not_turn = True
                elif option in ("stat","stats","self"):
                    stat.examine_hunger()
                    stat.examine_health()
                    print("You need to eat something in",stat.hunger,"turns.")
                    if stat.health != HEALTH_MAX:
                        print("You need to heal your wounds in",stat.health,"turns.")
                elif option in ("o","objective","current objective"):
                    stat.print_objective()
                    not_turn = True
                # Spells
                elif option in ("spells","spell","spellbook","words","word","demon words","ozkavosh","ozkavosh words"):
                    demon_words()
                # Inventory
                elif option in ("inventory","inv","i"):
                    option = "inventory"
                    inv.examine_inventory(option, room_current)
                    not_turn = True
                elif option .endswith("gold"):
                    inv.examine_inventory(option, room_current)
                elif option.endswith("letter"):
                    option = "letter"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("key","key of ahm'domosh")):
                    if inv.key_skeleton or room_current.key_skeleton:
                        option = "key of Ahm'domosh"
                    else:
                        option = "key"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("pickaxe","pick","pickaxes","picks")):
                    option = "pickaxe"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("shrubbery","shrub")):
                    option = "shrubbery"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("half-eaten cake","half cake","half-eaten funnel cake","half eaten funnel cake","half funnel cake","half-eaten cakes","half cakes","half-eaten funnel cakes","half eaten funnel cakes","half funnel cakes")):
                    option = "half-eaten funnel cake"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("cake","cakes")):
                    if (inv.half_funnel_cake or room_current.half_funnel_cake) and not inv.funnel_cake and not room_current.funnel_cake:
                        option = "half-eaten funnel cake"
                    else:
                        option = "funnel cake"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("foot","rabbit","feet","foots")):
                    option = "lucky rabbit foot"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("bowl","porridge")):
                    if option.endswith("bowl") and (inv.bowl or room_current.bowl) and not inv.porridge and not room_current.porridge:
                        option = "bowl"
                    else:
                        option = "bowl of porridge"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("lantern","lanterns")):
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("oil","vial","vials")):
                    option = "vial of lantern oil"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("pies","pie")):
                    option = "chicken pot pie"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("biscuit","biscuits","hardtack")):
                    option = "hardtack biscuit"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("hook","hooks")):
                    option = "grappling hook"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("staff of garrotxa","staff")):
                    option = "staff of Garrotxa"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("ticket","raffle")):
                    option = "raffle ticket"
                    inv.examine_inventory(option, room_current)
                elif option.endswith("coal"):
                    option = "piece of coal"
                    inv.examine_inventory(option, room_current)
                elif option.endswith("potato"):
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("bandages","bandage")):
                    option = "bandage"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("journals","journal")):
                    option = "journal"
                    inv.examine_inventory(option, room_current)
                elif option.endswith("book"):
                    option = "book"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("brie","brie cheese")):
                    option = "slice of brie cheese"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("munster","munster cheese")):
                    option = "slice of munster cheese"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("stilton","stilton cheese")):
                    option = "slice of stilton cheese"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("swiss","swiss cheese")):
                    option = "slice of swiss cheese"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("wensleydale","wensleydale cheese")):
                    option = "slice of wensleydale cheese"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("potion","rejuvination")):
                    option = "potion of rejuvination"
                    inv.examine_inventory(option, room_current)
                elif option.endswith(("flask","flasks")):
                    option = "flask"
                    inv.examine_inventory(option, room_current)
                elif option.endswith("stone"):
                    option = "dragonstone"
                    inv.examine_inventory(option, room_current)
                elif option.endswith("bird"):
                    option = "wooden bird"
                    inv.examine_inventory(option, room_current)
                elif option.endswith("note"):
                    option = "note"
                    inv.examine_inventory(option, room_current)
                elif option.endswith("memo"):
                    option = "memo"
                    inv.examine_inventory(option, room_current)
                # Room
                elif option in ("room","surroundings","place","area",room_current.name):
                    room_current.description()
                    room_current.items_present()
                # Objects in rooms
                # Jail
                elif room_id == "roomJailCell":
                    if option in ("walls","stone walls","wall","stone wall","stone"):
                        print("12 tally marks have been etched in, representing all the years you've been here.")
                    elif option in ("haystack","hay","stack"):
                        print("A fairly comfortable place to sleep.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            room_current.gold += 8
                            print("You find some supplies.")
                            room_current.items_present()
                    elif option in ("solid metal door","solid door","metal door","door"):
                        print("It's made of cold steel. There is a small slit in it.")
                    elif option in ("slit","small slit","through slit","through small slit"):
                        print("You can see out into the corridor. Other jail cells are visible, but you can't see inside of them.")
                        #if not roomCurrent.counter_1 and not playerName:
                           # roomCurrent.counter_1 = 1
                           # removed due to satement has no effect
                    elif ask_name:
                        if option in ("woman","her","stranger"):
                            print("She is wearing white robes, covering her face and body.")
                        elif option in ("portal","mystical portal"):
                            print("It's elliptical with a glowing purple border. Through the other side you can see stone walls.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Courtyard North
                elif room_id == "roomCourtyardNorth":
                    if option in ("crowd","people"):
                        print("Some look pretty excited for the carnival.")
                    if option in ("building","buildings"):
                        print("Stone walls. Wooden roofs. They all look pretty similar.")
                    if option in ("urchin boy","boy","young urchin boy","young boy") and not room_carnival_wheel_game.character_dead:
                        print("He's wearing dirty, ragged clothing.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Courtyard South
                elif room_id == "roomCourtyardSouth":
                    if option in ("large elegant fountain","large fountain","elegant fountain","fountain"):
                        print("It's large... and elegant.")
                    elif option in ("crowd","busy people","people"):
                        print("You feel creepy examining everyone around you, making you quickly stop.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Carnival
                elif room_id == "roomCarnival":
                    if option in ("tents","tent"):
                        print("The tents are striped in a variety of colours.")
                    elif option in ("lights","light","lighting"):
                        print("The lights brighten the place up, as you would expect lights to do.")
                    elif option in ("banners","banner","colourful banners"):
                        print("The banners have cows on them, representing the Goddess Garrotxa.")
                    elif option in ("crowd","adults","children","people"):
                        print("The crowd is noisy and generally excited.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Shell Game
                elif room_id == "roomCarnivalShellGame":
                    if option in ("sybil","her","woman","old woman"):
                        print("Sybil is hunched at the table. She has only one eye, and a lot of missing teeth. Her ragged clothing makes her look homeless.")
                    elif option in ("table","wooden table"):
                        print("It looks like it could collapse at any moment. The table surface has a lot of scratch marks, from shuffling of shells no doubt.")
                    elif option == "shells":
                        print("They are conch shells.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Funnel Cakes Galore
                elif room_id == "roomCarnivalFood":
                    if option in ("older overweight vendor","overweight vendor","vendor","him","man"):
                        print("The vendor looks happy to see you. His apron is grease-stained, and his sleeves are rolled up.")
                    elif option in ("stove","stovetop"):
                        print("It's made of cast iron.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Road Mid
                elif room_id == "roomRoadMid":
                    if option in ("sign","the sign"):
                        print("The sign reads: \"North: Mount Magna, East: Temple of Garrotxa, West: Lake Laguiole, South: Town of Airedale\"")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Mount Entrance
                elif room_id == "roomMountEntrance":
                    if option in ("sign","the sign"):
                        print("It reads: \"Mount Magna coal mine is CLOSED. Dangerous CREATURE inside.\"")
                    elif option in ("a body","body","the body","dead body","a dead body","the dead body"):
                        print("It looks like a miner covered in claw marks.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            room_current.coal += LOOT_ENTRANCE_COAL
                            room_current.note += LOOT_ENTRANCE_NOTE
                            print("You search the body and find some supplies.")
                            room_current.items_present()
                    elif option in ("vault","vault door"):
                        if room_current.north_blocked:
                            print("It is locked.")
                        else:
                            print("It is unlocked.")
                        print("The first dial reads %s." % room_current.counter_1)
                        print("The second dial reads %s." % room_current.counter_2)
                        print("The third dial reads %s." % room_current.counter_3)
                        print("The fourth dial reads %s." % room_current.counter_4)
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Bridge
                elif room_id == "roomBridge":
                    if option in ("troll","ugg","the troll"):
                        if room_current.character_dead:
                            print("It's completely charred.")
                        elif room_current.east_blocked:
                            print("He's licking his lips and rubbing his belly. No doubt thinking about funnel cakes.")
                        else:
                            print("He's excited to see how many funnel cakes he can buy.")
                    elif option in ("wooden bridge","the bridge"):
                        print("It's made of wood.")
                    elif option in ("river","the river"):
                        print("The stream is flowing north to south.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Lake
                elif room_id == "roomLake":
                    if option in ("writing","tablet","stone tablet"):
                        print("The writing on the tablet neatly reads, \"OZH VO'SES SA.\"")
                        if not spell_unlock:
                            spell_unlock = 1
                    elif option in "stranger":
                        if room_current.character_dead:
                            print("He's dead.")
                        elif room_current.is_give():
                            print("He looks sad.")
                        else:
                            print("He looks happy to have his bird statue back.")
                    elif option in ("lockbox","box"):
                        if not room_current.counter_1:
                            print("It's locked.")
                        elif room_current.counter_2:
                            print("It's open.")
                        else:
                            print("It's unlocked, but closed.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Forest, Field
                elif room_id in ("roomForest","roomField"):
                    if option in ("hemisphere","obsidian","obsidian hemisphere"):
                        print("It looks strangely out of place.")
                    else:
                        print("You cannot examine that.")
                # Temple Inside
                elif room_id == "roomTempleInside":
                    if option in ("figure","ghost","ghostly figure"):
                        if not room_current.character_dead:
                            print("It looks like a cow, wrapped in white robes.")
                        else:
                            print("The figure is gone.")
                    elif option in ("statue","statue of garrotxa","garrotxa","large statue","large statue of garroxta","statue of garrotxa","the statue"):
                        print("The statue is made of white marble. It looks like a woman wearing white robes, with a cow's head. In one hand is a butter churn; in the other is a wheel of cheese.")
                    elif option in ("carpet","velvet carpet","velvet"):
                        print("The carpet is red, and has cows embroidered on it.")
                    elif option == "pedestal":
                        print("It's made of marble.")
                    elif option == "stand":
                        print("It's designed to hold the staff of Garrotxa")
                    elif option in ("mural","murals","text"):
                        print("Examine which one? There is a West, North, and East mural.")
                    elif option in ("west mural","west text", "west wall"):
                        print("The image shows a tall, cow-headed woman wearing white robes, standing at the top of Mount Magna with outstretched arms. A group of followers, wearing similar robes, bow down around her. Below, the text reads:\n")
                        print("Four a thousand years, the goddess of cheese, Garrotxa, was worshipped peacefully amongst the people of Kashkaval as a herald of propserity, fertility, and music. She lived atop Mount Magna and walked across the fields of Fermiere for most of her days. At the beginning of what most know to be as the First Age, her thirteen most devoted followers were given special robes by the goddess herself, made out of layers of divine cheesecloth. These followers were deemed the prophets of Garrotxa, and were representatives of the main cities throughout Kashkaval.")
                    elif option in ("north mural","north text", "north wall"):
                        print("The image shows a giant horned devil with open wings standing in a grassy field. He holds Garrotxa in one hand and a spear in the other. Flames protrude from the ground up into the sky. Below, the text reads:\n")
                        print("The demon king, Vesh'arkosh of the Underworld, jealous of Garrotxa's dominion of the Overworld, emerged to the surface to find her. After a great battle between the two, Garrotxa was slain and thrown into the ocean. The four demon lords, servants of Vesh'arkosh, terrorized the land to rid the world of all those who sided with Garrotxa. For a hundred years, the prophets of Garrotxa and the demons fought to control Kashkaval, initiating the \"War of Gods.\" In the end, Vesh'arkosh and his demon lords were killed along with all thirteen prophets of Garrotxa, leaving the Overworld without gods. This was the start of the Second Age. The people of Kashkaval, however, still continued to worship the late Garrotxa for what she represented.")
                    elif option in ("east mural","east text", "east wall"):
                        print("The image shows a set of red, angry eyes overlooking a city gleaming with light. Below, the text reads:\n")
                        print("Fifty years later after the War of Gods, lesser demons, known as vesh'raheen, began to attack the Garrotxian temples across Kashkaval. They would tear apart the bodies of those who visited the temples with their massive claws, and then escape to the safety of the Underworld. Many speculated that one of the demon lords was still alive and planning to make a return, although nothing came to fruition. All the cities and towns were threatened by the vesh'raheen, except the small town of Airedale, making people believe a one of the prophets of Garrotxa was alive as well, but in hiding. This conjecture created both great hope and fear, giving birth to the Third Age.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # roomRoadCorner
                elif room_id == "roomRoadCorner":
                    if option in ("black knight","knight") and not room_current.character_dead and room_current.counter_1:
                        print("He is standing upright with his arms resting on his broadsword. Sunlight reflects off his black armor.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Cavern
                elif room_id == "roomCave_2_llm":
                    if option in ("a body","body","the body","dead body","a dead body","the dead body"):
                        print("The man has several claw marks on his back and arms. The face is mangled and unrecognizable.")
                        if not room_current.item_found:
                            room_current.item_found = True

                            room_current.journal += LOOT_B_JOURNAL
                            room_current.gold += LOOT_B_GOLD
                            print("You search the body and find some supplies.")
                            room_current.items_present()
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomCave__3_lllm_treasure_crevasse":
                    if option in ("chest","treasure chest"):
                        if room_current.item_found:
                            print("It is open.")
                        else:
                            print("It is closed.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomCave_4_mr":
                    if option in ("text","strange text","wall","walls"):
                        print("Written in blood, you can see the words, \"OZH SOL FEK.\"")
                        if not spell_killself:
                            spell_killself = 1
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomCave_6_lllm":
                    if option in ("a body","body","the body","dead body","a dead body","the dead body","corpse"):
                        print("The man is missing an arm and has claw marks on his chest.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            room_current.gold += LOOT_A_GOLD
                            room_current.oil += LOOT_A_OIL
                            print("You search the body and find some supplies.")
                            room_current.items_present()
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomCave_6_m":
                    if option in ("a body","body","the body","dead body","a dead body","the dead body","corpse"):
                        print("The corpse is rotted away, being here for at least a couple months.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            room_current.pickaxe += LOOT_C_PICKAXE
                            room_current.oil += LOOT_C_OIL
                            print("You search the body and find some supplies.")
                            room_current.items_present()
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Lair
                elif room_id == "roomLairWest":
                    if option in ("skeleton","the skeleton"):
                        print("The ribs are all broken, although the rest seems intact. It is spattered in old blood.")
                    elif option in ("table","the table"):
                        print("It's made out of the same stone as the cavern walls.")
                    elif option in ("blood","the blood"):
                        print("It looks fresh.")
                    elif option in ("opening","small opening"):
                        print("Just big enough for you to squeeze through, although probably not much else. You can see a DEAD BODY on the other side.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomLairHole":
                    if option in ("a body","body","the body","dead body","a dead body","the dead body","corpse"):
                        print("The man appears completely unscathed and has perhaps starved to death.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            room_current.oil += LOOT_HOLE_OIL
                            print("You search the body and find some supplies.")
                            room_current.items_present()
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomLairMid":
                    if option in ("backpack","the backpack", "my backpack","creature","the creature"):
                        if room_current.counter_3 and room_current.counter_2:
                            room_current.pickaxe += 1
                            room_current.staff += 1
                            inside = "The staff and your pickaxe are the only items within armsreach, although trying to take them may WAKE UP the creature, which lays unconcious in the way."
                        elif room_current.counter_3:
                            room_current.pickaxe += 1
                            inside = "Your pickaxe is the only item within armsreach, although trying to take it may WAKE UP the creature, which lays unconcious in the way."
                        elif room_current.counter_2:
                            room_current.staff += 1
                            inside = "The staff is the only item within armsreach, although trying to take it may WAKE UP the creature, which lays unconcious in the way."
                        else:
                            inside = "Nothing in the backpack is within armsreach. The creature lays unconcious in the way."
                        print("Your backpack is somewhat visible within a gap in the rubble.",inside)
                        room_current.items_present()
                    elif option in ("a body","body","the body","dead body","a dead body","the dead body","corpse"):
                        print("The man's head has been removed, and claw marks cover the rest of his body.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            room_current.bandage += LOOT_MID_BANDAGE
                            room_current.biscuit += LOOT_MID_BISCUIT
                            print("You search the body and find some supplies.")
                            room_current.items_present()
                    elif option in ("statue","gargoyle","gargoyle statue","pedestal","stone pedestal"):
                        print("It's made out of stone.")
                    elif option in ("statues","gargoyles","gargoyle statues","pedestals","stone pedestals"):
                        print("They're made out of stone.")
                    elif option in ("fountain","obsidian fountain"):
                        print("A mysterious purple fluid flows from it.")
                    elif option in ("fluid","purple fluid"):
                        print("You don't want to know what it is.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomLairEast":
                    if option in ("strange text","text"):
                        print("While it is difficult to make to make the text out, it reads, \"OZH THOK ALATHO.\"")
                        if not spell_jump:
                            spell_jump = 1
                    elif option in ("statue","gargoyle","gargoyle statue","pedestal","stone pedestal"):
                        print("It's made out of stone.")
                    elif option in ("crack","cracks","light","outside"):
                        print("Through the cracks, you can see a grassy field on the other end.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomShrineNorth":
                    if option in ("candles","floating candles"):
                        print("Definitely magical.")
                    elif option in ("pedestal","the pedestal","wall","walls"):
                        print("It's made out of obsidian.")
                    elif option in ("pit","circular pit"):
                        print("It's shallowly filled with water.")
                    elif option == "water":
                        print("The spookiest water you've ever seen.")

                # Field
                elif room_id == "roomRoad2Mid":
                    if option in ("sign","the sign"):
                        print("It reads: \"North: House of Roquefort, West: Fermiere Farm, South: Mount Magna\"")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomFarm":
                    if option in ("field","barren field","soil","ash"):
                        print("The soil is mixed with ash and dead crops.")
                    elif option in ("dead crops","crops"):
                        print("Well, they're certainly not alive.")
                    else:
                        print("You cannot examine that.")
                elif room_id == "roomBarn":
                    if option in ("wall","writing"):
                        print("Burnt into the barn wall reads, \"OZH GROTH SOL.\"")
                        if not spell_light:
                            spell_light = 1
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomBarnUp":
                    if option in ("a body","body","the body","dead body","a dead body","the dead body"):
                        print("Most of it is burnt to a crisp.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            print("You search the body and find a memo.")
                            room_current.memo += 1
                            room_current.items_present()
                            # inv.letterRead = "It reads:\n\nTo whoever is still alive,\n\nBy the time you read this, I will probably be dead. Within the last two weeks, the Ozhkavosh have invaded most of Kashkaval. My greatest fears have come true. Vesh'kathal is alive and has returned to the Overworld. I thought keeping away from the cities of Finn and Fermiere would be a good idea, but the demon lord himself, disguised as my very own son, found me here, tricked me into letting him into the barn, and burnt the whole damn farmland to the ground. I would have travelled down to Airedale, but there's no way I'm crossing that cursed mountain. If you are still alive and well, Airedale may be your last safe haven from the Ozhkavosh. Don't make the same mistake I did."
                    elif option in ("haystacks","hay","stacks of hay","haystack","stack of hay"):
                        print("Most of them are burnt.")
                    elif option in "table":
                        print("It is covered in ash.")
                        if not room_current.item_found:
                            room_current.item_found = True
                            print("You search the body and find a memo.")
                            room_current.memo += 1
                            room_current.items_present()
                    elif option in ("chair","wall","walls"):
                        print("It's made of wood.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # Mysterious book
                elif room_id == "roomBookMirror":
                    if option in ("statue","gargoyle","gargoyle statue") and not room_current.character_dead:
                        print("It's made out of stone.")
                    elif option in ("pile","stone","dust","pile of stone dust","stone dust","pile of dust") and room_current.character_dead:
                        print("Rest in piece Mr. Gargoyle. You will be missed.")
                    elif option == "pedestal" and room_current.item_found:
                        print("It's made out of obsidian.")
                    elif option in ("text","wall","writing"):
                        print("Very faintly, you can see, \"IZH TAL ET OZH ICHA REK'TAL.\"")
                        if not word_mirror:
                            word_mirror = 1
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id.startswith("roomBook_3") and not room_id == "roomBook_3_End":
                    if option.endswith("statue") or option.startswith("statue"):
                        print("It's made out of obsidian.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                # House
                elif room_id == "roomHouseGate":
                    if option == "gate":
                        print("Made out of heavy, metal bars.")
                    elif option in ("metal plaque","plaque"):
                        print("It reads: \"Property of Eden Von Roquefort\"")
                    elif option in ("wall","stone wall","large stone wall","walls","stone walls","large stone walls"):
                        print("It enclosed the entire house.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomHouseFoyer":
                    if option in ("chandilier","glass chandilier","large glass chandilier"):
                        print("It looks as heavy as it is expensive.")
                    elif option in ("carpet","velvet carpet","velvet"):
                        print("With how nice it looks, you feel oddly guilty about standing on it with your dirty shoes.")
                    elif option in ("bust","busts"):
                        print("You do not recognize any of the faces.")
                    elif option in ("paintings","painting"):
                        print("They all show images of cheese.")
                    elif option in ("door","rectangular door","metal door","rectangular metal door"):
                        print("Reminds you of your jail cell.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomHouseKitchen":
                    if option in ("gadget","complicated gadget","gadgets","complicated gadgets"):
                        print("Made out of metal, you do not recognize any of them or understand what they're for.")
                    elif option in ("lever","the lever"):
                        print("It is currently set to the",room_current.counter_1,"position.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomHousePantry":
                    if option in ("cabinet","cabinets","cheese","cheeses"):
                        print("You feel your arteries getting clogged just looking at it all.")
                    elif option in "wall":
                        print("Out of all the things you choose to examine, you choose to examine the wall. How odd.")
                    elif option in "dial":
                        print("It is currently set to" + room_current.counter_1 + ".")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                elif room_id == "roomHouseHallway":
                    if option in ("carpet","velvet carpet","velvet"):
                        print("With how nice it looks, you feel oddly guilty about standing on it with your dirty shoes.")
                    else:
                        print("You cannot examine that.")
                        not_turn = True
                else:
                    print("You cannot examine that.")
                    not_turn = True

        # Read
        elif option.startswith("read"):
            option = option[5:]
            if option.endswith("letter"):
                if inv.letter:
                    print(inv.letterRead)
                else:
                    print("You do not have a letter to read.")
                    not_turn = True
            elif option in ("journal","the journal","1","2","3","4","5","6","journal 1","journal 2","journal 3","journal 4","journal 5","journal 6","journal entry 1","journal entry 2","journal entry 3","journal entry 4","journal entry 5","journal entry 6", ):
                if inv.journal:
                    # Journal Reading interface
                    print("There are six dated entries.\n	1. 31 Friesla 577\n	2. 39 Friesla 577\n	3. 42 Friesla 577\n	4. 43 Friesla 577\n	5. 3 Chaumes 577\n	6. 6 Chaumes 577\n\nWhat would you like to read?")
                    choice_made = False
                    while not choice_made:
                        if not option.endswith(("1","2","3","4","5","6")):
                            option = input("\n> ").lower()
                        if option.endswith("1"):
                            choice_made = True
                            print("31 Friesla 577\n\nThis book is property of Rodney Williams of Pecorino Romano. I have been appointed to investigate reports of strange activity at the Mount Magna mine. While I have no current information about the mine itself, the locals of the nearby town named Airedale may provide some insight.")
                        elif option.endswith("2"):
                            choice_made = True
                            print("39 Friesla 577\n\nI have come across something very strange at the entrance of the mine. Someone, or something, has set up what seems to be an altar or shrine to the Ozkavosh. Various gargoyle statues sat around the room and there was a fountain oozing a mysterious purple fluid. I dared not find out what it was. Most shockingly, I found a partially-eaten human body at a table. We've either got cannibals here, or a vesh'raheen.")
                        elif option.endswith("3"):
                            choice_made = True
                            print("42 Friesla 577\n\nSpent the last few days here in the cavern. Airedale workers were all over the place mining for coal. I told them about the altar at the North entrance, but none of them believed me. I'll need to investigate further.")
                        elif option.endswith("4"):
                            choice_made = True
                            print("43 Friesla 577\n\nThe miners and I have been hearing strange noises in the cave. A few of us have reportedly gone missing. After a heated discussion concerning our safety, we've decided to abandon the mine and return to Airedale. On our way back, I found some writing along one of the cavern walls. \"OZH SOL FEK\" it read. I have no idea what it means.")
                            if not spell_killself:
                                spell_killself = 1
                        elif option.endswith("5"):
                            choice_made = True
                            print("3 Chaumes 577\n\nHaven't written an entry for a while now. The residents of the town have been very fairly nice and hospitable. Crime, however, have become more prevalent since the mine shut down, although the guards seem to keep it in check. Just learned that the mine was the town's central source of income, so a large portion of the population here are now without jobs. Maybe they should starting working in lumber with all the trees around. I tried to get more information about the mine from whoever I could although most don't like to talk about it. I've decided to return back to the cave to get to the bottom of this.")
                        elif option.endswith("6"):
                            choice_made = True
                            print("6 Chaumes 577\n\nA strange creature has been roaming the mines, killing the consuming those it comes it in contact with. While I haven't been able to obtain descriptions of its appearance, I have come across corpses covered in claw marks. Having a source of light seems to keep it away, if only for a while, which I've notified the locals of. That, along with all the growling and screeching I've been hearing, makes me fear this creature may be a vesh'raheen, servant of the Ozkavosh, Vesh'kathal. The problem is that there does not seem to be any reason for a vesh'raheen to be here as they do not live in caves, let alone, anywhere here in Kashkaval. That is, of course, unless Vesh'kathal wants to keep someone from entering or crossing the mines. I will return to Romano Pecorino to report my findings and scale up this investigation. Something very suspicious is happening here.")
                        else:
                            print("Choose 1-6.")
                else:
                    print("You do not have a journal to read.")
                    not_turn = True
            elif option.endswith("book"):
                if inv.book:
                    print("As you stare into the open book, the symbols on the pages consume your mind.")

                    if room_id == "roomBookMirror":
                        # From Mirror puzzle to Movement Puzzle
                        room_id = "roomBook_3_1"
                        room_current = room_book_3_1
                        inv = Inventory(note_1 = vault_answer_1, note_2 = vault_answer_2, note_3 = vault_answer_3, note_4 = vault_answer_4)
                    elif room_id.startswith("roomBook_3"):
                        # From Movement puzzle to outside
                        room_id = room_id_outside
                        room_current = room_current_outside
                        if inv.key_skeleton:
                            inv_outside.key_skeleton = 1
                        else:
                            inv_outside.key_skeleton = 0
                        if inv.book:
                            inv_outside.book = 1
                        inv = inv_outside
                        if room_id_outside.startswith("roomHouse"):
                            silenced = True
                            print("You feel the strange force take over you again.")
                    else:
                        # From outside to inside
                        room_id_outside = room_id
                        room_current_outside = room_current
                        inv_outside = inv
                        if room_book_3_end.first_time: # If puzzle has not been completed
                            room_id = "roomBookMirror"
                            room_current = room_book_mirror
                        else:
                            room_id = "roomBook_3_End"
                            room_current = room_book_3_end
                        inv = Inventory(note_1 = vault_answer_1, note_2 = vault_answer_2, note_3 = vault_answer_3, note_4 = vault_answer_4)
                        if inv_outside.key_skeleton:
                            inv.key_skeleton = 1
                        if room_book_3_end.item_found:
                            inv.book = 1
                        silenced = False
                        print("You feel the strange force leave your body.")
                    room_current.description()
                    room_current.items_present()
            elif option.endswith("note"):
                if inv.note:
                    print(inv.noteRead)
            elif option.endswith("memo"):
                if inv.memo:
                    print(inv.memoRead)
                    if not spell_oblivion:
                        spell_oblivion = 2
            elif option in ("sign", "the sign"):
                if room_id == "roomMountEntrance":
                    print("It reads: \"Mount Magna coal mine is CLOSED. Dangerous CREATURE inside.\"")
                elif room_id == "roomRoadMid":
                    print("The sign reads: \"North: Mount Magna, East: Temple of Garrotxa, West: Lake Laguiole, South: Town of Airedale\"")
                    room_current.item_found = True
                elif room_id == "roomCourtyardNorth":
                    print("The sign reads: \"Come one, come all, to the Wonderful Wheel of Mystery! Want to get rich quick? Spin the wheel test your luck! Only at the Airedale Carnival!\"")
                elif room_id == "roomRoad2Mid":
                    print("It reads: \"North: House of Roquefort, West: Fermiere Farm, South: Mount Magna\"")
                    room_current.item_found = True
                else:
                    print("There is no sign here.")
            elif room_id == "roomLake":
                if option in ("writing","tablet","stone tablet"):
                    print("The writing on the tablet neatly reads, \"OZH VO'SES SA.\"")
                    if not spell_unlock:
                        spell_unlock = 1
                else:
                    print("You cannot read that.")
                    not_turn = True
            elif room_id == "roomTempleInside":
                if option in ("mural","murals","text"):
                    print("Read which one? There is a West, North, and East mural.")
                elif option in ("west mural","west text", "west wall"):
                    print("The image shows a tall woman with a head of a cow, wearing white robes, standing at the top of Mount Magna with outstretched arms. A group of followers, wearing the same robes, bow down around her. Below, the text reads:\n")
                    print("Four a thousand years, the goddess of cheese, Garrotxa, was worshipped peacefully amongst the people of Kashkaval as a herald of propserity, fertility, and music. She lived atop Mount Magna and walked across the fields of Fermiere for most of her days. At the beginning of what most know to be as the First Age, her thirteen most devoted followers were given special robes by the goddess herself, made out of layers of divine cheesecloth. These followers were deemed the prophets of Garrotxa, and were representatives of the main cities throughout Kashkaval.")
                elif option in ("north mural","north text", "north wall"):
                    print("The image shows a giant horned devil with open wings standing in a grassy field. He holds Garrotxa in one hand and a spear in the other. Flames protrude from the ground up into the sky. Below, the text reads:\n")
                    print("The demon king, Vesh'arkosh of the Underworld, jealous of Garrotxa's dominion of the Overworld, emerged to the surface to find her. After a great battle between the two, Garrotxa was slain and thrown into the ocean. The four demon lords, servants of Vesh'arkosh, terrorized the land to rid the world of all those who sided with Garrotxa. For a hundred years, the prophets of Garrotxa and the demons fought to control Kashkaval, initiating the \"War of Gods.\" In the end, Vesh'arkosh and his demon lords were killed along with all thirteen prophets of Garrotxa, leaving the Overworld without gods. This was the start of the Second Age. The people of Kashkaval, however, still continued to worship the late Garrotxa for what she represented.")
                elif option in ("east mural","east text", "east wall"):
                    print("The image shows a set of red, angry eyes overlooking a city gleaming with light. Below, the text reads:\n")
                    print("Fifty years later after the War of Gods, lesser demons, known as vesh'raheen, began to attack the Garrotxian temples across Kashkaval. They would tear apart the bodies of those who visited the temples with their massive claws, and then escape to the safety of the Underworld. Many speculated that one of the demon lords was still alive and planning to make a return, although nothing came to fruition. All the cities and towns were threatened by the vesh'raheen, except the small town of Airedale, making people believe a one of the prophets of Garrotxa was alive as well, but in hiding. This conjecture created both great hope and fear, giving birth to the Third Age.")
                else:
                    print("You cannot read that.")
                    not_turn = True
            elif room_id == "roomCave_4_mr":
                if option in ("text","strange text","wall","walls"):
                    print("Written in blood, you can see the words, \"OZH SOL FEK.\"")
                    if not spell_killself:
                        spell_killself = 1
                else:
                    print("You cannot read that.")
                    not_turn = True
            elif room_id == "roomLairEast":
                if option in ("strange text","text","wall"):
                    print("While it is difficult to make to make the text out, it reads, \"OZH THOK ALATHO.\"")
                    if not spell_jump:
                        spell_jump = 1
                else:
                    print("You cannot read that.")
                    not_turn = True
            elif room_id == "roomBarn":
                    if option in ("wall","writing"):
                        print("Burnt into the barn wall reads, \"Ozh groth sol.\"")
                        if not spell_light:
                            spell_light = 1
                    else:
                        print("You cannot read that.")
                        not_turn = True
            elif room_id == "roomBookMirror":
                if option in ("text","wall","writing"):
                        print("Very faintly, you can see, \"Izh tal et ozh icha rek'tal.\"")
                        if not word_mirror:
                            word_mirror = 1
                else:
                    print("You cannot read that.")
                    not_turn = True
            elif room_id == "roomHouseGate":
                if option in ("metal plaque","plaque"):
                    print("It reads: \"Property of Eden Von Roquefort\"")
                else:
                    print("You cannot read that.")
                    not_turn = True
            else:
                print("You cannot read that.")
                not_turn = True
        # Walk, Move, Go
        elif option in ("north","n","east","e","south","s","west","w","up","u","down","d") or option.startswith("walk") or option.startswith("move") or option.startswith("go"):
            if option.startswith("walk") or option.startswith("move"):
                option = option[5:]
            elif option.startswith("go"):
                option = option[3:]
            # Sets walk direction
            direction_blocked = False
            if option in ("north","n"):
                direction = "North"
                if room_id == "roomLairHole":
                    if inv.item_types() > 1:
                        room_current.north_blocked = True
                    else:
                        room_current.north_blocked = False
                if room_current.north and not room_current.north_blocked:
                    room_id = room_current.north
                    change_room = True
                elif room_current.north_blocked:
                    direction_blocked = True
            elif option in ("east","e"):
                direction = "East"
                if room_current.east and not room_current.east_blocked:
                    room_id = room_current.east
                    change_room = True
                elif room_current.east_blocked:
                    direction_blocked = True
            elif option in ("south","s"):
                direction = "South"
                if room_id == "roomLairWest":
                    if inv.item_types() > 1:
                        room_current.south_blocked = True
                    else:
                        room_current.south_blocked = False
                if room_current.south and not room_current.south_blocked:
                    room_id = room_current.south
                    change_room = True
                elif room_current.south_blocked:
                    direction_blocked = True
            elif option in ("west","w"):
                direction = "West"
                if room_current.west and not room_current.west_blocked:
                    room_id = room_current.west
                    change_room = True
                elif room_current.west_blocked:
                    direction_blocked = True
            elif option in ("up","u"):
                direction = "up"
                if room_current.up and not room_current.up_blocked:
                    room_id = room_current.up
                    change_room = True
                elif room_current.up_blocked:
                    direction_blocked = True
            elif option in ("down","d"):
                direction = "down"
                if room_current.down and not room_current.down_blocked:
                    room_id = room_current.down
                    change_room = True
                elif room_current.down_blocked:
                    direction_blocked = True
            elif option == "":
                print("Go where?")
            else:
                print("You cannot go there.")
                not_turn = True
            if not change_room and direction in ("North","East","South","West","up","down") and not direction_blocked:
                print("You cannot go %s." % direction)
                not_turn = True
        # Use, Mine, Unlock
        # Mine pickaxe to get coal if in mine
        # Unlock doors
        elif option.startswith(("use","unlock","mine","throw","light","fire","shoot","heal")):
            use = False
            unlock = False
            mine = False
            throw = False
            light = False
            fire = False
            shoot = False
            heal = False
            if option.startswith("use"):
                option = option[4:]
                if option == "":
                    print("Use what?")
                    not_turn = True
                else:
                    use = True
            elif option.startswith("unlock"):
                option = option[7:]
                if option == "":
                    print("Unlock what?")
                    not_turn = True
                else:
                    unlock = True
            elif option.startswith("mine"):
                option = option[5:]
                if option == "":
                    print("Mine what?")
                    not_turn = True
                else:
                    mine = True
            elif option.startswith("throw"):
                option = option[6:]
                if option == "":
                    print("Throw what?")
                    not_turn = True
                else:
                    throw = True
            elif option.startswith("light"):
                option = option[6:]
                if option == "":
                    print("Light what?")
                    not_turn = True
                else:
                    light = True
            elif option.startswith("fire"):
                option = option[5:]
                if option == "":
                    print("Fire what?")
                    not_turn = True
                else:
                    fire = True
            elif option.startswith("shoot"):
                option = option[6:]
                if option == "":
                    print("Shoot what?")
                    not_turn = True
                else:
                    shoot = True
            elif option.startswith("heal"):
                option = option[5:]
                heal = True
            # Use/unlock key to unlock roomJailCell
            if (use and option.startswith("key")) or unlock:
                if room_id == "roomJailCell" and room_jail_cell.east_blocked:
                    if inv.key or inv.key_skeleton:
                        room_jail_cell.east_blocked = False
                        print("You unlock the cell door.")
                        print("You can now go East.")
                        if not room_current.counter_1 and not player_name:
                            room_jail_corridor.letter += 1
                            room_current.counter_ans_1 = 1
                    else:
                        print("You cannot unlock the cell door without a key.")
                        not_turn = True
                elif room_id == "roomHouseEntrance" and room_house_entrance.north_blocked:
                    if inv.key_skeleton:
                        room_house_entrance.north_blocked = False
                        print("You unlock the house door. The key of Ahm'domosh disintegrates, returing to the Underworld.")
                        inv.key_skeleton -= 1
                    elif inv.key:
                        print("You cannot unlock the house door with your jail cell key.")
                        not_turn = True
                    else:
                        print("You cannot unlock the house door with a key.")
                elif room_id == "roomHouseGate" and room_house_gate.north_blocked:
                    if inv.key_skeleton:
                        room_house_gate.north_blocked = False
                        print("You unlock the gate with the key of Ahm'domosh.")
                    elif inv.key:
                        print("You cannot unlock the gate with your jail cell key.")
                        not_turn = True
                    else:
                        print("You cannot unlock the gate without a key.")
                        not_turn = True
                elif room_id == "roomLake" and not room_current.counter_1:
                    if inv.key_skeleton:
                        room_current.counter_1 = 1
                        print("You unlock the lockbox with the key of Ahm'domosh.")
                    elif inv.key:
                        print("You cannot unlock the lockbox with your jail cell key.")
                        not_turn = True
                    else:
                        print("You cannot unlock the lockbox without a key.")
                        not_turn = True
                elif room_id == "roomHouseHallway":
                    print("You do not have a key.")
                else:
                    print("There is nothing here to unlock.")
            # Use bandage to heal wounds
            elif (heal and option in ("","wounds","wound","bleeding","injury","self")) or (use and option in ("bandage","bandages")):
                if inv.bandage:
                    if stat.health < stat.healthmax:
                        stat.health = stat.healthmax
                        inv.bandage -= 1
                        print("You apply a bandage to your wound to stop the bleeding.")
                    else:
                        print("You are not injured.")
                        not_turn = True
                else:
                    print("You do not have any bandages.")
                    not_turn = True
            # Use oil to light lantern
            elif (use and (option.startswith("oil") or option.startswith("vial") or option.endswith("oil"))) or (light and option.startswith("lantern")):
                if inv.oil:
                    if inv.lantern:
                        if oil_counter == 0:
                            print("You fill your lantern with a vial of oil, and light it. It starts to burn.")
                        else:
                            print("You top up your lantern with a vial of oil. It continues to burn.")
                        oil_counter += OIL_DURATION
                        inv.oil -= 1
                    else:
                        print("You do not have a lantern.")
                        not_turn = True
                else:
                    print("You do not have any vials of lantern oil.")
                    not_turn = True
            # Use/Throw grappling hook to get across crevasse
            elif (use or throw) and option.startswith("grappling hook") or option.startswith("hook"):
                if inv.hook:
                    if room_current.is_crevasse:
                        if room_current.north_blocked or room_current.east_blocked or room_current.west_blocked or room_current.south_blocked:
                            room_current.north_blocked = False
                            room_current.east_blocked = False
                            room_current.west_blocked = False
                            room_current.south_blocked = False
                            print("You throw the grappling hook across the crevasse, which catches on a stalagmite on the other end. You tie the rope on a stalagmite on your end, opening a way across.")
                            inv.hook -= 1
                            room_current.hook += 1
                            room_current.items_present()
                        else:
                            print("You can already cross the crevasse.")
                            not_turn = True
                    else:
                        print("You cannot throw a grappling hook here.")
                        not_turn = True
                else:
                    print("You do not have a grappling hook.")
                    not_turn = True
            # Use/Mine with pickaxe
            elif (use or mine) and option in ("pickaxe","pick","vein","veins","coal","coal vein","coal veins","rubble","rocks","rock"):
                if inv.pickaxe:
                    if room_current.is_mine:
                        if ((use and option in ("pickaxe","pick")) or (mine and option in ("vein","veins","coal","coal vein","coal veins"))) and room_id.endswith("coalmine"): # coal
                            if random.randint(1,100) > PICKAXE_BREAK_CHANCE:
                                room_current.counter_1 -= 1
                                inv.coal += 1
                                print("You mine away at the coal vein and get a piece of coal.")
                                if inv.coal > 1:
                                    print("You have",inv.coal,"pieces of coal.")
                                else:
                                    print("You have 1 piece of coal.")
                                if not room_current.counter_1:
                                    room_current.is_mine = False
                                    print("There is no more coal left.")
                            else:
                                inv.pickaxe -= 1
                                print("You mine away at the coal vein and break your pickaxe.")
                                if inv.pickaxe > 1:
                                    print("You have",inv.pickaxe,"spare pickaxes.")
                                elif inv.pickaxe:
                                    print("You have a spare pickaxe.")
                                else:
                                    print("You have no spare pickaxe.")
                        elif (use and option in ("pickaxe","pick")) or (mine and option in ("rubble","rocks","rock")): # rubble
                            room_current.counter_1 -= 1
                            print("You mine away at the rubble, breaking apart some of the rock.")
                            if not room_current.counter_1:
                                room_current.is_mine = False
                                room_current.north_blocked = False
                                print("The opening is now large enough to go through.")
                                print("You can now go North.")
                        elif mine:
                            print("You cannot mine that.")
                            not_turn = True
                        elif use:
                            print("You cannot use that.")
                            not_turn = True
                    else:
                        print("You cannot mine anything here.")
                        not_turn = True
                elif mine:
                    print("You cannot mine anything without a pickaxe.")
                    not_turn = True
                else:
                    print("You cannot use that.")
                    not_turn = True
            # Use staff on characters in room
            elif (use or fire or shoot) and option.startswith("the staff") or option.startswith("staff"):
                if inv.staff:
                    if not room_current.character_dead or room_id == "roomHouseOffice" or room_id.startswith("roomLair") or (room_id.startswith("roomCave") and creature_chase_counter in [1,2]) or (room_id.startswith("roomJail") and jail_guard_counter in [1,2]):
                        room_current.character_dead = True
                        print("A bolt of lightning fires out from the staff, striking ",end = "")
                        if room_id == "roomCarnivalShellGame":
                            print("the old woman. As she topples over, all her gold is spilled across the ground.")
                            room_current.is_bet = False
                            room_current.gold += inv_shell.gold
                            inv_shell.gold = 0
                            room_current.items_present()
                        elif room_id.startswith("roomJail"):
                            print("a jail guard. The rest surround you and take you down.")
                            end_game = True
                        elif room_id == "roomCarnivalWheelGame":
                            print("the man. The crowd goes into panic as guards enter the tent and overwhelm you.")
                            end_game = True
                        elif room_id == "roomCarnivalFood":
                            print("the vendor. He falls over, leaving his supply of food behind.")
                            room_current.is_buy = False
                            room_current.funnel_cake += inv_food.funnel_cake
                            inv_food.funnel_cakes = 0
                            room_current.pie += 10
                            room_current.items_present()
                        elif room_id == "roomBridge":
                            print("the troll. It falls over, dropping the funnel cakes in its hands.")
                            room_current.east_blocked = False
                            room_current.funnel_cake += 1
                            room_current.half_funnel_cake += 3
                            room_current.items_present()
                        elif room_id == "roomGeneralStore":
                            print("the shopkeeper, leaving his store supplies behind.")
                            room_current.is_buy = False
                            room_current.is_sell = False
                            room_current.oil += 5
                            room_current.foot += 5
                            room_current.lantern += 1
                            room_current.bandage += 5
                            room_current.items_present()
                        elif room_id == "roomBlacksmith":
                            print("the blacksmith, leaving his supplies behind.")
                            room_current.is_buy = False
                            room_current.is_sell = False
                            room_current.pickaxe += 2
                            room_current.hook += 3
                            room_current.items_present()
                        elif room_id == "roomAlchemist":
                            print("Tim the Enchanter, leaving his supplies behind.")
                            room_current.is_buy = False
                            room_current.is_fill = False
                            room_current.is_sell = False
                            room_current.potion += 3
                            room_current.flask += 4
                            room_current.items_present()
                        elif room_id in ("roomCarnival","roomCourtyardNorth","roomCourtyardSouth"):
                            print("a random civilian. The loud noise alerts the town guards, who catch up to you and kill you.")
                            end_game = True
                        elif room_id == "roomGate":
                            print("the gate guard. Another nearby guard one draws his sword and impales you.")
                            end_game = True
                        elif room_id == "roomRoadCorner" and room_road_corner.counter_1:
                            print("the black knight. He shouts, \"IZH VO'POZ!\" before his body vaporizes into nothing.")
                            if not spell_persuade:
                                spell_persuade = 1
                            room_road_corner.west_blocked = False
                        elif room_id == "roomHouseOffice":
                            room_current.counter_2 += 1
                            if room_current.counter_2 == 1:
                                print("Eden Von Roquefort. His dead body flies back and crashes on the desk.")
                            elif room_current.counter_2 == 2:
                                print("Vesh'kathal. She resists the shock and charges towards you, knocking the staff out of your hand and onto the floor. The holy staff merely touching her arm causes her scales to burn, making her to topple over in pain.")
                                inv.staff -= 1
                                room_current.staff += 1
                                room_current.items_present()
                            else:
                                print("Vesh'kathal. She is severly weaked, but manages to stay alive.")
                        elif room_id.startswith("roomCave"):
                            print("the creature, which resists the shock. It only gets angrier.")
                        elif room_id.startswith("roomLair"):
                            print("the creature, which resists the shock. It only gets angrier.")
                            if not room_lair_chase:
                                room_lair_chase = True
                        elif room_id == "roomLake":
                            print("the stranger, leaving his supplies behind.")
                            room_current.pie += 1
                            room_current.items_present()
                    else:
                        print("There's no one else here.")
                else:
                    print("You do not have the staff of Garrotxa.")
                    not_turn = True
            else:
                if use:
                    print("You cannot use that.")
                elif unlock:
                    print("You cannot unlock that.")
                elif mine:
                    print("You cannot mine that.")
                elif throw:
                    print("You cannot throw that.")
                elif light:
                    print("You cannot light that.")
                elif heal:
                    print("You cannot heal that.")
                not_turn = True
        # Turn, set
        # Unlock vault in roomCorridor
        elif option.startswith("turn") or option.startswith("rotate") or option.startswith("set") or option.startswith("change") or option.startswith("push") or option.startswith("pull"):
            if option.startswith("turn"):
                option = option[5:]
                if option == "":
                    print("Turn what?")
                    not_turn = True
                elif room_id not in ("roomMountEntrance","roomHousePantry"):
                    print("You cannot turn that.")
                    not_turn = True
            elif option.startswith("rotate"):
                option = option[7:]
                if option == "":
                    print("Rotate what?")
                    not_turn = True
                elif room_id not in ("roomMountEntrance","roomHousePantry"):
                    print("You cannot rotate that.")
                    not_turn = True
            elif option.startswith("set"):
                option = option[4:]
                if option == "":
                    print("Set what?")
                    not_turn = True
                elif room_id not in ("roomMountEntrance","roomHousePantry","roomHouseKitchen"):
                    print("You cannot set that.")
                    not_turn = True
            elif option.startswith("change"):
                option = option[7:]
                if option == "":
                    print("Change what?")
                    not_turn = True
                elif room_id not in ("roomMountEntrance","roomHousePantry","roomHouseKitchen"):
                    print("You cannot change that.")
                    not_turn = True
            elif option.startswith("push"):
                option = option[5:]
                if option == "":
                    print("Push what?")
                    not_turn = True
                elif room_id not in ("roomHousePantry","roomHouseKitchen"):
                    print("You cannot push that.")
                    not_turn = True
            elif option.startswith("pull"):
                option = option[5:]
                if option == "":
                    print("Pull what?")
                    not_turn = True
                elif room_id not in ("roomHousePantry","roomHouseKitchen"):
                    print("You cannot pull that.")
                    not_turn = True
            if option != "":
                if room_id == "roomMountEntrance":
                    # Set numbers in vault in roomMountEntrance
                    change_vault_1 = False
                    change_vault_2 = False
                    change_vault_3 = False
                    change_vault_4 = False
                    if option.startswith("dial 1 to"):
                        option = option[10:]
                        change_vault_1 = True
                    elif option.startswith("first dial to"):
                        option = option[14:]
                        change_vault_1 = True
                    elif option.startswith("dial 2 to"):
                        option = option[10:]
                        change_vault_2 = True
                    elif option.startswith("second dial to"):
                        option = option[15:]
                        change_vault_2 = True
                    elif option.startswith("dial 3 to"):
                        option = option[10:]
                        change_vault_3 = True
                    elif option.startswith("third dial to"):
                        option = option[14:]
                        change_vault_3 = True
                    elif option.startswith("dial 4 to"):
                        option = option[10:]
                        change_vault_4 = True
                    elif option.startswith("fourth dial to"):
                        option = option[15:]
                        change_vault_4 = True
                    if option == "":
                        if change_vault_1:
                            print("Change first dial to what?")
                            not_turn = True
                        elif change_vault_2:
                            print("Change second dial to what?")
                            not_turn = True
                        elif change_vault_3:
                            print("Change third dial to what?")
                            not_turn = True
                        elif change_vault_4:
                            print("Change fourth dial to what?")
                            not_turn = True
                    elif option.isdigit():
                        option = int(option)
                        if option in range(10):
                            if change_vault_1:
                                if room_current.counter_1 == option:
                                    print("The first dial is already set to %s." % option)
                                else:
                                    room_current.counter_1 = option
                                    print("You set first dial to %i." % option)
                            elif change_vault_2:
                                if room_current.counter_2 == option:
                                    print("The second dial is already set to %s." % option)
                                else:
                                    room_current.counter_2 = option
                                    print("You set the second dial to %i." % option)
                            elif change_vault_3:
                                if room_current.counter_3 == option:
                                    print("The third dial is already set to %s." % option)
                                else:
                                    room_current.counter_3 = option
                                    print("You set the third dial to %i." % option)
                            elif change_vault_4:
                                if room_current.counter_4 == option:
                                    print("The fourth dial is already set to %s." % option)
                                else:
                                    room_current.counter_4 = option
                                    print("You set the fourth dial to %i." % option)
                            print("\nThe first dial reads %s." % room_current.counter_1)
                            print("The second dial reads %s." % room_current.counter_2)
                            print("The third dial reads %s." % room_current.counter_3)
                            print("The fourth dial reads %s." % room_current.counter_4)
                        else:
                            print("You cannot do that.")
                            not_turn = True
                    else:
                        print("You cannot do that.")
                        not_turn = True
                    if (room_current.counter_1, room_current.counter_2, room_current.counter_3, room_current.counter_4) == (room_current.counter_ans_1, room_current.counter_ans_2, room_current.counter_ans_3, room_current.counter_ans_4) and room_current.north_blocked:
                        print("\nYou hear a loud clunk, as the vault door creaks open.")
                        print("You can now to North.")
                        room_current.north_blocked = False
                elif room_id == "roomHousePantry":
                    change_dial = False
                    if option.startswith("dial to"):
                        option = option[8:]
                    elif option.startswith("dial"):
                        option = option[5:]
                    if option == "":
                        print("Change dial to what?")
                        not_turn = True
                    elif option == "green":
                        if not room_current.counter_1 == "GREEN":
                            room_current.counter_1 = "GREEN"
                            change_dial = True
                    elif option == "red":
                        if not room_current.counter_1 == "RED":
                            room_current.counter_1 = "RED"
                            change_dial = True
                    elif option == "blue":
                        if not room_current.counter_1 == "BLUE":
                            room_current.counter_1 = "BLUE"
                            change_dial = True
                    else:
                        print("You cannot change the dial to" + option + ".")
                    if option in ("green","red","blue"):
                        if change_dial:
                            print("You set the dial to " + option + ".")
                        else:
                            print("The dial is already set to " + option + ".")
                if room_house_pantry.counter_1 == DIAL_ANSWER and room_house_kitchen.counter_1 == LEVER_ANSWER and room_house_foyer.north_blocked:
                    print("You hear a loud metalic clunk echo from the foyer.")
                    room_house_foyer.north_blocked = False
                elif room_id == "roomHouseKitchen":
                    if option.startswith("lever to"):
                        option = option[9:]
                    elif option.startswith("lever"):
                        option = option[6:]

                    if option == "":
                        print("Change lever to what?")
                        not_turn = True
                    elif option in ("forward","forwards"):
                        if room_current.counter_1 == "FORWARD":
                            print("The lever is already set to the forward position.")
                        else:
                            room_current.counter_1 = "FORWARD"
                            print("You set the lever to the forward position.")
                    elif option in ("backward","back","backwards"):
                        if room_current.counter_1 == "BACKWARDS":
                            print("The lever is already set to the backwards position.")
                        else:
                            room_current.counter_1 = "BACKWARDS"
                            print("You set the lever to the backwards position.")

                    else:
                        print("You cannot change the lever to " + option + ".")
                    if room_house_pantry.counter_1 == DIAL_ANSWER and room_house_kitchen.counter_1 == LEVER_ANSWER and room_house_foyer.north_blocked:
                        print("You hear a loud metalic clunk echo from the foyer.")
                        room_house_foyer.north_blocked = False


        # Open
        # Treasure chest in roomCave__3_lllm_treasure_crevasse
        elif option.startswith("open"):
            option = option[5:]
            if room_id == "roomCave__3_lllm_treasure_crevasse":
                if option in ("chest","treasure chest","the chest","the treasure chest"):
                    if room_current.counter_1:##continue ##
                        if not room_current.item_found:
                            room_current.item_found = True
                            room_current.gold += CHEST_REWARD
                            room_current.stone += 1
                            print("The rusted hinges of the chest break as the heavy lid of the chest swings back. You find something inside.")
                            room_current.items_present()
                        else:
                            print("The treasure chest is already open.")
                            not_turn = True
                    else:
                        print("The chest is locked.")
                else:
                    print("You cannot open that.")
                    not_turn = True
            elif room_id == "roomLake":
                if option in ("lockbox","box"):
                    if not room_current.counter_1: # not unlocked (locked)
                        print("You cannot open the lockbox. It is locked.")
                    else: # unlocked
                        if room_current.counter_2 == 1: # open
                            print("It is already open.")
                        else:
                            room_current.counter_2 = 1 # is now open
                            if room_current.item_found:
                                print("You open the lockbox.")
                            else:
                                print("You open the lockbox and find some gold inside.")
                                room_current.gold += LAKE_GOLD_REWARD
                                room_current.item_found = True
                                room_current.items_present()
                else:
                    print("You cannot open that.")
                    not_turn = True

            else:
                print("You cannot open that.")
                not_turn = True
        # Close
        # Treasure chest in roomCave__3_lllm_treasure_crevasse
        elif option.startswith("close"):
            option = option[6:]
            if room_id == "roomCave__3_lllm_treasure_crevasse":
                if option in ("chest","treasure chest","the chest","the treasure chest"):
                    if not room_current.item_found:
                        print("The treasure chest is already closed.")
                        not_turn = True
                    else:
                        print("The rusted hinges of the chest are broken, making it unable to close.")
                else:
                    print("You cannot close that.")
                    not_turn = True
            elif room_id == "roomLake":
                if not room_current.counter_2:
                    print("It is already closed.")
                else:
                    room_current.counter_2 = 0
                    print("You close the lockbox.")
            else:
                print("You cannot close that.")
                not_turn = True
        # Eat
        # Eat food to regain hunger
        elif option.startswith("eat"):
            if stat.hunger > HUNGER_MAX:
                print("You are too full to eat anything.")
            else:
                option = option[4:]
                food_empty = False
                if option in ("cake","cakes","funnel cake","funnel cakes"):
                    food_name = "funnel cake"
                    if inv.funnel_cake:
                        inv.funnel_cake -= 1
                        stat.hunger += HUNGER_FUNNELCAKE
                    elif inv.half_funnel_cake:
                        inv.half_funnel_cake -= 1
                        stat.hunger += HUNGER_HALFFUNNELCAKE
                    else:
                        food_empty = True
                elif option in ("half-eaten cake","half cake","half-eaten funnel cake","half eaten funnel cake","half funnel cake","half-eaten cakes","half cakes","half-eaten funnel cakes","half eaten funnel cakes","half funnel cakes"):
                    food_name = "half-eaten funnel cake"
                    if inv.half_funnel_cake:
                        inv.half_funnel_cake -= 1
                        stat.hunger += HUNGER_HALFFUNNELCAKE
                    else:
                        food_empty = True
                elif option in ("porridge","bowl of porridge"):
                    food_name = "bowl of porridge"
                    if inv.porridge:
                        inv.porridge -= 1
                        inv.bowl += 1
                        stat.hunger += HUNGER_PORRIDGE
                    else:
                        food_empty = True
                elif option in ("bowl","porridge bowl"):
                    food_name = "bowl"
                    if not (inv.bowl or inv.porridge):
                        food_empty = True
                elif option in ("pie","pies","chicken","chicken pot","chicken pot pie"):
                    food_name = "chicken pot pie"
                    if inv.pie:
                        inv.pie -= 1
                        stat.hunger += HUNGER_PIE
                    else:
                        food_empty = True
                elif option in ("hardtack biscuit","hardtack biscuits","biscuit","biscuits","hardtack"):
                    food_name = "hardtack biscuit"
                    if inv.biscuit:
                        inv.biscuit -= 1
                        stat.hunger += HUNGER_BISCUIT
                    else:
                        food_empty = True
                elif option in ("potato","rotten potato"):
                    food_name = "potato"
                    if not inv.potato:
                        food_empty = True
                elif option in ("brie","slice of brie","slice of brie cheese", "brie cheese"):
                    food_name = "slice of brie cheese"
                    if inv.brie:
                        inv.brie -= 1
                        stat.hunger += HUNGER_CHEESE
                    else:
                        food_empty = True
                elif option in ("munster","slice of munster","slice of munster cheese","munster cheese"):
                    food_name = "slice of munster cheese"
                    if inv.munster:
                        inv.munster -= 1
                        stat.hunger += HUNGER_CHEESE
                    else:
                        food_empty = True
                elif option in ("stilton","slice of stilton","slice of stilton cheese","stilton cheese"):
                    food_name = "slice of stilton cheese"
                    if inv.stilton:
                        inv.stilton -= 1
                        stat.hunger += HUNGER_CHEESE
                    else:
                        food_empty = True
                elif option in ("swiss","slice of swiss","slice of swiss cheese","swiss cheese"):
                    food_name = "slice of swiss cheese"
                    if inv.swiss:
                        inv.swiss -= 1
                        stat.hunger += HUNGER_CHEESE
                elif option in ("wensleydale","slice of wensleydale","slice of wensleydale cheese","wensleydale cheese"):
                    food_name = "slice of wensleydale cheese"
                    if inv.wensleydale:
                        inv.wensleydale -= 1
                        stat.hunger += HUNGER_CHEESE
                elif option in ("potion","potion of rejuvination","potions","potions of rejuvination"):
                    food_name = "potion of rejuvination"
                    if not inv.potion:
                        food_empty = True
                elif option == "":
                    food_name = "null"
                else:
                    food_name = "invalid"
                if food_empty:
                    print("You have no " + food_name + " to eat.")
                    not_turn = True
                elif food_name in ("potato","rotten potato"):
                    print("You eat the rotten potato and quickly feel sick to your stomach. You thought the five second rule was a thing? What about the 5 month rule?")
                    end_game = True
                elif food_name == "potion of rejuvination":
                    print("While the potion may be rather thick, you can't eat a liquid. Well, I guess you could, much the chewing motions would be be kind of a waste of energy.")
                    not_turn = True
                elif food_name == "bowl":
                    print("Despite how hungry you may be, you can't actually eat the bowl itself, considering it's made out of metal.")
                    not_turn = True
                elif food_name == "null":
                    print("Eat what?")
                    not_turn = True
                elif food_name == "invalid":
                    print("You cannot eat that.")
                    not_turn = True
                elif food_name not in ("null","nomessage"):
                    print("You eat a " + food_name + ".")
        # Drink
        # Potion
        elif option.startswith("drink"):
            if stat.hunger > HUNGER_MAX:
                print("You are too full to drink anything.")
            else:
                option = option[6:]
                drink_empty = False
                if option in ("potion","potion of rejuvination"):
                    drink_name = "potion of rejuvination"
                    if inv.potion:
                        inv.potion -= 1
                        inv.flask += 1
                        stat.hunger += HUNGER_POTION
                        stat.health = HEALTH_MAX
                        stat.shield += HUNGER_POTION
                    else:
                        drink_empty = True
                elif option in ("fluid","mysterious fluid","purple fluid","mysterious purple fluid") and room_id == "roomLairMid":
                    print("So you wake up after after being chased by a creature and find yourself in a pretty creepy place with a strange-looking fountain and you think to yourself, \"Oh geez, you know what I should do? Drink this mysterious purple fluid and see what happens. Surely nothing bad. Obviously this is how I escape. Oh wait, that's a terrible idea.\" You reconsider your live decisions.")
                    drink_name = "nomessage"
                elif option == "":
                    drink_name = "null"
                else:
                    drink_name = "invalid"
                if drink_empty:
                    print("You have no " + drink_name + " to drink.")
                    not_turn = True
                elif drink_name == "invalid":
                    print("You cannot drink that.")
                    not_turn = True
                elif drink_name == "null":
                    print("Drink what?")
                    not_turn = True
                elif drink_name not in ("null","nomessage"):
                    if drink_name == "potion of rejuvination":
                        shield_message = "You feel an aura of energy surround you, PROTECTING you from HARM."
                    else:
                        shield_message = ""
                    print("You drink a " + drink_name + ".",shield_message)

        # Fill/Refill
        # Exchange flask for potion
        elif option.startswith("fill") or option.startswith("refill"):
            if option.startswith("fill"):
                option = option[5:]
            else:
                option = option[7:]
            if room_current.is_fill:
                if option == "":
                    print("Fill what?")
                    not_turn = True
                else:
                    fill_flask = False
                    if option in ("flask","empty flask"):
                        fill_count = 1
                        fill_flask = True
                    elif option in ("flasks","empty flasks","all flasks","every flask"):
                        fill_count = inv.flask
                        fill_flask = True
                    elif option.endswith("flask"):
                        fill_count = option[:len(option) - len("flask") - 1]
                        fill_flask = True
                    elif option.endswith("flasks"):
                        fill_count = option[:len(option) - len("flasks") - 1]
                        fill_flask = True
                    elif option.endswith("empty flask"):
                        fill_count = option[:len(option) - len("empty flask") - 1]
                        fill_flask = True
                    elif option.endswith("empty flasks"):
                        fill_count = option[:len(option) - len("empty flasks") - 1]
                        fill_flask = True
                    if fill_flask:
                        if fill_flask:
                            item_fill_name = "flask"
                            items_fill_name = "flasks"
                            item_return_name = "potion of rejuvination"
                            items_return_name = "potions of rejuvination"
                            inv_item_fill = inv.flask
                            inv_item_return = inv.potion
                    item_in_store = False
                    if room_id == "roomAlchemist":
                        shop_keeper_name = "Tim the Enchanter"
                        if fill_flask:
                            item_in_store = True
                    if item_in_store:
                        fill_item_count_okay = False
                        try:
                            fill_count = float(fill_count)
                            if float(fill_count) % 1 == 0 and fill_count > 0:
                                fill_item_count_okay = True
                                fill_count = int(fill_count)
                            else:
                                if fill_count:
                                    print("You cannot fill",fill_count,"%s." % items_fill_name)
                                    not_turn = True
                        except ValueError:
                            print("You cannot fill \"" + fill_count + "\" %s." % items_fill_name)
                        if fill_item_count_okay:
                            if inv.flask >= fill_count:
                                if inv.gold >= fill_count * price:
                                    if fill_count > 1:
                                        print("You give",shop_keeper_name,fill_count * price,"gold and",fill_count,items_fill_name,"to fill. He gives you",fill_count,"potions of rejuvination in return.")
                                    elif fill_count == 1:
                                        print("You give",shop_keeper_name,fill_count * price,"gold and a",item_fill_name,"to fill. He gives you a potion of rejuvination in return.")
                                    if fill_flask:
                                        inv.potion += fill_count
                                        inv.flask -= fill_count
                                        inv_item_fill -= fill_count
                                        inv_item_return += fill_count
                                        inv.gold -= fill_count * price
                                    if inv_item_return:
                                        if inv_item_return == 1:
                                            print("You have",inv_item_return,item_return_name,"and",inv.gold,"gold.")
                                        else:
                                            print("You have",inv_item_return,items_return_name,"and",inv.gold,"gold.")
                                    if inv_item_fill:
                                        if inv_item_fill == 1:
                                            print("You have",inv_item_fill,item_fill_name + ".")
                                        else:
                                            print("You have",inv_item_fill,items_fill_name + ".")
                                    print("You have",inv.gold,"gold.")
                                else:
                                    if fill_count > 1:
                                        print("You do not have enough gold to fill",fill_count,"%s." % items_name)
                                    else:
                                        print("You do not have enough gold to fill a %s." % item_name)
                            else:
                                if fill_count > 1:
                                    print("You do not have",fill_count,"flasks to fill.")
                                    not_turn = True
                                else:
                                    print("You do not have any flasks to fill.")
                                    not_turn = True

            else:
                # If not isFill
                print("You cannot fill anything here.")
                not_turn = True
        # Take, Get
        # Move items from room to inventory
        elif option.startswith(("take","get","pick up","grab","obtain","acquire")):
            if option.startswith("take"):
                option = option[5:]
            elif option.startswith("get"):
                option = option[4:]
            elif option.startswith("pick up"):
                option = option[8:]
            elif option.startswith("grab"):
                option = option[5:]
            elif option.startswith("obtain"):
                option = option[7:]
            elif option.startswith("acquire"):
                option = option[8:]
            item_name = False
            items_name = False
            inv_item = False
            room_item = False
            take_count = 0
            # All/Everything
            if option in ("all","everything") and room_current.item_types():
                if room_id == "roomTempleBasement" and not room_current.character_dead and room_current.staff:
                    print("\"You are not worthy to take the staff!\" The figure zaps you with a bolt of electricity.")
                    stat.lower_health()
                elif room_id == "roomLairMid" and room_current.counter_2 and not room_lair_chase and room_current.staff and room_current.pickaxe:
                    room_lair_chase = True
                    creature_lair_chase_counter -= 1 # To make it balanced with taking them individually
                    room_current.counter_2 = 0
                    room_current.counter_1 = 0
                    inv.staff += room_current.staff
                    inv.pickaxe += room_current.pickaxe
                    room_current.staff = 0
                    room_current.pickaxe = 0
                    print("Your arm brushes up against the creature as you take the staff and pickaxe, awakening it.")
                    if oil_counter or light_counter:
                        if oil_counter:
                            source = "your lantern"
                        else:
                            source = "the ball of light"
                        print("Luckily, the light from %s blinds it, giving you some extra time." % source)
                elif room_id == "roomLairMid" and room_current.counter_2 and not room_lair_chase and room_current.staff:
                    room_lair_chase = True
                    room_current.counter_2 = 0
                    inv.staff += room_current.staff
                    room_current.staff = 0
                    print("Your arm brushes up against the creature as you take the staff, awakening it.")
                    if oil_counter or light_counter:
                        if oil_counter:
                            source = "your lantern"
                        else:
                            source = "the ball of light"
                        print("Luckily, the light from %s blinds it, giving you some extra time." % source)
                elif room_id == "roomLairMid" and room_current.counter_1 and not room_lair_chase and room_current.pickaxe:
                    room_lair_chase = True
                    room_current.counter_1 = 0
                    inv.pickaxe += room_current.pickaxe
                    room_current.pickaxe = 0
                    print("Your arm brushes up against the creature as you take the pickaxe, awakening it.")
                    if oil_counter or light_counter:
                        if oil_counter:
                            source = "your lantern"
                        else:
                            source = "the ball of light"
                        print("Luckily, the light from %s blinds it, giving you some extra time." % source)
                else:
                    inv.gold += room_current.gold
                    inv.letter += room_current.letter
                    inv.key += room_current.key
                    inv.key_skeleton += room_current.key_skeleton
                    inv.pickaxe += room_current.pickaxe
                    inv.shrubbery += room_current.shrubbery
                    inv.funnel_cake += room_current.funnel_cake
                    inv.half_funnel_cake += room_current.half_funnel_cake
                    inv.foot += room_current.foot
                    inv.porridge += room_current.porridge
                    inv.bowl += room_current.bowl
                    inv.lantern += room_current.lantern
                    inv.oil += room_current.oil
                    inv.pie += room_current.pie
                    inv.biscuit += room_current.biscuit
                    inv.hook += room_current.hook
                    inv.staff += room_current.staff
                    inv.ticket += room_current.ticket
                    inv.coal += room_current.coal
                    inv.potato += room_current.potato
                    inv.bandage += room_current.bandage
                    inv.journal += room_current.journal
                    inv.book += room_current.book
                    inv.brie += room_current.brie
                    inv.munster += room_current.munster
                    inv.stilton += room_current.stilton
                    inv.swiss += room_current.swiss
                    inv.wensleydale += room_current.wensleydale
                    inv.potion += room_current.potion
                    inv.flask += room_current.flask
                    inv.stone += room_current.stone
                    inv.bird += room_current.bird
                    inv.note += room_current.note
                    room_current.gold = 0
                    room_current.letter = 0
                    room_current.key = 0
                    room_current.key_skeleton = 0
                    room_current.pickaxe = 0
                    room_current.shrubbery = 0
                    room_current.funnel_cake = 0
                    room_current.half_funnel_cake = 0
                    room_current.foot = 0
                    room_current.porridge = 0
                    room_current.bowl = 0
                    room_current.lantern = 0
                    room_current.oil = 0
                    room_current.pie = 0
                    room_current.biscuit = 0
                    room_current.hook = 0
                    room_current.staff = 0
                    room_current.ticket = 0
                    room_current.coal = 0
                    room_current.potato = 0
                    room_current.bandage = 0
                    room_current.journal = 0
                    room_current.book = 0
                    room_current.brie = 0
                    room_current.munster = 0
                    room_current.stilton = 0
                    room_current.swiss = 0
                    room_current.wensleydale = 0
                    room_current.potion = 0
                    room_current.flask = 0
                    room_current.stone = 0
                    room_current.bird = 0
                    room_current.note = 0
                    room_current.memo = 0
                    print("You take everything.")
                item_name = "everything"
                items_name = "everything"
                take_count = "all"
            # Gold # continue add quantities like in buy and sell
            elif "gold" in option and room_current.gold:
                item_name = "gold"
                items_name = "gold"
                inv_item = inv.gold
                room_item = room_current.gold
                if option == item_name:
                    take_count = room_current.gold
                elif option.endswith("gold"):
                    take_count = option[:len(option) - len("gold") - 1]
            # Letter
            elif "letter" in option and room_current.letter:
                item_name = "letter"
                items_name = "letters"
                inv_item = inv.letter
                room_item = room_current.letter
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith("letter"):
                    take_count = option[:len(option) - len("letter") - 1]
                elif option.endswith("letters"):
                    take_count = option[:len(option) - len("letters") - 1]
            # Skeleton key
            elif "key of ahm'domosh" in option and room_current.key_skeleton:
                item_name = "key of Ahm'domosh"
                items_name = "keys of Ahm'domosh"
                inv_item = inv.key_skeleton
                room_item = room_current.key_skeleton
                if option == item_name.lower():
                    take_count = 1
                elif option == items_name.lower():
                    take_count = room_item
                elif option.endswith("key of ahm'domosh"):
                    take_count = option[:len(option) - len("key of ahm'domosh") - 1]
                elif option.endswith("keys of ahm'domosh"):
                    take_count = option[:len(option) - len("keys of ahm'domosh") - 1]
            # Key
            elif "key" in option and (room_current.key or room_current.key_skeleton):
                item_name = "key"
                items_name = "keys"
                if room_current.key:
                    inv_item = inv.key
                    room_item = room_current.key
                elif room_current.key_skeleton:
                    inv_item = inv.key_skeleton
                    room_item = room_current.key_skeleton
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith("key"):
                    take_count = option[:len(option) - len("key") - 1]
                elif option.endswith("keys"):
                    take_count = option[:len(option) - len("keys") - 1]
            # Pickaxe
            elif "pick" in option and room_current.pickaxe:
                item_name = "pickaxe"
                items_name = "pickaxes"
                inv_item = inv.pickaxe
                room_item = room_current.pickaxe
                if option in (item_name,"pick"):
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith("pick"):
                    take_count = option[:len(option) - len("pick") - 1]
                elif option.endswith("picks"):
                    take_count = option[:len(option) - len("picks") - 1]
                elif option.endswith("pickaxe"):
                    take_count = option[:len(option) - len("pickaxe") - 1]
                elif option.endswith("pickaxes"):
                    take_count = option[:len(option) - len("pickaxes") - 1]
            # shrubbery
            elif ("shrubbery" in option) or ("shrubberies" in option) and room_current.shrubbery:
                item_name = "shrubbery"
                items_name = "shrubberies"
                inv_item = inv.shrubbery
                room_item = room_current.shrubbery
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith("shrubbery"):
                    take_count = option[:len(option) - len("shrubbery") - 1]
                elif option.endswith("shrubberies"):
                    take_count = option[:len(option) - len("shrubberies") - 1]
            # Half-eaten funnel cake
            elif ("cake" in option) and ("half" in option) and room_current.half_funnel_cake:
                item_name = "half-eaten funnel cake"
                items_name = "half-eaten funnel cakes"
                inv_item = inv.half_funnel_cake
                room_item = room_current.half_funnel_cake
                if option.endswith("half-eaten funnel cake"):
                    take_count = option[:len(option) - len("half-eaten funnel cake") - 1]
                if option.endswith("half eaten funnel cake"):
                    take_count = option[:len(option) - len("half eaten funnel cake") - 1]
                elif option.endswith("half funnel cake"):
                    take_count = option[:len(option) - len("half funnel cake") - 1]
                elif option.endswith("half-eaten cake"):
                    take_count = option[:len(option) - len("half-eaten cake") - 1]
                elif option.endswith("half eaten cake"):
                    take_count = option[:len(option) - len("half eaten cake") - 1]
                elif option.endswith("half cake"):
                    take_count = option[:len(option) - len("half cake") - 1]
                elif option.endswith("half-eaten funnel cakes"):
                    take_count = option[:len(option) - len("half-eaten funnel cakes") - 1]
                elif option.endswith("half eaten funnel cakes"):
                    take_count = option[:len(option) - len("half eaten funnel cakes") - 1]
                elif option.endswith("half funnel cakes"):
                    take_count = option[:len(option) - len("half funnel cakes") - 1]
                elif option.endswith("half-eaten cakes"):
                    take_count = option[:len(option) - len("half-eaten cakes") - 1]
                elif option.endswith("half eaten cakes"):
                    take_count = option[:len(option) - len("half eaten cakes") - 1]
                elif option.endswith("half cakes"):
                    take_count = option[:len(option) - len("half cakes") - 1]
            # Funnel cake and Half-eaten funnel cake
            # If half-eaten cake is in room and cake not in room, treat half-eaten cake as cake
            elif "cake" in option and (room_current.funnel_cake or room_current.half_funnel_cake):
                if room_current.half_funnel_cake and not room_current.funnel_cake:
                    item_name = "half-eaten funnel cake"
                    items_name = "half-eaten funnel cakes"
                    inv_item = inv.half_funnel_cake
                    room_item = room_current.half_funnel_cake
                else:
                    item_name = "funnel cake"
                    items_name = "funnel cakes"
                    inv_item = inv.funnel_cake
                    room_item = room_current.funnel_cake
                if option in (item_name,"cake","funnel cake"):
                    take_count = 1
                elif option in (items_name,"cakes","funnel cakes"):
                    take_count = room_item
                elif option.endswith("funnel cake"):
                    take_count = option[:len(option) - len("funnel cake") - 1]
                elif option.endswith("funnel cakes"):
                    take_count = option[:len(option) - len("funnel cakes") - 1]
                elif option.endswith("cake"):
                    take_count = option[:len(option) - len("cake") - 1]
                elif option.endswith("cakes"):
                    take_count = option[:len(option) - len("cakes") - 1]
            # Lucky rabbit foot
            elif ("foot" in option) or ("feet" in option) and room_current.foot:
                item_name = "lucky rabbit foot"
                items_name = "lucky rabbit feet"
                inv_item = inv.foot
                room_item = room_current.foot
                if option in (item_name,"foot","rabbit foot","lucky foot"):
                    take_count = 1
                elif option in (items_name,"feet","rabbit feet","lucky feet"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith(("rabbit foot","rabbit feet")):
                    take_count = option[:len(option) - len("rabbit foot") - 1]
                elif option.endswith(("lucky foot","lucky feet")):
                    take_count = option[:len(option) - len("lucky foot") - 1]
                elif option.endswith(("foot","feet")):
                    take_count = option[:len(option) - len("foot") - 1]
            # Porridge (bowl of porridge)
            elif "porridge" in option and room_current.porridge:
                item_name = "bowl of porridge"
                items_name = "bowls of porridge"
                inv_item = inv.porridge
                room_item = room_current.porridge
                if option == item_name:
                    take_count = 1
                elif option in (items_name,"porridge"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("porridge"):
                    take_count = option[:len(option) - len("porridge") - 1]
            # Bowl
            elif "bowl" in option and (room_current.bowl or room_current.porridge):
                if room_current.porridge and not room_current.bowl:
                    item_name = "bowl of porridge"
                    items_name = "bowls of porridge"
                    inv_item = inv.porridge
                    room_item = room_current.porridge
                else:
                    item_name = "bowl"
                    items_name = "bowls"
                    inv_item = inv.bowl
                    room_item = room_current.bowl
                if option in (item_name,"bowl"):
                    take_count = 1
                elif option in (items_name,"bowls"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]

            # Vial of lantern oil
            elif ("oil" in option) or ("vial" in option) and room_current.oil:
                item_name = "vial of lantern oil"
                items_name = "vials of lantern oil"
                inv_item = inv.oil
                room_item = room_current.oil
                if option in (item_name,"vial"):
                    take_count = 1
                elif option in (items_name,"oil","vials","lantern oil"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("vial"):
                    take_count = option[:len(option) - len("vial") - 1]
                elif option.endswith("vials"):
                    take_count = option[:len(option) - len("vials") - 1]
                elif option.endswith("lantern oil"):
                    take_count = option[:len(option) - len("lantern oil") - 1]
                elif option.endswith("oil"):
                    take_count = option[:len(option) - len("oil") - 1]
            # Lantern
            elif "lantern" in option and room_current.lantern:
                item_name = "lantern"
                items_name = "lanterns"
                inv_item = inv.lantern
                room_item = room_current.lantern
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]

            # Hardtack biscuit
            elif ("biscuit" in option) or ("hardtack" in option) and room_current.biscuit:
                item_name = "hardtack biscuit"
                items_name = "hardtack biscuit"
                inv_item = inv.biscuit
                room_item = room_current.biscuit
                if option in (item_name,"biscuit"):
                    take_count = 1
                elif option in (items_name,"biscuits"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("biscuit"):
                    take_count = option[:len(option) - len("biscuit") - 1]
                elif option.endswith("biscuits"):
                    take_count = option[:len(option) - len("biscuits") - 1]
                elif option.endswith("hardtack"):
                    take_count = option[:len(option) - len("hardtack") - 1]
            # Coil of hook
            elif "hook" in option and room_current.hook:
                item_name = "grappling hook"
                items_name = "grappling hooks"
                inv_item = inv.hook
                room_item = room_current.hook
                if option in (item_name,"hook"):
                    take_count = 1
                elif option in (items_name,"hooks"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("hook"):
                    take_count = option[:len(option) - len("hook") - 1]
                elif option.endswith("hooks"):
                    take_count = option[:len(option) - len("hooks") - 1]
            # The staff of Garrotxa
            elif ("staff" in option) or ("staves" in option) and room_current.staff:
                item_name = "staff of Garrotxa"
                items_name = "staves of Garrotxa"
                inv_item = inv.staff
                room_item = room_current.staff
                if option in (item_name.lower(),"staff"):
                    take_count = 1
                elif option in (items_name.lower(),"staves"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name.lower()) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name.lower()) - 1]
                elif option.endswith("staff"):
                    take_count = option[:len(option) - len("staff") - 1]
                elif option.endswith("staves"):
                    take_count = option[:len(option) - len("staves") - 1]
            # Raffle ticket
            elif "ticket" in option and room_current.ticket:
                item_name = "raffle ticket"
                items_name = "raffle tickets"
                inv_item = inv.ticket
                room_item = room_current.ticket
                if option in (item_name,"ticket"):
                    take_count = 1
                elif option in (items_name,"tickets"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("ticket"):
                    take_count = option[:len(option) - len("ticket") - 1]
                elif option.endswith("tickets"):
                    take_count = option[:len(option) - len("tickets") - 1]
            # Piece of coal
            elif "coal" in option and room_current.coal:
                item_name = "piece of coal"
                items_name = "pieces of coal"
                inv_item = inv.coal
                room_item = room_current.coal
                if option == item_name:
                    take_count = 1
                elif option in (items_name,"coal"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("coal"):
                    take_count = option[:len(option) - len("coal") - 1]
            # Potato
            elif "potato" in option and room_current.potato:
                item_name = "rotten potato"
                items_name = "rotten potatoes"
                inv_item = inv.potato
                room_item = room_current.potato
                if option in (item_name,"potato"):
                    take_count = 1
                elif option in (items_name,"potatoes"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("potato"):
                    take_count = option[:len(option) - len("potato") - 1]
                elif option.endswith("potatoes"):
                    take_count = option[:len(option) - len("potatoes") - 1]

            # Bandage
            elif "bandage" in option and room_current.bandage:
                item_name = "bandage"
                items_name = "bandages"
                inv_item = inv.bandage
                room_item = room_current.bandage
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
            # Journal
            elif "journal" in option and room_current.journal:
                item_name = "journal"
                items_name = "journals"
                inv_item = inv.journal
                room_item = room_current.journal
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
            # Mysterious book
            elif "book" in option and room_current.book:
                item_name = "mysterious book"
                items_name = "mysterious books"
                inv_item = inv.book
                room_item = room_current.book
                if option in (item_name,"book"):
                    take_count = 1
                elif option in (items_name,"books"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len("book") - len("book") - 1]
                elif option.endswith(items_name):
                    take_count = option[:len("books") - len("books") - 1]
             # Cheeses
            elif "brie" in option and room_current.brie:
                item_name = "slice of brie cheese"
                items_name = "slices of brie cheese"
                inv_item = inv.brie
                room_item = room_current.brie
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("brie"):
                    take_count = option[:len(option) - len("brie") - 1]
                elif option.endswith("brie cheese"):
                    take_count = option[:len(option) - len("brie cheese") - 1]
            elif "munster" in option and room_current.munster:
                item_name = "slice of munster cheese"
                items_name = "slices of munster cheese"
                inv_item = inv.munster
                room_item = room_current.munster
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("munster"):
                    take_count = option[:len(option) - len("munster") - 1]
                elif option.endswith("munster cheese"):
                    take_count = option[:len(option) - len("munster cheese") - 1]
            elif "stilton" in option and room_current.brie:
                item_name = "slice of stilton cheese"
                items_name = "slices of stilton cheese"
                inv_item = inv.stilton
                room_item = room_current.stilton
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("stilton"):
                    take_count = option[:len(option) - len("stilton") - 1]
                elif option.endswith("stilton cheese"):
                    take_count = option[:len(option) - len("stilton cheese") - 1]
            elif "swiss" in option and room_current.brie:
                item_name = "slice of swiss cheese"
                items_name = "slices of swiss cheese"
                inv_item = inv.swiss
                room_item = room_current.swiss
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("swiss"):
                    take_count = option[:len(option) - len("swiss") - 1]
                elif option.endswith("swiss cheese"):
                    take_count = option[:len(option) - len("swiss cheese") - 1]
            elif "wensleydale" in option and room_current.brie:
                item_name = "slice of wensleydale cheese"
                items_name = "slices of wensleydale cheese"
                inv_item = inv.wensleydale
                room_item = room_current.wensleydale
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("wensleydale"):
                    take_count = option[:len(option) - len("wensleydale") - 1]
                elif option.endswith("wensleydale cheese"):
                    take_count = option[:len(option) - len("wensleydale cheese") - 1]
            # Potion
            elif "potion" in option and room_current.potion:
                item_name = "potion of rejuvination"
                items_name = "potions of rejuvination"
                inv_item = inv.potion
                room_item = room_current.potion
                if option in (item_name,"potion"):
                    take_count = 1
                elif option in (items_name,"potions"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("potion"):
                    take_count = option[:len(option) - len("potion") - 1]
                elif option.endswith("potions"):
                    take_count = option[:len(option) - len("potions") - 1]
            # Flask
            elif "flask" in option and room_current.flask:
                item_name = "flask"
                items_name = "flasks"
                inv_item = inv.flask
                room_item = room_current.flask
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
            # Dragonstone
            elif "stone" in option and room_current.stone:
                item_name = "dragonstone"
                items_name = "dragonstones"
                inv_item = inv.stone
                room_item = room_current.stone
                if option in (item_name,"stone"):
                    take_count = 1
                elif option in (items_name,"stones"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("stone"):
                    take_count = option[:len(option) - len("stone") - 1]
                elif option.endswith("stones"):
                    take_count = option[:len(option) - len("stones") - 1]
            # Wooden bird
            elif "bird" in option and room_current.bird:
                item_name = "wooden bird"
                items_name = "wooden birds"
                inv_item = inv.bird
                room_item = room_current.bird
                if option in (item_name,"bird"):
                    take_count = 1
                elif option in (items_name,"birds"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("bird"):
                    take_count = option[:len(option) - len("bird") - 1]
                elif option.endswith("birds"):
                    take_count = option[:len(option) - len("birds") - 1]
            # Note
            elif "note" in option and room_current.note:
                item_name = "note"
                items_name = "notes"
                inv_item = inv.note
                room_item = room_current.note
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
            # Memo
            elif "memo" in option and room_current.memo:
                item_name = "memo"
                items_name = "memos"
                inv_item = inv.memo
                room_item = room_current.memo
                if option == item_name:
                    take_count = 1
                elif option == items_name:
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
            # Chicken pot pie
            elif "pie" in option and room_current.pie:
                item_name = "chicken pot pie"
                items_name = "chicken pot pies"
                inv_item = inv.pie
                room_item = room_current.pie
                if option in (item_name,"chicken pie","pot pie","pie"):
                    take_count = 1
                elif option in (items_name,"chicken pies","pot pies","pies"):
                    take_count = room_item
                elif option.endswith(item_name):
                    take_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    take_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("pot pie"):
                    take_count = option[:len(option) - len("pot pie") - 1]
                elif option.endswith("chicken pie"):
                    take_count = option[:len(option) - len("chicken pie") - 1]
                elif option.endswith("pie"):
                    take_count = option[:len(option) - len("pie") - 1]
                elif option.endswith("pot pies"):
                    take_count = option[:len(option) - len("pot pies") - 1]
                elif option.endswith("chicken pies"):
                    take_count = option[:len(option) - len("chicken pies") - 1]
                elif option.endswith("pies"):
                    take_count = option[:len(option) - len("pies") - 1]
            elif option == "":
                print("Take what?")
                not_turn = True
            else:
                if option in ("all","everything"):
                    print("You cannot take anything here.")
                else:
                    print("There is no %s here to take." % option)
                not_turn = True
            if item_name:
                take_count_okay = False
                try:
                    take_count = float(take_count)
                    if take_count % 1 == 0 and take_count > 0 and take_count <= room_item:
                         take_count = int(take_count)
                         take_count_okay = True
                    else:
                        print("You cannot take",take_count,"%s." % items_name)
                        not_turn = True
                except ValueError:
                    if take_count in ("all","every"):
                        take_count = room_item
                        take_count_okay = True
                    elif take_count in ("a","the","only 1","only one"):
                        take_count = 1
                        take_count_okay = True
                    else:
                        print("You cannot take \"" + take_count + "\" %s." % items_name)
                        not_turn = True
                if take_count_okay and not item_name == "everything":
                    # Once takeCountOkay, take events go here
                    if room_id == "roomTempleBasement" and not room_current.character_dead and item_name == "staff of Garrotxa":
                        print("\"You are not worthy to take the staff!\" The figure zaps you with a bolt of electricity.")
                        stat.lower_health()
                        item_name = ""
                    elif room_id == "roomLairMid" and room_current.counter_2 and not room_lair_chase and item_name == "staff of Garrotxa":
                        room_lair_chase = True
                        room_current.counter_2 = 0
                        inv.staff += room_current.staff
                        room_current.staff = 0
                        print("Your arm brushes up against the creature as you take the staff, awakening it.")
                        if oil_counter or light_counter:
                            if oil_counter:
                                source = "your lantern"
                            else:
                                source = "the ball of light"
                            print("Luckily, the light from %s blinds it, giving you some extra time." % source)
                    elif room_id == "roomLairMid" and room_current.counter_1 and not room_lair_chase and item_name == "pickaxe":
                        room_lair_chase = True
                        room_current.counter_1 = 0
                        inv.pickaxe += room_current.pickaxe
                        room_current.pickaxe = 0
                        print("Your arm brushes up against the creature as you take the pickaxe, awakening it.")
                        if oil_counter or light_counter:
                            if oil_counter:
                                source = "your lantern"
                            else:
                                source = "the ball of light"
                            print("Luckily, the light from %s blinds it, giving you some extra time." % source)
                        else:
                            print("Unfortunately, the lack of light allows the creature to quickly recover.")
                            room_current.counter_1 += 1
                    elif take_count > 1:
                        print("You take %s %s." % (take_count,items_name))
                    elif room_item > 1:
                        print("You take a %s." % item_name)
                    else:
                        print("You take the %s." % item_name)
                    inv_item += take_count
                    room_item -= take_count
                    if item_name == "gold":
                        inv.gold = inv_item
                        room_current.gold = room_item
                    elif item_name == "letter":
                        inv.letter = inv_item
                        room_current.letter = room_item
                    elif item_name == "key":
                        inv.key = inv_item
                        room_current.key = room_item
                    elif item_name == "key of Ahm'domosh":
                        inv.key_skeleton = inv_item
                        room_current.key_skeleton = room_item
                    elif item_name == "pickaxe":
                        inv.pickaxe = inv_item
                        room_current.pickaxe = room_item
                    elif item_name == "shrubbery":
                        inv.shrubbery = inv_item
                        room_current.shrubbery = room_item
                    elif item_name == "funnel cake":
                        inv.funnel_cake = inv_item
                        room_current.funnel_cake = room_item
                    elif item_name == "half-eaten funnel cake":
                        inv.half_funnel_cake = inv_item
                        room_current.half_funnel_cake = room_item
                    elif item_name == "lucky rabbit foot":
                        inv.foot = inv_item
                        room_current.foot = room_item
                    elif item_name == "bowl of porridge":
                        inv.porridge = inv_item
                        room_current.porridge = room_item
                    elif item_name == "bowl":
                        inv.bowl = inv_item
                        room_current.bowl = room_item
                    elif item_name == "lantern":
                        inv.lantern = inv_item
                        room_current.lantern = room_item
                    elif item_name == "vial of lantern oil":
                        inv.oil = inv_item
                        room_current.oil = room_item
                    elif item_name == "chicken pot pie":
                        inv.pie = inv_item
                        room_current.pie = room_item
                    elif item_name == "hardtack biscuit":
                        inv.biscuit = inv_item
                        room_current.biscuit = room_item
                    elif item_name == "grappling hook":
                        inv.hook = inv_item
                        room_current.hook = room_item
                    elif item_name == "staff of Garrotxa":
                        inv.staff = inv_item
                        room_current.staff = room_item
                    elif item_name == "raffle ticket":
                        inv.ticket = inv_item
                        room_current.ticket = room_item
                    elif item_name == "piece of coal":
                        inv.coal = inv_item
                        room_current.coal = room_item
                    elif item_name == "rotten potato":
                        inv.potato = inv_item
                        room_current.potato = room_item
                    elif item_name == "bandage":
                        inv.bandage = inv_item
                        room_current.bandage = room_item
                    elif item_name == "journal":
                        inv.journal = inv_item
                        room_current.journal = room_item
                    elif item_name == "mysterious book":
                        inv.book = inv_item
                        room_current.book = room_item
                    elif item_name == "slice of brie cheese":
                        inv.brie = inv_item
                        room_current.brie = room_item
                    elif item_name == "slice of munster cheese":
                        inv.munster = inv_item
                        room_current.munster = room_item
                    elif item_name == "slice of stilton cheese":
                        inv.stilton = inv_item
                        room_current.stilton = room_item
                    elif item_name == "slice of swiss cheese":
                        inv.swiss = inv_item
                        room_current.swiss = room_item
                    elif item_name == "slice of wensleydale cheese":
                        inv.wensleydale = inv_item
                        room_current.wensleydale = room_item
                    elif item_name == "potion of rejuvination":
                        inv.potion = inv_item
                        room_current.potion = room_item
                    elif item_name == "flask":
                        inv.flask = inv_item
                        room_current.flask = room_item
                    elif item_name == "dragonstone":
                        inv.stone = inv_item
                        room_current.stone = room_item
                    elif item_name == "wooden bird":
                        inv.bird = inv_item
                        room_current.bird = room_item
                    elif item_name == "note":
                        inv.note = inv_item
                        room_current.note = room_item
                    elif item_name == "memo":
                        inv.memo = inv_item
                        room_current.memo = room_item
                if inv_item > 1 and not inv_item == take_count:
                    print("You have",inv_item,"%s." % items_name)
        # Drop
        elif option.startswith(("drop","discard","remove")):
            if option.startswith("drop"):
                option = option[5:]
            elif option.startswith("discard"):
                option = option[8:]
            elif option.startswith("remove"):
                option = option[7:]
            item_name = False
            items_name = False
            room_item = False
            inv_item = False
            drop_count = 0
            # All/Everything
            if option in ("all","everything") and inv.item_types():
                room_current.gold += inv.gold
                room_current.letter += inv.letter
                room_current.key += inv.key
                room_current.key_skeleton += inv.key_skeleton
                room_current.pickaxe += inv.pickaxe
                room_current.shrubbery += inv.shrubbery
                room_current.funnel_cake += inv.funnel_cake
                room_current.half_funnel_cake += inv.half_funnel_cake
                room_current.foot += inv.foot
                room_current.porridge += inv.porridge
                room_current.bowl += inv.bowl
                room_current.lantern += inv.lantern
                room_current.oil += inv.oil
                room_current.pie += inv.pie
                room_current.biscuit += inv.biscuit
                room_current.hook += inv.hook
                room_current.staff += inv.staff
                room_current.ticket += inv.ticket
                room_current.coal += inv.coal
                room_current.potato += inv.potato
                room_current.bandage += inv.bandage
                room_current.journal += inv.journal
                room_current.book += inv.book
                room_current.brie += inv.brie
                room_current.munster += inv.munster
                room_current.stilton += inv.stilton
                room_current.swiss += inv.swiss
                room_current.wensleydale += inv.wensleydale
                room_current.potion += inv.potion
                room_current.flask += inv.flask
                room_current.stone += inv.stone
                room_current.bird += inv.bird
                room_current.memo += inv.memo
                inv = Inventory(note_1 = vault_answer_1, note_2 = vault_answer_2, note_3 = vault_answer_3, note_4 = vault_answer_4)
                print("You drop everything.")
                item_name = "everything"
                items_name = "everything"
                drop_count = "all"
            # Gold # continue add quantities like in buy and sell
            elif "gold" in option and inv.gold:
                item_name = "gold"
                items_name = "gold"
                room_item = room_current.gold
                inv_item = inv.gold
                if option == item_name:
                    drop_count = inv.gold
                elif option.endswith("gold"):
                    drop_count = option[:len(option) - len("gold") - 1]
            # Letter
            elif "letter" in option and inv.letter:
                item_name = "letter"
                items_name = "letters"
                room_item = room_current.letter
                inv_item = inv.letter
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith("letter"):
                    drop_count = option[:len(option) - len("letter") - 1]
                elif option.endswith("letters"):
                    drop_count = option[:len(option) - len("letters") - 1]
            # Skeleton key
            elif "key of ahm'domosh" in option and inv.key_skeleton:
                item_name = "key of Ahm'domosh"
                items_name = "keys of Ahm'domosh"
                room_item = room_current.key_skeleton
                inv_item = inv.key_skeleton
                if option == item_name.lower():
                    drop_count = 1
                elif option == items_name.lower():
                    drop_count = inv_item
                elif option.endswith("key of ahm'domosh"):
                    drop_count = option[:len(option) - len("key of ahm'domosh") - 1]
                elif option.endswith("keys of ahm'domosh"):
                    drop_count = option[:len(option) - len("keys of ahm'domosh") - 1]
            # Key
            elif "key" in option and (inv.key or inv.key_skeleton):
                item_name = "key"
                items_name = "keys"
                if inv.key:
                    room_item = room_current.key
                    inv_item = inv.key
                elif inv.key_skeleton:
                    room_item = room_current.key_Skeleton
                    inv_item = inv.key_skeleton
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith("key"):
                    drop_count = option[:len(option) - len("key") - 1]
                elif option.endswith("keys"):
                    drop_count = option[:len(option) - len("keys") - 1]
            # Pickaxe
            elif "pick" in option and inv.pickaxe:
                item_name = "pickaxe"
                items_name = "pickaxes"
                room_item = room_current.pickaxe
                inv_item = inv.pickaxe
                if option in (item_name,"pick"):
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith("pick"):
                    drop_count = option[:len(option) - len("pick") - 1]
                elif option.endswith("picks"):
                    drop_count = option[:len(option) - len("picks") - 1]
                elif option.endswith("pickaxe"):
                    drop_count = option[:len(option) - len("pickaxe") - 1]
                elif option.endswith("pickaxes"):
                    drop_count = option[:len(option) - len("pickaxes") - 1]
            # shrubbery
            elif ("shrubbery" in option) or ("shrubberies" in option) and inv.shrubbery:
                item_name = "shrubbery"
                items_name = "shrubberies"
                room_item = room_current.shrubbery
                inv_item = inv.shrubbery
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith("shrubbery"):
                    drop_count = option[:len(option) - len("shrubbery") - 1]
                elif option.endswith("shrubberies"):
                    drop_count = option[:len(option) - len("shrubberies") - 1]
            # Half-eaten funnel cake
            elif ("cake" in option) and ("half" in option) and inv.half_funnel_cake:
                item_name = "half-eaten funnel cake"
                items_name = "half-eaten funnel cakes"
                room_item = room_current.half_funnel_cake
                inv_item = inv.half_funnel_cake
                if option.endswith("half-eaten funnel cake"):
                    drop_count = option[:len(option) - len("half-eaten funnel cake") - 1]
                if option.endswith("half eaten funnel cake"):
                    drop_count = option[:len(option) - len("half eaten funnel cake") - 1]
                elif option.endswith("half funnel cake"):
                    drop_count = option[:len(option) - len("half funnel cake") - 1]
                elif option.endswith("half-eaten cake"):
                    drop_count = option[:len(option) - len("half-eaten cake") - 1]
                elif option.endswith("half eaten cake"):
                    drop_count = option[:len(option) - len("half eaten cake") - 1]
                elif option.endswith("half cake"):
                    drop_count = option[:len(option) - len("half cake") - 1]
                elif option.endswith("half-eaten funnel cakes"):
                    drop_count = option[:len(option) - len("half-eaten funnel cakes") - 1]
                elif option.endswith("half eaten funnel cakes"):
                    drop_count = option[:len(option) - len("half eaten funnel cakes") - 1]
                elif option.endswith("half funnel cakes"):
                    drop_count = option[:len(option) - len("half funnel cakes") - 1]
                elif option.endswith("half-eaten cakes"):
                    drop_count = option[:len(option) - len("half-eaten cakes") - 1]
                elif option.endswith("half eaten cakes"):
                    drop_count = option[:len(option) - len("half eaten cakes") - 1]
                elif option.endswith("half cakes"):
                    drop_count = option[:len(option) - len("half cakes") - 1]
            # Funnel cake and Half-eaten funnel cake
            # If half-eaten cake is in room and cake not in inv, treat half-eaten cake as cake
            elif "cake" in option and (inv.funnel_cake or inv.half_funnel_cake):
                if inv.half_funnel_cake and not inv.funnel_cake:
                    item_name = "half-eaten funnel cake"
                    items_name = "half-eaten funnel cakes"
                    room_item = room_current.half_funnel_cake
                    inv_item = inv.half_funnel_cake
                else:
                    item_name = "funnel cake"
                    items_name = "funnel cakes"
                    room_item = room_current.funnel_cake
                    inv_item = inv.funnel_cake
                if option in (item_name,"cake","funnel cake"):
                    drop_count = 1
                elif option in (items_name,"cakes","funnel cakes"):
                    drop_count = inv_item
                elif option.endswith("funnel cake"):
                    drop_count = option[:len(option) - len("funnel cake") - 1]
                elif option.endswith("funnel cakes"):
                    drop_count = option[:len(option) - len("funnel cakes") - 1]
                elif option.endswith("cake"):
                    drop_count = option[:len(option) - len("cake") - 1]
                elif option.endswith("cakes"):
                    drop_count = option[:len(option) - len("cakes") - 1]
            # Lucky rabbit foot
            elif ("foot" in option) or ("feet" in option) and inv.foot:
                item_name = "lucky rabbit foot"
                items_name = "lucky rabbit feet"
                room_item = room_current.foot
                inv_item = inv.foot
                if option in (item_name,"foot","rabbit foot","lucky foot"):
                    drop_count = 1
                elif option in (items_name,"feet","rabbit feet","lucky feet"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith(("rabbit foot","rabbit feet")):
                    drop_count = option[:len(option) - len("rabbit foot") - 1]
                elif option.endswith(("lucky foot","lucky feet")):
                    drop_count = option[:len(option) - len("lucky foot") - 1]
                elif option.endswith(("foot","feet")):
                    drop_count = option[:len(option) - len("foot") - 1]
            # Porridge (bowl of porridge)
            elif "porridge" in option and inv.porridge:
                item_name = "bowl of porridge"
                items_name = "bowls of porridge"
                room_item = room_current.porridge
                inv_item = inv.porridge
                if option == item_name:
                    drop_count = 1
                elif option in (items_name,"porridge"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("porridge"):
                    drop_count = option[:len(option) - len("porridge") - 1]
            # Bowl
            elif "bowl" in option and (inv.bowl or inv.porridge):
                if inv.porridge and not inv.bowl:
                    item_name = "bowl of porridge"
                    items_name = "bowls of porridge"
                    room_item = room_current.porridge
                    inv_item = inv.porridge
                else:
                    item_name = "bowl"
                    items_name = "bowls"
                    room_item = room_current.bowl
                    inv_item = inv.bowl
                if option in (item_name,"bowl"):
                    drop_count = 1
                elif option in (items_name,"bowls"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
            # Lantern
            elif "lantern" in option and inv.lantern:
                item_name = "lantern"
                items_name = "lanterns"
                room_item = room_current.lantern
                inv_item = inv.lantern
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
            # Vial of lantern oil
            elif ("oil" in option) or ("vial" in option) and inv.oil:
                item_name = "vial of lantern oil"
                items_name = "vials of lantern oil"
                room_item = room_current.oil
                inv_item = inv.oil
                if option in (item_name,"vial"):
                    drop_count = 1
                elif option in (items_name,"oil","vials","lantern oil"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("vial"):
                    drop_count = option[:len(option) - len("vial") - 1]
                elif option.endswith("vials"):
                    drop_count = option[:len(option) - len("vials") - 1]
                elif option.endswith("lantern oil"):
                    drop_count = option[:len(option) - len("lantern oil") - 1]
                elif option.endswith("oil"):
                    drop_count = option[:len(option) - len("oil") - 1]
            # Hardtack biscuit
            elif ("biscuit" in option) or ("hardtack" in option) and inv.biscuit:
                item_name = "hardtack biscuit"
                items_name = "hardtack biscuit"
                room_item = room_current.biscuit
                inv_item = inv.biscuit
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("biscuit"):
                    drop_count = option[:len(option) - len("biscuit") - 1]
                elif option.endswith("biscuits"):
                    drop_count = option[:len(option) - len("biscuits") - 1]
                elif option.endswith("hardtack"):
                    drop_count = option[:len(option) - len("hardtack") - 1]
            # Coil of hook
            elif "hook" in option and inv.hook:
                item_name = "grappling hook"
                items_name = "grappling hooks"
                room_item = room_current.hook
                inv_item = inv.hook
                if option in (item_name,"hook"):
                    drop_count = 1
                elif option in (items_name,"hooks"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("hook"):
                    drop_count = option[:len(option) - len("hook") - 1]
                elif option.endswith("hooks"):
                    drop_count = option[:len(option) - len("hooks") - 1]
            # The staff of Garrotxa
            elif ("staff" in option) or ("staves" in option) and inv.staff:
                item_name = "staff of Garrotxa"
                items_name = "staves of Garrotxa"
                room_item = room_current.staff
                inv_item = inv.staff
                if option in (item_name.lower(),"staff"):
                    drop_count = 1
                elif option in (items_name.lower(),"staves"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name.lower()) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name.lower()) - 1]
                elif option.endswith("staff"):
                    drop_count = option[:len(option) - len("staff") - 1]
                elif option.endswith("staves"):
                    drop_count = option[:len(option) - len("staves") - 1]
            # Raffle ticket
            elif "ticket" in option and inv.ticket:
                item_name = "raffle ticket"
                items_name = "raffle tickets"
                room_item = room_current.ticket
                inv_item = inv.ticket
                if option in (item_name,"ticket"):
                    drop_count = 1
                elif option in (items_name,"tickets"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("ticket"):
                    drop_count = option[:len(option) - len("ticket") - 1]
                elif option.endswith("tickets"):
                    drop_count = option[:len(option) - len("tickets") - 1]
            # Piece of coal
            elif "coal" in option and inv.coal:
                item_name = "piece of coal"
                items_name = "pieces of coal"
                room_item = room_current.coal
                inv_item = inv.coal
                if option == item_name:
                    drop_count = 1
                elif option in (items_name,"coal"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("coal"):
                    drop_count = option[:len(option) - len("coal") - 1]
            # Potato
            elif "potato" in option and inv.potato:
                item_name = "rotten potato"
                items_name = "rotten potatoes"
                room_item = room_current.potato
                inv_item = inv.potato
                if option in (item_name,"potato"):
                    drop_count = 1
                elif option in (items_name,"potatoes"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("potato"):
                    drop_count = option[:len(option) - len("potato") - 1]
                elif option.endswith("potatoes"):
                    drop_count = option[:len(option) - len("potatoes") - 1]
            # Bandage
            elif "bandage" in option and inv.bandage:
                item_name = "bandage"
                items_name = "bandages"
                room_item = room_current.bandage
                inv_item = inv.bandage
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
            # Journal
            elif "journal" in option and inv.journal:
                item_name = "journal"
                items_name = "journals"
                room_item = room_current.journal
                inv_item = inv.journal
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
            # Mysterious book
            elif "book" in option and inv.book:
                item_name = "mysterious book"
                items_name = "mysterious books"
                room_item = room_current.book
                inv_item = room_current.book
                if option in (item_name,"book"):
                    drop_count = 1
                elif option in (items_name,"books"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("book"):
                    drop_count = option[:len(option) - len("book") - 1]
                elif option.endswith("books"):
                    drop_count = option[:len(option) - len("books") - 1]
             # Cheeses
            elif "brie" in option and inv.brie:
                item_name = "slice of brie cheese"
                items_name = "slices of brie cheese"
                room_item = room_current.brie
                inv_item = inv.brie
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("brie"):
                    drop_count = option[:len(option) - len("brie") - 1]
                elif option.endswith("brie cheese"):
                    drop_count = option[:len(option) - len("brie cheese") - 1]
            elif "munster" in option and inv.munster:
                item_name = "slice of munster cheese"
                items_name = "slices of munster cheese"
                room_item = room_current.munster
                inv_item = inv.munster
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("munster"):
                    drop_count = option[:len(option) - len("munster") - 1]
                elif option.endswith("munster cheese"):
                    drop_count = option[:len(option) - len("munster cheese") - 1]
            elif "stilton" in option and inv.brie:
                item_name = "slice of stilton cheese"
                items_name = "slices of stilton cheese"
                room_item = room_current.stilton
                inv_item = inv.stilton
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("stilton"):
                    drop_count = option[:len(option) - len("stilton") - 1]
                elif option.endswith("stilton cheese"):
                    drop_count = option[:len(option) - len("stilton cheese") - 1]
            elif "swiss" in option and inv.brie:
                item_name = "slice of swiss cheese"
                items_name = "slices of swiss cheese"
                room_item = room_current.swiss
                inv_item = inv.swiss
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("swiss"):
                    drop_count = option[:len(option) - len("swiss") - 1]
                elif option.endswith("swiss cheese"):
                    drop_count = option[:len(option) - len("swiss cheese") - 1]
            elif "wensleydale" in option and inv.brie:
                item_name = "slice of wensleydale cheese"
                items_name = "slices of wensleydale cheese"
                room_item = room_current.wensleydale
                inv_item = inv.wensleydale
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("wensleydale"):
                    drop_count = option[:len(option) - len("wensleydale") - 1]
                elif option.endswith("wensleydale cheese"):
                    drop_count = option[:len(option) - len("wensleydale cheese") - 1]
            # Potion
            elif "potion" in option and inv.potion:
                item_name = "potion of rejuvination"
                items_name = "potions of rejuvination"
                room_item = room_current.potion
                inv_item = inv.potion
                if option in (item_name,"potion"):
                    drop_count = 1
                elif option in (items_name,"potions"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("potion"):
                    drop_count = option[:len(option) - len("potion") - 1]
                elif option.endswith("potions"):
                    drop_count = option[:len(option) - len("potions") - 1]
            # Flask
            elif "flask" in option and inv.flask:
                item_name = "flask"
                items_name = "flasks"
                room_item = room_current.flask
                inv_item = inv.flask
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
            # Dragonstone
            elif "stone" in option and inv.stone:
                item_name = "dragonstone"
                items_name = "dragonstones"
                room_item = room_current.stone
                inv_item = inv.stone
                if option in (item_name,"stone"):
                    drop_count = 1
                elif option in (items_name,"stones"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("stone"):
                    drop_count = option[:len(option) - len("stone") - 1]
                elif option.endswith("stones"):
                    drop_count = option[:len(option) - len("stones") - 1]
            # Wooden bird
            elif "bird" in option and inv.bird:
                item_name = "wooden bird"
                items_name = "wooden birds"
                room_item = room_current.bird
                inv_item = inv.bird
                if option in (item_name,"bird"):
                    drop_count = 1
                elif option in (items_name,"birds"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("bird"):
                    drop_count = option[:len(option) - len("bird") - 1]
                elif option.endswith("birds"):
                    drop_count = option[:len(option) - len("birds") - 1]
            # Note
            elif "note" in option and inv.note:
                item_name = "note"
                items_name = "notes"
                room_item = room_current.note
                inv_item = inv.note
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
            # Memo
            elif "memo" in option and inv.memo:
                item_name = "memo"
                items_name = "memos"
                room_item = room_current.memo
                inv_item = inv.note
                if option == item_name:
                    drop_count = 1
                elif option == items_name:
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
            # Chicken pot pie
            elif "pie" in option and inv.pie:
                item_name = "chicken pot pie"
                items_name = "chicken pot pies"
                room_item = room_current.pie
                inv_item = inv.pie
                if option in (item_name,"chicken pie","pot pie","pie"):
                    drop_count = 1
                elif option in (items_name,"chicken pies","pot pies","pies"):
                    drop_count = inv_item
                elif option.endswith(item_name):
                    drop_count = option[:len(option) - len(item_name) - 1]
                elif option.endswith(items_name):
                    drop_count = option[:len(option) - len(items_name) - 1]
                elif option.endswith("pot pie"):
                    drop_count = option[:len(option) - len("pot pie") - 1]
                elif option.endswith("chicken pie"):
                    drop_count = option[:len(option) - len("chicken pie") - 1]
                elif option.endswith("pie"):
                    drop_count = option[:len(option) - len("pie") - 1]
                elif option.endswith("pot pies"):
                    drop_count = option[:len(option) - len("pot pies") - 1]
                elif option.endswith("chicken pies"):
                    drop_count = option[:len(option) - len("chicken pies") - 1]
                elif option.endswith("pies"):
                    drop_count = option[:len(option) - len("pies") - 1]
            elif option == "":
                print("Drop what?")
                not_turn = True
            else:
                if option in ("all","everything"):
                    print("You have nothing to drop.")
                else:
                    print("You have no %s to drop." % option)
                not_turn = True
            if item_name:
                drop_count_okay = False
                try:
                    drop_count = float(drop_count)
                    if drop_count % 1 == 0 and drop_count > 0 and drop_count <= inv_item:
                         drop_count = int(drop_count)
                         drop_count_okay = True
                    else:
                        print("You cannot drop",drop_count,"%s." % items_name)
                        not_turn = True
                except ValueError:
                    if drop_count in ("all","every"):
                        drop_count = inv_item
                        drop_count_okay = True
                    elif drop_count in ("a","the","only 1","only one"):
                        drop_count = 1
                        drop_count_okay = True
                    else:
                        print("You cannot drop \"" + drop_count + "\" %s." % items_name)
                        not_turn = True
                if drop_count_okay and not item_name == "everything":
                    if drop_count > 1:
                        print("You drop %s %s." % (drop_count,items_name))
                    elif inv_item > 1:
                        print("You drop a %s." % item_name)
                    else:
                        print("You drop the %s." % item_name)
                    room_item += drop_count
                    inv_item -= drop_count
                    if item_name == "gold":
                        room_current.gold = room_item
                        inv.gold = inv_item
                    elif item_name == "letter":
                        room_current.letter = room_item
                        inv.letter = inv_item
                    elif item_name == "key":
                        room_current.key = room_item
                        inv.key = inv_item
                    elif item_name == "key of Ahm'domosh":
                        room_current.key_skeleton = room_item
                        inv.key_skeleton = inv_item
                    elif item_name == "pickaxe":
                        room_current.pickaxe = room_item
                        inv.pickaxe = inv_item
                    elif item_name == "shrubbery":
                        room_current.shrubbery = room_item
                        inv.shrubbery = inv_item
                    elif item_name == "funnel cake":
                        room_current.funnel_cake = room_item
                        inv.funnel_cake = inv_item
                    elif item_name == "half-eaten funnel cake":
                        room_current.half_funnel_cake = room_item
                        inv.half_funnel_cake = inv_item
                    elif item_name == "lucky rabbit foot":
                        room_current.foot = room_item
                        inv.foot = inv_item
                    elif item_name == "bowl of porridge":
                        room_current.porridge = room_item
                        inv.porridge = inv_item
                    elif item_name == "bowl":
                        room_current.bowl = room_item
                        inv.bowl = inv_item
                    elif item_name == "lantern":
                        room_current.lantern = room_item
                        inv.lantern = inv_item
                    elif item_name == "vial of lantern oil":
                        room_current.oil = room_item
                        inv.oil = inv_item
                    elif item_name == "chicken pot pie":
                        room_current.pie = room_item
                        inv.pie = inv_item
                    elif item_name == "hardtack biscuit":
                        room_current.biscuit = room_item
                        inv.biscuit = inv_item
                    elif item_name == "grappling hook":
                        room_current.hook = room_item
                        inv.hook = inv_item
                    elif item_name == "staff of Garrotxa":
                        room_current.staff = room_item
                        inv.staff = inv_item
                    elif item_name == "raffle ticket":
                        room_current.ticket = room_item
                        inv.ticket = inv_item
                    elif item_name == "piece of coal":
                        room_current.coal = room_item
                        inv.coal = inv_item
                    elif item_name == "rotten potato":
                        room_current.potato = room_item
                        inv.potato = inv_item
                    elif item_name == "bandage":
                        room_current.bandage = room_item
                        inv.bandage = inv_item
                    elif item_name == "journal":
                        room_current.journal = room_item
                        inv.journal = inv_item
                    elif item_name == "mysterious book":
                        room_current.book = room_item
                        inv.book = inv_item
                    elif item_name == "slice of brie cheese":
                        room_current.brie = room_item
                        inv.brie = inv_item
                    elif item_name == "slice of munster cheese":
                        room_current.munster = room_item
                        inv.munster = inv_item
                    elif item_name == "slice of stilton cheese":
                        room_current.stilton = room_item
                        inv.stilton = inv_item
                    elif item_name == "slice of swiss cheese":
                        room_current.swiss = room_item
                        inv.swiss = inv_item
                    elif item_name == "slice of wensleydale cheese":
                        room_current.wensleydale = room_item
                        inv.wensleydale = inv_item
                    elif item_name == "potion of rejuvination":
                        room_current.potion = room_item
                        inv.potion = inv_item
                    elif item_name == "flask":
                        room_current.flask = room_item
                        inv.flask = inv_item
                    elif item_name == "dragonstone":
                        room_current.stone = room_item
                        inv.stone = inv_item
                    elif item_name == "wooden bird":
                        room_current.bird = room_item
                        inv.bird = inv_item
                    elif item_name == "note":
                        room_current.note = room_item
                        inv.note = inv_item
                    elif item_name == "memo":
                        room_current.memo = room_item
                        inv.memo = inv_item
        # Hurt, Punch, Kick
        elif option.startswith("punch") or option.startswith("kick"):
            hurt = False
            if option.startswith("punch"):
                if option == "punch":
                    print("Punch what?")
                    not_turn = True
                else:
                    option = option[6:]
                    hurt = "punch"
            elif option.startswith("kick"):
                if option == "kick":
                    print("Kick what?")
                    not_turn = True
                else:
                    option = option[5:]
                    hurt = "kick"
            if hurt:
                if option in ("self","myself","me"):
                    if hurt == "punch":
                        print("You punch yourself.")
                        stat.lower_health()
                    else:
                        print("You try to kick yourself, however that would work, and quickly get frustrated. You end up kicking the back of one of your calves with your other foot, causing you to fall over and hit your head.")
                        stat.lower_health()
                elif room_id == "roomCarnivalFood":
                    if option in ("vendor","man","the vendor","the man"):
                        print("You %s the vendor.\n\nHe panicly shouts, \"Help, I'm being attacked!\" Town guards enter the tent and beat you to death." % hurt)
                        end_game = True
                    else:
                        print("You can't %s that." % hurt)
                elif room_id == "roomCarnivalShellGame":
                    if option in ("sybil","woman","old woman"):
                        print("You %s Sybil.\n\nShe falls over on her back and yells, \"Azara Telkathena!\" Green lightning shoots out from her hands, frying you to death." % hurt)
                        end_game = True
                    else:
                        print("You can't %s that." % hurt)
                elif room_id == "roomGeneralStore":
                    if option in ("shopkeeper","man","the shopkeeper","the man"):
                        print("You %s the shopkeeper. \n\n\"What do you think you're doing?\" He grabs your arm and breaks it. \"That'll teach you a lesson.\"")
                        end_game = True
                # add interactions with all rooms with people
                elif room_id == "roomBridge":
                    if option in ("troll","the troll","ugg"):
                        if room_current.character_dead:
                            print("You %s the troll's charred remains. Your hand gets covered in ash.")
                        else:
                            print("You %s the troll. He gets angry and punches you back." % hurt)
                            stat.lower_health()
                    else:
                        print("You can't %s that." % hurt)
                elif room_id == "roomTempleInside":
                    if option in ("ghostly figure","ghost","figure"):
                        if room_current.character_dead:
                            print("There's no %s here to %s." % (option,hurt))
                        else:
                            print("You %s the ghostly figure, going right through it. \"Do not think you can defeat me with mere physical attacks.\" It zaps you, cutting open a wound in your chest." % hurt)
                            stat.lower_health()
                else:
                    print("You cannot",hurt,"that.")
                    not_turn = True
        # Say, Yell, Shout, Scream
        elif option.startswith("say") or option.startswith("yell") or option.startswith("shout") or option.startswith("scream"):
            spell = False
            valid = False
            say = False
            if silenced:
                print("You try to speak but cannot say anything.")
            else:
                if option.startswith("say"):
                    option = option[4:5].upper() + option[5:]
                    if option.startswith("\""):
                        option = option[1:2].upper() + option[2:]
                    say = True
                elif option.startswith("yell"):
                    option = option[5:].upper()
                elif option.startswith("shout"):
                    option = option[6:].upper()
                elif option.startswith("scream"):
                    option = option[7:].upper()
                option = option.strip("\"").strip("\'")
                if ask_name:
                    mynameis = False
                    iam = False
                    im = False
                    if option.lower().startswith("my name is "):
                        option2 = option[11:].title()
                        mynameis = True
                    elif option.lower().startswith("i am "):
                        option2 = option[5:].title()
                        iam = True
                    elif option.lower().startswith("i'm "):
                        option2 = option[4:].title()
                        im = True
                    else:
                        option2 = option.title()
                    if mynameis:
                        option = "My name is " + option2
                    elif iam:
                        option = "I am " + option2
                    elif im:
                        option = "I'm " + option2
                    else:
                        option = option2
                    player_name = option2
                if option == "":
                    print("Say what?")
                    not_turn = True
                elif say:
                    print("You say, \"%s.\"" % option)
                    option = option.lower()
                else:
                    print('You shout "%s!" at the top of your lungs!' % option)
                    option = option.lower()
                # Game responsive
                if option in ("raan mir tah", "laas yah nir", "mid vur shaan", "feim zii gron", "gol hah dov", "od ah viing", "lok vah koor", "ven gaar nos", "zun haal viik", "faas ru maar", "mul qah diiv", "joor zah frul", "gaan lah haas", "yol toor shul", "fo krah diin", "liz slen nus", "kaan drem ov", "krii lun aus", "rii vaaz zol", "tiid klo ul", "strun bah qo", "dur neh viir", "zul mey gut", "fus ro dah", "wuld nah kest", "zii los dii du", "slen tiid vo", "nahl dal vus", "diil qoth zaam", "ven mul riik", "riik lo sah"):
                    print("You promptly remind yourself this is not Skyrim.")
                # Room dependent
                elif room_id == "roomTempleBasement":
                    if not room_current.character_dead:
                        if stat.health < stat.healthmax:
                            heal = "Your wounds are magically healed. "
                        else:
                            heal = ""
                        if option in room_current.counter_ans_1:
                            print("\"Good. You have proven yourself worthy. The staff is yours.\" %sThe figure fades away." % heal)
                            stat.health = stat.healthmax
                            room_current.character_dead = True
                            # Roquefort message
                            room_temple_entrance.first_time = True
                            # Black knight spawn
                            room_road_corner.counter_1 = 1
                            room_road_corner.character_dead = False
                            room_road_corner.west_blocked = True
                        else:
                            if option.startswith("ozh ensh") or option in ("ozh vo'ses sa", "izh vo'poz", "ozh groth sol", "ozh vo'irush", "ozh gluth nith", "ozh gluth izh sol"):
                                print("\"You dare speak that devilish tongue in this sacred temple? Think again, Ozkavosh fiend.\" The figure zaps you with a bolt of electricity.")
                                option = ""
                                end_game = True
                            else:
                                print("\"Incorrect.\" The figure zaps you with a bolt of electricity.")
                                stat.lower_health()
                # Spells
                if option.startswith("ozh ensh") or option in ("ozh vo'ses sa","izh vo'poz","ozh thok alatho","ozh groth sol","ozh vo'irush","ozh gluth nith","ozh gluth izh sol","ozh sol fek"):
                    spell = True
                # Learn (I learn)
                # roomLake
                if option.startswith("ozh ensh"):
                    option = option[9:].lower()
                    if option == "ozh ensh":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    I learn.\n    Spell - Translates the meaning and effects of words from Ozkavosh.")
                        valid = True
                        spell_learn = 2
                    elif option == "ozh vo'ses sa":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    I unlock this.\n    Spell - Opens any lock.")
                        valid = True
                        spell_unlock = 2
                    elif option == "izh vo'poz":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    You have no power.\n    Spell - Persuades those blocking the way.")
                        valid = True
                        spell_persuade = 2
                    elif option == "ozh thok alatho":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    I move forward\n    Spell - Crosses large gaps.")
                        valid = True
                        spell_jump = 2
                    elif option == "ozh groth sol":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    I open the light.\n    Spell - Creates a glowing ball that illuminates your surroundings.")
                        valid = True
                        spell_light = 2
                    elif option == "ozh vo'irush":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    I am without illness.\n    Spell - Mends all wounds and illnesses.")
                        valid = True
                        spell_heal = 2
                    elif option == "ozh gluth nith":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    I consume the Earth.\n    Spell - Satifsies all hunger.")
                        valid = True
                        spell_feed = 2
                    elif option == "ozh gluth izh sol":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    I consume your soul.\n    Spell - Kills your enemies.")
                        valid = True
                        spell_kill = 2
                    elif option == "ozh sol fek":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    My life ends.\n    Spell - Kills self.")
                        valid = True
                        spell_killself = 2
                    # roomBarn letter
                    elif option == "eyik vo'hollom":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    Behold oblivion.\n    Spell - Opens obsidian hemispheres.")
                        valid = True
                        spell_oblivion = 2
                    # Not spells
                    # roomShrineNorth.firstTime
                    elif option == "omoz gloth izh":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    Darkness welcomes you.")
                        valid = True
                        word_darkness = 2
                    # roomHouseOffice
                    # Vesh'kathal says after Eden dies in dialogue (either you kill or she makes you kill him)
                    elif option == "ozkavosh icha domosh sa nith":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    Demon-kind shall reign upon this land.")
                        valid = True
                        word_reign = 2
                    elif option == "izh icha vo'fek ozh domosh":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    You will not stop my reign.")
                        valid = True
                        word_stop = 2
                    elif option == "ahm'fol":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    Servant of Vesh'arkosh")
                        valid = True
                        word_servant = 2
                    elif option == "sof izh":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    Curse you.")
                        valid = True
                        word_curse = 2
                    # roomBookMirror
                    # Hints the puzzle solution
                    elif option == "izh tal et ozh icha rek'tal":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    Talk and I will mirror.")
                        valid = True
                        word_mirror = 2
                    elif option == "ahm'domosh":
                        print("Information enters your thoughts as the meaning of the words become clear.")
                        print("    Highest dominion.")
                        valid = True
                        word_dominion = 2
                    if valid:
                        spell_learn = 2
                # Unlock (I unhide this)
                # roomLake after saving stranger
                elif option == "ozh vo'ses sa":
                    if room_id in ("roomJailCell","roomMountEntrance","roomHouseGate","roomHouseEntrance") and (room_current.north_blocked or room_current.east_blocked or room_current.south_blocked or room_current.west_blocked) or (room_id in ("roomLake","roomCave__3_lllm_treasure_crevasse") and not room_current.counter_1):
                        print("You feel a surge of energy emit from the utterance of your words into the lock, unlocking it.")
                        if room_id in ("roomLake","roomCave__3_lllm_treasure_crevasse"):
                            room_current.counter_1 = 1
                            valid = True
                            spell_unlock = 2
                        else:
                            valid = True
                            if room_current.north_blocked and room_current.north:
                                print("You can now go North.")
                                room_current.north_blocked = False
                            if room_current.east_blocked and room_current.east:
                                print("You can now go East.")
                                room_current.east_blocked = False
                            if room_current.west_blocked and room_current.west:
                                print("You can now go West.")
                                room_current.south_blocked = False
                            if room_current.south_blocked and room_current.south:
                                print("You can now go South.")
                                room_current.west_blocked = False
                            if room_id == "roomJailCell":
                                if not room_current.counter_1 and not player_name:
                                    room_jail_corridor.letter += 1
                                    room_current.counter_ans_1 = 1
                                if not player_name:
                                    player_name = "the hero of Kashkaval"
                                inv.letterRead = "It reads:\n\nTo " + player_name + ",\n\nA certain Eden Von Roquefort has set up residence NORTH of MOUNT MAGNA. While he purports to be a lowly cheese mage, reliable sources claim him to be the demon lord, Vesh'kathal the Deceiver, a shapeshifter infamous of manipulating the minds and bending the wills of others. Legend tells of a saviour, deemed the Monterey Messiah, who will save all of Kashkaval from his wickedness. It has be brought to my attention that you are that saviour that the legends speak of. While I have very important matters to attend to, the best I can do is help instruct you in how to defeat this demon lord:\n\nFIRST, you must acquire the staff from the Garrotxian temple NORTHEAST of this town, for it is the only weapon capable of defeating such a powerful demon.\n\nNEXT, once you have the staff, go NORTH through the MINES of MOUNT MAGNA and find him at his house on the other end.\n\nFINALLY, kill Roquefort and Kashkaval will be saved from his wrath.\n\nI know this is probably a lot to digest at once, but you are our only hope. I fear in your attempt to complete this task, Vesh'kathal will attempt to thwart you. He may attempt to contact and manipulate you, or have his minions work to stop you. Whatever he does, you must persevere.\n\nMay you be blessed,\n\nThe last prophet of Garrotxa"
                # Oblivion - Open hemispheres
                # roomBarn letter
                elif option == "eyik vo'hollom" and room_id in ("roomForest","roomField") and room_current.east_blocked:
                    room_forest.east_blocked = False
                    room_field.east_blocked = False
                    print("You hear strange whispers in every direction around you. Suddenly, the hemisphere begins to hum and an opening appears, leading inside.")
                    print("You can no go East.")
                # Persuade (You have no power)
                # roomRoadCorner after defeating black knight
                elif option == "izh vo'poz":
                    if room_id in ("roomGate","roomBridge","roomTempleInside","roomRoadCorner"):
                        # roomGate
                        if room_id == "roomGate" and room_current.north_blocked:
                            print("You feel a surge of energy emit from the utterance of your words towards the guard.")
                            print("The guard is convinced you gave him his shrubbery and lets you through the gate.")
                            room_gate.north_blocked = False
                            room_gate.is_give = False
                            valid = True
                        # roomBridge
                        elif room_id == "roomBridge" and room_current.east_blocked:
                            print("You feel a surge of energy emit from the utterance of your words towards the troll.")
                            print('The troll is convinced you gave him all the funnel cakes in the world and goes back under the bridge.')
                            room_bridge.east_blocked = False
                            valid = True
                        # roomTempleInside
                        elif room_id == "roomTempleInside" and not room_current.character_dead:
                            print("You feel a surge of energy emit from the utterance of your words towards the ghostly figure.")
                            valid = True
                        # roomRoadCorner
                        elif room_id == "roomRoadCorner" and not room_current.character_dead:
                            print("You feel a surge of energy emit from the utterance of your words towards the ghostly figure.")
                            print("The black knights say, \"One shall pass.\" before walking off into the forest.")
                            room_current.character_dead = True
                            valid = True
                        if valid:
                            spell_persuade = 2
                # Jump (I move forward)
                # roomLairEast
                elif option == "ozh thok alatho":
                    if room_id.endswith("crevasse"):
                        # roomCave_3_llm_crevasse
                        if room_id == "roomCave_3_llm_crevasse":
                            direction = "West"
                            room_id = room_current.west
                            change_room = True
                            valid = True
                        elif room_id == "roomCave__3_lllm_treasure_crevasse":
                            direction = "East"
                            room_id = room_current.east
                            change_room = True
                            valid = True
                        elif room_id == "roomCave_8_mr_crevasse":
                            direction = "north"
                            room_id = room_current.north
                            change_room = True
                            valid = True
                        elif room_id == "roomCave_9_mr_crevasse":
                            direction = "south"
                            room_id = room_current.south
                            change_room = True
                            valid = True
                        if valid:
                            spell_persuade = 2
                        print("You feel a great sense of power from the utterance of your words, causing you to jump across the crevasse.")
                # Light (I open light)
                # Obtained from Barn
                elif option == "ozh groth sol":
                    if light_counter < LIGHT_DURATION:
                        if light_counter:
                            print("You feel a surge of energy emit from the utterance of your words as the ball of light brightens.")
                        else:
                            print("You feel a surge of energy emit from the utterance of your words as a ball of light appears in front of you.")
                        light_counter = LIGHT_DURATION
                    valid = True
                    spell_light = 2
                # Heal (I without illness)
                # Obtained at House/Never
                elif option == "ozh vo'irush":
                    if not stat.health == HEALTH_MAX:
                        stat.health = HEALTH_MAX
                        print("You feel a surge of energy emit from the utterance of your words into your wounds.")
                        valid = True
                        spell_heal = 2
                # Feed (I eat earth)
                # Obtained at House/Never
                elif option == "ozh gluth nith":
                    stat.hunger = HUNGER_MAX
                    print("You feel a surge of energy emit from the utterance of your words into your stomach.")
                    valid = True
                    spell_feed = 2
                # Kill (I eat your soul)
                # From losing the game at the end (implicit)
                elif option == "ozh gluth izh sol":
                    if not room_current.character_dead or room_id.startswith("roomLair") or (room_id.startswith("roomCave") and creature_chase_counter in [1,2]) or (room_id.startswith("roomJail") and jail_guard_counter in [1,2]):
                        room_current.character_dead = True
                        print("You feel a surge of energy emit from the utterance of your words, consuming the soul of ", end = "")
                        valid = True
                        spell_kill = 2
                        if room_id == "roomCarnivalShellGame":
                            print("the old woman. As she topples over, all her gold is spilled across the ground.")
                            room_current.is_bet = False
                            room_current.gold += inv_shell.gold
                            inv_shell.gold = 0
                            room_current.items_present()
                        elif room_id.startswith("roomJail"):
                            print("a jail guard. The rest surround you and take you down.")
                            end_game = True
                        elif room_id == "roomCarnivalWheelGame":
                            print("the man. The crowd goes into panic as guards enter the tent and overwhelm you.")
                            end_game = True
                        elif room_id == "roomCarnivalFood":
                            print("the vendor. He falls over, leaving his supply of food behind.")
                            room_current.is_buy = False
                            room_current.funnel_cake += inv_food.funnel_cake
                            inv_food.funnel_cakes = 0
                            room_current.pie += 10
                            room_current.items_present()
                        elif room_id == "roomBridge":
                            print("the troll. It falls over, dropping the funnel cakes in its hands.")
                            room_current.east_blocked = False
                            room_current.funnel_cake += 1
                            room_current.half_funnel_cake += 3
                            room_current.items_present()
                        elif room_id == "roomGeneralStore":
                            print("the shopkeeper, leaving his store supplies behind.")
                            room_current.is_buy = False
                            room_current.is_sell = False
                            room_current.oil += 5
                            room_current.foot += 5
                            room_current.lantern += 1
                            room_current.bandage += 5
                            room_current.items_present()
                        elif room_id == "roomBlacksmith":
                            print("the blacksmith, leaving his supplies behind.")
                            room_current.is_buy = False
                            room_current.is_sell = False
                            room_current.pickaxe += 2
                            room_current.hook += 3
                            room_current.items_present()
                        elif room_id == "roomAlchemist":
                            print("Tim the Enchanter, leaving his supplies behind.")
                            room_current.is_buy = False
                            room_current.is_fill = False
                            room_current.is_sell = False
                            room_current.potion += 3
                            room_current.flask += 4
                            room_current.items_present()
                        elif room_id in ("roomCarnival","roomCourtyardNorth","roomCourtyardSouth"):
                            print("a random civilian. The loud noise alerts the town guards, who catch up to you and kill you.")
                            end_game = True
                        elif room_id == "roomGate":
                            print("the gate guard. Another nearby guard one draws his sword and impales you.")
                            end_game = True
                        elif room_id == "roomRoadCorner" and room_road_corner.counter_1:
                            print("the black knight. He shouts, \"IZH VO'POZ!\" before his body vaporizes into nothing.")
                            if not spell_persuade:
                                spell_persuade = 1
                            room_road_corner.west_blocked = False
                        elif room_id == "roomHouseOffice":
                            room_current.counter_2 += 1
                            if room_current.counter_2 == 1:
                                print("Eden Von Roquefort. His body flies back and crashes on the desk.")
                            elif room_current.counter_2 == 2:
                                print("Vesh'kathal. She resists the shock and charges towards you, knocking the staff out of your hand. Merely grazing her arm against the holy staff causes her scales to burn, making her to topple over in pain.")
                                inv.staff -= 1
                                room_current.staff += 1
                                room_current.items_present()
                            else:
                                print("Vesh'kathal. She is severly weaked, but manages to stay alive.")
                        elif room_id.startswith("roomCave"):
                            print("the creature, which resists the spell. It only gets angrier.")
                        elif room_id.startswith("roomLair"):
                            print("the creature, which resists the spell. It only gets angrier.")
                            if not room_lair_chase:
                                room_lair_chase = True
                        elif room_id == "roomLake":
                            print("the stranger, leaving his supplies behind.")
                            room_current.pie += 1
                            room_current.items_present()
                # Kill self (My life ends)
                # From Journal
                elif option == "ozh sol fek":
                    print("You feel a surge of energy emit from the utterance of your words as your own heart stops.")
                    end_game = True
                    valid = True
                    spell_killself = 2
                if spell and not valid:
                    print("You feel a strange sense of energy flow throughout your body although nothing else happens.")

                # Responses
                if room_id == "roomRoadCorner" and not room_current.character_dead and room_current.counter_1 and option not in ("ozh gluth izh sol","izh vo'poz"):
                    print("The black knight stands silently, ignoring your words.")
                elif room_id == "roomBookMirror" and not room_current.character_dead:
                    print("\nThe gargoyle says, \"%s\" in return." % reverse_cap(option))
                    if option == "los hzi htulg hzo":
                        print("You are overwhelmed with pain and agony as you fall to your knees.")
                        end_game = True
                    elif option == "zop'ov hzi":
                        print("You stand motionless... forever.")
                        end_game = True
                    elif option == "los htorg hzo":
                        if not room_current.counter_1:
                            print("A ball of light appears in the room.")
                        else:
                            print("The ball of light brightens.")
                        # statement has no effect, deepsource
                        # roomCurrent.counter_1
                    elif option == "kef los hzo":
                        print("It crumbles into pieces. A pedestal emerges from the floor, with a mysterious book on it.")
                        room_current.character_dead = True
                        room_current.item_found = True
                        room_current.book += 1
                        room_current.items_present()
        # Filler commands
        # Do nothing important
        # Lie down
        elif option in ("save","save game","save the game"):
            print("HAHAHAHA. YOU THOUGHT THIS GAME WAS ACTUALLY GOOD ENOUGH TO HAVE A SAVE FEATURE?")
            not_turn = True
        elif option in ("load","load game","load saved game"):
            print("No saved game to load.")
            not_turn = True
        elif option.startswith("lie down on") or option.startswith("lie down in"):
            option = option[11:]
            if option in ("floor","ground","back"):
                    print("You lie down. It'x pretty relaxing.")
            elif room_id == "roomJailCell":
                if option == "haystack":
                    print("You lie down. The haystack makes your back a bit itchy, but you've gotten used to it by now.")
            else:
                print("You can't do that.")
        elif option.endswith("lie down"):
            print("You lie down. It's pretty relaxing.")
        # Wait
        elif option.startswith("wait") or option == "z":
            print("Time passes.")
        # Do Nothing
        elif option == "do nothing":
            print("Nothing done.")
        # Dance
        elif option in ("dance","jig"):
            print("You have the time of your life.")
        # Sing
        elif option.startswith("sing"):
            option = option[5:]
            print('You sing, "%s" to your heart\'s content.')
        # Super powers
        elif option.startswith("fly") or option.startswith("teleport") or option.startswith("turn invisible") or option.startswith("breathe fire"):
            print("As cool as it would be to %s, you can't. Sorry you don't have super powers." % option)
        # Hug
        elif option.startswith("hug"):
            print("For super convoluted lore reasons, you can't %s. Something about an evil witch and ancient curses. Pretty deep stuff." % option)
        # Emoticons
        elif option == "d:":
            print("No need to be so sad.")
        elif option in (":)",":>)",":D"):
            print(":)")
        # Buy
        # Exhange money for items in shops
        elif option.startswith("buy") or option.startswith("purchase"):
            if option.startswith("buy"):
                option = option[4:]
            elif option.startswith("purchase"):
                optoin = option[9:]
            if room_current.is_buy:
                if option == "":
                    print("Buy what?")
                    not_turn = True
                else:
                    buy_pickaxe = False
                    buy_funnel_cake = False
                    buy_foot = False
                    buy_lantern = False
                    buy_oil = False
                    buy_pie = False
                    buy_hook = False
                    buy_bandage = False
                    buy_ticket = False
                    buy_potion = False
                    # Checking what is being bought and how many
                    # Buy pickaxe
                    if option in ("pick","pickaxe","a pick","a pickaxe"):
                        buy_count = 1
                        buy_pickaxe = True
                    elif option.endswith("pickaxe"):
                        buy_count = option[:len(option) - len("pickaxe") - 1]
                        buy_pickaxe = True
                    elif option.endswith("pickaxes"):
                        buy_count = option[:len(option) - len("pickaxes") - 1]
                        buy_pickaxe = True
                    elif option.endswith("pick"):
                        buy_count = option[:len(option) - len("pick") - 1]
                        buy_pickaxe = True
                    elif option.endswith("picks"):
                        buy_count = option[:len(option) - len("picks") - 1]
                        buy_pickaxe = True
                    # Buy funnel cake
                    elif option.startswith("funnel") or option.startswith("cake"):
                        buy_count = 1
                        buy_funnel_cake = True
                    elif option.endswith("funnel cake"):
                        buy_count = option[:len(option) - len("funnel cake") - 1]
                        buy_funnel_cake = True
                    elif option.endswith("funnel cakes"):
                        buy_count = option[:len(option) - len("funnel cakes") - 1]
                        buy_funnel_cake = True
                    elif option.endswith("cake"):
                        buy_count = option[:len(option) - len("cake") - 1]
                        buy_funnel_cake = True
                    elif option.endswith("cakes"):
                        buy_count = option[:len(option) - len("cakes") - 1]
                        buy_funnel_cake = True
                    # Buy lucky rabbit foot
                    elif option.startswith("lucky") or option.startswith("rabbit") or option.startswith("foot") or option.startswith("feet"):
                        buy_count = 1
                        buy_foot = True
                    elif option.endswith("lucky rabbit foot") or option.endswith("lucky rabbit feet"):
                        buy_count = option[:len(option) - len("lucky rabbit foot") - 1]
                        buy_foot = True
                    elif option.endswith("lucky rabbit"):
                        buy_count = option[:len(option) - len("lucky rabbit") - 1]
                        buy_foot = True
                    elif option.endswith("lucky foot") or option.endswith("lucky feet"):
                        buy_count = option[:len(option) - len("lucky foot") - 1]
                        buy_foot = True
                    elif option.endswith("foot") or option.endswith("feet"):
                        buy_count = option[:len(option) - len("foot") - 1]
                        buy_foot = True
                    # Buy lantern
                    elif option == "lantern":
                        buy_count = 1
                        buy_lantern = True
                    elif option == "lanterns":
                        buy_count = 1
                        buy_lantern = True
                    elif option.endswith("lantern"):
                        buy_count = option[:len(option) - len("lantern") - 1]
                        buy_lantern = True
                    elif option.endswith("lanterns"):
                        buy_count = option[:len(option) - len("lanterns") - 1]
                        buy_lantern = True
                    # Buy vial of lantern oil
                    elif option.startswith("vial") or option.startswith("oil") or option.startswith("lantern oil"):
                        buy_count = 1
                        buy_oil = True
                    elif option.endswith("vials of lantern oil"):
                        buy_count = option[:len(option) - len("vials of lantern oil") - 1]
                        buy_oil = True
                    elif option.endswith("vial of lantern oil"):
                        buy_count = option[:len(option) - len("vial of lantern oil") - 1]
                        buy_oil =True
                    elif option.endswith("vial of oil"):
                        buy_count = option[:len(option) - len("vial of oil") - 1]
                        buy_oil =True
                    elif option.endswith("vials of oil"):
                        buy_count = option[:len(option) - len("vials of oil") - 1]
                        buy_oil =True
                    elif option.endswith("oil"):
                        buy_count = option[:len(option) - len("oil") - 1]
                        buy_oil = True
                    elif option.endswith("vial"):
                        buy_count = option[:len(option) - len("vial") - 1]
                        buy_oil =True
                    elif option.endswith("vials"):
                        buy_count = option[:len(option) - len("vials") - 1]
                        buy_oil =True
                    # Buy pie
                    elif option.startswith("chicken") or option.startswith("pie"):
                        buy_count = 1
                        buy_pie = True
                    elif option.endswith("chicken pot pie"):
                        buy_count = option[:len(option) - len("chicken pot pie") - 1]
                        buy_pie = True
                    elif option.endswith("chicken pot pies"):
                        buy_count = option[:len(option) - len("chicken pot pies") - 1]
                        buy_pie = True
                    elif option.endswith("chicken pie"):
                        buy_count = option[:len(option) - len("chicken pie") - 1]
                        buy_pie = True
                    elif option.endswith("chicken pies"):
                        buy_count = option[:len(option) - len("chicken pies") - 1]
                        buy_pie = True
                    elif option.endswith("pie"):
                        buy_count = option[:len(option) - len("pie") - 1]
                        buy_pie = True
                    elif option.endswith("pies"):
                        buy_count = option[:len(option) - len("pies") - 1]
                        buy_pie = True
                    # Buy grappling hook
                    elif option.startswith("grappling") or option.startswith("hook"):
                        buy_count = 1
                        buy_hook = True
                    elif option.endswith("grappling hook"):
                        buy_count = option[:len(option) - len("grappling hook") - 1]
                        buy_hook = True
                    elif option.endswith("grappling hooks"):
                        buy_count = option[:len(option) - len("grappling hooks") - 1]
                        buy_hook = True
                    elif option.endswith("hook"):
                        buy_count = option[:len(option) - len("hook") - 1]
                        buy_hook = True
                    elif option.endswith("hooks"):
                        buy_count = option[:len(option) - len("hooks") - 1]
                        buy_hook = True
                    # Buy bandage
                    elif option in ("bandage","bandages"):
                        buy_count = 1
                        buy_bandage = True
                    elif option.endswith("bandage"):
                        buy_count = option[:len(option) - len("bandage") - 1]
                        buy_bandage = True
                    elif option.endswith("bandages"):
                        buy_count = option[:len(option) - len("bandages") - 1]
                        buy_bandage = True
                    # Buy ticket
                    elif option in ("raffle ticket","ticket","raffle"):
                        buy_count = 1
                        buy_ticket = True
                    elif option.endswith("raffle ticket"):
                        buy_count = option[:len(option) - len("raffle ticket") - 1]
                        buy_ticket = True
                    elif option.endswith("ticket"):
                        buy_count = option[:len(option) - len("ticket") - 1]
                        buy_ticket = True
                    elif option.endswith("raffle tickets"):
                        buy_count = option[:len(option) - len("raffle tickets") - 1]
                        buy_ticket = True
                    elif option.endswith("tickets"):
                        buy_count = option[:len(option) - len("tickets") - 1]
                        buy_ticket = True
                    # Potion
                    elif option in ("potion","potion of rejuvination"):
                        buy_count = 1
                        buy_potion = True
                    elif option.endswith("potion of rejuvination"):
                        buy_count = option[:len(option) - len("potion of rejuvination") - 1]
                        buy_potion = True
                    elif option.endswith("potions of rejuvination"):
                        buy_count = option[:len(option) - len("potions of rejuvination") - 1]
                        buy_potion = True
                    elif option.endswith("potion"):
                        buy_count = option[:len(option) - len("potion") - 1]
                        buy_potion = True
                    elif option.endswith("potions"):
                        buy_count = option[:len(option) - len("potions") - 1]
                        buy_potion = True
                    else:
                        print("You cannot buy that.")
                        not_turn = True
                    if buy_pickaxe or buy_funnel_cake or buy_foot or buy_lantern or buy_oil or buy_pie or buy_hook or buy_bandage or buy_ticket or buy_potion:
                        # Item information
                        if buy_funnel_cake:
                            item_name = "funnel cake"
                            items_name = "funnel cakes"
                            inv_item = inv.funnel_cake
                            price = PRICE_BUY_FUNNELCAKE
                        elif buy_pie:
                            item_name = "chicken pot pie"
                            items_name = "chicken pot pies"
                            inv_item = inv.pie
                            price = PRICE_BUY_PIE
                        elif buy_foot:
                            item_name = "lucky rabbit foot"
                            items_name = "lucky rabbit feet"
                            inv_item = inv.foot
                            price = PRICE_BUY_FOOT
                        elif buy_lantern:
                            item_name = "lantern"
                            items_name = "lanterns"
                            inv_item = inv.lantern
                            price = PRICE_BUY_LANTERN
                        elif buy_oil:
                            item_name = "vial of lantern oil"
                            items_name = "vials of lantern oil"
                            inv_item = inv.oil
                            price = PRICE_BUY_OIL
                        elif buy_bandage:
                            item_name = "bandage"
                            items_name = "bandages"
                            inv_item = inv.bandage
                            price = PRICE_BUY_BANDAGE
                        elif buy_pickaxe:
                            item_name = "pickaxe"
                            items_name = "pickaxes"
                            inv_item = inv.pickaxe
                            price = PRICE_BUY_PICKAXE
                        elif buy_hook:
                            item_name = "grappling hook"
                            items_name = "grappling hooks"
                            inv_item = inv.hook
                            price = PRICE_BUY_HOOK
                        elif buy_ticket:
                            item_name = "raffle ticket"
                            items_name = "raffle tickets"
                            inv_item = inv.ticket
                            price = PRICE_BUY_TICKET
                        elif buy_potion:
                            item_name = "potion of rejuvination"
                            items_name = "potions of rejuvination"
                            inv_item = inv.potion
                            price = PRICE_BUY_POTION
                        item_in_store = False
                        # Funnel Cakes Galore
                        if room_id == "roomCarnivalFood":
                            shop_keeper_name = "vendor"
                            if inv_food.funnel_cake:
                                if buy_funnel_cake or buy_pie:
                                    item_in_store = True
                            else:
                                if buy_pie:
                                    item_in_store = True
                        # General Store
                        elif room_id == "roomGeneralStore":
                            shop_keeper_name = "the shopkeeper"
                            if buy_foot or buy_lantern or buy_oil or buy_bandage:
                                item_in_store = True
                        # Blacksmith
                        elif room_id == "roomBlacksmith":
                            shop_keeper_name = "the blacksmith"
                            if buy_pickaxe or buy_hook:
                                item_in_store = True
                        # Wheel of Mystery
                        elif room_id == "roomCarnivalWheelGame":
                            shop_keeper_name = "the man"
                            if buy_ticket:
                                item_in_store = True
                        # Alchemist's hut
                        elif room_id == "roomAlchemist":
                            shop_keeper_name = "Tim the Enchanter"
                            if buy_potion:
                                item_in_store = True
                            # Checks if invItem buy_count is valid
                            # Must be equivalent to an integer
                            # Must not be negative
                            # With cost, must not exceed inv.gold
                        if item_in_store:
                            buy_item_count_okay = False
                            try:
                                buy_count = float(buy_count)
                                if float(buy_count) % 1 == 0 and buy_count > 0:
                                    buy_item_count_okay = True
                                    buy_count = int(buy_count)
                                else:
                                    print("You cannot buy",buy_count,"%s." % items_name)
                                    not_turn = True
                            except ValueError:
                                print("You cannot buy \"" + buy_count + "\" %s." % items_name)
                                not_turn = True
                            # Buying funnel cakes
                            if buy_item_count_okay:
                                # Checks if inventory has enough money
                                if inv.gold >= buy_count * price:
                                    # If buying funnel cakes past limit
                                    if buy_funnel_cake and buy_count >= inv_food.funnel_cake:
                                        if buy_count > inv_food.funnel_cake:
                                            print("\n\"It looks like you bought out my final batch of funnel cakes for today. There's only %s cakes left, so I guess that'll do.\"" % inv_food.funnel_cake)
                                        else:
                                            print("\n\"It looks like you bought out my final batch of funnel cakes. I've run out of batter so I won't be able to make any more for today.\"")
                                        buy_count = inv_food.funnel_cake
                                    inv.gold -= buy_count * price
                                    if buy_count > 1:
                                        print("You give",shop_keeper_name,buy_count * price,'gold. He gives you %s %s.' % (buy_count, items_name))
                                    elif buy_count == 1:
                                        print("You give",shop_keeper_name,buy_count * price,'gold. He gives you a %s.' % item_name)
                                    # Adds purchased items to inventory
                                    if buy_funnel_cake:
                                        inv.funnel_cake += buy_count
                                        inv_item += buy_count
                                        inv_food.funnel_cake -= buy_count
                                    elif buy_pie:
                                        inv.pie += buy_count
                                        inv_item += buy_count
                                    elif buy_pickaxe:
                                        inv.pickaxe += buy_count
                                        inv_item += buy_count
                                    elif buy_foot:
                                        inv.foot += buy_count
                                        inv_item += buy_count
                                    elif buy_lantern:
                                        inv.lantern += buy_count
                                        inv_item += buy_count
                                    elif buy_oil:
                                        inv.oil += buy_count
                                        inv_item += buy_count
                                    elif buy_hook:
                                        inv.hook += buy_count
                                        inv_item += buy_count
                                    elif buy_bandage:
                                        inv.bandage += buy_count
                                        inv_item += buy_count
                                    elif buy_ticket:
                                        inv.ticket += buy_count
                                        inv_item += buy_count
                                    elif buy_potion:
                                        inv.potion += buy_count
                                        inv_item += buy_count
                                    # Tells users item count
                                    if inv_item:
                                        if inv_item > 1:
                                            print("You have",inv_item,"%s." % items_name)
                                        else:
                                            print("You have",inv_item,"%s." % item_name)
                                        print("You have",inv.gold,"gold.")
                                        if room_id == "roomCarnivalWheelGame" and inv.ticket >= 1 and room_carnival_wheel_game.is_buy:
                                            # Can't buy more tickets
                                            room_carnival_wheel_game.is_buy = False
                                            # No one in room
                                            room_carnival_wheel_game.character_dead = True
                                            # Can return ticket in roomCarnival
                                            room_carnival.is_give = True
                                            # Wheel game is closed
                                            room_carnival.west_blocked = True
                                            print("\nJust as you buy the ticket, someone walks around behind the stage and notices magnets lined across the back of the wheel. \"HEY! This raffle's rigged! Throw this FRAUD in jail!\" Guards enter the tent and arrest the raffle host.\n\nA spokesperson walks in and announces to the crowd, \"I apologize on behalf of the carnival for what has happened here. If you would like to be compensated for your tickets, it will be arranged just outside in the fair grounds. Now, everyone out. This man will be taken to the town jail for his crime.\" The crowd of people storm out, eager to give their tickets back.") ## continue make more concise and format well
                                            # print("\"Settle down everyone. We've sold our last ticket. It's time to spin the wonderful wheel of mystery!\" The man takes hold of the large wheel at the centre of the stage and with all his weight, pushes one end down, causing it to turn. The crowd cheers as the numbers along the edge pass the ticker at the top of the wheel. It finally stops at 42. \"I have the ticket! I have it!\" shouts a bearded man in the crowd. Just as he approaches the stage, someone grabs hold of him. \"Wait a minute, I've seen you before.\" His beard is torn off, revealing him in disguise. \"You won yesterday's raffle. In fact, you've been winning the raffle ever since this bloody carnival began. This raffle is rigged! Get 'em!\" Guards outside the tent notice the commotion and enter, grabbing hold of the raffle host and his accomplice to arrest them. \n\nA spokesperson enters the tent. She announces to the crowd, \"I apologize on behalf of the carnival for what has happened here. If you would like to be compensated for your tickets, it will be arranged outside in the fair grounds. Now, everyone out. These two will be taken to the town jail for their crimes.\" The crowd begrungenly walks out.")
                                    else:
                                        print("You have no %s." % items_name)
                                else:
                                    if buy_count > 1:
                                        print("You do not have enough gold to buy",buy_count,"%s." % items_name)
                                        not_turn = True
                                    else:
                                        print("You do not have enough gold to buy a %s." % item_name)
                                        not_turn = True
                        else:
                            print("You cannot buy any",items_name,"here.")
                            not_turn = True
            # If not isBuy
            else:
                print("You cannot buy anything here.")
                not_turn = True
        # Bet
        # For gambling in shops
        # Carnival Shell Game
        # Carnival Wheel Game
        elif option.startswith("bet") or option.startswith("gamble"):
            if option.startswith("bet"):
                option = option[4:]
            elif option.startswith("gamble"):
                option = option[7:]
            if room_current.is_bet:
                if option == "":
                    print("Bet what?")
                    option = False
                    not_turn = True
                else:
                    try:
                        if float(option) % 1 == 0:
                            option = int(option)
                        else:
                            option = float(option)
                        print("Bet",option,"what?")
                        not_turn = True
                        option = False
                    except ValueError:
                        pass
                if option:
                    # Sybil's Shell Game
                    if room_id == "roomCarnivalShellGame":
                        # If bet is already made
                        bet_gold = True
                        if room_carnival_shell_game.bet_made:
                            print("You've already bet",s_bet,"gold. Sybil is waiting for you to choose the left, middle, or right shell.")
                            not_turn = True
                        # If bet is not made
                        else:
                            if option.endswith("gold"):
                                s_bet = option[:len(option) - len("gold") - 1]
                            else:
                                print("You cannot bet that.")
                                bet_gold = False
                                not_turn = True
                            # Checks if bet s_bet is valid
                            bet_gold_okay = False
                            if bet_gold:
                                if s_bet == "":
                                    print("Bet how much gold?")
                                    not_turn = True
                                else:
                                    try:
                                        if float(s_bet) % 1 == 0 and float(s_bet) >= 0:
                                            bet_gold_okay = True
                                            s_bet = int(float(s_bet))
                                        else:
                                            bet_gold = False
                                            print('You cannot bet "' + s_bet + '" gold.')
                                            not_turn = True
                                    except ValueError:
                                        if s_bet in ("all","every"):
                                            bet_gold_okay = True
                                            s_bet = inv.gold
                                        elif s_bet in ("none","no","zero"):
                                            bet_gold_okay = True
                                            s_bet = 0
                                        else:
                                            print('You cannot bet "' + s_bet + '" gold.')
                                            not_turn = True
                            if bet_gold_okay:
                                if inv.gold >= s_bet:
                                    inv.gold -= s_bet
                                    inv_shell.gold += s_bet
                                    if s_bet > 0:
                                        print("You bet",s_bet,"gold.",end=" ")
                                    else:
                                        print('You bet nothing. "Playing just for fun, I see. So it shall be."',end=" ")
                                    print('Sybil takes out a stone, places it under one of the shells, and elaborately shuffles them all on the table. "Choose a shell," she says, pointing to the left, middle and right shells.')
                                    print("\nYou have %s gold." % inv.gold)
                                    room_carnival_shell_game.bet_made = True
                                else:
                                    print("You do not have enough gold to bet",s_bet,"gold.")
                                    not_turn = True
            else:
                print("You cannot bet on anything here.")
                not_turn = True
        # Choose
        # For gambling in shops
        # Carnival Shell Game
        elif option.startswith("choose"):
            option = option[7:]
            if room_current.is_bet:
                if option == "":
                    print("Choose what?")
                    not_turn = True
                else:
                    # Sybil's Shell Game
                    if room_id == "roomCarnivalShellGame":
                        if room_current.bet_made:
                            # If bet is already made
                            if "left" in option:
                                s_choice = "left"
                            elif "middle" in option:
                                s_choice = "middle"
                            elif "right" in option:
                                s_choice = "right"
                            else:
                                s_choice = "invalid"
                            if s_choice != "invalid":
                                # If win
                                if random.randint(1,100) < (33 + LUCKY_FOOT_MODIFIER * inv.foot):
                                    if room_current.character_dead:
                                        print("You choose the",s_choice,"shell. As you just killed Sybil, you take a look under the shell and see that you have won. Congratulations for being a terrible person.")
                                        room_current.bet_made = False
                                    else:
                                        print("Sybil raises the",s_choice,"shell and reveals the stone underneath.")
                                        print('"Ahh! Luck is on your side," she exclaims.',end=" ")
                                        if s_bet > 0:
                                            if (s_bet * SHELL_REWARD_MULTIPLIER) >= inv_shell.gold:
                                                print("\"You seem you have run my coffers dry. My days of carnival work here is over. This is all I can give you.\" She hands you %s gold and begins packing her stuff to leave." % inv_shell.gold)
                                                inv.gold += inv_shell.gold
                                                inv_shell.gold = 0
                                                room_current.is_bet = False
                                                room_carnival.south_blocked = True
                                            else:
                                                inv.gold += s_bet * SHELL_REWARD_MULTIPLIER
                                                inv_shell.gold -= s_bet * SHELL_REWARD_MULTIPLIER
                                                print("\"Here's your %s gold.\"" % (s_bet * SHELL_REWARD_MULTIPLIER))
                                        else:
                                            print('"If only you bet something, you could reap your reward. Oh well."')
                                        print("\nYou have",inv.gold,"gold.")
                                        room_current.bet_made = False
                                # If lose
                                else:
                                    print("Sybil raises the",s_choice,"shell and reveals nothing underneath.")
                                    print('"Luck is not on your side today," she exclaims.',end=" ")
                                    if s_bet > 0:
                                        print('"I guess your gold belongs to me."')
                                    else:
                                        print('"I guess you are fortunate not to bet anything."')
                                    room_current.bet_made = False
                            else:
                                print("Choose the left, middle, or right shell.")
                        # If bet is not made
                        else:
                            print("You cannot choose a shell until you bet gold.")
                            not_turn = True
        elif option.startswith("give"):
            if option == "give":
                option = ""
            else:
                option = option[len("give "):]
            if room_id == "roomBridge":
                # name X gold -> X gold
                if option.startswith("troll"):
                    if option == "troll":
                        option = ""
                    else:
                        option = option[len("troll "):]
                elif option.startswith("ugg"):
                    if option == "ugg":
                        option = ""
                    else:
                        option = option[len("ugg "):]
                # X gold to name -> X gold
                elif option.endswith("to troll"):
                    option = option[:len(option) - len(" to troll")]
                elif option.endswith("to ugg"):
                    option = option[:len(option) - len(" to ugg")]
            elif room_id == "roomGate":
                # name X shrubbery
                if option.startswith("guard"):
                    if option == "guard":
                        option = ""
                    else:
                        option = option[len("guard "):]
                elif option.startswith("the guard"):
                    if option == "the guard":
                        option = ""
                    else:
                        option = option[len("the guard"):]
                # X shrubbery to name
                elif option.endswith("to guard"):
                    option = option[:len(option) - len(" to guard")]
                elif option.endswith("to the guard"):
                    option = option[:len(option) - len(" to the guard")]
            elif room_id == "roomCarnival":
                # spokesperson X ticket
                if option.startswith("spokesperson"):
                    if option == "spokesperson":
                        option = ""
                    else:
                        option = option[len("spokesperson "):]
                elif option.startswith("the spokesperson"):
                    if option == "the spokesperson":
                        option = ""
                    else:
                        option = option[len("the spokesperson ")]
                # X ticket to spokesperson
                elif option.endswith("to spokesperson"):
                    option = option[:len(option) - len(" to spokesperson")]
                elif option.endswith("to the spokesperson"):
                    option = option[:len(option) - len(" to the spokesperson")]
            elif room_id == "roomLake":
                if option.startswith("stranger"):
                    if option == "stranger":
                        option = ""
                    else:
                        option = option[len("stranger ")]
                elif option.endswith("to stranger"):
                    option = option[:len(option) - len(" to stranger")]
            elif room_id == "roomHouseOffice":
                # eden X staff
                if option.startswith("eden von roquefort"):
                    if option == "eden von roquefort":
                        option = ""
                    else:
                        option = option[len("eden von roquefort")]
                elif option.startswith("eden"):
                    if option == "eden":
                        option = ""
                    else:
                        option = option[len("eden ")]
                elif option.startswith("roquefort"):
                    if option == "roquefort":
                        option = ""
                    else:
                        option = option[len("roquefort ")]
                # X staff to eden
                elif option.endswith("to eden von roquefort"):
                    option = option[:len(option) - len(" to eden von roquefort")]
                elif option.endswith("to eden"):
                    option = option[:len(option) - len(" to eden")]
                elif option.endswith("to roquefort"):
                    option = option[:len(option) - len(" to roquefort")]
            if room_current.is_give:
                give_gold = False
                give_funnel_cake = False
                give_half_funnel_cake = False
                give_shrubbery = False
                give_ticket = False
                give_staff = False
                give_bird = False
                if option == "":
                    print("Give what?")
                    not_turn = True
                else:
                    # Gold
                    if option == "gold":
                        give_count = 1
                        give_gold = True
                    elif option.endswith("gold"):
                        give_count = option[:len(option) - len("gold") - 1]
                        give_gold = True
                    # Half-eaten funnel cake
                    elif option in ("half-eaten cake","half cake","half-eaten funnel cake","half eaten funnel cake","half funnel cake","half-eaten cakes","half cakes","half-eaten funnel cakes","half eaten funnel cakes","half funnel cakes"):
                        give_count = 1
                        give_half_funnel_cake = True
                    # Funnel cake
                    elif option in ("cake","cakes","funnel cake","funnel cakes"):
                        give_count = 1
                        give_funnel_cake = True
                    elif option.endswith("funnel cake"):
                        give_count = option[:len(option) - len("funnel cake") - 1]
                        give_funnel_cake = True
                    elif option.endswith("funnel cakes"):
                        give_count = option[:len(option) - len("funnel cakes") - 1]
                        give_funnel_cake = True
                    elif option.endswith("cake"):
                        give_count = option[:len(option) - len("cake") - 1]
                        give_funnel_cake = True
                    elif option.endswith("cakes"):
                        give_count = option[:len(option) - len("cakes") - 1]
                        give_funnel_cake = True
                    # shrubbery
                    elif option in ("shrubberies","shrubbery"):
                        give_count = 1
                        give_shrubbery = True
                    elif option.endswith("shrubbery"):
                        give_count = option[:len(option) - len("shrubbery") - 1]
                        give_shrubbery = True
                    elif option.endswith("shrubberies"):
                        give_count = option[:len(option) - len("shrubberies") - 1]
                        give_shrubbery = True
                    # Raffle ticket
                    elif option in ("raffle ticket","ticket","raffle tickets","tickets"):
                        give_count = 1
                        give_ticket = True
                    elif option.endswith("raffle ticket"):
                        give_count = option[:len(option) - len("raffle ticket") - 1]
                        give_ticket = True
                    elif option.endswith("raffle tickets"):
                        give_count = option[:len(option) - len("raffle tickets") - 1]
                        give_ticket = True
                    elif option.endswith("ticket"):
                        give_count = option[:len(option) - len("ticket") - 1]
                        give_ticket = True
                    elif option.endswith("tickets"):
                        give_count = option[:len(option) - len("tickets") - 1]
                        give_ticket = True
                    # Staff
                    elif option in ("staff","the staff","staff of garrotxa","the staff of garrotxa"):
                        give_count = 1
                        give_staff = True
                    elif option.endswith("staff"):
                        give_count = option[:len(option) - len("staff") - 1]
                        give_staff = True
                    elif option.endswith("the staff of garrotxa"):
                        give_count = option[:len(option) - len("the staff of garrotxa") - 1]
                        give_staff = True
                    elif option.endswith("staff of garrotxa"):
                        give_count = option[:len(option) - len("staff of garrotxa") - 1]
                        give_staff = True
                    # Wooden Bird
                    elif option in ("bird","wooden bird","birds","wooden birds"):
                        give_count = 1
                        give_bird = True
                    elif option.endswith("wooden bird"):
                        give_count = option[:len(option) - len("wooden bird") - 1]
                        give_bird = True
                    elif option.endswith("wooden birds"):
                        give_count = option[:len(option) - len("wooden birds") - 1]
                        give_bird = True
                    elif option.endswith("bird"):
                        give_count = option[:len(option) - len("bird") - 1]
                        give_bird = True
                    elif option.endswith("birds"):
                        give_count = option[:len(option) - len("birds") - 1]
                        give_bird = True
                    else:
                        print("You cannot give that.")
                        not_turn = True
                    if give_gold or give_funnel_cake or give_half_funnel_cake or give_shrubbery or give_ticket or give_staff or give_bird:
                        # Item Information
                        if give_gold:
                            item_name = "gold"
                            items_name = "gold"
                            inv_item = inv.gold
                        elif give_funnel_cake:
                            item_name = "a funnel cake"
                            items_name = "funnel cakes"
                            inv_item = inv.funnel_cake
                        elif give_half_funnel_cake:
                            item_name = "a half-eaten funnel cake"
                            items_name = "half-eaten funnel cakes"
                            inv_item = inv.half_funnel_cake
                        elif give_shrubbery:
                            item_name = "a shrubbery"
                            items_name = "shrubberies"
                            inv_item = inv.shrubbery
                        elif give_ticket:
                            item_name = "your raffle ticket"
                            items_name = "raffle tickets"
                            inv_item = inv.ticket
                        elif give_staff:
                            item_name = "the staff of Garrotxa"
                            items_name = "the staves of Garrotxa"
                            inv_item = inv.staff
                        elif give_bird:
                            item_name = "wooden bird"
                            items_name = "wooden birds"
                            inv_item = inv.bird
                        item_can_give = False
                        # Bridge
                        if room_id == "roomBridge":
                            receiver_name = "the troll"
                            if give_gold or give_funnel_cake or give_half_funnel_cake:
                                item_can_give = True
                        # Gate
                        if room_id == "roomGate":
                            receiver_name = "the guard"
                            if give_shrubbery:
                                item_can_give = True
                        # Carnival
                        if room_id == "roomCarnival":
                            receiver_name = "the spokesperson"
                            if give_ticket:
                                item_can_give = True
                        # Office
                        if room_id == "roomHouseOffice":
                            receiver_name = "Eden Von Roquefort"
                            if give_staff:
                                item_can_give = True
                        # Lake
                        if room_id == "roomLake":
                            receiver_name = "the stranger"
                            if give_bird:
                                item_can_give = True
                        if item_can_give:
                            give_item_count_okay = False
                            try:
                                give_count = float(give_count)
                                if float(give_count) % 1 == 0 and give_count > 0:
                                    give_item_count_okay = True
                                    give_count = int(give_count)
                                else:
                                    if give_count == 1:
                                        print("You can't give a %s." % item_name)
                                    else:
                                        print("You can't give",give_count,"%s." % items_name)
                            except ValueError:
                                print("You cannot give that.")
                                not_turn = True
                            if give_item_count_okay:
                                # Checks if inventory has enough item
                                if inv_item >= give_count:
                                    inv_item -= give_count
                                    if give_gold:
                                        inv.gold -= give_count
                                        inv_troll.gold += give_count
                                    elif give_funnel_cake:
                                        inv.funnel_cake -= give_count
                                        inv_troll.gold += give_count * TROLL_FUNNELCAKE_MULTIPLIER
                                    elif give_half_funnel_cake:
                                        inv.half_funnel_cake -= give_count
                                        inv_troll.gold += give_count * TROLL_HALFFUNNELCAKE_MULTIPLIER
                                    elif give_shrubbery:
                                        inv.shrubbery -= give_count
                                        inv_gate.shrubbery += give_count
                                    elif give_ticket:
                                        inv.ticket -= give_count
                                    elif give_staff:
                                        inv.staff -= give_count
                                    elif give_bird:
                                        inv.bird -= give_count
                                    # Give response
                                    if room_current.character_dead and room_id == "roomBridge":
                                        print('You place %s %s by the troll\'s body to pay respects.' % (give_count,items_name))
                                    else:
                                        if give_count == 1 and not give_gold:
                                            print(hi)
                                            #print('You give %s %s.' % (receiverName,itemName))
                                            #Deepsource warns about UnboundLocalError due to Variable used before assignment
                                        elif give_count > 1 and not give_gold:
                                            print('You give %s %s %s.' % (receiver_name,give_count,items_name))
                                        # Response once item given
                                        if not room_bridge.east_blocked and room_id == "roomBridge":
                                            print('"Thank you human! Ugg never have enough funnel cakes."')
                                        elif room_id == "roomCarnival":
                                            print("Amongst the crowd of people handing her tickets, she miscounts and gives you %s gold in compensation for your troubles." % RAFFLE_COMPENSATION)
                                            inv.gold += RAFFLE_COMPENSATION
                                            inv_spokesperson.ticket += 1
                                            print("\nYou have %s gold." % inv.gold)
                                        elif room_id == "roomHouseOffice":
                                            room_current.counter_1 = 1
                                            room_current.is_give = False
                                            room_current.character_dead = True # spawns vesh, which kills Eden
                                            room_current.counter_2 += 1
                                        elif room_id == "roomLake":
                                            print("\"Thank you!\" He gives a chicken pot pie.\n\n\"One more thing. You see that stone tablet? Whatever is written there is in language of demons, or the TONGUE OF THE OZKAVOSH. Some phrases are merely words. However, some are SPELLS and can grant you great powers when SPOKEN.\n\nOne such example is, \'OZH ENSH,\' which when spoken as a prefix followed by other words in Ozkavosh, forms a spell that will translate them for you.\nOnce you know what that spell is, you can SAY that spell on its own to cast it.\nYou can EXAMINE your SPELLS if you ever forget what they are.\n\nTry to figure out what written on that TABLET and see if you can open my LOCKBOX. You can take whatever is inside.\"")
                                            inv.pie += LAKE_PIE_REWARD
                                            room_current.is_give = False
                                            if not spell_learn:
                                                spell_learn = 2
                                    if room_bridge.east_blocked and inv_troll.gold < TROLL_GOAL and room_id == "roomBridge":
                                        print('"Ugg only needs %s gold left until Ugg has enough to buy all the funnel cakes Ugg wants."' % (TROLL_GOAL - inv_troll.gold))
                                # If not enough items in inventory to give
                                else:
                                    if give_count > 1:
                                        print("You do not have enough to give %s %s to %s." % (give_count,items_name,receiver_name))
                                        not_turn = True
                                    else:
                                        print("You do not have any %s to give to %s." % (items_name,receiver_name))
                                        not_turn = True
                        else:
                            print("You cannot give any",items_name,"here.")
                            not_turn = True
                        # Result after give
                        if room_bridge.east_blocked and inv_troll.gold >= TROLL_GOAL:
                            print('The troll celebrates as his funnel cake dreams are fulfilled. "Ugg is very happy!" he cheers. He grabs everything you\'ve given him and goes back under the bridge.')
                            room_bridge.east_blocked = False
                        if room_gate.north_blocked and inv_gate.shrubbery:
                            print("The guard takes a quick look. \"Yes, it is a good shrubbery. I like the laurels particularly.\" He lets you through the gate.")
                            print("You can now go North.")
                            room_gate.north_blocked = False
                            room_gate.is_give = False

            else:
                print("You can't give anything here.")
                not_turn = True
        # Sell
        # Exchange items for gold
        elif option.startswith("sell"):
            option = option[5:]
            if room_current.is_sell:
                if option == "":
                    print("Sell what?")
                    not_turn = True
                else:
                    sell_coal = False
                    sell_stone = False
                    # Checking what is being sold and how many
                    # Sell coal
                    if option in ("coal", "piece of coal", "pieces of coal"):
                        sell_count = 1
                        sell_coal = True
                    elif option.endswith("pieces of coal"):
                        sell_count = option[:len(option) - len("pieces of coal") - 1]
                        sell_coal = True
                    elif option.endswith("piece of coal"):
                        sell_count = option[:len(option) - len("piece of coal") - 1]
                        sell_coal = True
                    elif option.endswith("coal"):
                        sell_count = option[:len(option) - len("coal") - 1]
                        sell_coal = True
                    # Dragonstone
                    elif option in ("dragonstone", "stone"):
                        sell_count = 1
                        sell_stone = True
                    elif option.endswith("dragonstone"):
                        sell_count = option[:len(option) - len("dragonstone") - 1]
                        sell_stone = True
                    elif option.endswith("stone"):
                        sell_count = option[:len(option) - len("stone") - 1]
                        sell_stone = True
                    else:
                        print("You cannot sell that.")
                    if sell_coal or sell_stone:
                       # Item information
                        if sell_coal:
                            item_name = "piece of coal"
                            items_name = "pieces of coal"
                            inv_item = inv.coal
                            price = PRICE_SELL_COAL
                        elif sell_stone:
                            item_name = "dragonstone"
                            items_name = "dragonstones"
                            inv_item = inv.stone
                            price = PRICE_SELL_STONE
                        item_in_store = False
                        # Blacksmith
                        if room_id == "roomBlacksmith":
                            shop_keeper_name = "the blacksmith"
                            if sell_coal:
                                item_in_store = True
                        # Alchemist
                        if room_id == "roomAlchemist":
                            shop_keeper_name = "Tim the Enchanter"
                            if sell_stone:
                                item_in_store = True
                        if item_in_store:
                            sell_item_count_okay = False
                            try:
                                sell_count = float(sell_count)
                                if float(sell_count) % 1 == 0 and sell_count > 0:
                                    sell_item_count_okay = True
                                    sell_count = int(sell_count)
                                else:
                                    print("You cannot sell ",sell_count," %s." % items_name)
                                    not_turn = True
                            except ValueError:
                                if sell_count in ("all","every"):
                                    sell_count = inv_item
                                    sell_item_count_okay = True
                                elif sell_count in ("a","the","only one","only 1"):
                                    sell_count = 1
                                    sell_item_count_okay = True
                                else:
                                    print("You cannot sell \"" + sell_count + "\" %s." % items_name)
                                    not_turn = True
                            # Selling coal
                            if sell_item_count_okay:
                                # Checks if inventory has enough item
                                if inv_item >= sell_count:
                                    inv_item -= sell_count
                                    if sell_coal:
                                        inv.coal -= sell_count
                                    elif sell_stone:
                                        inv.stone -= sell_count
                                    if sell_count == 1:
                                        print("You give the %s" % shop_keeper_name,"a %s. He gives you %s gold." % (item_name,sell_count * price))
                                    elif sell_count > 1:
                                        print("You give the %s" % shop_keeper_name,"%s %s. He gives you %s gold." % (sell_count,items_name,sell_count * price))
                                    inv.gold += sell_count * price
                                    print("You have",inv.gold,"gold.")
                                    # Sell is completed
                                    if room_id == "roomAlchemist":
                                        room_current.is_sell = False
                                        room_current.is_buy = True
                                        room_current.is_fill = True
                                        print("\"Wow, a full-sized dragonstone! Once I get that ground up, that will make enough powder to last me a life time.\" He grabs a mortar and pestle and works away at the dragonstone. After tossing some odd-looking herbs and the powder into the cauldron, the water thickens and turns red almost immediately. \"My potions both heal your wounds and satisfy your hunger. If you have an empty flask, you can refill it for a reduced cost. Those flasks don't come cheap after all.\"")
                                        print("\nGoods available to buy:\n    Potion of rejuvination (%s gold)" % PRICE_BUY_POTION)
                                        print("\nGoods available to fill:\n    Flask (%s gold)" % PRICE_REFILL_POTION)
                                else:
                                    if sell_count > 1:
                                        print("You do not have %s %s." % (sell_count,items_name))
                                        not_turn = True
                                    else:
                                        print("You do not have have %s %s." % (sell_count,item_name))
                                        not_turn = True
                        else:
                            print("You cannot sell any",items_name,"here.")
                            not_ture = True
            # If not inSell
            else:
                print("You cannot sell anything here.")
                not_turn = True
        # Universally invalid action
        else:
            print("You cannot do that.")
            not_turn = True

#_______Special Decisions__________________________________________________________
# Being inside certain rooms allows for special actions.
# Shops, locked rooms

#_______Finished user input and all return values_______________________________


#_______Current Room____________________________________________________________
# Current room information
        # Refers to room classes for current room information
        if change_room:
            # Jail
            if room_id == "roomJailCell":
                room_current = room_jail_cell
            elif room_id == "roomJailCorridor":
                room_current = room_jail_corridor
            elif room_id == "roomJailFoyer":
                room_current = room_jail_foyer
            elif room_id == "roomJailAntechamber":
                room_current = room_jail_antechamber
            elif room_id == "roomJailHallway":
                room_current = room_jail_hallway
            elif room_id == "roomJailBreakRoom":
                room_current = room_jail_break_room
            elif room_id == "roomJailEntrance":
                room_current = room_jail_entrance
            # Town
            elif room_id == "roomCourtyardNorth":
                room_current = room_courtyard_north
            elif room_id == "roomCourtyardSouth":
                room_current = room_courtyard_south
            elif room_id == "roomBlacksmith":
                room_current = room_blacksmith
            elif room_id == "roomAlchemist":
                room_current = room_alchemist
            elif room_id == "roomCarnival":
                room_current = room_carnival
            elif room_id == "roomCarnivalShellGame":
                room_current = room_carnival_shell_game
            elif room_id == "roomCarnivalFood":
                room_current = room_carnival_food
            elif room_id == "roomCarnivalWheelGame":
                room_current = room_carnival_wheel_game
            elif room_id == "roomGeneralStore":
                room_current = room_general_store
            elif room_id == "roomGate":
                room_current = room_gate
            # Road
            elif room_id == "roomRoadSouth":
                room_current = room_road_south
            elif room_id == "roomRoadMid":
                room_current = room_road_mid
            elif room_id == "roomRoadNorth":
                room_current = room_road_north
            elif room_id == "roomRoadEast":
                room_current = room_road_east
            elif room_id == "roomRoadWest":
                room_current = room_road_west
            elif room_id == "roomRoadCorner":
                room_current = room_road_corner
            elif room_id == "roomLake":
                room_current = room_lake
            elif room_id == "roomForest":
                room_current = room_forest
            elif room_id == "roomShrineSouth":
                room_current = room_shrine_south
                if not word_darkness:
                    word_darkness = 1
            # Bridge
            elif room_id == "roomBridge":
                room_current = room_bridge
            # Temple
            elif room_id == "roomTempleEntrance":
                room_current = room_temple_entrance
            elif room_id == "roomTempleInside":
                room_current = room_temple_inside
            elif room_id == "roomTempleBasement":
                room_current = room_temple_basement
            # Cave
            elif room_id == "roomMountEntrance":
                room_current = room_mount_entrance
            # 1
            elif room_id == "roomCave_1_m":
                room_current = room_cave_1_m
            # 2
            elif room_id == "roomCave_2_m":
                room_current = room_cave_2_m
            elif room_id == "roomCave_2_mr":
                room_current = room_cave_2_mr
            elif room_id == "roomCave_2_lm":
                room_current = room_cave_2_lm
            elif room_id == "roomCave_2_llm":
                room_current = room_cave_2_llm
            # 3
            elif room_id == "roomCave_3_m_coalmine":
                room_current = room_cave_3_m_coalmine
            elif room_id == "roomCave_3_mr":
                room_current = room_cave_3_mr
            elif room_id == "roomCave_3_mrr_coalmine":
                room_current = room_cave_3_mrr_coalmine
            elif room_id == "roomCave_3_lm_coalmine":
                room_current = room_cave_3_lm_coalmine
            elif room_id == "roomCave_3_llm_crevasse":
                room_current = room_cave_3_llm_crevasse
            elif room_id == "roomCave__3_lllm_treasure_crevasse":
                room_current = room_cave_3_lllm_treasure_crevasse
            # 4
            elif room_id == "roomCave_4_m":
                room_current = room_cave_4_m
            elif room_id == "roomCave_4_mr":
                room_current = room_cave_4_mr
            elif room_id == "roomCave_4_lm":
                room_current = room_cave_4_lm
            elif room_id == "roomCave_4_llm":
                room_current = room_cave_4_llm
            # 5
            elif room_id == "roomCave_5_m":
                room_current = room_cave_5_m
            elif room_id == "roomCave_5_mr_coalmine":
                room_current = room_cave_5_mr_coalmine
            elif room_id == "roomCave_5_lm_coalmine":
                room_current = room_cave_5_lm_coalmine
            elif room_id == "roomCave_5_llm":
                room_current = room_cave_5_llm
            elif room_id == "roomCave_5_lllm":
                room_current = room_cave_5_lllm
            # 6
            elif room_id == "roomCave_6_m":
                room_current = room_cave_6_m
            elif room_id == "roomCave_6_mr":
                room_current = room_cave_6_mr
            elif room_id == "roomCave_6_lm_coalmine":
                room_current = room_cave_6_lm_coalmine
            elif room_id == "roomCave_6_llm_coalmine":
                room_current = room_cave_6_llm_coalmine
            elif room_id == "roomCave_6_lllm":
                room_current = room_cave_6_lllm
            # 7
            elif room_id == "roomCave_7_m":
                room_current = room_cave_7_m
            elif room_id == "roomCave_7_mr":
                room_current = room_cave_7_mr
            elif room_id == "roomCave_7_lm":
                room_current = room_cave_7_lm
            elif room_id == "roomCave_7_llm":
                room_current = room_cave_7_llm
            elif room_id == "roomCave_7_lllm":
                room_current = room_cave_7_lllm
            # 8
            elif room_id == "roomCave_8_mr_crevasse":
                room_current = room_cave_8_mr_crevasse
            elif room_id == "roomCave_8_llm_coalmine":
                room_current = room_cave_8_llm_coalmine
            # 9
            elif room_id == "roomCave_9_mr_crevasse":
                room_current = room_cave_9_mr_crevasse
            # 10
            elif room_id == "roomCave__10_m":
                room_current = room_cave__10_m
            elif room_id == "roomCave__10_mr":
                room_current = room_cave__10_mr
            elif room_id == "roomCave__10_mrr":
                room_current = room_cave__10_mrr
            elif room_id == "roomCave__10_mrrr":
                room_current = room_cave__10_mrrr
            elif room_id == "roomCave__10_lm":
                room_current = room_cave__10_lm
            # 11
            elif room_id == "roomCave__11_mrrr":
                room_current = room_cave__11_mrrr
            elif room_id == "roomCave__11_lm":
                room_current = room_cave__11_lm
            # Darkness
            elif room_id == "roomDarkness":
                room_current = room_darkness
            # Lair
            elif room_id == "roomLairMid":
                room_current = room_lair_mid
            elif room_id == "roomLairEast":
                room_current = room_lair_east
            elif room_id == "roomLairWest":
                room_current = room_lair_west
            elif room_id == "roomLairHole":
                room_current = room_lair_hole
            # Field
            elif room_id == "roomRoad2South":
                room_current = room_road_2_south
            elif room_id == "roomRoad2Mid":
                room_current = room_road_2_mid
            elif room_id == "roomFarm":
                room_current = room_farm
            elif room_id == "roomBarn":
                room_current = room_barn
            elif room_id == "roomBarnUp":
                room_current = room_barn_up
            elif room_id == "roomHouseGate":
                room_current = room_house_gate
            elif room_id == "roomField":
                room_current = room_field
            elif room_id == "roomShrineNorth":
                room_current = room_shrine_north
                if not word_darkness:
                    word_darkness = 1
            # House
            elif room_id == "roomHouseEntrance":
                room_current = room_house_entrance
            elif room_id == "roomHouseFoyer":
                room_current = room_house_foyer
            elif room_id == "roomHouseKitchen":
                room_current = room_house_kitchen
            elif room_id == "roomHousePantry":
                room_current = room_house_pantry
            elif room_id == "roomHouseHallway":
                room_current = room_house_hallway
            elif room_id == "roomHouseOffice":
                room_current = room_house_office
            # Mysterious book
            elif room_id == "roomBookAnimal":
                room_current = room_book_animal
            elif room_id == "roomBookMirror":
                room_current = room_book_mirror
            elif room_id == "roomBook_3_1":
                room_current = room_book_3_1
            elif room_id == "roomBook_3_2":
                room_current = room_book_3_2
            elif room_id == "roomBook_3_3":
                room_current = room_book_3_3
            elif room_id == "roomBook_3_4":
                room_current = room_book_3_4
            elif room_id == "roomBook_3_5":
                room_current = room_book_3_5
            elif room_id == "roomBook_3_6":
                room_current = room_book_3_6
            elif room_id == "roomBook_3_7":
                room_current = room_book_3_7
            elif room_id == "roomBook_3_8":
                room_current = room_book_3_8
            elif room_id == "roomBook_3_End":
                room_current = room_book_3_end
                room_current.item_found = True
                if not word_dominion:
                    word_dominion = 1

            else:
                print("Uh oh, you broke the game.",room_id,"does not exist. Room not changed.")
            if direction:
                print("You go %s." % direction)
                just_entered = True
            # Rubble falling
            if room_id.startswith("roomCave_") and not room_id.startswith("roomCave__") and random.randint(1,100) <= RUBBLE_FALL_CHANCE:
                print("The mountain shakes and some rubble falls and hits you.")
                stat.lower_health()


            change_room = False
        elif direction == "North" and room_current.north_blocked:
            print(room_current.north_blocked_reason)
            not_turn = True
        elif direction == "East" and room_current.east_blocked:
            print(room_current.east_blocked_reason)
            not_turn = True
        elif direction == "South" and room_current.south_blocked:
            print(room_current.south_blocked_reason)
            not_turn = True
        elif direction == "West" and room_current.west_blocked:
            print(room_current.west_blocked_reason)
            not_turn = True
#_______Events__________________________________________________________________
        # Before justEntered description
        if room_id.startswith("roomCave") and not room_id == "roomCave_1_m":
            # Creatures does not naturally roam if have staff in normal cave
            # However, lantern is still needed to prevent creature chase
            if inv.staff and not room_id.startswith("roomCave__"):
                creature_roam = False
            else:
                creature_roam = True
            # Chase begins immediately if no light
            if not ((oil_counter and (inv.lantern or room_current.lantern)) or light_counter):
                creature_roam = False
                creature_chase = True
                if creature_chase and creature_chase_counter > 5:
                    creature_chase_counter = 6
        if room_id == "roomJailCell" and room_current.counter_1 and not not_turn:
            if room_current.counter_1 == 1:
                print("\nYou hear a loud crack of thunder and a mystical portal opens in the nearby corridor. A woman veiled in white robes jumps through, entering the room. She swiftly runs through the corridor, scanning each cell she passes. Suddenly, she stops at your cell, pauses and draws nearer. \"Tell me your name, stranger.\" she exclaims. \"You may be who I'm looking for.\" She looks worried.")
                ask_name = True
                room_current.counter_1 += 1
            elif turn_counter >= 2 and ask_name:
                if player_name:
                    if player_name.lower() == "ozh gluth izh sol":
                        print("\n\"Ha! You think you can kill me with the tongue of the Ozkavosh? You are a fool!\" The woman transforms in a scaly demon, sprouting wings and sharp claws. \"No mortal shall defeat Vesh'kathal the Deceiver. OZH GLUTH IZH SOL!\"\n\nYou are overwhelmed with pain and agony as you fall to your knees.\n")
                        end_game = True
                        player_name = False
                        ask_name = False
                    elif player_name.lower() in ("ozh ensh","ozh vo'ses sa","izh vo'poz","ozh sol fek","ozh thok alatho","ozh groth sol","eyik vo'hollom","ozh vo'irush","ozh gluth nith","omoz gloth nith","izh tal el ozh icha rek'tal","ahm'domosh","ozhkavosh icha domosh sa nith","izh icha vo'fek ozh domosh","ahm'fol","sof izh"):
                        print("\n\"" + player_name + "? You dare speak the tongue of the Ozhkavosh to me? She zaps you with a bolt of electricity. \"I'll let you live your last few moments bleeding in your cell. Farewell.\" She leaves through the portal from whence she came. The portal snaps shut and disappears.")
                        end_game = True
                        player_name = False
                        ask_name = False
                    elif player_name.lower() in ("eden von roquefort","vesh'kathal","vesh'raheen","vesh'arkosh","garrotxa","rodney williams"):
                        print("\n\"" + player_name + "? I do not appreciate being lied to.\" She zaps you with a bolt of electricity. \"I'll let you live your last few moments bleeding in your cell. Farewell.\" She leaves through the portal from whence she came. The portal snaps shut and disappears.")
                        end_game = True
                        player_name = False
                        ask_name = False
                    else:
                        print("\n\"" + player_name + "? Finally, my search is over. This letter is for you. READ it and you will understand the urgency of the situation. I unforunately have no time to explain as I have much yet to do.\" She nods, tosses a key and a letter through your cell window, and quickly leaves through the portal from whence she came. The portal snaps shut and disappears.")
                        room_current.letter += 1
                        room_current.key += 1
                        room_current.items_present()
                        inv.letterRead = "It reads:\n\nTo " + player_name + ",\n\nA certain Eden Von Roquefort has set up residence NORTH of MOUNT MAGNA. While he purports to be a lowly cheese mage, reliable sources claim him to be the demon lord, Vesh'kathal the Deceiver, a shapeshifter infamous of manipulating the minds and bending the wills of others. Legend tells of a saviour, deemed the Monterey Messiah, who will save all of Kashkaval from his wickedness. It has be brought to my attention that you are that saviour that the legends speak of. While I have very important matters to attend to, the best I can do is help instruct you in how to defeat this demon lord:\n\nFIRST, you must acquire the staff from the Garrotxian temple NORTHEAST of this town, for it is the only weapon capable of defeating such a powerful demon.\n\nNEXT, once you have the staff, go NORTH through the MINES of MOUNT MAGNA and find him at his house on the other end.\n\nFINALLY, kill Roquefort and Kashkaval will be saved from his wrath.\n\nI know this is probably a lot to digest at once, but you are our only hope. I fear in your attempt to complete this task, Vesh'kathal will attempt to thwart you. He may attempt to contact and manipulate you, or have his minions work to stop you. Whatever he does, you must persevere.\n\nMay you be blessed,\n\nThe last prophet of Garrotxa"
                        ask_name = False
                if not player_name and ask_name:
                    if room_current.counter_1 == 2:
                        print('\nThe stranger impatiently waits for your response. "I beg of you. Tell me your name. This is of utmost importance."')
                    elif room_current.counter_1 == 3:
                        print("\nThe stranger quickly grows angry as you continue to ignore her.")
                    else:
                        print("\n\"Why am I wasting my time with a mute rotting in a jail cell?\" She zaps you with a bolt of electricity and walks back through the portal, which snaps shut and disappears.")
                        ask_name = False
                        end_game = True
                    room_current.counter_1 += 1
        elif room_id == "roomJailFoyer":
            # if jailGuards == False: 
            # used singleton pattern, deepsource warning
             if jail_guards is False:
                jail_guards = True
                jail_guard_counter = 3
        elif room_id == "roomCourtyardSouth":

            #if jailGuards == True:
            # used singleton pattern, deepsource warning
                if jail_guards is True:
                    print("You get lost in the crowd, confusing and disorienting the jail guards. They lose interest, probably because they don't get paid enough.")
                jail_guards = False
        # Creature stops chase at crevasse if visible or outside
        elif room_id == "roomMountEntrance" or (room_id.endswith("crevasse") and room_id_last.endswith("crevasse") and room_id != room_id_last):
            if room_id == "roomMountEntrance":
                creature_roam = False
                creature_chase = False
                if creature_chase_counter <= 2:
                    print("The creature is blinded by the outside light and stops its chase, returning back to the cavern.")
                creature_roam_counter = random.randint(CREATURE_ROAM_MIN,CREATURE_ROAM_MAX)
                creature_chase_counter = random.randint(CREATURE_CHASE_MIN,CREATURE_CHASE_MAX)
            else:
                if creature_chase_counter <= 2:
                    creature_roam = False
                    creature_chase = False
                    print("The creature stops at the crevasse, unable to cross. Frustrated, it crawls away.")
                    creature_roam_counter = random.randint(CREATURE_ROAM_MIN,CREATURE_ROAM_MAX)
                    creature_chase_counter = random.randint(CREATURE_CHASE_MIN,CREATURE_CHASE_MAX)
        # Creature stops chas at outside of lair
        elif room_id == "roomRoad2South":
            room_lair_chase = False
            if creature_lair_chase_counter <= 2 and room_id_last == "roomLairEast":
                print("The creature is blinded by the outside light and stops its chase, returning back to the cavern.")
        # If player returns to lair after exiting it
        elif room_id == "roomLairEast" and room_id_last == "roomRoad2South":
            print("The creature is just at the opening and notices you immediately. It claws your face off.")
            end_game = True
            # continue
            # see how actually works out, may be better to have as post-justEntered text

        # Lose lantern
        # Start of creature chase
        if room_id == "roomCave_9_mr_crevasse" and room_current.first_time:
            if inv.lantern > 1:
                lantern_count = "lanterns"
            elif inv.lantern == 1:
                lantern_count = "lantern"
            else:
                lantern_count = False
            inv.lantern = 0
            room_cave_8_mr_crevasse.hook = 0
            room_cave_8_mr_crevasse.north_blocked = True
            if lantern_count:
                lantern_loss = "Your " + lantern_count + " fall into the abyss below."
                aswell = " as well"
            else:
                lantern_loss = ""
                aswell = ""
            print("As you cross the crevasse, the entire mountain begins to shake and a loud rumble echoes throughout the cavern walls.",lantern_loss,"You finally make it to the other side just before the grappling hook shakes loose and falls%s." % aswell)
        # Rubble falls
        elif room_id == "roomCave__10_mr" and room_current.first_time:
            print("Rubble collapses from above as the mountain shakes, blocking the path behind you.")
            room_cave_9_mr_crevasse.north_blocked = True
        # Enter darkness
        elif room_id == "roomDarkness":
            creature_roam = False
            creature_chase = False
            stat.hunger = HUNGER_DARKNESS
            stat.health = HEALTH_MAX - 1
            stat.shield = 0
            oil_counter = 0
            light_counter = 0
            creature_roam_counter = random.randint(CREATURE_ROAM_MIN,CREATURE_ROAM_MAX)
            creature_chase_counter = random.randint(CREATURE_CHASE_MIN,CREATURE_CHASE_MAX)
            if inv.pickaxe:
                room_lair_mid.counter_3 = 1
            if inv.staff:
                room_lair_mid.counter_2 = 1
            inv = Inventory(note_1 = vault_answer_1, note_2 = vault_answer_2, note_3 = vault_answer_3, note_4 = vault_answer_4)
            print("The mountain shakes again, and more rubble collapses from above. A large rock hits you, knocking you unconcious.")

        # OLD CODE

        # Crevasse block check
        # if roomCurrent.isCrevasse:
        #     if not roomCurrent.hook and not roomCurrent.northBlocked and not roomCurrent.eastBlocked and not roomCurrent.westBlocked and not roomCurrent.southBlocked:
        #         if roomID == "roomCave_3_llm_crevasse":
        #             roomCurrent.westBlocked = True
        #         elif roomID == "roomCave__3_lllm_treasure_crevasse":
        #             roomCurrent.eastBlocked = True
        #         elif roomID == "roomCave_8_mr_crevasse":
        #             roomCurrent.northBlocked = True
        #         elif roomID == "roomCave_9_mr_crevasse":
        #             roomCurrent.southBlocked = True

        # END OF OLD CODE


        #DEEPSOURCE OUTPUT
        if (
            room_current.is_crevasse
            and not room_current.hook and not room_current.north_blocked and not room_current.east_blocked and not room_current.west_blocked
            and not room_current.south_blocked
        ):
            if room_id == "roomCave_3_llm_crevasse":
                room_current.west_blocked = True
            elif room_id == "roomCave__3_lllm_treasure_crevasse":
                room_current.east_blocked = True
            elif room_id == "roomCave_8_mr_crevasse":
                room_current.north_blocked = True
            elif room_id == "roomCave_9_mr_crevasse":
                room_current.south_blocked = True
        #END DEEPSOURCE OUTPUT

        # Grappling hook spawn check
        if room_id in ("roomCave_3_llm_crevasse","roomCave__3_lllm_treasure_crevasse","roomCave_8_mr_crevasse","roomCave_9_mr_crevasse"):
            if room_id == "roomCave__3_lllm_treasure_crevasse" and room_current.east_blocked and not room_cave_3_llm_crevasse.west_blocked and room_cave_3_llm_crevasse.hook:
                room_current.east_blocked = False
                room_current.hook += 1
                room_cave_3_llm_crevasse.hook -= 1
            elif room_id == "roomCave_3_llm_crevasse" and room_current.west_blocked and not room_cave_3_lllm_treasure_crevasse.east_blocked and room_cave_3_lllm_treasure_crevasse.hook:
                room_current.west_blocked = False
                room_current.hook += 1
                room_cave_3_lllm_treasure_crevasse.hook -= 1
            elif room_id == "roomCave_9_mr_crevasse" and room_current.south_blocked and not room_cave_8_mr_crevasse.north_blocked and room_cave_8_mr_crevasse.hook:
                room_current.south_blocked = False
                room_current.hook += 1
                room_cave_8_mr_crevasse.hook -= 1
            elif room_id == "roomCave_8_mr_crevasse" and room_current.north_blocked and not room_cave_9_mr_crevasse.south_blocked and room_cave_9_mr_crevasse.hook:
                room_current.north_blocked = False
                room_current.hook += 1
                room_cave_9_mr_crevasse.hook -= 1

        if room_id == "roomHouseEntrance" and room_id_last == "roomHouseGate" and not room_current.first_time:
            silenced = True
            print("You feel the strange force take over you again.")
        elif room_id == "roomHouseGate" and room_id_last == "roomHouseEntrance":
            silenced = False
            print("You feel the strange force leave your body.")
#_______________________________________________________________________________
        # justEntered Description
        # Prints room description if just entered.
        if just_entered:
            room_current.description()
            room_current.items_present()
            just_entered = False
#_______________________________________________________________________________

# COUNTERS
# Counts end of turn
        direction = False
        if not not_turn or end_game:
            # After changeRoom description
            turn_counter += 1
            turn_counter_total += 1
            # Darkness loop
            if room_id == "roomDarkness":
                darkness_counter = DARKNESS_DURATION
                while darkness_counter:
                    option = input("\n\n\n\n> ").lower()
                    darkness_counter -= 1
                    if darkness_counter:
                        print("You feel nothing.")
                room_id = "roomLairMid"
                room_current = room_lair_mid
                print("You wake up.")
                room_current.description()
                room_current.items_present()

            # Jail guards
            if jail_guards and not end_game:
                jail_guard_counter -= 1
                if jail_guard_counter == 2:
                    print("\nJail guards notice you walking into the foyer and begin to run towards you from the eastern hallway, armed with bludgeons.")
                elif jail_guard_counter == 1:
                    print("\nThe jail guards draw nearer, closing in the distance.")
                elif jail_guard_counter == 0:
                    print("\nThe jail guards catch up and grab hold of you. They beat you to death for trying to escape.")
                    end_game = True
            # Lair Creature
            if room_lair_chase:
                if creature_lair_chase_counter > 5:
                    print("\nThe creature notices it is trapped and tries to escape.")
                elif creature_lair_chase_counter == 5:
                    print("\nThe creature screeches as it claws away at the rock around it.")
                elif creature_lair_chase_counter == 4:
                    print("\nThe creature's torso erupts free as it breaks the surrounding rubble.")
                elif creature_lair_chase_counter == 3:
                    print("\nThe creature is almost free, with only its foot caught in the rocks.")
                elif creature_lair_chase_counter == 2:
                    print("\nThe creature entirely breaks free from the rocks, which stops to release an ear-piercing scream. It erupts into full sprint towards you.")
                elif creature_lair_chase_counter == 1:
                    print("\nThe creature extends its arms towards you as it runs, continuing it's chaotic screeching in full force. It claws your arm.")
                    stat.lower_health()
                else:
                    print("\nThe creature grabs hold of you, tearing you to pieces.")
                    end_game = True
                creature_lair_chase_counter -= 1
            if creature_roam:
                creature_roam_counter -= 1
                if creature_roam_counter == 0:
                    creature_roam = False
                    creature_chase = True
            if creature_chase:
                creature_chase_counter -= 1
                if creature_chase_counter > CREATURE_CHASE_MIN:
                    print("\nSomething doesn't feel quite right...")
                elif creature_chase_counter >= 9:
                    print("\nA faint noise echoes in the cavern.")
                elif creature_chase_counter >= 5:
                    print("\nDistant breathing can be heard in rhythm of steady footsteps.")
                elif creature_chase_counter == 4:
                    print("\nThe breathing draws nearer as the footsteps quicken in pace.")
                elif creature_chase_counter == 3:
                    print("\nThe breathing turns into growling, which reverberates throughout the cavern walls.")
                elif creature_chase_counter == 2:
                    print("\nA creature appears, which stops to release an ear-piercing scream. It erupts into full sprint towards you.")
                elif creature_chase_counter == 1:
                    print("\nThe creature extends its arms towards you as it runs, continuing it's chaotic screeching in full force. It claws your arm.")
                    stat.lower_health()
                elif creature_chase_counter == 0:
                    print("\nThe creature grabs hold of you, tearing you to pieces.")
                    end_game = True
            # Raffle reimbursement
            if room_id == "roomCarnival" and room_current.counter_1 <= RAFFLE_TIMER:
                if room_current.is_give:
                    room_current.counter_1 += 1
                if room_current.counter_1 > RAFFLE_TIMER:
                    print("\nThe spokesperson and the guards pack and up and leave the grounds.")
                    room_current.is_give = False
            if not room_id.startswith("roomBook") or room_id.startswith("roomDarkness"):
                # Hunger
                stat.lower_hunger()
                stat.lower_shield()
                if stat.hunger <= 0:
                    end_game = True
                elif stat.hunger <= HUNGER_WARNING:
                    print()
                    stat.examine_hunger()
                # Health
                if stat.health in range(1,stat.healthmax):
                    stat.lower_health()
                    print()
                    stat.examine_health()
                if stat.health <= 0:
                    end_game = True
                # Oil
                if oil_counter:
                    inv.lanternDescription = "Perfect for lighting dark areas. It is currently LIT."
                    oil_counter -= 1
                else:
                    inv.lanternDescription = "Perfect for lighting dark areas. It is currently UNLIT."
                # Oil warning
                if inv.lantern > 0 or room_current.lantern > 0:
                    if oil_counter in range(3,5):
                        print("\nYour lantern flickers.")
                    elif oil_counter == 2:
                        print("\nYour lantern is about to run out of oil.")
                    elif oil_counter == 1:
                        print("\nYour lantern has ran out of oil.")

            # Ball of light
            if light_counter:
                light_counter -= 1
                if light_counter > 2:
                    print("\nA ball of light illuminates your surroundings.")
                elif light_counter == 2:
                    print("\nA ball of light dimly illuminates your surroundings.")
                elif light_counter == 1:
                    print("\nA ball of light fades away.")


            # Roquefort messages
            # roomCourtyardNorth
            if room_id == "roomCourtyardNorth" and room_current.first_time:
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"I do not know who you are, but you if you seek to do me harm, you are making a grave mistake.\"")
                #messageCounter = 1
                #Deepsource said unsed variable found for 'messageCounter = 1'
            # roomRoadSouth
            elif room_id == "roomRoadMid" and room_current.first_time:
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"You continue to work against me. You know nothing of who you are dealing with! Why do you persist?\"")
            # roomCave_5_m or roomCave_5_llm
            if room_id in ("roomCave_5_m","roomCave_5_llm") and (room_cave_5_m.first_time and room_cave_5_llm.first_time):
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"You are still determined to defeat me? If I cannot persuade you, then so be it. Be warned that that it will take more than cold steel to defeat a cheese mage such as myself.\"")
            # roomTempleEntrance after get staff
            if room_id == "roomTempleEntrance" and room_temple_basement.character_dead and room_current.first_time:
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"The staff of Garrotxa? No mere mortal would obtain such a weapon to defeat me. You clearly have a plan. No matter. You will be stopped.\"")
            # roomRoad2South
            if room_id == "roomRoad2South" and room_current.first_time:
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"One does not simply obtain the staff of Garrotxa, kill my knight and travel through the mines of Mount Magna on their own accord. You must be an assassin or something of the likes. But sent by who?\"")
            # roomBarn
            if room_id == "roomBarn" and room_current.first_time:
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"Who ARE you? You seem driven to kill me, yet for reasons still unbeknownst to me. This seems personal, yet I do not recall ever wronging you. This must be something more at stake here.\"")
            # roomHouseEntrance
            if room_id == "roomHouseEntrance" and room_current.first_time:
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"Enough. You speak the tongue of demon-kind in order to trespass into my property. Clearly you are a servant of the Ozhkavosh. I will do what I can in my power to stop you. Hold your tongue for you are silenced!\"")
                print("A strange force takes over you.")
                silenced = True
            # roomHouseFoyer
            if room_id == "roomHouseFoyer" and room_current.first_time:
                print("\nYou feel like someone is trying to enter your mind. A voice echoes in your head.")
                print("\"It seems your power is beyond that of my own. I don't know how you got through that door as I had enchanted it with my strongest incantations. If what I fear is true, then I will simply make one request of you: See me at my office. There is one final thing to discuss.")

            # End game dialogue
            if room_id == "roomHouseOffice":
                # Eden asks to give staff at firstTime
                if not room_current.character_dead:
                    # If player gives staff: counter_1 = 1 and isGive = False
                    #if roomCurrent.counter_1 == 1 and roomCurrent.isGive == False:
                    #singleton
                    if room_current.counter_1 == 1 and room_current.is_give is False: 
                 # spawn Vesh ()
                        room_current.counter_2 = 1
                    # If player does not give staff: counter_1 = 0 and isGive = True
                    #elif roomCurrent.counter_1 == 0 and roomCurrent.isGive == True:
                    # Singleton
                    elif room_current.counter_1 == 0 and room_current.is_give is True:
                        # If player does something else, or nothing, given a second chance
                        room_current.counter_3 += 1
                        if room_current.counter_3 == 2:
                            # Roquefort asks again (print)
                            print("Roquefort asks you again. \"I plead of you. Break free from the demon's control and give me the staff.\"")
                        elif room_current.counter_3 > 2:
                            # Roquefort kills you if you reject 2nd opportunity to give
                            print("\"If you will not give me the staff, then I will take it by force.\" Roquefort extends his arms forward and shoots a fireball at you.")
                            end_game = True
                # If player kills Roquefort
                # Vesh is in room, uninjured
                elif room_current.counter_2 == 1: # staff has been used once or Eden is dead
                    # Spawn Vesh (print)
                    # Reveals self
                    # Tries to kill you
                    room_current.counter_4 += 1
                    if room_current.counter_4 == 1:

                        if room_current.counter_1: # attemptted to give staff
                            response = "\"Fool!\" She transforms into a scaly demon, sprouting wings and sharp claws. \"IZH ICHA VO'FEK OZH DOMOSH! IZH VO'POZ!\" You lose all control of your body and immediately grab the staff back. You aim at Roquefort and fire a bolt of lighting, killing him. \"INSOLENT HUMAN. YOU DARE DEFY ME IN GIVING THE STAFF TO THE ENEMY? NO MATTER, FOR I AM VESH'KATHAL, LAST OF THE AHM'FOL, DECEIVER OF MANY, AND NOW, THANKS YOU TO, RULER OF KASHKAVAL. WITH THE FINAL PROPHET OF GARROTXA DEAD, NO ONE WILL BE ABLE TO STOP MY REIGN. NOW, YOU TOO MUST DIE, AND THE STAFF OF GARROTXA SHALL BE DESTROYED.\"\nYou feel the control over your own body returning."
                            if not word_stop:
                                word_stop = 1
                            if not word_servant:
                                word_servant = 1
                            inv.staff += 1
                        else:
                            response = "\"You did it! Finally, Roquefort has fallen. Peace can be restored to all of Kashkaval. After all this, I think I ought to introduce myself.\" She transforms into a scaly demon, sprouting wings and sharp claws. \"OZKAVOSH ICHA DOMOSH SA NITH. I AM VESH'KATHAL, LAST OF THE AHM'FOL, DECEIVER OF MANY, AND NOW, THANKS YOU TO, RULER OF KASHKAVAL. WITH THE FINAL PROPHET OF GARROTXA DEAD, NO ONE WILL BE ABLE TO STOP MY REIGN. NOW, YOU TOO MUST DIE, AND THE STAFF OF GARROTXA SHALL BE DESTROYED.\""
                            if not word_servant:
                                word_servant = 1
                        print("\nYou hear a loud crack of thunder and a mystical portal opens in the office. The woman veiled in white robes enters the room.",response)
                    # Player does not respond and dies
                    else:
                        print("Vesh'kathal lets out a bellowing roar. \"OZH GLUTH IZH SOL!\"\n\nYou are overwhelmed with pain and agony as you fall to your knees.")
                        if not spell_kill:
                            spell_kill = 1
                        end_game = True
                # Player injures vesh after reveal and loses staff
                elif room_current.counter_2 == 2:
                    room_current.counter_4 += 1
                    if room_current.counter_4 == 3:
                        print("Vesh'kathal recovers from her burns, and gets back up on her feet.")
                    elif room_current.counter_4 > 3:
                        print("Vesh'kathal lets out a bellowing roar. \"OZH GLUTH IZH SOL!\"\n\nYou are overwhelmed with pain and agony as you fall to your knees.")
                        if not spell_kill:
                            spell_kill = 1
                        end_game = True
                else:
                    # Vesh resists hit and tries to kill you again (differently?)
                    if inv.potato:
                        # somehow involve potato
                        print("\nShe grabs hold of you and pummels you against the wall. The potato you've been carrying falls out and hits her square in the face. \"GGAAAAAAAHHHH\" she screams in agony, \"A POTATO OF GARROTXA. MY GREATEST WEAKNESS. I THOUGHT I WAS SAFE WHEN I BURNT DOWN EVERY LAST CROP ON THAT CURSED FARM.\" Streams of light begin to errupt from Vesh'kathal's body, paralyzing her. She turns to stone shortly before she explodes, sending shards of rock flying across the room.\n\nYou take a deep breath and walk over to Roquefort's corpse. You take a closer look at his ragged clothing and and notice it's made out of cheesecloth. As soon as you lay hands on it, you feel a surge of energy throughout your body and hear a booming voice from the heavens.\n\n\"I have returned.\"\n")
                        if not word_curse:
                             word_curse = 1
                        win = True
                    else:
                        # Kills you
                        print("Vesh'kathal lets out a bellowing roar. \"OZH GLUTH IZH SOL!\"\n\nYou are overwhelmed with pain and agony as you fall to your knees.")
                        if not spell_kill:
                            spell_kill = 1
                    end_game = True


        # Objective check
        # Main
        if room_id == "roomCourtyardSouth":
            stat.set_objective_main(1)
        if inv.staff:
            stat.set_objective_main(2)
        if room_id == "roomRoad2South":
            stat.set_objective_main(3)
        if room_id == "roomHouseFoyer":
            stat.set_objective_main(4)
        if room_house_office.character_dead:
            stat.set_objective_main(5)
        # Secondary add
        if room_id == "roomCourtyardSouth":
            stat.add_objective_secondary(1)
        if room_id == "roomCourtyardNorth":
            stat.add_objective_secondary(2)
        if room_carnival_wheel_game.character_dead:
            stat.add_objective_secondary(3)
        if room_id == "roomGate":
            stat.add_objective_secondary(4)
        if room_id == "roomBridge":
            stat.add_objective_secondary(5)
        if room_id == "roomAlchemist":
            stat.add_objective_secondary(6)
        if room_id == "roomLake":
            stat.add_objective_secondary(7)
        if room_id == "roomLake" and spell_unlock != 2 and not room_current.is_give:
            stat.add_objective_secondary(8)
        if not room_lake.is_give:
            stat.add_objective_secondary(9)
        if room_id == "roomMountEntrance":
            stat.add_objective_secondary(10)
        if room_id == "roomCave_3_llm_crevasse":
            stat.add_objective_secondary(11)
        if room_id == "roomCave__3_lllm_treasure_crevasse":
            stat.add_objective_secondary(12)
        if room_id == "roomTempleEntrance":
            stat.add_objective_secondary(13)
        if room_id == "roomTempleBasement":
            stat.add_objective_secondary(14)
        if room_id == "roomRoadCorner" and room_current.west_blocked:
            stat.add_objective_secondary(15)
        if room_id == "roomLairMid":
            stat.add_objective_secondary(16)
        if room_id == "roomHouseEntrance":
            stat.add_objective_secondary(17)
        if spell_oblivion == 2:
            stat.add_objective_secondary(18)
        if room_id == "roomBookMirror":
            stat.add_objective_secondary(19)
        if room_id == "roomBook_3_1":
            stat.add_objective_secondary(20)
        if room_id == "roomHouseFoyer":
            stat.add_objective_secondary(21)
        if room_id == "roomHouseOffice":
            stat.add_objective_secondary(22)
        # Secondary remove
        if inv.gold >= RAFFLE_COMPENSATION:
            stat.remove_objective_secondary(1)

        if inv.ticket:
            stat.remove_objective_secondary(2)
        if inv_spokesperson.ticket or (room_carnival_wheel_game.character_dead and not room_carnival.is_give):
            stat.remove_objective_secondary(3)
        if not room_gate.north_blocked:
            stat.remove_objective_secondary(4)
        if not room_bridge.east_blocked:
            stat.remove_objective_secondary(5)
        if room_alchemist.is_buy:
            stat.remove_objective_secondary(6)
        if not room_lake.is_give:
            stat.remove_objective_secondary(7)
        if spell_unlock == 2:
            stat.remove_objective_secondary(8)
        if room_lake.item_found:
            stat.remove_objective_secondary(9)
        if not room_mount_entrance.north_blocked:
            stat.remove_objective_secondary(10)
        if room_id == "roomCave__3_lllm_treasure_crevasse":
            stat.remove_objective_secondary(11)
        if room_cave_3_lllm_treasure_crevasse.item_found:
            stat.remove_objective_secondary(12)
        if not room_temple_entrance.north_blocked:
            stat.remove_objective_secondary(13)
        if room_temple_basement.character_dead:
            stat.remove_objective_secondary(14)
        if (not room_road_corner.west_blocked) and room_temple_basement.character_dead:
            stat.remove_objective_secondary(15)
        if room_id == "roomRoad2South":
            stat.remove_objective_secondary(16)
        if not room_house_entrance.north_blocked:
            stat.remove_objective_secondary(17)
        if not room_id == "roomShrineNorth":
            stat.remove_objective_secondary(18)
        if room_book_mirror.character_dead:
            stat.remove_objective_secondary(19)
        if (not room_id.startswith("roomBook_3")) and room_book_3_end.item_found:
            stat.remove_objective_secondary(20)
        if not room_house_foyer.north_blocked:
            stat.remove_objective_secondary(21)
        if room_house_office.character_dead:
            stat.remove_objective_secondary(22)

        room_current.first_time = False

    # End Game Message
    if win:
        print("Congratulations! You win!\nYou took %s turns.\n\nTotal deaths: %s\nTotal turns: %s\n" % (turn_counter,deaths_total,turn_counter_total))
    else:
        deaths_total += 1
        if stat.health <= 0:
            cause = " from bleeding out"
        elif stat.hunger <= 0:
            cause = " from starvation"
        else:
            cause = ""
        if turn_counter == 1:
            turn = "turn"
        else:
            turn = "turns"
        print("\nOh no! You died%s.\nYou took %s %s this life.\n\nTotal deaths: %s\nTotal turns: %s\n" % (cause,turn_counter,turn, deaths_total,turn_counter_total))

    # Restart the program
    repeat()
# Start game
if __name__ == "__main__":
    menu()
 