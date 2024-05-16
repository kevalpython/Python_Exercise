import re

def validate_emails(emails):
    valid_emails = []
    for email in emails:
        if re.match(r'^[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$', email):
            valid_emails.append(email)
    return valid_emails

emails = ['abc@gmail.com', '123$tt*@xyz.com', 'good@bad@uk.in', 'nasa@usa12.space',
          'no-reply@domain.in', 'ramhanuman@saketa.lok', 'ruhi.mohan@exter123.123',
          'fake@fake123.fakercom']

valid_emails = validate_emails(emails)

print("Valid emails:", valid_emails)