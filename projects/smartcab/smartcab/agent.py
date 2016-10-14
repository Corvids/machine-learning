import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import numpy as np

"""
to run code:
python smartcab/agent.py
python -m smartcab.agent

"""

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        self.next_waypoint = None
        self.sum_reward = 0

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.state = None
        self.sum_reward = 0
        self.next_waypoint = None

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        action =  np.random.choice((None, 'forward', 'left', 'right'))

        # TODO: Update state
        self.state = (inputs, self.next_waypoint)

        # TODO: Select action according to your policy
        action = self.next_waypoint
        motion = False

        if self.next_waypoint == 'forward':
            if inputs['light'] == 'green':
                motion = True
        elif self.next_waypoint == 'left':
            if inputs['light'] == 'green' and inputs['oncoming'] != 'forward':
                motion = True
        elif self.next_waypoint == 'right':
            if inputs['light'] == 'red' and inputs['oncoming'] != 'left' or inputs['left'] != 'forward':
                motion = True
        else:
            motion = False
            action = None

        # Execute action and get reward
        reward = self.env.act(self, action)
        self.sum_reward += reward

        # TODO: Learn policy based on state, action, reward

        print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.5, display=True)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=10)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
