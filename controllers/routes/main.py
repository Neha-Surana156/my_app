from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    if at.Flex365.onClick:
        at.Flex437.styles.display ='flex'
        at.Flex372.styles.display ='none'
    
    if at.Flex366.onClick:
        at.Flex437.styles.display ='flex'
        at.Flex372.styles.display ='none'

    if at.Flex431.onClick:
        at.Flex372.styles.display ='flex'
        at.Flex437.styles.display ='none'
    
    if at.Flex430.onClick:
        at.Flex372.styles.display ='flex'
        at.Flex437.styles.display ='none'
    
    if at.Flex277.onClick:
        at.Flex278.styles.display ='flex'
    
    if at.Flex338.onClick:
        at.Flex337.styles.display ='flex'
    
    if at.Flex311.onClick:
        at.Flex310.styles.display ='flex'
    
    if at.Flex316.onClick:
        at.Flex315.styles.display ='flex'
    
    if at.Flex321.onClick:
        at.Flex320.styles.display ='flex'
    
    if at.Flex335.onClick:
        at.Flex336.styles.display ='flex'
    
    if at.Flex333.onClick:
        at.Flex334.styles.display ='flex'
    
    if at.Flex331.onClick:
        at.Flex332.styles.display ='flex'

    if at.Button8.onClick:
        at.Flex606.styles.display ='flex'
        at.Flex601.styles.display ='flex'
        at.Flex168.styles.display ='none'
        at.Flex591.styles.display ='none'

    if at.Button7.onClick:
        at.Flex168.styles.display ='flex'
        at.Flex591.styles.display ='flex'
        at.Flex606.styles.display ='none'
        at.Flex601.styles.display ='none'
    

    pass