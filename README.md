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

>login.first_login() will generate root and ctf ssh keys in this directory.

#other functions or uses
>t = login.get_t()
>t.get_targets(<id>)
>t.submit_flag([])

#All implementation related details added in the Project Report

You can directly run 
>python codeyoloco/login.py
and
>python codeyoloco/exploit_and_submit.py
or call their functions (login.first_login() and exploit_and_submit.exploit())
Calling exploit will automatically get all targets and run the exploits stated 
in codeyoloco/config.txt and submit the flags too.