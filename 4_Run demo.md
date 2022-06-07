# Kafka - 분산데이터스트리밍 플랫폼


export WORKDIR='/root/kafka-eda'
cd $WORKDIR

#########################################################################################
# 1. (deploy-server) Order
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda'
cd $WORKDIR
source venv/bin/activate

python order.py


#########################################################################################
# 2. (deploy-server) Transactions
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda'
cd $WORKDIR
source venv/bin/activate

python transactions.py


#########################################################################################
# 3. (deploy-server) Analytics
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda-demo'
cd $WORKDIR

source venv/bin/activate
python analytics.py


#########################################################################################
# 4. (deploy-server) SMS Alert
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda-demo'
cd $WORKDIR

source venv/bin/activate
python sms.py