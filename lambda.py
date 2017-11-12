from __future__ import print_function
import gameMovement
import gameRoom

##ALL GLOBALS MUST BE PASSED AS SESSION ATTRIBUTES

movement = gameMovement.Game()
room = gameRoom.RoomInteraction()

# --------------- Helpers that build all of the responses ----------------------

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
def intro():
    welcome = "You wake up much more excited than normal on this Saturday morning. Rolling out of bed, you realize that your new Armazon echo has arrived. Running to your front door you find it in its sleek black package. Before ordering you had heard rumors of the echo recording conversations to use in advertising but you brushed them off as conspiracy theories. You spend the entire morning setting up your echo right in the middle of your house and getting it running so that you can have the entire world of consumerism at your fingertips. After setting it up you decide to take a nap and sleeo for a while. You are currently in the bedroom. "
    return build_response({},build_speechlet_response("Intro",welcome,"Please choose a direction.", False))

def handle_session_end_request():
    return build_response({},build_speechlet_response("Exit","Thank you for playing. Big sister is watching.","",True))

def move(intent, session):
    if "Direction" in intent['slots']:
        direction = intent['slots']['Direction']['value']
    else:
        direction = "test"
    move_str = movement.changePosition(direction) + room.getInfo(movement.getPositionName())
    return build_response({},build_speechlet_response("Move",move_str,"",False))

def info(intent, session):
    r = room.getInfo(movement.getPositionName()) + movement.getMovementOptionsText()
    #r = movement.getMovementOptionsText()
    return build_response({},build_speechlet_response("Info",r,"Anything else?",False))

def help():
    help = "Use your voice to move around and interact with things."
    return build_response({},build_speechlet_response("Help",help,"",False))

def interact(intent, session):
  obj = intent['slots']['Object']['value']
  pos = movement.getPositionName()
  text = room.interact(pos, obj)

  return build_response({},build_speechlet_response("Interact",text,"",False))
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
  return intro()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    roomInteraction = gameRoom.RoomInteraction()
    # Dispatch to your skill's intent handlers
    if intent_name == "Go":
        return move(intent, session)
    elif intent_name == "Info":
        return info(intent, session)
    elif intent_name == "Help":
        return help()
    elif intent_name == "Interact":
        return interact(intent,session)
    elif intent_name == "" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def end():
    #Ending dialogue
    return("Laying down for the night you think back on the events of the past day. As you recall each of the people you talked to you realize that the ads you had seen were specifically targeted to the topics of the conversations you had. How would they be able to know what you were talking about? Then it dawns on you. The armazon echo, sitting proudly on the table in the center of your house had been transmitting all of your information even when it was supposedly not listening. You jump up and go to call the news station and let them know that you have a way to prove the conspiracy theories. After hanging up the phone you hear your doorbell ring. As you open it up you see an armazon drone speeding away. Looking down you realize there is a package at your feet with the label big sister is watching, then BOOM, the package explodes. The secret remains safe with armazon. The end.")

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
