import yaml
import os
staging_root_path = "kustomize_chart/fast-api/overlays/staging"
kustomization_path = os.path.join(staging_root_path, "kustomization.yaml")

with open(kustomization_path, 'r') as f:
    kustomization = yaml.safe_load(f)
    
print(kustomization)
kustomization['namespace'] = 'production'
kustomization['nameSuffix'] = '-production'

print(kustomization)
kustomization_path_production = kustomization_path.replace("staging", "production")
with open(kustomization_path_production, 'w') as yaml_file:
    yaml.dump(kustomization, yaml_file, sort_keys=False)
