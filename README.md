# codeyoloco
CSE 545 Project and CTF

The root of our package is this directory: codeyoloco

Any scripts/modules should be added to one level deep from here in ./codeyoloco.
Eg: $.ipython
	>from codeyoloco import login

Use a virtualenv preferably:
setup like this:
$.sudo apt-get install python-pip
$.pip install virtualenv
$.virtualenv ~/venv
$.source ~/venv/bin/activate  #Add this line at end of ~/.bashrc file
$.pip install -r requirements.txt

Or installing the package will install the requirements for you too:
$.sudo python setup.py develop

Now you can use all functions in it as follows:
$.ipython
>from codeyoloco import login
#check if import is successful.
#Write aggregation functions to make our task easy on the War Day

