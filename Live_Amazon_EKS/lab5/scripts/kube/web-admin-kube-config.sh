aws eks update-kubeconfig --name dev-cluster --role-arn arn:aws:iam::455231079534:role/WebAdminRole --alias web-admin --region us-west-2
echo ----------
echo 'Updated /home/ssm-user/.kube/config to use the following IAM role:'
echo 'WebAdminRole (web-admin)'
echo ----------
