#pragma once

struct GLFWwindow;

namespace simple {

class Input {
 public:
  static void attach(GLFWwindow* window);
  static void detach(GLFWwindow* window);

  static void new_frame();

  static bool key_down(int key);
  static bool key_pressed(int key);
  static bool mouse_down(int button);
  static bool mouse_pressed(int button);

  static void mouse_position(double& x, double& y);
  static void mouse_delta(double& dx, double& dy);
};

}  // namespace simple

