from flask import *
from flask_ask import *
import random

app = Flask(__name__)
ask = Ask(app,'/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def useComputer():
  events = session.attributes['events']

def interact(o):
  room = session.attributes['room']
  event = session.attributes['events']
  urgent = session.attributes['urgent']
  if urgent == 0:
    if room == 'Bathroom' and o == 'toilet':
      session.attributes['urgent'] = 'Bathroom'
      session.attributes['events']['Bathroom'] = 1
      return("You are sitting on the toilet, waiting for things to happen, when all of a sudden your cellphone rings. You pull out your phone and it's your concerned friend. You pick up the phone and she asks how you are doing. You respond, saying no better than usual. She tells you about Sky High Happy pills, which are the new anti-depresents. You tell her that you are fine and hang up the phone. You finish, stand up, and wash your hands.")
    elif room == 'Kitchen' and o == 'dog':
      session.attributes['urgent'] = 'Kitchen'
      session.attributes['events']['Kitchen'] = 1
      return("You pat your dog on the head. You ask if he is hungry and he wags his tail. After filling up the food bowl, you say. Wow, I really love that JoJo's Fatty Pooch Dog Chow! Too bad we are running low.")
    elif room =='Livingroom' and o == 'door':
      session.attributes['urgent'] = 'Livingroom'
      session.attributes['events']['Livingroom'] = 1
      return("You open the door and a sharply dressed man in a suit stands in front of you. He asks if you are interested in having the x666 in-body credit card scanner implanted. You feel like that is a little weird as you are already broke and politely decline.")
    elif room == 'Office' and o == 'phone':
      session.attributes['urgent'] = 'Office'
      session.attributes['events']['Office'] = 1
      return("As you contemplate the universe behind your desk, you figure that no work will be getting done so you give your friend Kathy a call, hoping she will want to speak with you. She states how she is SUPER DUPER MEGA excited for fallout 5. She says EA was the perfect choice as the development team. You hang up, since fallout is your least favorite game series.")
    elif room == 'Porch' and o == 'sam':
      session.attributes['urgent'] = 'Porch'
      session.attributes['events']['Porch'] = 1
      return("You speak to sam. They don't look happy. They speak up and tell you about how much of a loser you are. This doesn't surprise you, since you are a loser. They tell you that they know you are trying your best to find a job but they are disappointed that you haven't found any success and know that you aren't really trying. They are tired of you taking advantage of their work into the relationship while you contribute nothing, as always. ")
    else:
      if room == 'Bedroom' and o == 'computer':
        return("computer stuff")
        session.attributes['urgent'] = 0
    return("You really should head into your bedroom and check out your computer. You have a sudden urge to see what's going on in this cruel world")

def getAd(a):
  rads = ["Introduce your home to the new Smart House, by armazon. Connect everything to our network! We promise it's safe."]
  rads.append("Defeat in home pests with the Bug Nuke! Our 100% deet gaseous bomb is guaranteed to kill everything AND be environmentally unfriendly!")
  rads.append("Beat all your friends in eSports! Sign up for experimental genetic enhancements today! Don't worry, if it goes wrong we will end it quickly.")
  rads.append("Make money by offering your brain power for cryptocurrency mining! You get a 5% cut each month!")
  rads.append("Give your family lifetime benefits when you sacrifice yourself for research in artificial general intelligence! Help be a part of the creation of a new and superior race! This message has been brought to you by r slash Totally not robots.")
  if a == 'rand':
    return rads[random.randInt(0,4)]
  ads = {}
  ads['Porch'] = "Is your significant other telling you to get a job? Come down to the Evil Corp job selection headquarters to be assigned a function. Your only purpose in life is to produce materials!"
  ads['Office'] = "Get ready for a brand new, two map, action-packed first person shooter. Fallout five. EA, it's in the game."
  ads['Bathroom'] = "Find your happy place with Sky High Happy pills. Don't be down, turn that frown upside down! Get rid of your depression today."
  ads['Livingroom'] = "Introducing the model X six six six in-body credit card chip, you can buy anything at any store! Get your implant at your local co-op health center."
  ads['Kitchen'] = "Is your dog on the verge of being taken by animal services? Fill it up with JoJo's Fatty Pooch Dog Chow. Make your dog morbidly obese, just like the average American!"
  return ads[a]

def getInfo():
  room = session.attributes['room']
  event = session.attributes['events']
  if room == 'Bathroom':
    if event['Bathroom'] == 0:
      return("You are in the bathroom. The toilet stares at you. You stare back. You wonder if you should use it. To the East is the Living Room.")
    else:
      return("You are in the bathroom. You have already used the bathroom today. Try again tommorow. To the East is the Living Room.")
  elif room == 'Livingroom':
    if event['Livingroom'] == 0:
      return("You are in the living room. There is a small T.V. an old armchair and a sofa. You hear a knock at the front door. To your East is the kitchen. To the West is the Bathroom. To the North is the Hallway.")
    else:
      return("You are in the living room. The T.V. crackles in the background. To your East is the kitchen. To the West is the Bathroom. To the North is the Hallway.")
  elif room == 'Kitchen':
    if event['Kitchen'] == 0:
      return("You are in the kitchen. It seems like months since the last time you had the motivation to cook anything in here. Your dog sits in the corner. You should give him a pat on the head. He looks hungry. You wouldn't want him to starve. To the West is the living Room.") 
    else:
      return('You are in the kitchen. Your doggo looks so full and chunky, like the average american. Good thing you fed him already. To the West is the living room.')

  elif room == 'Office':
    if event['Office'] == 0:
      return('You are in the office. So much of your life has been wasted here. You have many fond memories of slaving away behind this desk for a faceless corporation that does not care about you or your wellbeing. You see your phone beside the couch. You wonder if any of your friends will want to speak to you. Probably not, but you should try anyway. To the East is the Hallway"')
    else:
      return("You are in the office. You remember all of the wasted years. Your friends didn't even want to talk with you. To the West is the hallway.")

  elif room == 'Porch':
    if event['Porch'] == 0:
      return("You are in the back porch. Your significant other, Sam, sits across from you smoking. You wonder when they last gave you the time of day. Might as well try to start up a conversation. To the South is the hallway") 
    else:
      return("You are in the back porch. Your significant other, Sam, continues smoking, no longer wanting to have a conversation with someone as worthless as you. To the South is the hallway.")

  elif room == 'Hallway':
    return("You are in the hallway. Your shiny new Armazon Echo sits proudly on the center table. You hear an ad. It says " + getAd('rand') + " To the North is the back porch. To the West is the bedroom. To the East is the office. To the South is the Living room.")

  elif room == 'Bedroom':
    return("You are in the bedroom. There is a computer in the corner and an unmade bed. Sleeping is the only thing left in the world you enjoy. To the East is the hallway.")

@ask.launch #Welcome sentence
def launch():
  session.attributes['urgent'] = 0
  session.attributes['room'] = "Bedroom"
  session.attributes['events'] = {'Bathroom':0,'Livingroom':0,'Kitchen':0,'Office':0,'Porch':0}
  return question("You wake up on a dull Saturday morning, ")

@ask.intent('Go') #Change rooms
def door(d): #door, N,S,E,W
  go(d)
  info = getInfo()
  return question(info)

@ask.intent('Help')
def sayHelp():
  return question('The availible commands are go, info, and interact.')

@ask.intent('Info') #Get info about current room
def Info():
  info = getInfo()
  return question(info)

@ask.intent('Interact') #interect with objects, people, etc...
def interact(o): #object
  i = interact(o)

app.run('localhost',1337)

