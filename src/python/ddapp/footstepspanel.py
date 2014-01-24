import PythonQt
from PythonQt import QtCore, QtGui
from ddapp import lcmUtils
from ddapp import applogic as app
from ddapp.utime import getUtime
from ddapp import objectmodel as om
from ddapp.timercallback import TimerCallback
from ddapp import footsteps

import numpy as np
import math


def _makeButton(text, func):

    b = QtGui.QPushButton(text)
    b.connect('clicked()', func)
    return b


def getVisibleRobotModel():
    for obj in om.objects.values():
        if isinstance(obj, om.RobotModelItem) and obj.getProperty('Visible'):
            return obj


class FootstepsPanel(object):

    def __init__(self):

        self.widget = QtGui.QWidget()
        self.widget.setWindowTitle('Footsteps Panel')

        l = QtGui.QVBoxLayout(self.widget)

        l.addWidget(_makeButton('new walking goal', self.onNewWalkingGoal))
        l.addWidget(QtGui.QLabel(''))
        l.addWidget(_makeButton('execute footstep plan', self.onExecute))
        l.addWidget(QtGui.QLabel(''))
        l.addWidget(_makeButton('stop walking', self.onStop))
        l.addStretch()

    def onNewWalkingGoal(self):
        model = getVisibleRobotModel()
        footsteps.createWalkingGoal(model)

    def onExecute(self):
        footsteps.commitFootstepPlan()

    def onStop(self):
        footsteps.sendStopWalking()


def init():

    global panel
    global dock

    panel = FootstepsPanel()
    dock = app.addWidgetToDock(panel.widget)
    #dock.hide()

    return panel
