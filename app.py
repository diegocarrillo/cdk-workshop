#!/usr/bin/env python3

from aws_cdk import core

from workshop.workshop_stack import WorkshopStack

#We call your CDK application an app, which is represented by the AWS CDK class App.
#This code loads and instantiates an instance of the CdkWorkshopStack class from 
#worshop/workshop_stack.py file. We won’t need to look at this file anymore.

app = core.App()
WorkshopStack(app, "workshop", env={'region': 'us-east-1'})


#AWS CDK apps are effectively only a definition of your infrastructure using code. 
# When CDK apps are executed, they produce (or “synthesize”, in CDK parlance) an AWS CloudFormation template 
# for each stack defined in your application.
app.synth()
