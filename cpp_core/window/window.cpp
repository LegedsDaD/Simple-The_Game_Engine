#include "window.h"

#include <cstdio>
#include <stdexcept>

#include "platform/glfw.h"
#include "platform/window_hints.h"

namespace simple {

static void glfw_error_callback(int error, const char* description) {
  (void)error;
  if (description) std::fprintf(stderr, "[Simple][GLFW] %s\n", description);
}

Window::Window() {
  glfwSetErrorCallback(glfw_error_callback);
  if (!glfwInit()) throw std::runtime_error("Failed to initialize GLFW");
}

Window::~Window() {
  destroy();
  glfwTerminate();
}

void Window::create(int width, int height, const std::string& title) {
  if (window_) return;

  platform::apply_glfw_window_hints();

  window_ = glfwCreateWindow(width, height, title.c_str(), nullptr, nullptr);
  if (!window_) throw std::runtime_error("Failed to create GLFW window");

  glfwMakeContextCurrent(window_);
  glfwSwapInterval(1);
}

void Window::destroy() {
  if (!window_) return;
  glfwDestroyWindow(window_);
  window_ = nullptr;
}

void Window::poll_events() { glfwPollEvents(); }

void Window::swap_buffers() {
  if (!window_) return;
  glfwSwapBuffers(window_);
}

bool Window::should_close() const { return window_ ? glfwWindowShouldClose(window_) != 0 : true; }

void Window::request_close() {
  if (window_) glfwSetWindowShouldClose(window_, GLFW_TRUE);
}

void Window::get_framebuffer_size(int& w, int& h) const {
  if (!window_) {
    w = 0;
    h = 0;
    return;
  }
  glfwGetFramebufferSize(window_, &w, &h);
}

}  // namespace simple
