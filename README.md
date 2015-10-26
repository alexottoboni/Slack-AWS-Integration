# Slack-AWS-Integration

Notify your Slack Channel when your AWS machine finishes launching.
Requires Python, BOTO, curl

It helps if you set the environment variable `$AWS_REGION` to the region the machine was launched in. 
Otherwise we guess what region and keep trying.
