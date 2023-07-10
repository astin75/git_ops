# eks_tutorial
# git_ops


 helm install -n argocd argocd ./argo_cd
 kubectl port-forward svc/argocd-server -n argocd 8080:443
argocd admin initial-password -n argocd

 helm install -n argo argo-workflow ./argo_workflow
 kubectl -n argo port-forward deployment/argo-server 2746:2746
