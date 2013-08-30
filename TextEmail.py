import smtplib
from email.MIMEText import MIMEText
import LocalSettings

LocalSettings.EMAIL_ADDR_DEFAULT

def SendEmail(
    body_text,
    subject,
    src_email     = LocalSettings.EMAIL_ADDR_DEFAULT,
    dest_emails   = [LocalSettings.EMAIL_ADDR_DEFAULT],
    smtp_server   = LocalSettings.SMTP_SERVER_DEFAULT):
    '''Sends a plain text email.
    body_text   is a string containing the message's text
    subject     is a string containing the subject line
    src_email   is a string containing the originator's email address
    dest_emails is either a single destination email address in
                string form or a list of multiple email addresses
    smtp_server is a string containing the name of the email server
    '''
    # If the caller specified the desitination email address as a string, then
    # convert it to a list of destination email addresses.
    if isinstance(dest_emails, str):
        dest_emails = [dest_emails]

    # Fill out the message information.
    msg = MIMEText(body_text)
    msg['Subject'] = subject
    msg['From']    = src_email
    msg['To']      = ', '.join(dest_emails)

    # Create a connection to the SMTP server and send the email.
    smtp_conn = smtplib.SMTP()
    smtp_conn.connect(smtp_server)
    smtp_conn.sendmail(src_email, dest_emails, msg.as_string())
    smtp_conn.close()
