# Deploy Ansible Core using GCP Deployment Manager
Auto configure an Ansible Core host in GCP on Ubuntu 18.04LTE.

Still a work in progress. Most of the code should work. Still letf is:
1. The code is lacking error checking and comments.
2. Automate the assignment of an iam policy to the service account.  
3. Automate the generation and download of the service account authentication key to the new host.

Once the host is installed you will still need to manually generate the Service Account key in the GCP console, copy the resulting json file to the /etc/ansible/keys directory and update the inventory configuration file located in the /etc/ansible/inventory directory (a placeholder in the file shows where to enter the filename).

The configuration makes a couple of assumptions which you need to consider.
1. You have a custom VPC and a specific subnet you want to place the host on.
2. You have a firewall policy in place which must be updated to allow access to the host (ssh for example).

To deploy the files on gcp run

<b>gcloud deployment-manager deployments create [deployment name] --config ansible-host.yaml</b>

To remove the deployment on gcp run

<b>gcloud deployment-manager deployments delete [deployment name]</b>
