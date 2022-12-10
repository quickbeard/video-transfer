# video-transfer
Serialize and send a video between one client and multiple servers.

+++++++++++++++++++++++++++++++++++++++++**Client**+++++++++++++++++++++++++++++++++++++++++

sudo apt update

sudo apt install -y python3 python3-pip

sudo pip3 install numpy pandas scipy

sudo apt install -y libopencv-dev python3-opencv


+++++++++++++++++++++++++++++++++++++++++**Server**+++++++++++++++++++++++++++++++++++++++++

sudo apt update

sudo apt install -y python3 python3-pip

sudo pip3 install numpy pandas scipy

sudo apt install -y libopencv-dev python3-opencv


Create a new port for listening. Pick a port number bigger than 1023, i.e., 1024-49151 (Registered/User ports) or 49152-65535 (Dynamic/Private ports). Don't forget to replace the port number in the Python code and make sure the chosen port is not being used:

netstat -lntu

netstat -an | grep :2022

sudo ufw allow 2022

