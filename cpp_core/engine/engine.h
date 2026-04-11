#pragma once

#include <string>

namespace simple {

class Scene;

class Engine {
 public:
  Engine();
  ~Engine();

  Engine(const Engine&) = delete;
  Engine& operator=(const Engine&) = delete;
  Engine(Engine&&) = delete;
  Engine& operator=(Engine&&) = delete;

  void run(Scene& scene, int width, int height, const std::string& title);

  // Scene-level input bridge.
  static bool input_key_down(int key);
  static bool input_key_pressed(int key);
  static bool input_mouse_down(int button);
  static bool input_mouse_pressed(int button);
  static void input_mouse_position(double& x, double& y);
  static void input_mouse_delta(double& dx, double& dy);
};

}  // namespace simple

