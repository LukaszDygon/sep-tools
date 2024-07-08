DEPLOYMENT_NAME := "sep-database"

list:
  just --list

# install dependencies, activate Python environment for development and deploy kubernetes cluster. You can now use kubectl to connect.
init:
  pip install poetry
  poetry config virtualenvs.in-project true
  poetry install --no-root
  source .venv/bin/activate

  helm repo add opensearch https://opensearch-project.github.io/helm-charts/
  helm repo update

  alias kubectl="minikube kubectl --"


# show all pods
show-pods:
  kubectl get pods --namespace=default -l app.kubernetes.io/component=opensearch-cluster-master -w

kube-start:
  minikube start

kube-stop:
  minikube stop

kube-deploy:
  helm install {{DEPLOYMENT_NAME}} opensearch/opensearch --values=values.yaml

kube-delete:
  helm delete {{DEPLOYMENT_NAME}}   

kube-show:
  kubectl get pods --namespace=default -l app.kubernetes.io/component=opensearch-cluster-master -w