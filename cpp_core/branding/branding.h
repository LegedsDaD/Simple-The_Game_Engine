#pragma once

namespace simple {

// Responsible for drawing the "Made with Simple" on-screen overlay.
class Branding {
 public:
  Branding();
  ~Branding();

  Branding(const Branding&) = delete;
  Branding& operator=(const Branding&) = delete;

  void initialize();
  void draw_overlay(int framebuffer_w, int framebuffer_h);

 private:
  bool initialized_{false};
  float* vertices_{nullptr};  // flat (x,y) list
  int vertex_count_{0};
  int capacity_floats_{0};

  void build_text_mesh();
};

}  // namespace simple

