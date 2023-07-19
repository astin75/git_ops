import yaml
import os
staging_root_path = "kustomize_chart/fast-api/overlays/staging"
kustomization_path = os.path.join(staging_root_path, "kustomization.yaml")
workflow_patches_path = os.path.join(staging_root_path, "workflow-patches.yaml")

with open(kustomization_path, 'r') as f:
    kustomization = yaml.safe_load(f)
    

kustomization['namespace'] = 'production'

print(kustomization)
kustomization_path_production = kustomization_path.replace("staging", "production")
with open(kustomization_path_production, 'w') as yaml_file:
    yaml.dump(kustomization, yaml_file, sort_keys=False)
    
    
with open(workflow_patches_path, 'r') as f:
    workflow = yaml.safe_load(f)

workflow_patches_path_production = workflow_patches_path.replace("staging", "production")
with open(workflow_patches_path_production, 'w') as yaml_file:
    yaml.dump(workflow, yaml_file, sort_keys=False)
