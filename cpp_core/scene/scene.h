#pragma once

#include <functional>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "entity.h"

namespace simple {

struct Camera {
  simple::math::Transform transform{};
  float fov_degrees{60.0f};
  float z_near{0.1f};
  float z_far{100.0f};
};

class Scene {
 public:
  Scene();
  ~Scene();

  void add(const std::shared_ptr<Entity>& entity);
  void remove(const std::shared_ptr<Entity>& entity);
  void clear();

  const std::vector<std::shared_ptr<Entity>>& entities() const { return entities_; }

  Camera& camera() { return camera_; }
  const Camera& camera() const { return camera_; }

  void disable_branding();
  bool branding_enabled() const { return branding_enabled_; }

  void set_background_color(const simple::math::Vec3& rgb) { background_color_ = rgb; }
  const simple::math::Vec3& background_color() const { return background_color_; }

  // Frame timing (updated by the engine while running).
  double time_seconds() const { return time_seconds_; }
  float fps() const { return fps_; }
  std::uint64_t frame_index() const { return frame_index_; }

  // HUD text: queue draw commands from Python (typically inside on_update callback).
  struct TextCommand {
    std::string text;
    float x_px{0};
    float y_px{0};
    float scale{1.0f};
    simple::math::Vec3 color{1.0f, 1.0f, 1.0f};
  };

  void draw_text(const std::string& text, float x_px, float y_px, float scale = 1.0f,
                 const simple::math::Vec3& color = {1.0f, 1.0f, 1.0f});
  const std::vector<TextCommand>& hud_text() const { return hud_text_; }

  // 3D debug lines ("gizmos"): queue per-frame line segments in world space.
  struct LineCommand {
    simple::math::Vec3 a{};
    simple::math::Vec3 b{};
    simple::math::Vec3 color{1.0f, 1.0f, 1.0f};
  };
  void draw_line3d(const simple::math::Vec3& a, const simple::math::Vec3& b,
                   const simple::math::Vec3& color = {1.0f, 1.0f, 1.0f});
  const std::vector<LineCommand>& debug_lines() const { return debug_lines_; }

  // Screenshot capture: saves the current frame to a PPM file when requested.
  void request_screenshot(const std::string& path);
  const std::string& screenshot_path() const { return screenshot_path_; }
  void clear_screenshot_request() { screenshot_path_.clear(); }

  // Runtime window control (valid while running).
  void set_title(const std::string& title);
  void set_vsync(bool enabled);

  // Called every frame before rendering.
  void set_update_callback(std::function<void(float)> cb);
  void tick_update_callback(float dt) const;

  // Called by Engine once per frame.
  void begin_frame(float dt);

  void run(int width = 900, int height = 600, const char* title = "Simple");

  // Input helpers (valid while running).
  bool key_down(int key) const;
  bool key_pressed(int key) const;
  bool mouse_down(int button) const;
  bool mouse_pressed(int button) const;
  void mouse_position(double& x, double& y) const;
  void mouse_delta(double& dx, double& dy) const;

 private:
  std::vector<std::shared_ptr<Entity>> entities_{};
  Camera camera_{};
  bool branding_enabled_{true};
  simple::math::Vec3 background_color_{0.06f, 0.06f, 0.08f};
  double time_seconds_{0.0};
  float fps_{0.0f};
  std::uint64_t frame_index_{0};
  std::vector<TextCommand> hud_text_{};
  std::vector<LineCommand> debug_lines_{};
  std::string screenshot_path_{};
  std::function<void(float)> update_callback_{};
  bool running_{false};
};

}  // namespace simple
