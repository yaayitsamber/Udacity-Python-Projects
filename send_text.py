from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3a0bfaceb61046dd6950998f2c4daae3"
auth_token  = "6aafc49ecec8f5f2cf0b16f8086fc31e"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I LIVE MY LIFE A QUARTER MILE AT A TIME",
    to="+13602559421",    # Replace with your phone number
    from_="+13603835405") # Replace with your Twilio number
print message.sid
