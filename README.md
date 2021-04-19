# Webex Meeting Custom Guest Join Call
Sample code that uses the Webex Teams Web SDK to create a custom portal for joining webex meetings as a temporarily generated Guest User in Spaces, scheduled meetings or meetings in PMRs in addition to being able to call other Webex Teams users directly 1-1. 


## Installation/Configuration

It is recommend to set up your environment as followed:

In the CLI:
1.	Choose a folder, then create and activate a virtual environment for the project


2. Access the created virtual enviroment folder

3.	Clone this Github repository into the virtual environment folder.
    ```python
    git clone [add github link here]
    ```
    For Github link: 
        In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**
         

4. Access the folder you just created when cloning
    ```
    cd Webex_Custom_Guest_Call
    ```

5.	Install dependencies
    ```python
    pip install -r requirements.txt
    ```

6. Creating a Webex Teams Guest Issuer Auth

For this sample, the end user will be a Webex Teams Guest User.

To be able to create these Guest Users, you will need to create a "Guest Issuer" account on the Webex for Developers portal.

- Login to the Webex for Developers site at <https://developer.webex.com>

  - Once logged in, click on "My Webex Teams Apps" under your profile at the top
  - Click "Create a New App" button
  - Click "Create a Guest Issuer"
  - Choose a name, example: "Webex_Guests" // any name
  - Note: Free users cannot create guest issuers (request a demo account from any Cisco representative or a Cisco Partner)  

Be sure to note the Guest Issuer Name, Guest Issuer ID and Guest Issuer Shared Secret provided when you created the guest issuer authority to use in the next step.   

7. Edit `.env` and fill out the requested values:  

`GUEST_ISSUER_ID`: Specified when creating the Guest Issuer  described above.  
`GUEST_SHARED_SECRET`: This is the Guest Issuer Shared Secret obtained when creating the Guest Issuer 
`GUEST_ISSUER_SUBJECT`: This is the Guest Issuer Name.  
`GUEST_DISPLAY_NAME`: This is the display name of the guest user you are generating. (i.e. Johnny Guest).  
`GUEST_TOKEN_EXPIRATION`: Time in seconds the guest token should be valid for. The default value  in the samle is 5400 seconds or 90 minutes which is usually enough for a regular tele-consultation or to have the guest join a meeting that lasts 1 hour (in case of extension)  


8. This repository contains some css and font files from the Cisco UI Kit project (http://cisco-ui.cisco.com) for version 1.3.5. If you wish to update them with a later version to add newer UI elements that might have been released for the Kit, download the corresponding official distribution file, extract the zip file and replace the fonts folder in the STATIC folder of your copy of this project. Also copy css/cui-standard.min.css to the STATIC/CSS folder  


## Usage
 
 
  - Once the application is correctly configured you can launch it from the terminal using the python command:

    ```$ python app.py```

  - Now a web browser to our web server at <http://localhost:5100/> (assuming you left the default port and web server address in the `app.py` source file), then enter the destination in the input box (i.e. foo@acme.com , could be a user or the URI of a Webex meeting) and click on the Submit button.  

![/IMAGES/SpecifyDestination.png](/IMAGES/SpecifyDestination.png)

  - IMPORTANT: You must specify localhost if running locally and you have not changed the Flask code in `app.py` to use https with a certificate or else the Webex Teams Web SDK will throw an error when you trying  to connect the audio/video of the call.  

  - You can also specify the destination to call without having to enter it in an input box by using the 'join' path of the sample application instead of going to to the root path. This is an example of calling the Webex Teams user foo@acme.com: <http://localhost:5100/join/foo@acme.com>  

  - The main call page is loaded and after a few seconds.  
  - Once the green **Call** button is enabled, click on it to place a call to the destination specified in the URI provided.  

  - In a few seconds, you should see the call in the browser!  

  - The call will appear video muted initially. You can click on the green camera icon to start sending video. 

  - You can mute your audio or video at any time using the corresponding icons.  

  - You can also lower the quality of the video sent in the meeting by clicking on the blue call rate button.

  - The gray webex, mic and camera icons on the right contain the status of the call and the webex connection, you can mouse over them to reveal the status  

  - If content is shared in the meeting, the main remote video window will be replaced with the content being shared until the sharing stops.


#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.