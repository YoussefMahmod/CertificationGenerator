from io import BytesIO
import os
from sys import maxsize
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from csv import reader
import re
from mailsender import SendMail
images = []

file = open("/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf", "rb")
bytes_font = BytesIO(file.read())
my_font = ImageFont.truetype(bytes_font, 72)

print("Enter X,Y which you need to start writing names from.")
x = int(input("X:"))
y = int(input("Y:"))

mp = {1: x}

for i in range(2, 1000):
    mp[i] = mp[i-1] - 16.5


def get_path(message, validator):
    path = input(message)
    path = validator(path)
    return path


def file_exist(file):
    return os.path.isfile(file)


def validate_file_input(file_path):
    while file_exist(file_path) is False:
        print('Invalid File Path')
        if input('Do you want to try again ? (Y/N) :').lower() != 'y':
            print('Bye Bye see ya later...')
            exit(0)
        file_path = input('Insert the path again:')
    print('File Located successfully !')
    return file_path


def get_column_idx(li):
    col_name = input('Column Name:')
    try:
        return li.index(col_name)
    except ValueError:
        print("This Column doesn't exists")
        if input('Do you want to try again ? (Y,N):').lower() != 'y':
            print('Bye Bye see ya late ...')
            exit(0)
        else:
            return get_column_idx(li)


def get_date(target_path, validator=None):
    result = []
    with open(target_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        column_idx = -1
        for row in csv_reader:
            if column_idx == -1:
                column_idx = get_column_idx(row)
            if len(row[column_idx]) > 0:
                result.append(row[column_idx])
        if len(result) > 1:
            result.pop(0)
            print('Data Fetched Successfully ...')
        else:
            print('Invalid Data!')
            exit(0)
    if validator is not None:
        validator(result)
    return result


def generate_images(attendees, certification_file_path):
    if 'Certifications' not in os.listdir():
        os.mkdir('Certifications')
        
    for attendee in attendees:
        k = attendee
        photo_name = '_'.join(k.split(' '))
        img = Image.open(certification_file_path)
        i1 = ImageDraw.Draw(img)
        images.append(f"{photo_name}.png")
        print(f'{photo_name}.png created successfully!.')
        words = 0
        for c in attendee:
            if c != ' ':
                words += 1

        i1.text((mp[words], y), f'{attendee}', font=my_font, fill=(0, 0, 0), align='centre')
        img.save(f'Certifications/{photo_name}.png')
    

def format_names(names):
    for idx in range(len(names)):
        res = []
        for name in list(names[idx].split(' ')):
            res.append(name[0].upper() + ''.join(name[1::]))
            res.append(' ')
        res.pop()
        names[idx] = ''.join(res)


def validate_mails(mails):
    if len(mails) == 0:
        return False

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    for mail in mails:
        if not re.fullmatch(regex, mail):
            if input("Invalid Mail Founded!!!, Do You wanna Regenerate data(Y/N):").lower() != 'y':
                print("See you bye")
                exit(0)
            return get_date(path, validate_mails)

    return mails


def send_emails():
    print("CSV Emails ", end="")
    mails = get_date(path)
    sender_mail = input("Sender e-mail: ")
    sender_mail_password = input("Sender password: ")
    subject = input("Message subject: ")
    description = input("Message content: ")

    for idx in range(len(mails)):
        mail = SendMail(sender_mail, sender_mail_password, mails[idx], subject, description,
                        f'Certifications/{images[idx]}')
        print(mails[idx], images[idx])
        mail.send_certification()


cert_path = get_path('Insert Certification Image Path:', validate_file_input)
path = get_path('CSV File Path:', validate_file_input)
names = get_date(path, format_names)
generate_images(names, cert_path)
print('')
print('')
print('Please Check Your Images under /CertificationGenerator/Certifications Directory Before continue because you can\'t undo the following operations !!!')
print('')
if input('Continue to send images(Y/N):').lower() == 'y':
    send_emails()
    print('Images sent successfully.')
else:
    print('Ok, GoodBye see ya later!')
