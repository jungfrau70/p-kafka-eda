# Kafka - 분산데이터스트리밍 플랫폼


export WORKDIR='/root/p-kafka-eda/kafka-demo-3'
cd $WORKDIR


#########################################################################################
# 1. (deploy-server) Create kafka topics
#########################################################################################

## Create Topics :: orders, order_details
docker exec -it kafka1 kafka-topics --bootstrap-server=$DOCKER_HOST_IP:9092,$DOCKER_HOST_IP:9093,$DOCKER_HOST_IP:9094 \
                                    --create \
                                    --topic orders \
                                    --partitions 2 \
                                    --replication-factor 2

docker exec -it kafka1 kafka-topics --bootstrap-server=$DOCKER_HOST_IP:9092,$DOCKER_HOST_IP:9093,$DOCKER_HOST_IP:9094 \
                                    --create \
                                    --topic order_results \
                                    --partitions 2 \
                                    --replication-factor 2

#########################################################################################
# 2. (deploy-server) Order
#########################################################################################

## run the code in new bash terminal
source ../venv/bin/activate

python data_requester.py worker -p 10001

or

docker-compose order


#########################################################################################
# 3. (deploy-server) Transactions
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda/kafka-demo-3'
cd $WORKDIR
source ../venv/bin/activate

python data_processor.py worker -p 10002


#########################################################################################
# 4. (deploy-server) Aggregator
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda/kafka-demo-3'
cd $WORKDIR
source ../venv/bin/activate

python data_aggregator.py worker -p 10003


#########################################################################################
# 5. (deploy-server) db loader
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/p-kafka-eda/kafka-demo-3/db_loader/app'
cd $WORKDIR
source ../venv/bin/activate

python3 db.py && faust -A main worker -l info


#########################################################################################
# 6. (deploy-server) api_gateway
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/p-kafka-eda/kafka-demo-3/api_gateway'
cd $WORKDIR
source ../venv/bin/activate

uvicorn main:app --reload 


#########################################################################################
# 7. (deploy-server) View
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda/kafka-demo-3'
cd $WORKDIR

source venv/bin/activate
?????


#########################################################################################
# 8. (deploy-server) SMS Alert
#########################################################################################

## run the code in new bash terminal
export WORKDIR='/root/kafka-eda/kafka-demo-3'
cd $WORKDIR

source venv/bin/activate
python sms.py