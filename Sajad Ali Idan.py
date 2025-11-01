import numpy as np


with open("MyEmails.txt", "r") as file:
    lines = file.readlines()


emails = np.array([line.strip() for line in lines])


gmail_found = emails[np.char.find(emails, "@gmail.com") >= 0]


print("Your email addresses found:")
for email in gmail_found:
    print(email)


count = gmail_found.size


print(f"All email addresses found: {count}")
print("Nick name: [Sajad Ali]")