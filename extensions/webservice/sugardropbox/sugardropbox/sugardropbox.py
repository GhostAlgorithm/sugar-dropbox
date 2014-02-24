"""
# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 't0sa9x54txzlngv'
app_secret = 'b7sex5xvex59l53'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Login, similar a GDRrive
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

f = open('test.txt', 'rb')
response = client.put_file('/The first upload.txt', f)
import json
data = json.dumps(response)
ff = open("Data.json", "w")
ff.write(data)
ff.close()
"""
