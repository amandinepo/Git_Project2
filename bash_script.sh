sudo apt-get update
sudo apt-get upgrade
sudo apt-get update && sudo apt-get dist-upgrade

sudo apt install python3-venv
sudo apt-get install apache2
pip install dash
pip install pandas

python3 -m venv .venvs/dash
source .venvs/dash/bin/activate
sudo ufw allow 8050
python dash_part.py

