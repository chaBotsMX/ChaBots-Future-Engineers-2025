#!/bin/bash
set -e

# Setup ROS environment
source /opt/ros/humble/setup.bash

# Build the workspace
if [ -f /ros2_ws/src/CMakeLists.txt ]; then
    cd /ros2_ws
    colcon build
    source install/setup.bash
fi

exec "$@"
