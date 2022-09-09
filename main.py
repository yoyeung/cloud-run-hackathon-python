
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    data = request.json
    myselfDomain = data["_links"]["self"]["href"]
    arena = data["arena"]
    dims = arena["dims"]
    state = arena["state"]
    me = state[myselfDomain]
    del state[myselfDomain]
    closest = {distance : 100}
    for playerName in state:
        x, y = state[playerName]
        if me.x == x: # same row
            if closest.distance > abs(me.y - y):
                closest = { x: x, y: y, distance: abs(me.y - y)}
        if me.y == y: # same column
            if closest.distance > abs(me.x - x):
                closest = { x: x, y: y, distance: abs(me.x - x)}
             
    if me.x < closest.x: # on my right hand
    if me.x > closest.x # on my left hand
    if me.y < closest.y #behind me
    if me.y < closest.y # front of me
    
    
#   next = ['L','R','F'][random.randrange(3)]
    logger.info(f'right now x:{myselfData["x"]}, y:{myselfData["y"]}, next:{next}')
#     return next
    # TODO add your implementation here to replace the random response
    
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
