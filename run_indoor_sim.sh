#!/bin/bash

colcon build
source install/setup.bash

export WORLD_FILE="bruno-business-library.wbt"
ros2 launch project_cs460 robot_launch.py world:=$WORLD_FILE