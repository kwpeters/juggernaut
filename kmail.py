#! python -O

import TextEmail
import sys
import LocalSettings
import getopt


def Usage():
    text = '''
This script sends an email message.
Usage:
kmail.py [-a address] [-b] Email message text

Options:

-a address   Sends the email to the email address specified.
             If this option is not specified,
             LocalSettings.EMAIL_ADDR_DEFAULT will be used.

-b           Places the message in the body of the email.
             If this option is not specified, the message will
             be placed in the subject line.
'''
    return text


if __name__ == '__main__':

    # Setup defaults.
    email_addr      = LocalSettings.EMAIL_ADDR_DEFAULT
    message_in_body = False

    # Parse the command line options.
    # The -b option does not have an argument.
    # The -a option does require an argument.
    try:
        (options, args) = getopt.getopt(sys.argv[1:], 'ba:')
    except getopt.GetoptError:
        print Usage()
        sys.exit(1)

    for (option, value) in options:
        if option == '-a':
            email_addr = value
        elif option == '-b':
            message_in_body = True

    # The remaining arguments will make up the message.
    message = ' '.join(args)

    # Set the subject and body text of the email.
    if message_in_body:
        subject = 'A message from kmail'
        body    = message
    else:
        subject = message
        body    = ''

    # Send it!
    TextEmail.SendEmail(body, subject, email_addr, email_addr)
