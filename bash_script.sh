sudo apt-get update
sudo apt-get upgrade
sudo apt-get update && sudo apt-get dist-upgrade

sudo apt install python3-venv
sudo apt-get install apache2

mkdir flask_app && cd flask_app
python3 -m venv venv
source venv/bin/activate

pip install Flask

git clone https://github.com/amandinepo/Git_Project2.git
cd Git_Project2
pip install Flask
