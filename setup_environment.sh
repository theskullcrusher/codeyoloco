sudo apt-get install git-core
sudo apt-get install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
pip install virtualenv
virtualenv ~/venv
source ~/venv/bin/activate
echo "source ~/venv/bin/activate" | >> ~/.zshrc
git config --global user.email "ssshah22@asu.edu"
git config --global user.name "Suraj Shah"
git config --global credential.helper "cache --timeout=8000"
