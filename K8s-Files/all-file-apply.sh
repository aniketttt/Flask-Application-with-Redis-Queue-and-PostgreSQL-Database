kubectl apply -f postgres-deployment.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f flask-app-deployment.yaml
kubectl apply -f worker-deployment.yaml
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-configmap.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f flask-app-service.yaml
kubectl apply -f nginx-service.yaml