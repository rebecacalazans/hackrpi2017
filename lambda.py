from __future__ import print_function
import gameMovement
import gameRoom
import pickle

##ALL GLOBALS MUST BE PASSED AS SESSION ATTRIBUTES
# --------------- Helpers that build all of the responses ----------------------

def getVariables(session_attributes):
  movement = session_attributes['movement']
  room = session_attributes['roomInteraction']
  movement = pickle.loads(movement)
  room = pickle.loads(room)

  return(movement, room)

def setVariables(session_attributes, movement, room):
  movement = pickle.dumps(movement)
  room = pickle.dumps(room)
  session_attributes['movement'] = movement
  session_attributes['roomInteraction'] = room
  return {"movement":movement,"roomInteraction":room}

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def intro(attributes):
    welcome = "You wake up much more excited than normal on this Saturday morning. Rolling out of bed, you realize that your new Armazon echo has arrived. Running to your front door you find it in its sleek black package. Before ordering you had heard rumors of the echo recording conversations to use in advertising but you brushed them off as conspiracy theories. You spend the entire morning setting up your echo right in the middle of your house and getting it running so that you can have the entire world of consumerism at your fingertips. After setting it up you decide to take a nap and sleeo for a while. You are currently in the bedroom. "
    return build_response(attributes,build_speechlet_response("Intro",welcome,"Please choose a direction.", True))

def handle_session_end_request():
    return build_response({},build_speechlet_response("Exit","Thank you for playing. Big sister is watching.","",True))

def computer(o)
    if o == 'toilet':
        return("You check your computer. The news scrolls across your screen. You seem to notice that among the normal random advertisements there are also quite a few with mentions to anti-depressants. You wonder if your browsing history has led to adsense thinking that you are depressed like your friend did. ")
    if o == 'dog':
        return("You check your computer. After browsing reddit for a while, you see an e-mail pop up. It is from JoJo's Fatty Pooch Dog Chow, offering a 50% off coupon on your next order. You think that this is super helpful as you were just talking about how you needed some more. How neat.")
    if o == 'door':
        return("You check your computer. You think to yourself about the man at the door. The idea of a credit card chip seems ridiculous, but an artice on footbook seems to show that those who get the chip are happier and have a better quality of life. Maybe you should look into it after all.")
    if o == 'phone':
        return("You check your computer. The ads seem to be becoming more and more targeted towards the things in your life. Many of the banners at the top of the screen are about Fallout five and other EA titles. You start to become increasingly suspicious towards the machine in the middle of your house that you were so excited about just this morning.")
    if o == 'sam':
        return("You check your computer. After getting berated earlier, you decide to check some job-hunting sites. As you scroll through you feel even more worthless, you don't qualify for most of the jobs and those you do apply for never reply. As you try to take a break and scroll through some social media you seem to be berated by ads about getting a job.")

def move(intent, session):
  movement = session['attributes']['movement']
  room = session['attributes']['room']
  #if "direction" in intent['slot']:
    #direction = intent['slot']['direction']['value']
    #position = movement.getNextPosition(direction)
  move_str = movement.changePosition(direction)
  session_attributes = setAttributes(movement, room)
  build_response(session_attributes,build_speechlet_response("Move",move_str,"",False))

def info(intent, session):
  movement = session['attributes']['movement']
  room = session['attributes']['room']
  build_response({},build_speechlet_response("Info",room.getInfo() + movement.getMovementOptionsText(),"Anything else?",False))

def help():
    help = "Use your voice to move around and interact with things."
    return build_response({},build_speechlet_response("Help",help,"",False))

def interact(intent, session):
  movement, room = session['attributes']
  if "object" in intent['slot']:
    obj = intent['slot']['direction']['value']
  pos = movement.getPositionName()
  text = room.interact(pos, obj)

  session['attributes'] = getAttributes(movement, room)

  build_response({},build_speechlet_response("Interact",text,"",True))
# --------------- Events ------------------

def on_session_started(session_started_request, session):
  """ Called when the session starts """

  print("on_session_started requestId=" + session_started_request['requestId']
        + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
  """ Called when the user launches the skill without specifying what they
  want
  """

  print("on_launch requestId=" + launch_request['requestId'] +
        ", sessionId=" + session['sessionId'])
  # Dispatch to your skill's launch
  movement = gameMovement.Game()
  movement = pickle.dumps(movement)
  room = gameRoom.RoomInteraction()
  room = picke.dumps(room)

  session_attributes = {'movement':movement, 'roomInteraction':room}

  return intro(session_attributes)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    roomInteraction = RoomInteraction()
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "Go":
        return move(intent, session)
    elif intent_name == "Info":
        return info(intent, session)
    elif intent_name == "Help":
        return help()
    elif intent_name == "Interact":
        return interact()
    elif intent_name == "" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
