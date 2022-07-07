# Jupyter Lab - Python IDE

Prerequsites:
- Started deploy-server
- Started kafka-cluster

export WORKDIR='/root/p-kafka-eda/'
cd $WORKDIR

#########################################################################################
# 1. (deploy-server) Create python venv with dependencies
#########################################################################################

python3 -m venv venv [--copies]
source venv/bin/activate

cat <<EOF | tee requirements.txt
faust
EOF

pip install --upgrade pip
pip install -U -r requirements.txt 


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