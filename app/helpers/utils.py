import datetime
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart

import pandas as pd


def read_csv(csv):
    """
    Read the CSV file and return an Dataframe
    """
    df = pd.read_csv(csv)
    return df


def parse_date(date):
    """
    Get the date in a format "Month/Day" like "7/18"
    transform it into a datetime of the current year
    and return the datetime without formatting.
    """
    dateSplited = date.split('/')
    realDate = datetime.datetime(
        datetime.datetime.now().year,
        int(dateSplited[0]),
        int(dateSplited[1])
    )
    return realDate


class MailBox:
    def __init__(self, config: object) -> None:
        self.config = config
        self.msg = EmailMessage()
        self.msg["Subject"] = "Transaction Balance Stori"
        self.msg["From"] = self.config.MAIL_USERNAME
        self.msg["Body"] = self.msg.set_content("Email Stori")

    def send(self, body) -> None:
        try:
            message = MIMEMultipart('alternative')
            message['Subject'] = 'Transaction Balance Stori'
            message['To'] = self.config.MAIL_USERNAME
            message['From'] = self.config.MAIL_USERNAME
            message['Body'] = self.msg.set_content(body, subtype="html")

            server = smtplib.SMTP(
                self.config.MAIL_SERVER,
                self.config.MAIL_PORT
            )
            server.starttls()
            server.login(self.config.MAIL_USERNAME, self.config.MAIL_PASSWORD)
            message.attach(self.msg)
            server.sendmail(
                self.config.MAIL_USERNAME,
                self.config.MAIL_USERNAME,
                message.as_string()
            )

        except Exception as e:
            raise e
