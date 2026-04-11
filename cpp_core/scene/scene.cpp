#include "scene.h"

#include <algorithm>
#include <stdexcept>

#include "platform/glfw.h"

#include "../engine/engine.h"

namespace simple {

Scene::Scene() {
  camera_.transform.position = {0.0f, 0.0f, 3.5f};
}

Scene::~Scene() = default;

void Scene::add(const std::shared_ptr<Entity>& entity) {
  if (!entity) return;
  entities_.push_back(entity);
}

void Scene::remove(const std::shared_ptr<Entity>& entity) {
  entities_.erase(std::remove(entities_.begin(), entities_.end(), entity), entities_.end());
}

void Scene::clear() { entities_.clear(); }

void Scene::disable_branding() { branding_enabled_ = false; }

void Scene::draw_text(const std::string& text, float x_px, float y_px, float scale, const simple::math::Vec3& color) {
  if (text.empty()) return;
  hud_text_.push_back(TextCommand{text, x_px, y_px, scale, color});
}

void Scene::draw_line3d(const simple::math::Vec3& a, const simple::math::Vec3& b, const simple::math::Vec3& color) {
  debug_lines_.push_back(LineCommand{a, b, color});
}

void Scene::request_screenshot(const std::string& path) { screenshot_path_ = path; }

void Scene::set_title(const std::string& title) {
  GLFWwindow* win = glfwGetCurrentContext();
  if (!win) return;
  glfwSetWindowTitle(win, title.c_str());
}

void Scene::set_vsync(bool enabled) { glfwSwapInterval(enabled ? 1 : 0); }

void Scene::set_update_callback(std::function<void(float)> cb) { update_callback_ = std::move(cb); }

void Scene::tick_update_callback(float dt) const {
  if (update_callback_) update_callback_(dt);
}

void Scene::begin_frame(float dt) {
  frame_index_++;
  time_seconds_ += (double)dt;
  if (dt > 1e-6f) {
    const float inst = 1.0f / dt;
    fps_ = (fps_ <= 0.0f) ? inst : (fps_ * 0.90f + inst * 0.10f);
  }
  hud_text_.clear();
  debug_lines_.clear();
}

void Scene::run(int width, int height, const char* title) {
  if (running_) throw std::runtime_error("Scene is already running");
  running_ = true;
  try {
    Engine engine;
    engine.run(*this, width, height, title ? title : "Simple");
  } catch (...) {
    running_ = false;
    throw;
  }
  running_ = false;
}

bool Scene::key_down(int key) const { return Engine::input_key_down(key); }
bool Scene::key_pressed(int key) const { return Engine::input_key_pressed(key); }
bool Scene::mouse_down(int button) const { return Engine::input_mouse_down(button); }
bool Scene::mouse_pressed(int button) const { return Engine::input_mouse_pressed(button); }
void Scene::mouse_position(double& x, double& y) const { Engine::input_mouse_position(x, y); }
void Scene::mouse_delta(double& dx, double& dy) const { Engine::input_mouse_delta(dx, dy); }

}  // namespace simple
