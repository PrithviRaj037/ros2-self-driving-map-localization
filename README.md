# ROS 2 Self-Driving Robot: Map & Localization

This repository documents my step-by-step learning progress from the Udemy course **Self Driving and ROS 2 - Learn by Doing! Map & Localization**.

The goal of this project is to build practical knowledge in ROS 2 for mobile robotics, self-driving robot software, mapping, localization, SLAM, and autonomous navigation.

## Project Overview

This project follows a hands-on learning approach. Each concept is implemented, tested, documented, and pushed gradually as I progress through the course.

The repository starts with basic ROS 2 concepts such as nodes, publishers, subscribers, topics, and timers. These fundamentals are later extended toward self-driving robot applications such as robot description, simulation, sensor processing, mapping, localization, and navigation.

## Learning Goals

- Understand ROS 2 workspace and package structure
- Create ROS 2 nodes using Python and C++
- Use publishers and subscribers for topic-based communication
- Work with ROS 2 command-line tools
- Understand robot description using URDF/Xacro
- Simulate a mobile robot
- Work with sensors such as LiDAR and odometry
- Understand mapping and occupancy grids
- Learn robot localization in a known map
- Study SLAM concepts
- Build a foundation for autonomous navigation

## Current Progress

### Step 1: Simple ROS 2 Publisher

Implemented a simple ROS 2 publisher node in Python.

The node publishes `std_msgs/String` messages to the `/chatter` topic using a timer callback.

This helped me understand the basic ROS 2 communication flow:

```text
Node → Publisher → Topic → Subscriber
