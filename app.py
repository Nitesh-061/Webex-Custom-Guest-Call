""" 
Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
 """


from flask import Flask, render_template, request, redirect, url_for
from webexteamssdk import WebexTeamsAPI
from dotenv import load_dotenv
import time
import os


# load all environment variables
load_dotenv()


app = Flask(__name__)

@app.route('/join/<string:destination_id>')
def join_meeting(destination_id):
    #api = WebexTeamsAPI(access_token=os.getenv("WEBEX_TEAMS_ACCESS_TOKEN"))
    api = WebexTeamsAPI()
    subject = os.getenv("GUEST_ISSUER_SUBJECT") # This is the unique name of your guest issuer i.e. the mail address
    display_name = os.getenv("GUEST_DISPLAY_NAME") # This is the name your guest issuer will be seen as in the meeting
    guest_issuer_id = os.getenv("GUEST_ISSUER_ID") # The guest issuer id. You can obtain this from developer.webex.com
    expiration_time = os.getenv("GUEST_TOKEN_EXPIRATION") # Unix timestamp of how long this guest issuer should be valid for.
    secret = os.getenv("GUEST_SHARED_SECRET") # The secret, also obtained from developer.webex.com
    guest = api.guest_issuer.create(subject, display_name, guest_issuer_id, str(int(time.time())+int(expiration_time)), secret)

    print('Guest Token: ',guest.token)
    return render_template("joinmeeting.html", destination_id=destination_id, access_token=guest.token)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        posted_destination_id=request.form.get('destination') 
        return redirect(url_for('.join_meeting',destination_id=posted_destination_id))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)