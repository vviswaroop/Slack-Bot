import os
import time
import re
from slackclient import slack client

#instantiate slack client
slack client = =slackclient(os.version.get('xoxb-457910190834-460826906759-JSQJlD6UngIrAwJncbGKw21J'))

#starteerbot's user ID in slack :value is assigned after the bot startes up
starterbot_id = None

#constants
RTM_READ_DELAY = 1 #1 second delay from reading RTM
EXAMPLE COMMAND = 'do'
MENTION_REGEX = "^<0(|[WU].+?)>(.*)"
