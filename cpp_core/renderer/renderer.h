#pragma once

#include <cstddef>
#include <cstdint>
#include <string>
#include <unordered_map>

#include "platform/gl_loader.h"

struct GLFWwindow;

namespace simple {

class Scene;

class Renderer {
 public:
  Renderer();
  ~Renderer();

  void initialize(GLFWwindow* window);
  void begin_frame(int framebuffer_w, int framebuffer_h);
  void draw_scene(const Scene& scene);
  void draw_hud(const Scene& scene, int framebuffer_w, int framebuffer_h);
  void draw_debug_lines(const Scene& scene);
  bool capture_screenshot_ppm(const char* path, int framebuffer_w, int framebuffer_h);

  void ui_begin(int framebuffer_w, int framebuffer_h);
  void ui_draw_triangles_2d(const float* xy, int vertex_count);
  void ui_end();

 private:
  void create_cube_resources();
  void ensure_ui_pipeline();
  void ensure_line_pipeline();
  void destroy_resources();

  GLFWwindow* window_{nullptr};

  unsigned int cube_vao_{0};
  unsigned int cube_vbo_{0};

  unsigned int ui_vao_{0};
  unsigned int ui_vbo_{0};

  unsigned int line_vao_{0};
  unsigned int line_vbo_{0};

  unsigned int cube_program_{0};
  unsigned int ui_program_{0};
  unsigned int default_texture_{0};
  unsigned int line_program_{0};

  int u_cube_mvp_{-1};
  int u_cube_model_{-1};
  int u_cube_color_{-1};
  int u_cube_light_dir_{-1};
  int u_cube_cam_pos_{-1};
  int u_cube_use_tex_{-1};
  int u_cube_tex_{-1};

  int u_ui_resolution_{-1};
  int u_ui_color_{-1};

  int u_line_viewproj_{-1};

  unsigned int get_or_create_texture(const char* path);
  std::unordered_map<std::string, unsigned int> texture_cache_{};
};

}  // namespace simple
