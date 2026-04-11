#pragma once

#include <string>

struct GLFWwindow;

namespace simple {

class Window {
 public:
  Window();
  ~Window();

  Window(const Window&) = delete;
  Window& operator=(const Window&) = delete;
  Window(Window&&) = delete;
  Window& operator=(Window&&) = delete;

  void create(int width, int height, const std::string& title);
  void destroy();

  void poll_events();
  void swap_buffers();
  bool should_close() const;
  void request_close();

  void get_framebuffer_size(int& w, int& h) const;
  GLFWwindow* handle() const { return window_; }

 private:
  GLFWwindow* window_{nullptr};
};

}  // namespace simple

