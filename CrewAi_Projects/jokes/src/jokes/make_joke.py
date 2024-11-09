#!/usr/bin/env python
#from crew import JokesCrew
from CrewAi_Projects.jokes.src.jokes.crew import JokesCrew

# This  main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def createJoke(topic):
    """
    Run the crew.
    """
    inputs = {
        'topic': topic
    }
    return JokesCrew().crew().kickoff(inputs=inputs)