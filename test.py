import imaplib
import email
from speak import speak
import asyncio
from email.header import decode_header


def decode_mime_words(header_val):
    decoded_parts = decode_header(header_val)
    return "".join(
        part.decode(enc or "utf-8") if isinstance(part, bytes) else part
        for part, enc in decoded_parts
    )


def read_email_from_gmail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("dorukaytekinexxon@gmail.com", "byqr eqyb ncwz kenw")
    mail.select("inbox")
    result, data = mail.search(None, "UNSEEN")
    mail_ids = data[0]

    text = ""
    id_list = mail_ids.split()
    if id_list:
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        i = first_email_id
        while i <= latest_email_id:
            result, data = mail.fetch(str(i), "(RFC822)")
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = decode_mime_words(msg["subject"])
                    email_from = decode_mime_words(msg["from"])
                    email_sender = ""
                    for word in email_from.split():
                        if word != email_from.split()[-1]:
                            email_sender += word

                    text += "You Have A New Mail From : " + email_sender + "\n"
                    text += "And It's About : " + email_subject + "\n"
            i += 1
    else:
        text += "No New Mail Sir"

    asyncio.run(speak(text))


read_email_from_gmail()
