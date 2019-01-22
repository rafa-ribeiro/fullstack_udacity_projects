from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = "<REPLACE_ACCOUNT_SID_HERE>"
# Seu Auth Token, encontre em twilio.com/console
auth_token  = "<REPLACE_AUTH_TOKEN_HERE>"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="<REPLACE_YOUR_NUMBER_HERE>", 
    from_="<REPLACE_TWILIO_NUMBER_HERE>",
    body="<MESSAGE_HERE>")

print(message.sid)