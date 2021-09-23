# Author: Michael Ziegler   Date: April, 14th, 2020
# Purpose: To efficiently take notes on all of the topics covered in the Udemy: AWS Associate Developer Certification Course.

import tkinter as tk
from tkinter import font as tkfont
from tkinter import * 
import os

class NotesApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("NotesApp | Michael Ziegler")

        #Create Container
        container = tk.Frame(self, width=200, height=200)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Create Frames
        self.frames = {}
        for F in (StartPage, Amazon_EC2, Amazon_ECR, Amazon_ECS, AWS_Elastic_Beanstalk, AWS_Lambda, Elastic_Load_Balancing, Amazon_CloudFront, Amazon_Kinesis, Amazon_Route_53, Amazon_S3, Amazon_RDS, Amazon_DynamoDB, Amazon_DynamoDB_Accelerator, Amazon_ElastiCache, Amazon_SQS, Amazon_SNS, AWS_Step_Functions, Amazon_SWF, Amazon_API_Gateway, Amazon_SES, Amazon_Cognito, IAM, Amazon_CloudWatch, Amazon_EC2_Systems_Manager, AWS_CloudFormation, AWS_CloudTrail, AWS_CodeCommit, AWS_CodeBuild, AWS_CodeDeploy, AWS_CodePipeline, AWS_X_Ray, AWS_KMS):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.geometry("1100x400")
        self.show_frame("StartPage")

    #Controller Function Definitions
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS Developer Associate NoteBook", font=controller.title_font)
        label.pack(side = TOP, pady = 10)
        
        fm = Frame(self)
        fm2 = Frame(self)
        fm3 = Frame(self)
        fm4 = Frame(self)
    
        #Creating a photoimage object / importing button images 
        photo = PhotoImage(file =".\\bin\\ec2.PNG") 
        photo2 = PhotoImage(file =".\\bin\\ECR.PNG")
        photo3 = PhotoImage(file =".\\bin\\ECS.PNG")
        photo4 = PhotoImage(file =".\\bin\\ElasticBeanstalk.PNG")
        photo5 = PhotoImage(file =".\\bin\\lambd.PNG") 
        photo6 = PhotoImage(file =".\\bin\\ELB.PNG")
        photo7 = PhotoImage(file =".\\bin\\CloudFront.PNG")
        photo8 = PhotoImage(file =".\\bin\\Kinesis.PNG")
        photo9 = PhotoImage(file =".\\bin\\Route_53.PNG")
        photo10 = PhotoImage(file =".\\bin\\S3.PNG")

        photo11 = PhotoImage(file =".\\bin\\rds.PNG") 
        photo12 = PhotoImage(file =".\\bin\\Dynamo.PNG")
        photo13 = PhotoImage(file =".\\bin\\Acc.PNG")
        photo14 = PhotoImage(file =".\\bin\\elas.PNG")
        photo15 = PhotoImage(file =".\\bin\\sqs.PNG") 
        photo16 = PhotoImage(file =".\\bin\\sns.PNG")
        photo17 = PhotoImage(file =".\\bin\\step.PNG")
        photo18 = PhotoImage(file =".\\bin\\swf.PNG")
        photo19 = PhotoImage(file =".\\bin\\gateway.PNG")
        photo20 = PhotoImage(file =".\\bin\\ses.PNG")
        photo21 = PhotoImage(file =".\\bin\\cognito.PNG")

        photo22 = PhotoImage(file =".\\bin\\iam.PNG") 
        photo23 = PhotoImage(file =".\\bin\\cloudwatch.PNG")
        photo24 = PhotoImage(file =".\\bin\\systems.PNG")
        photo25 = PhotoImage(file =".\\bin\\cloudformation.PNG")
        photo26 = PhotoImage(file =".\\bin\\cloudtrail.PNG") 
        photo27 = PhotoImage(file =".\\bin\\codecommit.PNG")
        photo28 = PhotoImage(file =".\\bin\\codebuild.PNG")
        photo29 = PhotoImage(file =".\\bin\\codedeploy.PNG")
        photo30 = PhotoImage(file =".\\bin\\codepipeline.PNG")
        photo31 = PhotoImage(file =".\\bin\\xray.PNG")
        photo32 = PhotoImage(file =".\\bin\\kms.PNG")

        #Resizing images to fit on button 
        self.photoimage = photo.subsample(13, 13)
        self.photoimage2 = photo2.subsample(13, 13)
        self.photoimage3 = photo3.subsample(13, 13)
        self.photoimage4 = photo4.subsample(13, 13)
        self.photoimage5 = photo5.subsample(13, 13)
        self.photoimage6 = photo6.subsample(13, 13)
        self.photoimage7 = photo7.subsample(13, 13)
        self.photoimage8 = photo8.subsample(13, 13)
        self.photoimage9 = photo9.subsample(13, 13)
        self.photoimage10 = photo10.subsample(13, 13)

        self.photoimage11 = photo11.subsample(13, 13)
        self.photoimage12 = photo12.subsample(13, 13)
        self.photoimage13 = photo13.subsample(13, 13)
        self.photoimage14 = photo14.subsample(13, 13)
        self.photoimage15 = photo15.subsample(13, 13)
        self.photoimage16 = photo16.subsample(13, 13)
        self.photoimage17 = photo17.subsample(13, 13)
        self.photoimage18 = photo18.subsample(13, 13)
        self.photoimage19 = photo19.subsample(13, 13)
        self.photoimage20 = photo20.subsample(13, 13)
        self.photoimage21 = photo21.subsample(13, 13)

        self.photoimage22 = photo22.subsample(13, 13)
        self.photoimage23 = photo23.subsample(13, 13)
        self.photoimage24 = photo24.subsample(13, 13)
        self.photoimage25 = photo25.subsample(13, 13)
        self.photoimage26 = photo26.subsample(13, 13)
        self.photoimage27 = photo27.subsample(13, 13)
        self.photoimage28 = photo28.subsample(13, 13)
        self.photoimage29 = photo29.subsample(13, 13)
        self.photoimage30 = photo30.subsample(13, 13)
        self.photoimage31 = photo31.subsample(13, 13)
        self.photoimage32 = photo32.subsample(13, 13)
        
        #StartPage Image Buttons
        Button(fm, text = '', image = self.photoimage,
                           compound = LEFT, command=lambda: controller.show_frame("Amazon_EC2")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage2, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_ECR")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage3, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_ECS")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage4, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_Elastic_Beanstalk")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage5, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_Lambda")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage6, 
                            compound = LEFT, command=lambda: controller.show_frame("Elastic_Load_Balancing")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage7, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_CloudFront")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage8, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_Kinesis")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage9, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_Route_53")).pack(side = LEFT)
        Button(fm, text = '', image = self.photoimage10, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_S3")).pack(side = LEFT)
        #----------------------------------------------------------
        Button(fm2, text = '', image = self.photoimage11, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_RDS")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage12, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_DynamoDB")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage13, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_DynamoDB_Accelerator")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage14, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_ElastiCache")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage15, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_SQS")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage16, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_SNS")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage17, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_Step_Functions")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage18, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_SWF")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage19, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_API_Gateway")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage20, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_SES")).pack(side = LEFT)
        Button(fm2, text = '', image = self.photoimage21, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_Cognito")).pack(side = LEFT)
        #----------------------------------------------------------
        Button(fm3, text = '', image = self.photoimage22, 
                            compound = LEFT, command=lambda: controller.show_frame("IAM")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage23, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_CloudWatch")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage24, 
                            compound = LEFT, command=lambda: controller.show_frame("Amazon_EC2_Systems_Manager")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage25, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_CloudFormation")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage26, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_CloudTrail")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage27, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_CloudTrail")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage28, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_CodeBuild")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage29, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_CodeDeploy")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage30, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_CodePipeline")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage31, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_X_Ray")).pack(side = LEFT)
        Button(fm3, text = '', image = self.photoimage32, 
                            compound = LEFT, command=lambda: controller.show_frame("AWS_KMS")).pack(side = LEFT)
        
        fm.pack(side=TOP, padx=10, pady=0)
        fm2.pack(side=TOP, padx=10, pady=0)
        fm3.pack(side=TOP, padx=10, pady=0)
        fm4.pack(side=TOP, padx=10, pady=15)
        
class Amazon_EC2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Elastic Compute Cloud(EC2) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        self.ec2 = Text(self, width=100, height=40)
        filename=r".\MyNotes\ec2.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.ec2.insert(INSERT, line)
        self.ec2.pack()
        file.close()
        
    def save(self):
        text = self.ec2.get("0.0", END)
        with open(r".\MyNotes\ec2.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_ECR(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Elastic Container Registry(ECR) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        
        self.ecr = Text(self, width=100, height=40)
        filename=r".\MyNotes\ecr.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.ecr.insert(INSERT, line)
        self.ecr.pack()
        file.close()
        
    def save(self):
        text = self.ecr.get("0.0", END)
        with open(r".\MyNotes\ecr.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_ECS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Elastic Container Service(ECS)", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        self.ecs = Text(self, width=100, height=40)
        filename=r".\MyNotes\ecs.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.ecs.insert(INSERT, line)
        self.ecs.pack()
        file.close()
        
    def save(self):
        text = self.ecs.get("0.0", END)
        with open(r".\MyNotes\ecs.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")

        
class AWS_Elastic_Beanstalk(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS Elastic Beanstalk Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        
        self.elasticB = Text(self, width=100, height=40)
        filename=r".\MyNotes\elasticB.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.elasticB.insert(INSERT, line)
        self.elasticB.pack()
        file.close()
        
    def save(self):
        text = self.elasticB.get("0.0", END)
        with open(r".\MyNotes\elasticB.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_Lambda(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS Lambda Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        
        self.awslambda = Text(self, width=100, height=40)
        filename=r".\MyNotes\awslambda.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.awslambda.insert(INSERT, line)
        self.awslambda.pack()
        file.close()
        
    def save(self):
        text = self.awslambda.get("0.0", END)
        with open(r".\MyNotes\awslambda.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Elastic_Load_Balancing(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Elastic Load Balancing(ELB) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        
        self.elastic = Text(self, width=100, height=40)
        filename=r".\MyNotes\elastic.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.elastic.insert(INSERT, line)
        self.elastic.pack()
        file.close()
        
    def save(self):
        text = self.elastic.get("0.0", END)
        with open(r".\MyNotes\elastic.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_CloudFront(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon CloudFront Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        
        self.cloudfront = Text(self, width=100, height=40)
        filename=r".\MyNotes\cloudfront.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.cloudfront.insert(INSERT, line)
        self.cloudfront.pack()
        file.close()
        
    def save(self):
        text = self.cloudfront.get("0.0", END)
        with open(r".\MyNotes\cloudfront.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_Kinesis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Kinesis Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.kinesis = Text(self, width=100, height=40)
        filename=r".\MyNotes\kinesis.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.kinesis.insert(INSERT, line)
        self.kinesis.pack()
        file.close()
        
    def save(self):
        text = self.kinesis.get("0.0", END)
        with open(r".\MyNotes\kinesis.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_Route_53(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Route 53 Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.r53 = Text(self, width=100, height=40)
        filename=r".\MyNotes\r53.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.r53.insert(INSERT, line)
        self.r53.pack()
        file.close()
        
    def save(self):
        text = self.r53.get("0.0", END)
        with open(r".\MyNotes\r53.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_S3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Simple Cloud Storage Service(S3) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.s3 = Text(self, width=100, height=40)
        filename=r".\MyNotes\s3.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.s3.insert(INSERT, line)
        self.s3.pack()
        file.close()
        
    def save(self):
        text = self.s3.get("0.0", END)
        with open(r".\MyNotes\s3.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()

class Amazon_RDS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Relational Database Service(RDS) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.rds = Text(self, width=100, height=40)
        filename=r".\MyNotes\rds.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.rds.insert(INSERT, line)
        self.rds.pack()
        file.close()
        
    def save(self):
        text = self.rds.get("0.0", END)
        with open(r".\MyNotes\rds.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_DynamoDB(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon DynamoDB Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.dynamo = Text(self, width=100, height=40)
        filename=r".\MyNotes\dynamo.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.dynamo.insert(INSERT, line)
        self.dynamo.pack()
        file.close()
        
    def save(self):
        text = self.dynamo.get("0.0", END)
        with open(r".\MyNotes\dynamo.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_DynamoDB_Accelerator(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon DynamoDB Accelerator Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)
        
        self.acc = Text(self, width=100, height=40)
        filename=r".\MyNotes\acc.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.acc.insert(INSERT, line)
        self.acc.pack()
        file.close()
        
    def save(self):
        text = self.acc.get("0.0", END)
        with open(r".\MyNotes\acc.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()

class Amazon_ElastiCache(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon ElastiCache Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.elasticache = Text(self, width=100, height=40)
        filename=r".\MyNotes\elasticache.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.elasticache.insert(INSERT, line)
        self.elasticache.pack()
        file.close()
        
    def save(self):
        text = self.elasticache.get("0.0", END)
        with open(r".\MyNotes\elasticache.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_SQS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Simple Queue Service(SQS) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.sqs = Text(self, width=100, height=40)
        filename=r".\MyNotes\sqs.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.sqs.insert(INSERT, line)
        self.sqs.pack()
        file.close()
        
    def save(self):
        text = self.sqs.get("0.0", END)
        with open(r".\MyNotes\sqs.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_SNS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Simple Notification Service(SNS) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.sns = Text(self, width=100, height=40)
        filename=r".\MyNotes\sns.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.sns.insert(INSERT, line)
        self.sns.pack()
        file.close()
        
    def save(self):
        text = self.sns.get("0.0", END)
        with open(r".\MyNotes\sns.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_Step_Functions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS Step Functions Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.step = Text(self, width=100, height=40)
        filename=r".\MyNotes\step.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.step.insert(INSERT, line)
        self.step.pack()
        file.close()
        
    def save(self):
        text = self.step.get("0.0", END)
        with open(r".\MyNotes\step.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_SWF(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Simple Workflow Service(SWF) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.swf = Text(self, width=100, height=40)
        filename=r".\MyNotes\swf.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.swf.insert(INSERT, line)
        self.swf.pack()
        file.close()
        
    def save(self):
        text = self.swf.get("0.0", END)
        with open(r".\MyNotes\swf.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_API_Gateway(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon API Gateway Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.api = Text(self, width=100, height=40)
        filename=r".\MyNotes\api.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.api.insert(INSERT, line)
        self.api.pack()
        file.close()
        
    def save(self):
        text = self.api.get("0.0", END)
        with open(r".\MyNotes\api.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_SES(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Simple Email Service(SES) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.ses = Text(self, width=100, height=40)
        filename=r".\MyNotes\ses.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.ses.insert(INSERT, line)
        self.ses.pack()
        file.close()
        
    def save(self):
        text = self.ses.get("0.0", END)
        with open(r".\MyNotes\ses.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_Cognito(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon Cognito Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.cognito = Text(self, width=100, height=40)
        filename=r".\MyNotes\cognito.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.cognito.insert(INSERT, line)
        self.cognito.pack()
        file.close()
        
    def save(self):
        text = self.cognito.get("0.0", END)
        with open(r".\MyNotes\cognito.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class IAM(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Identity Access Managment(IAM) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.iam = Text(self, width=100, height=40)
        filename=r".\MyNotes\iam.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.iam.insert(INSERT, line)
        self.iam.pack()
        file.close()
        
    def save(self):
        text = self.iam.get("0.0", END)
        with open(r".\MyNotes\iam.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_CloudWatch(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon CloudWatch Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.cloudwatch = Text(self, width=100, height=40)
        filename=r".\MyNotes\cloudwatch.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.cloudwatch.insert(INSERT, line)
        self.cloudwatch.pack()
        file.close()
        
    def save(self):
        text = self.cloudwatch.get("0.0", END)
        with open(r".\MyNotes\cloudwatch.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class Amazon_EC2_Systems_Manager(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Amazon EC2 Systems Manager Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.systems = Text(self, width=100, height=40)
        filename=r".\MyNotes\systems.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.systems.insert(INSERT, line)
        self.systems.pack()
        file.close()
        
    def save(self):
        text = self.systems.get("0.0", END)
        with open(r".\MyNotes\systems.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_CloudFormation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS CloudFormation Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.cloudformation = Text(self, width=100, height=40)
        filename=r".\MyNotes\cloudformation.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.cloudformation.insert(INSERT, line)
        self.cloudformation.pack()
        file.close()
        
    def save(self):
        text = self.cloudformation.get("0.0", END)
        with open(r".\MyNotes\cloudformation.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_CloudTrail(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS CloudTrail Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.cloudtrail = Text(self, width=100, height=40)
        filename=r".\MyNotes\cloudtrail.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.cloudtrail.insert(INSERT, line)
        self.cloudtrail.pack()
        file.close()
        
    def save(self):
        text = self.cloudtrail.get("0.0", END)
        with open(r".\MyNotes\cloudtrail.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_CodeCommit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS CodeCommit Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.codecommit = Text(self, width=100, height=40)
        filename=r".\MyNotes\codecommit.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.codecommit.insert(INSERT, line)
        self.codecommit.pack()
        file.close()
        
    def save(self):
        text = self.codecommit.get("0.0", END)
        with open(r".\MyNotes\codecommit.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_CodeBuild(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS CodeBuild Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.codebuild = Text(self, width=100, height=40)
        filename=r".\MyNotes\codebuild.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.codebuild.insert(INSERT, line)
        self.codebuild.pack()
        file.close()
        
    def save(self):
        text = self.codebuild.get("0.0", END)
        with open(r".\MyNotes\codebuild.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_CodeDeploy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS CodeDeploy Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.codedeploy = Text(self, width=100, height=40)
        filename=r".\MyNotes\codedeploy.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.codedeploy.insert(INSERT, line)
        self.codedeploy.pack()
        file.close()
        
    def save(self):
        text = self.codedeploy.get("0.0", END)
        with open(r".\MyNotes\codedeploy.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_CodePipeline(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS CodePipeline Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.codepipeline = Text(self, width=100, height=40)
        filename=r".\MyNotes\codepipeline.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.codepipeline.insert(INSERT, line)
        self.codepipeline.pack()
        file.close()
        
    def save(self):
        text = self.codepipeline.get("0.0", END)
        with open(r".\MyNotes\codepipeline.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_X_Ray(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS X-Ray Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.xray = Text(self, width=100, height=40)
        filename=r".\MyNotes\xray.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.xray.insert(INSERT, line)
        self.xray.pack()
        file.close()
        
    def save(self):
        text = self.xray.get("0.0", END)
        with open(r".\MyNotes\xray.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
class AWS_KMS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AWS Key Managment Service(KMS) Notes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Save & Return", fg="white", bg="light green", font="Times 10 bold", command=self.save)
        button.pack(side=BOTTOM, fill="x", pady=15, padx=100)

        self.kms = Text(self, width=100, height=40)
        filename=r".\MyNotes\kms.txt"
        file = open(filename,'r')
        for line in file:
            line = line.strip('{')
            line = line.strip('}')
            self.kms.insert(INSERT, line)
        self.kms.pack()
        file.close()
        
    def save(self):
        text = self.kms.get("0.0", END)
        with open(r".\MyNotes\kms.txt", "w") as file:
            file.write(text)
        self.controller.show_frame("StartPage")
        file.close()
        
if __name__ == "__main__":
    app = NotesApp()
    app.mainloop()
