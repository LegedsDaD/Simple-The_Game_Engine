#include "engine.h"

#include <chrono>
#include <iostream>
#include <stdexcept>

#include "platform/glfw.h"

#include "../branding/branding.h"
#include "../input/input.h"
#include "../renderer/renderer.h"
#include "../scene/scene.h"
#include "../window/window.h"

namespace simple {

Engine::Engine() = default;
Engine::~Engine() = default;

bool Engine::input_key_down(int key) { return Input::key_down(key); }
bool Engine::input_key_pressed(int key) { return Input::key_pressed(key); }
bool Engine::input_mouse_down(int button) { return Input::mouse_down(button); }
bool Engine::input_mouse_pressed(int button) { return Input::mouse_pressed(button); }
void Engine::input_mouse_position(double& x, double& y) { Input::mouse_position(x, y); }
void Engine::input_mouse_delta(double& dx, double& dy) { Input::mouse_delta(dx, dy); }

void Engine::run(Scene& scene, int width, int height, const std::string& title) {
  std::cout << "Running on Simple Engine" << std::endl;

  Window window;
  window.create(width, height, title);

  Input::attach(window.handle());

  Renderer renderer;
  renderer.initialize(window.handle());

  Branding branding;
  branding.initialize();

  auto last = std::chrono::steady_clock::now();

  while (!window.should_close()) {
    const auto now = std::chrono::steady_clock::now();
    float dt = std::chrono::duration_cast<std::chrono::duration<float>>(now - last).count();
    if (dt > 0.1f) dt = 0.1f;
    last = now;

    Input::new_frame();
    window.poll_events();

    scene.begin_frame(dt);

    if (Input::key_pressed(GLFW_KEY_ESCAPE)) window.request_close();

    for (auto& e : scene.entities()) {
      if (e) e->update(dt);
    }

    scene.tick_update_callback(dt);

    int fb_w = 0, fb_h = 0;
    window.get_framebuffer_size(fb_w, fb_h);
    renderer.begin_frame(fb_w, fb_h);
    renderer.draw_scene(scene);
    renderer.draw_debug_lines(scene);

    renderer.draw_hud(scene, fb_w, fb_h);

    if (scene.branding_enabled()) branding.draw_overlay(fb_w, fb_h);

    if (!scene.screenshot_path().empty()) {
      renderer.capture_screenshot_ppm(scene.screenshot_path().c_str(), fb_w, fb_h);
      scene.clear_screenshot_request();
    }

    window.swap_buffers();
  }

  Input::detach(window.handle());
}

}  // namespace simple
