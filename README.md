# ROS Basics
## ROS Melodic Installation
> Alternatively you can follow [this link](http://wiki.ros.org/melodic/Installation/Ubuntu)
#### 1. Setup sources, list
`$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`
#### 2. Setup your keys
`sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654`
#### 3. Update debian package
`sudo apt update`
#### 4. Install desktop full version of ROS
`sudo apt install ros-melodic-desktop-full`
#### 5. Environment Setup
`echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc`
`source ~/.bashrc`
#### 6. Install Dependencies
`sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential`
#### 7. Initialize rosdep
`sudo apt install python-rosdep`
`sudo rosdep init`
`rosdep update`
### Load the environment file
`source /opt/ros/melodic/setup.bash`
## Turtlebot Package Installation
> Alternatively you can follow [this link](https://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/)
### Remote PC
- `$ cd ~/catkin_ws/src/`
- `$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git`
- `$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git`
- `$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git`
- `$ cd ~/catkin_ws && catkin_make`
#### Install more packages
- `$ sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan ros-melodic-rosserial-arduino ros-melodic-rosserial-python ros-melodic-rosserial-server ros-melodic-rosserial-client ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro ros-melodic-compressed-image-transport ros-melodic-rqt-image-view ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers`

### Turtlebot PC
- `$ cd ~/catkin_ws/src`
- `$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git`
- `$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git`
- `$ git clone https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git`
- `$ cd ~/catkin_ws && catkin_make`

### Time sync in both TurtleBot and Remote PC
- `$ sudo apt-get install ntpdate`
- `$ sudo ntpdate ntp.ubuntu.com`
