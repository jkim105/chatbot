# -*- coding: utf-8 -*-
#
# Copyright (C) 2001-2018 NLTK Project
# Author: Christine Lam (clam4) & Jisoo Kim (jkim74)
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
WellesleyCS Chatbot is a friendly FAQ bot to help navigate common questions 
related to the CS Department at Wellesley College.

The chatbot structure is based on that of chat.eliza. Thus, it uses
a translation table to convert from question to response
i.e. "I am" --> "you are"

Of course, since WellesleyCS Chatbot does not understand the meaning of any words,
responses are very limited. WellesleyCS Chatbot will usually answer very vaguely, or
respond to a question by asking a different question, in much the same way
as WellesleyCS.
"""
from __future__ import print_function

from util import Chat, reflections

# responses are matched top to bottom, so non-specific matches occur later
# for each match, a list of possible responses is provided
responses = (


# COMPUTER SCIENCE IN GENERAL
# Below are number of regexes aiming to respond to questions regarding the general questions of computer science.
# In particular, the most important aspect was to notice that people have different methods of saying certain things
# i.e., a positive word could be "cool", but it could also be "best".
# Thus we had to list couple of synonymous words that people may potentially use to ask such questions.
# This could be done with the | which shows the "or", or with (.*)? that would catch anything that goes in between certain words.


# What is Computer Science?
    (r'What is (CS|Comp(.*) Sci(.*))\?',
    ( "Computer Science is the study of computers and computer systems. Ask me what about what langauges you can learn.",
      "Computer Science is a ball of fun! You should take a class and see for yourself. :) I can also give class recommendations.",
      "Computer Science is all about learning how coding and algorithms work. Ask me about what what languages you can learn.",
      "Computer Science is based on different techniques and strategies to create efficient programs and algorithms. Ask me about the best thing in the CS Department.",
      "Computer Science is the best department and major at Wellesley College! Ask me how to declare a CS major!")),
      
# What is the >positive< thing about/in Computer Science?
    (r'What is the (.*)?(best|coolest|greatest|amazing)(.*)?(CS|Comp(.*) Sci(.*))(.*)?\?',
    ( "The best thing about the Computer Science Department at Wellesley is all the personalized attention and help. Ask me about what you can learn in CS.",
      "The CS professors at Wellesley are wonderful people and they help create an encouraging learning environment. If you would like to see if CS is right for you, you can ask me about that.",
      "The Computer Science Department at Wellesley is a community. They have so many resources to help students suceed. Ask me about how you one can suceed in CS!",
      "The coolest thing about the CS department is the amount of classes they have! We such a wide variety of CS-related classes. Ask me about classes I recommend.",
      "From students to professors, the CS department is an inclusive place to try your hand at coding. Ask me about what languages you can learn.")),

# What is the >negative< thing about/in Computer Science?
    (r'What is the (.*)?(worst(.*)?|horribl(.*)|shit(.*)?)(.*)(CS|Comp(.*) Sci(.*))(.*)?\?',
    ( "Sorry. I do not have any negative opinions.",
      "That is not a nice question. Please ask something else.",
      "The Computer Science Department has such a high demand, the professors are trying their best to keep up.",
      "Please don't ask negative questions. We are trying to create a positive environment in this department.",
      "The only flaw about the Computer Science Department is that it's so wonderful that demand for seats in classes are high, but there is not enough supply.")),


# ABOUT THE MAJOR
# Below are number of regexes aiming to respond to questions regarding the major and minor of computer science.
# Again, there was need to notice that people have different methods of saying certain things
# In addition, the responses that we have included shows possible "empathy" coming from a chat bot.
# Some answers were purposely left broad as either the response got to be too long, 
# or a better answer could have been given from the CS Website.

    (r'How many (.*)?(course(.*)?|class(.*)?|lecture(.*)?)(.*)?(major|minor|CS|Comp(.*) Sci(.*))(.*)?\?',
    ( "You need to take 10 courses to major and present a poster, or take 5 courses to minor in computer science. You can ask me about what courses are in the major or minor.",
      "A minor in CS only requires 5 courses. If you have time, the major is 10 courses with a poster. You can ask me about what courses are in the major or minor.",
      "The major requires 10 classes + a poster. The minor requires 5 classes. You can ask me about what courses are in the major or minor.",
      "The major requires 10 courses and a poster whereas the minor only requires 5 courses. You can ask me about what courses are in the major or minor.")),

# People may have doubts about whether CS Would be the right major for them.
# The responses to this regex aims to encourage people and give positive words of advice, possibly showing "empathy" towards the humans.
    (r'Is (.*)?(CS|Comp(.*) Sci(.*)|major|minor|program|degree)(.*)?me\?',
    ( "If you enjoy CS, then you should declare CS!",
      "Take a few classes first and see how you enjoy it. You can also ask me for any class recommendations.",
      "If your CS-pset is the first thing you want to finish, you may be learning towards CS.",
      "I believe that CS is applicable to any field, you can mix and match it with any other program and create a new unique blend.",
      "There isn't a right answer for everything in life. Sometimes you have to take the plunge.")),
      
# Similar to the above question, it is aimed for people questioning if they should major/minor in cs?
    (r'Should I (.*)?(major|minor)(.*)?\?',
    ( "If you enjoy it, I don't see why not!",
      "For sure! It'll be a great learning experience and also a very popular industry.",
      "Yes! If you are still unsure, talk to Takis Metaxas. He is the department chair and is very sweet.",
      "If you enjoy your classes and feel like you can spend the next few years doing CS-related things, do it!",
      "Talk with someone in the field to learn more about it!")),

# How to suceed?
    (r'How (.*)?succeed(.*)?\?',
    ( "There are many resources in the CS department. There are tutors, help-room, office hours, and supplemental instruction!",
      "Focus in class and make sure to review after!",
      "Read the textbook before and after class to help reinforce ideas.",
      "Work with a friend to bounce ideas off each other. The best way to learn is to explain to someone else.",
      "Practice makes perfect! Don’t be afraid to make mistakes!")),

# What langauges are used (class-specific) 
    (r'What (.*)?language(.*)? (.*)? cs(.*)\?',
    ( "Visit https://www.wellesley.edu/cs/curriculum/coursewebsites to learn more.",
      "You can talk with any of the professors in the CS department to learn more.",
      "Many classes code in either Python or Java.",
      "It depends on the class but you can find out by looking at the course browser or talking to the professor.",
      "Course Catalog will answer your question.")),   
      
# What langauges are used (general)
    (r'What (.*)?language(.*)? (.*)?\?',
    ( "A wide variety of languages are taught!",
      "There is much to learn, starting with Python, Java, etc etc.",
      "Many CS classes teach in either Python or Java.",
      "Languages are based off which course it is and the type of coding they are doing. ",
      "The CS department teaches in Python, Java, C, and much more depending on th specific class.")),    

# What do you learn in CS?
    (r'What (.*)?(learn|teach|taught|curriculum|lecture(.*)?|lesson(.*)?|educat(.*)?)(.*)?\?', 
    ( "The CS departments aims to teach good programming skills such as DRY (don't repeat yourself) and documentation skills.",
      "The CS department hopes to build students' confidence in their coding ability.",
      "Students learn about various algorithms and data structures during their time at Wellesley.",
      "Students learn about a variety of topics from Artifical Intelligence to Computer Music to Computational Biology to Cybersecurity!",
      "The CS department hopes to expose students to different uses of CS to help them find their specific focus and interests.")),     

# COURSE-SPECIFIC
# Below are regexes of course specific questions.
# There appear to be much similarity between the regexes, yet a small variety could be seen in order to catch specific questions.
# There are the catch words, such as "major", "minor", etc.


# Major Courses
    (r'What (.*)?(course(.*)?|class(.*)?)(.*) major?\?',
    ( "Two introductory courses (CS111 and CS230), a mathematical foundation (MATH225) with an additional 200 level math, four core courses (CS231, CS235, CS240, and CS251) and three additional courses (two at 300 level, one at 200 or 300 level) are required.",
      "CS111 and CS230, MATH225, CS231, CS235, CS240, and CS251, three additional CS courses (two at 300 level, one at 200 or 300 level), and 1 addition 200 level math")),

# Minor courses
    (r'What (.*)?(course(.*)?|class(.*)?)(.*) minor?\?',
    ( "CS111, and CS230 are mandatory. CS231, CS235, or CS240. And two additional courses (one at either 200 or 300 level, and another at 300 level).",
      "CS111 and CS230. A choice between CS231, CS235, or CS240. And two additional courses (one at either 200 or 300 level, and another at 300 level).")),

# Prereqs?
    (r'(Which|What) (.*)?(course(.*)?|class(.*)?) (.*)?preq(.*)?\?',
    ( "You can visit courses.wellesley.edu to learn more.",
      "You can visit https://www.wellesley.edu/cs/curriculum/coursewebsites to learn more.",
      "You can talk with any of the professors in the CS department to learn more.",
      "The most important preqs are CS 111, CS 230, and MATH 225 for the major. Once you have taken those 3 classes, most other classes are available to take.",
      "If you have finished the introducary series of CS 111 and CS 230, you are set for most other CS classes. If you would like a class recommendation, please ask me to recommend.",
      "Many of the 200 and 300 level classes require CS 111 & CS 230. MATH 225 is a non-CS prereq for CS 231.")),
      
# What class to take next?
    (r'What (.*)?next(.*)?\?',
    ( "You should finish the core requirements first which vary depending if you are majoring or minoring.",
      "Look at the course catalog to see when classes are offered as not every class is offered every semester or year.",
      "If you are looking for a specific class to take next, you can ask me for a class recommendation.",
      "Ask me for a class recommendation if you are looking for a fun class you may not have heard of.",
      "You can talk with any of the professors in the CS department for more personalized help.")),

# Should I take ___ or _____? 
    (r'Should (.*)or(.*)\?', 
    ( "Please check https://www.wellesley.edu/cs/curriculum/coursewebsites to see when each class is offered.",
      "If you have not finished your core major requirements, please finish those first.",
      "Feel free to talk to Takis Metaxas (department chair) about possible course options. There are pros and cons to each class!",
      "How about neither and asking me for a random recommendation?",
      "Please feel free to reach out to anyone in the CS department!")),  
# Random Class recommendation
    (r'(.*)? recommend(.*)?', 
    ( "CS232 with Eni is great! It is a class on Artificial Intellgience.",
      "CS203 with Andy Davis is a new class introduced in Spring 2020. It is about Computer Music.",
      "CS220 with Catherine is a class on Human-Computer Interaction. If you like design, this is a class for you.",
      "CS342 (Computer Security and Privacy) is for those people with an interest in cybersecurity and privacy.",
      "CS305 is all about Machine Learning, taught by Brian Tjaden. It is mandatory credit-non and also fills the EC requirement.",
      "CS321 is taught by Jordan Tynes and is on Mixed and Augmented Reality. If you are into VR/AR, this is the class for you.",    
      "CS304 with Scott Anderson is a useful class as Databases with Web Interfaces is applicable to many real world web designs.",
      "CS234 with Eni is a class about Data, Analytics, and Visualization. There are so many meaningful patterns in our digital traces.",      
      "CS204 (Introduction to Front-End Web Development) is great if you would like to learn how to create websites.")),  
      
# What courses are there (general)?  
    (r'What (.*)?(course(.*)?|class(.*)?)(.*)?\?',
    ( "You can visit courses.wellesley.edu to learn more.",
      "You can visit https://www.wellesley.edu/cs/curriculum/coursewebsites to learn more.",
      "There are courses on Data Structures and Algorithms to Data Visualization and Machine Learning and Social Computing!",
      "The CS department covers a wide range of courses from Social Computing to Computational Biology to Human-Computer Interations to Computer Music.",
      "You can talk with any of the professors in the CS department to learn more.")),

# Which CS intro class?
    (r'(What|Which) (.*)?(first|intro(.*)?)(.*)?\?',
    ( "CS 111 is good choice overall. It is the first step in becoming a CS Major. ",
      "The two introductary courses are CS111 and CS115. CS111 is more hard CS whereas CS115 is a blend of humanities and CS.",
      "If you have a strong background in CS from high school, talk to Takis Metaxas about possibly taking CS230 as your first class.",
      "If you are looking to major in CS, I would recommend taking CS111 which is required for the major.")),                    

# DECLARING
# Below regex explain the process of declaring as CS major/minor.
# The responses are purposely left broad for those who want to ask how to find a advisor (as it is a bit special in CS' case).

# How to declare as CS major/minor?
    (r'How (.*)?(declare|advisor)(.*)?\?',
    ( "Ask Takis Metaxas for more information.",
      "You can visit the CS Department website for more information.",
      "There are posters in the E-wing of the Science Center with information on how to find a CS advisor.",
      "Declaring a CS major is a two step process that involves finding an advisor by submitting a google form then submitting the official application through MyWellesley.",
      "Submit a Google form requesting a CS advisor and visit MyWellesley to submit the major declaration form.")),   
                                       
# MISC                                                
# Once the user has input "quit" in order to quit the program,
    (r'quit',
    ( "Goodbye!",
      "It was nice talking to you!"
      "Have a good day. Talk to me soon.",
      "I'm glad that we got to chat. Goodbye!",
      "I hope I was able to answer some of your questions!")),

# The following are the fall through cases. There are 15 different responses that this chat bot could give.
# This regex will be triggered it questions asked by the user cannot caught with the regexes above.
    (r'(.*)',
    ( "What do you mean? Could you repeat?",
      "I don't think I am able to answer your question.",
      "Please talk to Takis Metaxas for more help beyond this point.",
      "Apologies. This is the cap of my knowledge.",
      "I'm not sure I got the question. Maybe ask again?",
      "Please repeat your question.",
      "Sorry! I don't think I know the answer to that question.",
      "I'm not sure about that one. Please ask me a new question!",
      "I apologize, I am unable to find answers to your question.",
      "Come again? I didn't quite get that.",
      "I'm sorry, but the answer to the question that you're trying to find cannot be answered. Please try again.",
      "Email the CS Department head for the answer to that question!",
      "Ooh. You got me there. I don't know the answer to that.",
      "Oops. I don't know the answer. Sorry!",
      "Sorry, I don't understand your question."))
)

WellesleyCS_chatbot = Chat(responses, reflections)

def WellesleyCS_chat():
    print('*'*75)
    print("WellesleyCS Chatbot!".center(75))
    print('*'*75)
    print('"Created by Christine Lam & Jisoo Kim"'.center(75))
    print("* Learn more about the CS Department with the WellesleyCS Chatbot.")
    print("* Talk to the program by typing in plain English, using normal upper-")
    print('* and lower-case letters and proper punctuation.')
    print("* Type 'quit' when you are finished.")
    print('*'*75)
    print("What questions do you have?")

    WellesleyCS_chatbot.converse()

def demo():
    WellesleyCS_chat()

if __name__ == "__main__":
    demo()
