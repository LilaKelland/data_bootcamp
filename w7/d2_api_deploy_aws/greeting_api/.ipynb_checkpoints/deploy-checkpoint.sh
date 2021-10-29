#!/bin/bash
git pull
git commit -a -m "deploy"
git push
scp -i /Users/lilakelland/.ssh/MyKeyPair.pem /Users/lilakelland/Documents/data_bootcamp/w7/d2/greeting_api/greeting_api.py ubuntu@ec2-3-23-132-27.us-east-2.compute.amazonaws.com:~

