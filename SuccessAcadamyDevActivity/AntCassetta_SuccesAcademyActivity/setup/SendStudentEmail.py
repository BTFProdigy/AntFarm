import emails

# Prepare the email
message = emails.html(
    html="<h1>My message</h1><strong>I've got something to tell you!</strong>",
    subject="A very important message",
    mail_from="anthonyrrbc89@gmail.com",
)

# Send the email
r = message.send(
    to="kitcassetta@gmail.com",
    smtp={
        "host": "my-aws-smtp-server",
        "port": 587,
        "timeout": 5,
        "user": "",
        "password": "",
        "tls": True,
    },
)

# Check if the email was properly sent
assert r.status_code == 250