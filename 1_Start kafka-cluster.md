# Kafka - 분산데이터스트리밍 플랫폼

References:
-. https://karthiksharma1227.medium.com/integrating-kafka-with-pyspark-845b065ab2e5

export WORKDIR='/root/p-lens/kafka'
cd $WORKDIR


#########################################################################################
# 1. Start kafka-cluster
#########################################################################################

docker-compose up -d

Every 2.0s: docker-compose -f docker-compose-kafka.yml ps                                                                                 ubuntu: Tue Jun  7 09:22:37 2022

 Name             Command            State                                   Ports
-------------------------------------------------------------------------------------------------------------------
kafka1   /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp,:::9092->9092/tcp
kafka2   /etc/confluent/docker/run   Up      9092/tcp, 0.0.0.0:9093->9093/tcp,:::9093->9093/tcp
kafka3   /etc/confluent/docker/run   Up      9092/tcp, 0.0.0.0:9094->9094/tcp,:::9094->9094/tcp
zoo1     /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp,:::2181->2181/tcp, 2888/tcp, 3888/tcp
zoo2     /etc/confluent/docker/run   Up      2181/tcp, 0.0.0.0:2182->2182/tcp,:::2182->2182/tcp, 2888/tcp, 3888/tcp
zoo3     /etc/confluent/docker/run   Up      2181/tcp, 0.0.0.0:2183->2183/tcp,:::2183->2183/tcp, 2888/tcp, 3888/tcp


#########################################################################################
# 2. Stop kafka cluster
#########################################################################################

## Stop services
docker-compose down

## (if required) Clean up
docker-compose rm -svf

or 
containers=`docker ps -a | grep -e 'kaf\|zoo\|telegraf' | awk '{print $1}'`
for container in $containers
do
    docker stop $container
    docker rm $container
done
