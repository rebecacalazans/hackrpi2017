import random

class RoomInteraction:
  def __init__(self):
    self.rooms = ["Bedroom", "Bathroom", "Kitchen", "Livingroom", "Office", "Hallway", "Porch"]
    self.initializeRoomObject()
    self.initializeRoomInteractionMessages()
    self.initializeRoomInfo()
    self.visited = {}
    self.urgent = 0
    for room in self.rooms:
      self.visited[room] = 0

  def initializeRoomObject(self):
    self.roomObject = {}
    self.roomObject['Bathroom'] = 'toilet'
    self.roomObject['Kitchen'] = 'dog'
    self.roomObject['livingroom'] = 'door'
    self.roomObject['Office'] = 'phone'
    self.roomObject['Porch'] = 'Sam'
    self.roomObject['Bedroom'] = 'computer'

  def initializeRoomInteractionMessages(self):
    self.roomInteractionMessage = {}
    self.roomInteractionMessage['Bathroom'] = "You are sitting on the toilet, waiting for things to happen, when all of a sudden your cellphone rings. You pull out your phone and it's your concerned friend. You pick up the phone and she asks how you are doing. You respond, saying no better than usual. She tells you about Sky High Happy pills, which are the new anti-depresents. You tell her that you are fine and hang up the phone. You finish, stand up, and wash your hands."
    self.roomInteractionMessage['Kitchen'] = "You pat your dog on the head. You ask if he is hungry and he wags his tail. After filling up the food bowl, you say. Wow, I really love that JoJo's Fatty Pooch Dog Chow! Too bad we are running low."
    self.roomInteractionMessage['livingroom'] = "You open the door and a sharply dressed man in a suit stands in front of you. He asks if you are interested in having the x666 in-body credit card scanner implanted. You feel like that is a little weird as you are already broke and politely decline."
    self.roomInteractionMessage['Office'] = "As you contemplate the universe behind your desk, you figure that no work will be getting done so you give your friend Kathy a call, hoping she will want to speak with you. She states how she is SUPER DUPER MEGA excited for fallout 5. She says EA was the perfect choice as the development team. You hang up, since fallout is your least favorite game series."
    self.roomInteractionMessage['Porch'] = "You speak to sam. They don't look happy. They speak up and tell you about how much of a loser you are. This doesn't surprise you, since you are a loser. They tell you that they know you are trying your best to find a job but they are disappointed that you haven't found any success and know that you aren't really trying. They are tired of you taking advantage of their work into the relationship while you contribute nothing, as always. "
    self.roomInteractionMessage['Bedroom'] = "You really should head into your bedroom and check out your computer. You have a sudden urge to see what's going on in this cruel world"

  def initializeRoomInfo(self):
    self.roomInfo = {}
    self.roomInfo['Bathroom'] = ("You are in the bathroom. The toilet stares at you. You stare back. You wonder if you should use it. ",
      "You are in the bathroom. You have already used the bathroom today. Try again tommorow. ")
    self.roomInfo['livingroom'] = ("You are in the living room. There is a small T.V. an old armchair and a sofa. You hear a knock at the front door.",
      "You are in the living room. The T.V. crackles in the background. ")
    self.roomInfo['Kitchen'] = ("You are in the kitchen. It seems like months since the last time you had the motivation to cook anything in here. Your dog sits in the corner. You should give him a pat on the head. He looks hungry. You wouldn't want him to starve. ",
      'You are in the kitchen. Your doggo looks so full and chunky. Good thing you fed him already.')
    self.roomInfo['Office'] = ('You are in the office. So much of your life has been wasted here. You have many fond memories of slaving away behind this desk for a faceless corporation that does not care about you or your wellbeing. You see your phone beside the couch. You wonder if any of your friends will want to speak to you. Probably not, but you should try anyway.',
      "You are in the office. You remember all of the wasted years. Your friends didn't even want to talk with you. ")
    self.roomInfo['Porch'] = ("You are in the porch. Your significant other, Sam, sits across from you smoking. You wonder when they last gave you the time of day. Might as well try to start up a conversation.",
      "You are in the back porch. Your significant other, Sam, continues smoking, no longer wanting to have a conversation with someone as worthless as you. ")
    self.roomInfo['Hallway'] = ("You are in the hallway. Your shiny new Armazon Echo sits proudly on the center table. You hear an ad. It says " + self.getAd('rand'))
    self.roomInfo['Bedroom'] = ("You are in the bedroom. There is a computer in the corner and an unmade bed. Sleeping is the only thing left in the world you enjoy.")

  def interact(self, room, obj):
    if(room not in roomObject):
      return "You can't do that"
    if(obj != self.roomObject[room]):
      return "You can't do that"

    if room == "Bedroom":
      self.urgent = 0
      return("computer stuff")
    if self.urgent == 1:
      return("You really should head into your bedroom and check out your computer. You have a sudden urge to see what's going on in this cruel world")
    if self.visited[room] == 1:
      return (self.getInfo(room))
    self.urgent = 1
    self.visited[room] = 1
    return (self.roomInteractionMessage[room])

  def getAd(self, a):
    rads = ["Introduce your home to the new Smart House, by armazon. Connect everything to our network! We promise it's safe."]
    rads.append("Defeat in home pests with the Bug Nuke! Our 100% deet gaseous bomb is guaranteed to kill everything AND be environmentally unfriendly!")
    rads.append("Beat all your friends in eSports! Sign up for experimental genetic enhancements today! Don't worry, if it goes wrong we will end it quickly.")
    rads.append("Make money by offering your brain power for cryptocurrency mining! You get a 5% cut each month!")
    rads.append("Give your family lifetime benefits when you sacrifice yourself for research in artificial general intelligence! Help be a part of the creation of a new and superior race! This message has been brought to you by r slash Totally not robots.")
    if a == 'rand':
      return rads[random.randint(0,4)]
    ads = {}
    ads['Porch'] = "Is your significant other telling you to get a job? Come down to the Evil Corp job selection headquarters to be assigned a function. Your only purpose in life is to produce materials!"
    ads['Office'] = "Get ready for a brand new, two map, action-packed first person shooter. Fallout five. EA, it's in the game."
    ads['Bathroom'] = "Find your happy place with Sky High Happy pills. Don't be down, turn that frown upside down! Get rid of your depression today."
    ads['Livingroom'] = "Introducing the model X six six six in-body credit card chip, you can buy anything at any store! Get your implant at your local co-op health center."
    ads['Kitchen'] = "Is your dog on the verge of being taken by animal services? Fill it up with JoJo's Fatty Pooch Dog Chow. Make your dog morbidly obese, just like the average American!"
    return ads[a]

  def getInfo(self, room):
    return self.roomInfo[room][self.visited[room]]
