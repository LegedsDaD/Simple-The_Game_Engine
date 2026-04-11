#include "input.h"

#include <array>
#include <algorithm>

#include "platform/glfw.h"

namespace simple {

static std::array<unsigned char, GLFW_KEY_LAST + 1> g_key_down{};
static std::array<unsigned char, GLFW_KEY_LAST + 1> g_key_pressed{};

static std::array<unsigned char, GLFW_MOUSE_BUTTON_LAST + 1> g_mouse_down{};
static std::array<unsigned char, GLFW_MOUSE_BUTTON_LAST + 1> g_mouse_pressed{};

static double g_mouse_x = 0.0;
static double g_mouse_y = 0.0;
static double g_mouse_dx = 0.0;
static double g_mouse_dy = 0.0;

static void key_callback(GLFWwindow*, int key, int, int action, int) {
  if (key < 0 || key > GLFW_KEY_LAST) return;
  if (action == GLFW_PRESS) {
    g_key_down[(size_t)key] = 1;
    g_key_pressed[(size_t)key] = 1;
  } else if (action == GLFW_RELEASE) {
    g_key_down[(size_t)key] = 0;
  }
}

static void mouse_button_callback(GLFWwindow*, int button, int action, int) {
  if (button < 0 || button > GLFW_MOUSE_BUTTON_LAST) return;
  if (action == GLFW_PRESS) {
    g_mouse_down[(size_t)button] = 1;
    g_mouse_pressed[(size_t)button] = 1;
  } else if (action == GLFW_RELEASE) {
    g_mouse_down[(size_t)button] = 0;
  }
}

static void cursor_pos_callback(GLFWwindow*, double x, double y) {
  g_mouse_dx += (x - g_mouse_x);
  g_mouse_dy += (y - g_mouse_y);
  g_mouse_x = x;
  g_mouse_y = y;
}

void Input::attach(GLFWwindow* window) {
  std::fill(g_key_down.begin(), g_key_down.end(), 0);
  std::fill(g_key_pressed.begin(), g_key_pressed.end(), 0);
  std::fill(g_mouse_down.begin(), g_mouse_down.end(), 0);
  std::fill(g_mouse_pressed.begin(), g_mouse_pressed.end(), 0);

  g_mouse_x = g_mouse_y = 0.0;
  g_mouse_dx = g_mouse_dy = 0.0;

  glfwSetKeyCallback(window, key_callback);
  glfwSetMouseButtonCallback(window, mouse_button_callback);
  glfwSetCursorPosCallback(window, cursor_pos_callback);
  glfwGetCursorPos(window, &g_mouse_x, &g_mouse_y);
}

void Input::detach(GLFWwindow* window) {
  if (!window) return;
  glfwSetKeyCallback(window, nullptr);
  glfwSetMouseButtonCallback(window, nullptr);
  glfwSetCursorPosCallback(window, nullptr);
}

void Input::new_frame() {
  std::fill(g_key_pressed.begin(), g_key_pressed.end(), 0);
  std::fill(g_mouse_pressed.begin(), g_mouse_pressed.end(), 0);
  g_mouse_dx = 0.0;
  g_mouse_dy = 0.0;
}

bool Input::key_down(int key) {
  if (key < 0 || key > GLFW_KEY_LAST) return false;
  return g_key_down[(size_t)key] != 0;
}

bool Input::key_pressed(int key) {
  if (key < 0 || key > GLFW_KEY_LAST) return false;
  return g_key_pressed[(size_t)key] != 0;
}

bool Input::mouse_down(int button) {
  if (button < 0 || button > GLFW_MOUSE_BUTTON_LAST) return false;
  return g_mouse_down[(size_t)button] != 0;
}

bool Input::mouse_pressed(int button) {
  if (button < 0 || button > GLFW_MOUSE_BUTTON_LAST) return false;
  return g_mouse_pressed[(size_t)button] != 0;
}

void Input::mouse_position(double& x, double& y) {
  x = g_mouse_x;
  y = g_mouse_y;
}

void Input::mouse_delta(double& dx, double& dy) {
  dx = g_mouse_dx;
  dy = g_mouse_dy;
}

}  // namespace simple
