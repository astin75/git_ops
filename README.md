# git_ops

# env 
- docker install : https://docs.docker.com/engine/install/ (for minikube vm)
- minikube : https://minikube.sigs.k8s.io/docs/start/

## minikube start
- minikube start

# install argoCD, and argo workflow

### path ./helm_chart
### if no namespace, you need make it
- kubectl create namespace {namespace name}
### argo cd
install argocd
- helm install -n argocd argocd ./argo_cd

install argocd CLI 
- visit : https://argo-cd.readthedocs.io/en/stable/getting_started/#2-download-argo-cd-cli
- start from #2-download-argo-cd-cli
  
access argocd in web
- kubectl port-forward svc/argocd-server -n argocd 8080:443
- argocd admin initial-password -n argocd -> copy password
- visit : localhost:8080 (login : admin and password)

### argo workflow
install argo workflow
- helm install -n argo argo-workflow ./argo_workflow
- access argo workflow in web
- kubectl -n argo port-forward deployment/argo-server 2746:2746
- visit : localhost:2746

### access fast-api app
- kubectl -n staging port-forward deployment/fast-api 9009:80
- visit : localhost:9009/docs


### etc command
- kubectl kustomize kustomize_chart/fast-api/overlays/production/. > ppa_pro.yaml

