DEPLOYMENT_NAME := "sep-database"
OS_PASSWORD := "str0ng.P4ssw0rd"

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

kstart:
  minikube start

kstop:
  minikube stop

kdeploy:
  helm install {{DEPLOYMENT_NAME}} opensearch/opensearch --values=values.yaml

kdelete:
  helm delete {{DEPLOYMENT_NAME}}   

kshow:
  kubectl get pods --namespace=default -l app.kubernetes.io/component=opensearch-cluster-master -w

os-start:
  export OPENSEARCH_INITIAL_ADMIN_PASSWORD={{OS_PASSWORD}}
  docker-compose up -d

os-healthcheck:
  curl https://localhost:9200 -ku 'admin:{{OS_PASSWORD}}'

os-upload-example:
  curl -H "Content-Type: application/x-ndjson" -X PUT "https://localhost:9200/sep_articles" -ku admin:{{OS_PASSWORD}} --data-binary "@opensearch/mappings/sep_articles.json"
  curl -H "Content-Type: application/x-ndjson" -X PUT "https://localhost:9200/sep_articles/_bulk" -ku admin:{{OS_PASSWORD}} --data-binary "@data/html/json/sep_articles.json"