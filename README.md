# twilio-quest-data
Welcome to the Python Guild!

As members of the Python guild, you will be working through the challenges of TwilioQuest using the Python programming language. This project is pre-configured to do some interesting Twilio stuff using Python and the Flask web framework.
Setting Up

We assume that before you begin, you will have Python and pip installed on your system and available at the command line.

Before you can run this project, you will need to set three system environment variables. These are:

    TWILIO_ACCOUNT_SID : Get it from your Twilio Console.
    TWILIO_AUTH_TOKEN : Same as above.
    TWILIO_PHONE_NUMBER : A Twilio number that you own, that can be used for making calls and sending messages. You can find a list of phone numbers you control (and buy another one, if necessary) in the console.

For Mac and Linux, environment variables can be set by opening a terminal window and typing the following three commands - replace all the characters after the = with values from your Twilio account:

    export TWILIO_ACCOUNT_SID=ACXXXXXXXXX
    export TWILIO_AUTH_TOKEN=XXXXXXXXX
    export TWILIO_PHONE_NUMBER=+16518675309

On Windows, the easiest way to set permanent environment variables (as of Windows 8) is using the setx command. Note that there is no =, just the key and value separated by a space:

    setx TWILIO_ACCOUNT_SID ACXXXXXXXXX
    setx TWILIO_AUTH_TOKEN XXXXXXXXX
    setx TWILIO_PHONE_NUMBER +16518675309

Running the application

    Clone this repository. Navigate to the folder with the source code on your machine in a terminal window.

    From there we recommend creating a virtualenv and activating it to avoid installing dependencies globaly on your computer.

    virtualenv -p python3 env source env/bin/activate

    Install dependencies:

    pip install -r requirements.txt

    Run the web app: python app.py

    Open the app in your browser

    Enter your mobile number in the fields provided, and test both SMS text messages and phone calls being sent to the mobile number you provide. The web UI should look something like this:

python guild
Begin Questing!

This is but your first step into a larger world. Return to TwilioQuest to continue your adventure. Huzzah!
