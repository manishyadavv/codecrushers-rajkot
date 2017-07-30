# -*- coding: utf-8 -*-
import base64
import os
from email.mime.text import MIMEText

import httplib2
from apiclient import discovery
from googleapiclient import errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class Email:

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'gmail-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def __init__(self):
        """Shows basic usage of the Gmail API.

        Creates a Gmail API service object and outputs a list of label names
        of the user's Gmail account.
        """
        self.credentials = self.get_credentials()
        http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('gmail', 'v1', http=http)

    def create_message(sender, user, flat):
        """Create a message for an email.

        Args:
            sender: Email address of the sender.
            to: Email address of the receiver.
            subject: The subject of the email message.
            message_text: The text of the email message.

        Returns:
            An object containing a base64url encoded email object.
        """
        message_text = 'Dear %s,\nYou have been alloted a house under %s scheme. ' \
                       'Please contact us for further details' % (
                           user.name, flat.scheme.name)
        message = MIMEText(message_text)
        message['to'] = user.email
        message['from'] = 'v.parth98@gmail.com'
        message['subject'] = 'House Alloted'
        return {'raw': base64.urlsafe_b64encode(message.as_string())}

    def send_message(self, user_id, message):
        """Send an email message.

        Args:
                service: Authorized Gmail API service instance.
                user_id: User's email address. The special value "me"
                can be used to indicate the authenticated user.
                message: Message to be sent.

            Returns:
                Sent Message.
            """

        try:
            message = (self.service.users().messages().send(userId='me', body=message)
                       .execute())
            print('Message Id: %s' % message['id'])
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)


email = Email()
