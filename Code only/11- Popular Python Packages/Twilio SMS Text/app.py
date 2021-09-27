from twilio.rest import Client
account_SID = "AC38e55d46375c83c3a4928ac77fb95526"
auth_token = "71a90f0be1ae9f20c228ea04d932bac7"
client = Client(account_SID, auth_token)

sms = client.messages.create(
    to="+92 3351927492",
    from_="+1 734 418 6151",
    body="Hey, Raja! Congratulaions! You have been placed at Microsoft"
)
