'''
    By: Ronald Coe, Jr.
    Date: February 25, 2017
    Description:
'''
import sys
import urllib
import urllib2
import logging


def simple_http_server():
    '''
        The servers GET/POST logic will go here
    '''
    print "A server definition would start here."

def server_hello_response():
    '''
        The server's response to the initial greeting will be processed here
    '''
    print "I do beleive that I've been spoken to!"

def server_room_invite_response():
    '''
        When the BOT is added to a room this suite will handle responding to that event
    '''
    print "I have been added to a room"

if __name__ == '__main__':
    '''
    '''
    simple_http_server()
