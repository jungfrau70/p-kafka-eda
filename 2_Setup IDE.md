# Jupyter Lab - Python IDE

Prerequsites:
- Started deploy-server
- Started kafka-cluster

export WORKDIR='/root/kafka-eda'
cd $WORKDIR

#########################################################################################
# 1. (deploy-server) Create python venv with dependencies
#########################################################################################

apt-get install build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev liblz4-dev
git clone https://github.com/facebook/rocksdb.git
cd rocksdb
mkdir build && cd build
cmake ..
make
cd ..
export CPLUS_INCLUDE_PATH=${CPLUS_INCLUDE_PATH}${CPLUS_INCLUDE_PATH:+:}`pwd`/include/
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}${LD_LIBRARY_PATH:+:}`pwd`/build/
export LIBRARY_PATH=${LIBRARY_PATH}${LIBRARY_PATH:+:}`pwd`/build/

apt-get install python-virtualenv python-dev
virtualenv venv [--copies]
source venv/bin/activate

cat <<EOF | tee requirements.txt
aiodns==2.0.0
aiohttp==3.7.4
aiohttp-cors==0.7.0
aredis==1.1.5
async-timeout==3.0.1
attrs==19.1.0
cchardet==2.1.4
certifi==2019.9.11
cffi==1.12.3
chardet==3.0.4
ciso8601==2.1.1
Click==7.0
colorclass==2.2.0
colorlog==4.0.2
croniter==0.3.30
Cython==0.29.13
faust==1.7.4
gevent==1.4.0
greenlet==0.4.15
idna==2.8
influxdb==5.2.3
kafka-python==1.4.6
mode==4.0.1
multidict==4.5.2
mypy-extensions==0.4.1
opentracing==1.3.0
orjson==2.0.7
pycares==3.0.0
pycparser==2.19
python-dateutil==2.8.0
python-rocksdb==0.7.0
pytz==2019.2
requests==2.22.0
robinhood-aiokafka==1.0.4
setproctitle==1.1.10
six==1.12.0
terminaltables==3.1.0
urllib3==1.25.3
venusian==1.2.0
yarl==1.3.0
EOF

pip install --upgrade pip
pip install -r requirements.txt 


#########################################################################################
# 2. (deploy-server) Start jupyter lab
#########################################################################################

jupyter lab


#########################################################################################
# 3. (PC) Open jupyter lab
#########################################################################################

## Forward a port in vscode
8888

or 
Ctrl + Shift + P, type "Forward a port"

## Open webbrowser
http://localhost:8888/xxxx