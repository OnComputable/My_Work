from flask import Flask, request, jsonify
import pickle as cpickle  #cPickle was from python2
import copy
import math
import itertools
import os
import sys

sys.path.append(os.getcwd())
