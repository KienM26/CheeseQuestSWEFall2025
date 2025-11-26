# ## def need to move the entire inventory class here
# class Inventory(object):
#         def __init__(self, name = "room", gold = 0, letter = 0, key = 0, keySkeleton = 0, pickaxe = 0, shrubbery = 0, funnelCake = 0, halfFunnelCake = 0, foot = 0, porridge = 0, bowl = 0, lantern = 0, oil = 0, pie = 0, coal = 0, biscuit = 0, hook = 0, staff = 0, ticket = 0, potato = 0, bandage = 0, journal = 0, book = 0, brie = 0, munster = 0, stilton = 0, swiss = 0, wensleydale = 0, potion = 0, flask = 0, stone = 0, bird = 0, note = 0, memo = 0, note_1 = 0, note_2 = 0, note_3 = 0, note_4 = 0):
#             self.name = name
#             self.gold = gold
#             self.goldDescription = "The edges are worn down from handling."
#             self.letter = letter
#             self.letterDescription = "Made out of old parchment, the message on it is written in ink."
#             self.letterRead = "It reads:\n\nTo " + str(playerName) + ",\n\nA certain Eden Von Roquefort has set up residence NORTH of MOUNT MAGNA. While he purports to be a lowly cheese mage, reliable sources claim him to be the demon lord, Vesh'kathal the Deceiver, a shapeshifter infamous of manipulating the minds and bending the wills of others. Legend tells of a saviour, deemed the Monterey Messiah, who will save all of Kashkaval from his wickedness. It has be brought to my attention that you are that saviour that the legends speak of. While I have very important matters to attend to, the best I can do is help instruct you in how to defeat this demon lord:\n\nFIRST, you must acquire the staff from the Garrotxian temple NORTHEAST of this town, for it is the only weapon capable of defeating such a powerful demon.\n\nNEXT, once you have the staff, go NORTH through the MINES of MOUNT MAGNA and find him at his house on the other end.\n\nFINALLY, kill Roquefort and Kashkaval will be saved from his wrath.\n\nI know this is probably a lot to digest at once, but you are our only hope. I fear in your attempt to complete this task, Vesh'kathal will attempt to thwart you. He may attempt to contact and manipulate you, or have his minions work to stop you. Whatever he does, you must persevere.\n\nMay you be blessed,\n\nThe last prophet of Garrotxa"
#             self.key = key
#             self.keyDescription = "The key to your jail cell."
#             self.keySkeleton = keySkeleton
#             self.keySkeletonDescription = "The head is a skull with glowing purple eyes."
#             self.pickaxe = pickaxe
#             self.pickaxeDescription = "A sturdy tool useful for mining."
#             self.shrubbery = shrubbery
#             self.shrubberyDescription = "It's a very nice shrubbery, and not too expensive."
#             self.funnelCake = funnelCake
#             self.funnelCakeDescription = "It's covered in powdered sugar. Mmmmm... and still warm."
#             self.halfFunnelCake = halfFunnelCake
#             self.halfFunnelCakeDescription = "Ew. You can see the bite marks."
#             self.foot = foot
#             self.footDescription = "A prominent symbol of RNGesus, the ancient god of gambling, luck, and salt."
#             self.porridge = porridge
#             self.porridgeDescription = "Bland prison food. Makes you consider if eating this everyday was the real punishment."
#             self.bowl = bowl
#             self.bowlDescription = "Small and dented. Made of out of tin."
#             self.lantern = lantern
#             self.lanternDescription = "Perfect for lighting dark areas."
#             self.oil = oil
#             self.oilDescription = "Perfect for things that are perfect for lighting dark areas."
#             self.pie = pie
#             self.pieDescription = "Hardy and delicious. Just looking at it makes you hungry."
#             self.biscuit = biscuit
#             self.biscuitDescription = "Harder than a brick and probably just as tasty."
#             self.hook = hook
#             self.hookDescription = "Just having one makes you feel like a secret agent."
#             self.staff = staff
#             self.staffDescription = "Elaboratedly designed and encrusted with sapphires, this staff holds unspeakable power."
#             self.ticket = ticket
#             self.ticketDescription = "The number 77 is written on it."
#             self.coal = coal
#             self.coalDescription = "A valuable fuel source for a variety of uses."
#             self.potato = potato
#             self.potatoDescription = "It looks rotten and covered in ash. You probably shouldn't eat it."
#             self.bandage = bandage
#             self.bandageDescription = "Good for healing wounds."
#             self.journal = journal
#             self.journalDescription = "The cover is leather-bound. The whatever text there was along the spine is worn off."
#             self.book = book
#             self.bookDescription = "The cover is entirely black, made out of a material unbeknownst to you. It is heavier than it looks."
#             self.brie = brie
#             self.brieDescription = "Soft and creamy."
#             self.munster = munster
#             self.munsterDescription = "Milky white."
#             self.stilton = stilton
#             self.stiltonDescription = "Hard, with blue veins."
#             self.swiss = swiss
#             self.swissDescription = "It has more holes than the plot to the story of this game."
#             self.wensleydale = wensleydale
#             self.wensleydaleDescription = "Crumbly and a bit dry."
#             self.potion = potion
#             self.potionDescription = "The fluid is red, bubbling, and and foggy. Looks completely safe to drink."
#             self.flask = flask
#             self.flaskDescription = "It's empty."
#             self.stone = stone
#             self.stoneDescription = "It glows a pulsing red as if it were alive. It also seems to produces its own heat."
#             self.bird = bird
#             self.birdDescription = "It's crudely carved to look like a raven."
#             self.note = note
#             self.noteDescription = "Some numbers are written on the small slip of paper."
#             self.note_1 = note_1
#             self.note_2 = note_2
#             self.note_3 = note_3
#             self.note_4 = note_4
#             self.noteRead = "It reads: \"If you must enter, bring a LIGHT SOURCE to keep the creature away. It won't work forever, but it will give you some time. The vault code is %s%s%s%s.\"" % (note_1,note_2,note_3,note_4)
#             self.memo = memo
#             self.memoDescription = "The edges are burnt and the parchment is covered in ash."
#             self.memoRead = "It reads:\n\n\"To whoever is still alive,\n\nBy the time you read this, I will probably be dead. After I learned I could say \"EYIK VO'HOLLOM\" to enter the obisdian hemispheres, I came here from Airedale through one of them in order to help look for survivors up North. The demons went from farm to farm, burning all the crops down, and got me before I could escape. If you are to save this world from demon-kind, you must vanquish them with the staff of Garrotxa back in my home town. It is our only hope.\""
#             # "It reads:\n\nTo whoever is still alive,\n\nBy the time you read this, I will probably be dead. It turns out POTATOES, of all things, are the Ozkavosh's greatest WEAKNESS. After I learned I could say \"EYIK VO'HOLLOM\" to enter the obisdian hemispheres, I came here from Airedale through one in order to get as many potatoes as I could find. The demons went from farm to farm, burning all the crops down, and got me before I could escape. If you are to save this world from demon-kind, you must vanquish them with a potato. Either that, or get hold of the staff of Garrotxa back in my town."
#         def itemTypes(self):
#             type_count = 0
#             if self.gold:
#                 type_count += 1
#             if self.letter:
#                 type_count += 1
#             if self.key:
#                 type_count += 1
#             if self.keySkeleton:
#                 type_count += 1
#             if self.pickaxe:
#                 type_count += 1
#             if self.shrubbery:
#                 type_count += 1
#             if self.funnelCake:
#                 type_count += 1
#             if self.halfFunnelCake:
#                 type_count += 1
#             if self.foot:
#                 type_count += 1
#             if self.porridge:
#                 type_count += 1
#             if self.bowl:
#                 type_count += 1
#             if self.lantern:
#                 type_count += 1
#             if self.oil:
#                 type_count += 1
#             if self.pie:
#                 type_count += 1
#             if self.biscuit:
#                 type_count += 1
#             if self.hook:
#                 type_count += 1
#             if self.staff:
#                 type_count += 1
#             if self.ticket:
#                 type_count += 1
#             if self.coal:
#                 type_count += 1
#             if self.potato:
#                 type_count += 1
#             if self.bandage:
#                 type_count += 1
#             if self.journal:
#                 type_count += 1
#             if self.book:
#                 type_count += 1
#             if self.brie:
#                 type_count += 1
#             if self.munster:
#                 type_count += 1
#             if self.stilton:
#                 type_count += 1
#             if self.swiss:
#                 type_count += 1
#             if self.wensleydale:
#                 type_count += 1
#             if self.potion:
#                 type_count += 1
#             if self.flask:
#                 type_count += 1
#             if self.stone:
#                 type_count += 1
#             if self.bird:
#                 type_count += 1
#             if self.note:
#                 type_count += 1
#             if self.memo:
#                 type_count += 1
#             return type_count
#         def examineInventory(self, option, roomCurrent):
#             # Quantity and Description
#             # Inventory
#             if option == "inventory":
#                 if not self.itemTypes():
#                     print("You have nothing.")
#                 else:
#                     print("You have:")
#                     if self.bandage == 1:
#                         print("    a bandage")
#                     elif self.bandage > 1:
#                         print("   ",self.bandage,"bandages")
#                     if self.porridge:
#                         print("    a bowl of porridge")
#                     if self.bowl:
#                         print("    a bowl")
#                     if self.pie == 1:
#                         print("    a chicken pot pie")
#                     elif self.pie > 1:
#                         print("   ",self.pie,"chicken pot pies")
#                     if self.stone:
#                         print("    a dragonstone")
#                     if self.flask == 1:
#                         print("    a flask")
#                     elif self.flask > 1:
#                         print("   ",self.flask,"flasks")
#                     if self.funnelCake == 1:
#                         print("    a funnel cake")
#                     elif self.funnelCake > 1:
#                         print("   ",self.funnelCake,"funnel cakes")
#                     if self.gold:
#                         print("   ",self.gold,"gold")
#                     if self.hook == 1:
#                         print("    a grappling hook")
#                     elif self.hook > 1:
#                         print("   ",self.hook,"grappling hooks")
#                     if self.halfFunnelCake == 1:
#                         print("    a half-eaten funnel cake")
#                     elif self.halfFunnelCake > 1:
#                         print("   ",self.halfFunnelCake,"half-eaten funnel cakes")
#                     if self.biscuit == 1:
#                         print("    a hardtack biscuit")
#                     elif self.biscuit > 1:
#                         print("   ",self.biscuit,"hardtack biscuits")
#                     if self.journal == 1:
#                         print("    a journal")
#                     elif self.journal > 1:
#                         print("   ",self.journal,"journals")
#                     if self.key:
#                         print("    a key")
#                     if self.keySkeleton:
#                         print("    the key of Ahm'domosh")
#                     if self.lantern == 1:
#                         print("    a lantern")
#                     elif self.lantern > 1:
#                         print("   ",self.lantern,"lanterns")
#                     if self.letter:
#                         print("    a letter")
#                     if self.foot == 1:
#                         print("    a lucky rabbit foot")
#                     elif self.foot > 1:
#                         print("   ",self.foot,"lucky rabbit feet")
#                     if self.memo:
#                         print("    a memo")
#                     if self.book == 1:
#                         print("    a mysterious book")
#                     elif self.book > 1:
#                         print("   ",self.book,"mysterious books")
#                     if self.note:
#                         print("    a note")
#                     if self.pickaxe == 1:
#                         print("    a pickaxe")
#                     elif self.pickaxe > 1:
#                         print("   ",self.pickaxe,"pickaxes")
#                     if self.coal == 1:
#                         print("    a piece of coal")
#                     elif self.coal > 1:
#                         print("   ",self.coal,"pieces of coal")
#                     if self.potato:
#                         print("    a rotten potato")
#                     if self.potion == 1:
#                         print("    a potion of rejuvination")
#                     elif self.potion > 1:
#                         print("   ",self.potion,"potions of rejuvination")
#                     if self.ticket:
#                         print("    a raffle ticket")
#                     if self.shrubbery == 1:
#                         print("    a shrubbery")
#                     elif self.shrubbery > 1:
#                         print("   ",self.shrubbery,"shrubberies")
#                     if self.brie:
#                         print("    a slice of brie cheese")
#                     if self.munster:
#                         print("    a slice of munster cheese")
#                     if self.stilton:
#                         print("    a slice of stilton cheese")
#                     if self.swiss:
#                         print("    a slice of swiss cheese")
#                     if self.wensleydale:
#                         print("    a slice of wensleydale cheese")
#                     if self.staff:
#                         print("    the staff of Garrotxa")
#                     if self.oil == 1:
#                         print("    a vial of lantern oil")
#                     elif self.oil > 1:
#                         print("   ",self.oil,"vials of lantern oil")
#                     if self.bird:
#                         print("    a wooden bird")
#             # Individual items
#             elif option == "gold" and (self.gold or roomCurrent.gold):
#                 print(self.goldDescription)
#             elif option == "letter" and (self.letter or roomCurrent.letter):
#                     print(self.letterDescription)
#             elif option == "key" and (self.key or roomCurrent.key):
#                 print(self.keyDescription)
#             elif option == "key of Ahm'domosh" and (self.keySkeleton or roomCurrent.keySkeleton):
#                 print(self.keySkeletonDescription)
#             elif option == "pickaxe" and (self.pickaxe or roomCurrent.pickaxe):
#                 print(self.pickaxeDescription)
#             elif option == "shrubbery" and (self.shrubbery or roomCurrent.shrubbery):
#                 print(self.shrubberyDescription)
#             elif option == "funnelCake" and (self.funnelCake or roomCurrent.funnelCake):
#                 print(self.funnelCakeDescription)
#             elif option == "half-eaten funnel cake" and (self.halfFunnelCake or roomCurrent.halfFunnelCake):
#                 print(self.halfFunnelCakeDescription)
#             elif option == "lucky rabbit foot" and (self.foot or roomCurrent.foot):
#                 print(self.footDescription)
#             elif option == "bowl of porridge" and (self.porridge or roomCurrent.porridge):
#                 print(self.porridgeDescription)
#             elif option == "bowl" and (self.bowl or roomCurrent.bowl):
#                 print(self.bowlDescription)
#             elif option == "lantern" and (self.lantern or roomCurrent.lantern):
#                 print(self.lanternDescription)
#             elif option == "vial of oil lantern" and (self.oil or roomCurrent.oil):
#                 print(self.oilDescription)
#             elif option == "chicken pot pie" and (self.pie or roomCurrent.pie):
#                 print(self.pieDescription)
#             elif option == "hardtack biscuit" and (self.biscuit or roomCurrent.biscuit):
#                 print(self.biscuitDescription)
#             elif option == "grappling hook" and (self.hook or roomCurrent.hook):
#                 print(self.hookDescription)
#             elif option == "staff of Garrotxa" and (self.staff or roomCurrent.staff):
#                 print(self.staffDescription)
#             elif option == "raffle ticket" and (self.ticket or roomCurrent.ticket):
#                 print(self.ticketDescription)
#             elif option == "piece of coal" and (self.coal or roomCurrent.coal):
#                 print(self.coalDescription)
#             elif option == "potato" and (self.potato or roomCurrent.potato):
#                 print(self.potatoDescription)
#             elif option == "bandage" and (self.bandage or roomCurrent.bandage):
#                 print(self.bandageDescription)
#             elif option == "journal" and (self.journal or roomCurrent.journal):
#                 print(self.journalDescription)
#             elif option == "book" and (self.book or roomCurrent.book):
#                 print(self.bookDescription)
#             elif option == "brie" and (self.brie or roomCurrent.brie):
#                 print(self.brieDescription)
#             elif option == "slice of munster cheese" and (self.munster or roomCurrent.munster):
#                 print(self.munsterDescription)
#             elif option == "slice of stilton cheese" and (self.stilton or roomCurrent.stilton):
#                 print(self.stiltonDescription)
#             elif option == "slice of swiss cheese" and (self.swiss or roomCurrent.swiss):
#                 print(self.swissDescription)
#             elif option == "slice of wensleydale cheese" and (self.wensleydale or roomCurrent.wensleydale):
#                 print(self.wensleydaleDescription)
#             elif option == "potion or rejuvination" and (self.potion or roomCurrent.potion):
#                 print(self.potionDescription)
#             elif option == "flask" and (self.flask or roomCurrent.flask):
#                 print(self.flaskDescription)
#             elif option == "dragonstone" and (self.stone or roomCurrent.stone):
#                 print(self.stoneDescription)
#             elif option == "wooden bird" and (self.bird or roomCurrent.bird):
#                 print(self.birdDescription)
#             elif option == "note" and (self.note or roomCurrent.note):
#                 print(self.noteDescription)
#             elif option == "memo" and (self.memo or roomCurrent.memo):
#                 print(self.memoDescription)
#             else:
#                 if option == "gold":
#                     print("There is no gold here to examine.")
#                 else:
#                     print("There is no",option,"here to examine.")
