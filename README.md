# gcp_deployment_manager_ansible_core
Auto configure an Ansible Core host in GCP on Ubuntu 18.04LTE.

Still a work in progress. Still to do are:
1. Add metadata to compute image configuration to run the python script.  Right now the image is installed but Ansible is not installed.
2. The code is lacking error checking and comments.

Once the host is installed, you will need to manually copy the key from the newly created service account to the host.

To deploy the files on gcp run

gcloud deployment-manager deployments create [deployment name] --config ansible-host.yaml

To remove the deployment on gcp run

gcloud deployment-manager deployments delete [deployment name]
