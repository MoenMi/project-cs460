#!/bin/bash

rm -rf install build
colcon build
source install/setup.bash

export WORLD_FILE="maze1_smallest.wbt"
ros2 launch project_cs460 robot_launch.py world:=$WORLD_FILE