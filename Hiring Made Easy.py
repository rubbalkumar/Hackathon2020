# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 04:07:36 2020

@author: Rubbal K. Badhan
"""

from natural_language_processing import * 
import tkinter as tk
from tkinter import *


root = tk.Tk()
#logo = tk.PhotoImage(file="resume-template-application.jpg")

#w1 = tk.Label(root, image=logo).pack(side="right")

b= tk.Label(root, 
              justify=tk.CENTER,
              padx = 10, text="HIRING MADE EASY").pack(side="top")




w= tk.Label(root, 
              justify=tk.CENTER,
              padx = 10, text="JOB DESCRIPTION").pack(side="top")

explanation = """
              Since 2001, XYZ has supported Destination Marketing Organizations (DMOs) with tools, knowledge, and creativity to help them perform at the top of their game. 
              We believe the world’s top cities and smallest towns each have a role to play in creating a better experience for the people who visit and a better life for the people who call it home.
              We are looking to add to our professional, dedicated and hard-working team an independent, talented, top-notch Front End Web Developer with a great work ethic who 
              thrives in organizations that constantly adapt and evolve."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="top")

w3= tk.Label(root, 
              justify=tk.CENTER,
              padx = 10, text="RESPONSIBILITIES: ").pack(side="top")

ep2 = """Build performant components that adhere to the provided technical specifications and approved design or prototypes.
Deliver quality, standards-compliant code that adheres to XYZ best practices.
Peer review your team’s work and deliver proper and timely feedback to ensure code completeness and cleanliness.
Collaborate with team members and team lead to prioritize project tickets and meet deadlines for review and deployment."""

w4 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=ep2).pack(side="top")

w5 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text="REQUIREMENTS").pack(side="top")



ep3 = """
1) Bachelors degree
2) You have a deep understanding of HTML, Node.js, JSON, CSS, and JavaScript.
3) Familiarity with Python.
4) Some Internship experience in an agile work environment.
5) Good communication skills."""

w7 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=ep3).pack(side="top")

w6 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text="KEYWORDS").pack(side="top")



ep4 = """
Bachelors, JavaScript, CSS, HTML, MySQL, JSON, Python, Node.js, Visualization, Internship, Agile, Communication"""

w8 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=ep4).pack(side="top")



canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry(root) 
canvas1.create_window(200, 140, window=entry1)



def getResume (): 
    resume = entry1.get()
    matching = prediction(resume)
    label1 = tk.Label(root, text= matching)
    canvas1.create_window(200, 230, window=label1)
    
button1 = tk.Button(text='Submit Resume', command=getResume)
canvas1.create_window(200, 180, window=button1)



root.mainloop()