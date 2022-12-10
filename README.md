# video-transfer
Serialize and send a video between clients - servers.

+++++++++++++++++++++++++++++++++++++**SERVER**+++++++++++++++++++++++++++++++++

sudo apt update

sudo apt install -y python3 python3-pip

sudo pip3 install numpy pandas scipy

sudo apt install -y libopencv-dev python3-opencv

You must first create a new port for listening: Pick a port number bigger than 1023, i.e., 1024-49151 (Registered/User ports) or 49152-65535 (Dynamic/Private ports). Don't forget to replace the port number in the code and make sure the chosen port (e.g., 3333) is not being used:

netstat -lntu

netstat -an | grep :3333

sudo ufw allow 3333

Then run 'python3 server.py'.

+++++++++++++++++++++++++++++++++++++**CLIENT**++++++++++++++++++++++++++++++++++

sudo apt update

sudo apt install -y python3 python3-pip

sudo pip3 install numpy pandas scipy

sudo apt install -y libopencv-dev python3-opencv

Copy 2 files: serialize-send-client.py and client.py. Run 'python3 client.py' (run 'server.py' in servers first).
