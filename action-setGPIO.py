#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
# import sys
# sys.path.append('/usr/local/lib/python2.7/dist-packages')
# from gpiozero import LED
import RPi.GPIO as GPIO
import io

CONFIGURATION_ENCODING_FORMAT = "utf-8"
# CONFIG_INI = "config.ini"

# led = LED(17)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
# you have to add _snips and _snips-skills to the group gpio
# sudo adduser _snips gpio
# sudo adduser _snips-skills gpio
# otherwise it does not work for me

# class SnipsConfigParser(ConfigParser.SafeConfigParser):
#   def to_dict(self):
#       return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}

# def read_configuration_file(configuration_file):
#     try:
#         with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
#             conf_parser = SnipsConfigParser()
#             conf_parser.readfp(f)
#             return conf_parser.to_dict()
#     except (IOError, ConfigParser.Error) as e:
#         return dict()

def subscribe_intent_callback(hermes, intentMessage):
    # conf = read_configuration_file(CONFIG_INI)
    # action_wrapper(hermes, intentMessage, conf)
    intentname = intentMessage.intent.intent_name
    if intentname == "dante7597:MoveDeskUp":
        result_sentence = "Ich bewege den Tisch nach oben"
        # led.on()
        GPIO.output(17,False)
        hermes.publish_end_session(intentMessage.session_id, result_sentence)

    elif intentname == "dante7597:MoveDeskDown":
        result_sentence = "Ich bewege den Tisch nach unten"
        # led.off()
        GPIO.output(17,True)
        hermes.publish_end_session(intentMessage.session_id, result_sentence)


#def action_wrapper(hermes, intentMessage, conf):
#    """ Write the body of the function that will be executed once the intent is recognized. 
#    In your scope, you have the following objects : 
#    - intentMessage : an object that represents the recognized intent
#    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
#    - conf : a dictionary that holds the skills parameters you defined 
#    Refer to the documentation for further details. 
#    """ 
#    led.on()
#    result_sentence = "Die LED ist eingeschaltet"
#    current_session_id = intentMessage.session_id
#    hermes.publish_end_session(current_session_id, result_sentence)



if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intents(subscribe_intent_callback).start()
        #h.subscribe_intent("bertron:GPIOhigh", subscribe_intent_callback).start()
