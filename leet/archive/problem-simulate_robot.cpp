/*
  A robot starts at x=0;y=0 with heading facing North and takes a 1-D input of commands z such that:
  if z[i]=-2: The robot is commanded to turn left by PI/2
  if z[i]=-1: The robot is commanded to turn right by PI/2
  if z[i]>=0: The robot is commanded to move z[i] units along the current heading

  Your objective is to write a function that does the following:
  1. Process the commands and output the final position {x_final, y_final}
  2. Process the commands and output the maximum distance and its coordinates in the trajectory from the start point.

  Example-1:
  Input: {1, 2, 3, -2, 4}
  Outputs: Final position={-4, 6}; Max distance: sqrt(52) @ {-4, 6}

  Example-2:
  Input: {5, -2, 3, -1, 4, -1, 6, -1, 2}
  Outputs: Final position={3, 7}; Max distance: sqrt(90) @ {-3, 9}
*/

#include <math.h>
#include <iostream>
#include <vector>

// R = [cos(theta), -sin(theta),
//      sin(theta), cos(theta)]

// p_world
// v_robot = [input, 0]
// p_world += R_world_robot * v_robot * dt
// p_world += R_world_robot * p_robot (input, 0)

class Robot {
private:
  double yaw_ = 0.0; // North
  std::vector<int> position_;
  double max_dist_ = 0.0;

public:
  Robot() : position_{0, 0} {}

  void processInputs(const std::vector<int> inputs) {
    for (const auto input : inputs) {
      if (input == -2) {
        yaw_ += M_PI / 2.0;
      } else if (input == -1) {
        yaw_ -= M_PI / 2.0;
      } else {
        // p += R (2x2) * [input, 0]

        // Fix wrap around bug
        if (yaw_ > M_PI) {
          yaw_ -= M_PI;
        } else if (yaw_ < -M_PI) {
          yaw_ += M_PI;
        }

        // Advance
        position_[0] += (cos(yaw_) * input);
        position_[1] += (-sin(yaw_) * input);

        double dist = sqrt(pow(position_[0], 2) + pow(position_[1], 2));
        max_dist_ = std::max(max_dist_, dist);
      }
    }
  }

  void printWorldPosition() const {
    printf("(%d, %d)\n", position_[1], position_[0]);
  }

  void printMaxEuclideanDist() const {
    // double dist = sqrt(pow(position_[0], 2) + pow(position_[1], 2));
    // printf("%f\n", dist);
    printf("%f\n", max_dist_);
  }


};

int main() {
  {
    std::vector<int> inputs = {1, 2, 3, -2, 4};
    auto robot = Robot();
    robot.processInputs(inputs);
    robot.printWorldPosition();
    robot.printMaxEuclideanDist();
  }

  {
    std::vector<int> inputs = {5, -2, 3, -1, 4, -1, 6, -1, 2};
    auto robot = Robot();
    robot.processInputs(inputs);
    robot.printWorldPosition();
    robot.printMaxEuclideanDist();
  }

  return 0;
}
