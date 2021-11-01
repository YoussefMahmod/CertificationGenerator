# CertificationsGenerator

> ## Objectives

1. The script will help you create many certificates for the attendees in an easy and simple way and without any effort (Names will be centered wherever you want). You only have to select the column that contains their names and leave the rest to the script.

2. The script will also help you to send these images that it made for you to the attendees by selecting the column that contains the attendees’ emails in the same order of names (meaning that each name has a corresponding email in the same row).

<br>

---

<br>

> ## How to Clone and Install Requirements.

<br>

### 1. Clone

```bash
$ git clone https://github.com/YoussefMahmod/CertificationGenerator.git
```

### 2. Install Requirements

```bash
1. $ cd CertificationGenerator/
2. $ pip3 install -r requirements.txt (For Python3)
```

<br>

---

<br>

> ## How to Use

<br>

This script divded into two parts Generate Images and Send Images so i recommend you not to send images before you check generated images.

<br>

### 1. If You're in windows:

```
Simply run main.exe
```

### 2. If You're in Linux run the command

```shell
$ python3 main.py
```

<br>

---

<br>

> ## Script Run Flow

1. Enter the center point of your names (X, Y).

   ***

   **NOTE:**

   > ⚠ Here you should try 1-letter name say "a" and try to play with x, y till you center it wherever you want.

   ***

2. Enter Image Path(Certification template).
3. Enter CSV File Path(Data File).
4. Enter Name of column which contains attendees' Full Name(Actual column name not the letter on csv file).

   ***

   **NOTE:**

   > ⚠ If you reached this point so CONGRATULATIONS Your Images generated successfully under /CertificationGenerator/Certifications Directory

   > ⚠ Continue if and only if
   > 1.your images generated as expected
   > 2.you have Emails Column which have mail "corresponding" to each name inside a csv file to send to.

   ***

5. Enter Name of column which contains attendees' emails.
6. Enter sender mail.
7. Enter sender mail password.

   ***

   **NOTE:**

   > ⚠ I recommend you to use a token not your actual password that's will handle some SMTPauth errors.

   > ⚠ To generate a token for gmail use:
   > https://security.google.com/settings/security/apppasswords

   ***

8. Enter a Message Title.
9. Enter a Message Content or Description.

## Congratulations Your Certifications Sent Successfully!.
