# gcp_deployment_manager_ansible_core
Work in progress for educational purposes only.
There are multiple versions within this repository.  Mostly because I am in the process of learning both GCP IaC development and git hub at the same time so it is a bit of a mess.

To deploy the files on gcp run
gcloud deployment-manager deployments create [deployment name] --config [yaml file you want to deploy]

To remove the deployment on gcp run
gcloud deployment-manager deployments delete [deployment name]
