import smtplib
import imghdr
from email.message import EmailMessage


class SendMail:
    def __init__(self, from_mail, from_password, to_mail, subject, description, image_path):
        self.sender_email = from_mail
        self.sender_password = from_password
        self.reciever_email = to_mail
        self.message = EmailMessage()
        self.message['Subject'] = subject.strip()
        self.message['From'] = from_mail.strip()
        self.message['To'] = to_mail.strip()
        self.message.set_content(description.strip())
        self.image_path = image_path.strip()

    def send_certification(self):
        with open(self.image_path, 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name

        self.message.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender_email, self.sender_password)
            # print(self.message)
            smtp.send_message(self.message)
