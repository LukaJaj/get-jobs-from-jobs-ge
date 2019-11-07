from twilio.rest import Client
import jobs_eg_scrapper as scrapped_jobs

account_sid = 'AC65c833faebbac82390ad7685f389e13a'
auth_token = '13538f4eac89df148c4993c28221e2d0'
client = Client(account_sid, auth_token)

j=', '.join(scrapped_jobs.parse_jobs_ge())

message = client.messages.create(
                     body=j,
                     from_='+12016902744',
                     to='+995591108750'
                 )

print(message.sid)
