
kubectl create namespace monitoring

kubectl create secret -n monitoring generic telegraf --from-literal=env=prod
<!-- kubectl create secret -n monitoring generic telegraf --from-literal=env=prod --from-literal=monitor_username=youruser --from-literal=monitor_password=yourpassword --from-literal=monitor_host=https://your.influxdb.local --from-literal=monitor_database=yourdb -->

kubectl apply -f external.yaml
kubectl apply -f telegraf-ds.yaml

kubectl -n kube-system logs -f vrops-telegraf-k8s-c4qqn