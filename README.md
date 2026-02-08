# create a virtual environment
To create a virtual environment, run the command python -m venv (your environment name).

If you're on a Mac, use python3 -m venv (your environment name).

# Move into your virtual environment
Activate the virtual environment by accessing it. Open your environment; inside you'll see a folder called Scripts, and within that, you'll find a file called activate. The command is as follows:

/(your environment name)/Scripts/activate or ./(your environment name)/Scripts/activate

Once activated, you should see a green name in the bottom left corner of your VS console with the name of your environment.

# Download the dependencies
Download the project dependencies; you will find a file called requirements. Run the following command: pip install -r requirements.txt or python -m pip install -r requirements.txt

# Run uvicorn to run the local server
To start the local server, run the command uvicorn app.main:app --reload

After this, you can test it on Postan.

# OpenAI API key
Create a .env file in the root of your project and paste your API key inside, ideally named "OPENAI_API_KEY"