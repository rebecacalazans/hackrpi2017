from flask import *
from flask_ask import *
import random
import gameMovement
import gameRoom

app = Flask(__name__)
ask = Ask(app,'/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def useComputer():
  events = session.attributes['events']

def interact(obj):
  room = session.attributes['movement'].getPositionName()
  urgent = session.attributes['urgent']

  session.attributes['urgent'], message = session.attributes['roomInteraction'].interact(room, obj, urgent)
  return message

def getInfo():

  room = session.attributes['movement'].getPositionName()
  event = session.attributes['events']
  return session.attributes['roomInteraction'].getInfo(room, obj) + session.attreibutes['movement'].getMovementOptionsText()

@ask.launch #Welcome sentence
def launch():
  session.attributes['movement'] = gameMovement.Game()
  session.attributes['roomInteraction'] = gameRoom.RoomInteraction()
  session.attributes['urgent'] = 0
  return question("You wake up much more excited than normal on this Saturday morning. Rolling out of bed, you realize that your new Armazon echo has arrived. Running to your front door you find it in its sleek black package. Before ordering you had heard rumors of the echo recording conversations to use in advertising but you brushed them off as conspiracy theories. You spend the entire morning setting up your echo right in the middle of your house and getting it running so that you can have the entire world of consumerism at your fingertips. After setting it up you decide to take a nap and sleeo for a while. You are currently in the bedroom. " + move())

@ask.intent('Go') #Change rooms
def door(d): #door, N,S,E,W
  session.attributes['movement'].changePosition(d)
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

