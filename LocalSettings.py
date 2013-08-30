'''This module is used to store information specific to a user and PC.
Other Python scripts will import this file to gather information about
the user's environment'''

#
# Email-related settings.
#

# SMTP (outgoing mail) server.
SMTP_SERVER_ROCKWELL = 'mailrelay.ra.rockwell.com'
SMTP_SERVER_DEFAULT  = SMTP_SERVER_ROCKWELL

# Email addresses
EMAIL_ADDR_WORK     = 'kwpeters@ra.rockwell.com'
EMAIL_ADDR_GMAIL    = 'kwpeters@gmail.com'
EMAIL_ADDR_YAHOO    = 'petersk@yahoo.com'
EMAIL_ADDR_ALL      = [EMAIL_ADDR_WORK,
                       EMAIL_ADDR_GMAIL,
                       EMAIL_ADDR_YAHOO]
EMAIL_ADDR_DEFAULT  = EMAIL_ADDR_GMAIL

