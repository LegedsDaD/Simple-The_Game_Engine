#include "renderer.h"

#include <stdexcept>
#include <string>
#include <vector>
#include <fstream>

#include "platform/glfw.h"

#include "../math/transform.h"
#include "../renderer/texture.h"
#include "stb_easy_font.h"
#include "../scene/entity.h"
#include "../scene/scene.h"

namespace simple {

static unsigned int compile_shader(gl::GLenum type, const char* src) {
  unsigned int sh = gl::CreateShader(type);
  gl::ShaderSource(sh, 1, &src, nullptr);
  gl::CompileShader(sh);
  gl::GLint ok = 0;
  gl::GetShaderiv(sh, gl::GL_COMPILE_STATUS_, &ok);
  if (!ok) {
    gl::GLint len = 0;
    gl::GetShaderiv(sh, gl::GL_INFO_LOG_LENGTH_, &len);
    std::string log;
    log.resize(len > 1 ? (size_t)len : 1u);
    gl::GLsizei out_len = 0;
    gl::GetShaderInfoLog(sh, (gl::GLsizei)log.size(), &out_len, log.data());
    gl::DeleteShader(sh);
    throw std::runtime_error("Shader compile failed: " + log);
  }
  return sh;
}

static unsigned int link_program(unsigned int vs, unsigned int fs) {
  unsigned int prog = gl::CreateProgram();
  gl::AttachShader(prog, vs);
  gl::AttachShader(prog, fs);
  gl::LinkProgram(prog);
  gl::GLint ok = 0;
  gl::GetProgramiv(prog, gl::GL_LINK_STATUS_, &ok);
  if (!ok) {
    gl::GLint len = 0;
    gl::GetProgramiv(prog, gl::GL_INFO_LOG_LENGTH_, &len);
    std::string log;
    log.resize(len > 1 ? (size_t)len : 1u);
    gl::GLsizei out_len = 0;
    gl::GetProgramInfoLog(prog, (gl::GLsizei)log.size(), &out_len, log.data());
    gl::DeleteProgram(prog);
    throw std::runtime_error("Program link failed: " + log);
  }
  gl::DeleteShader(vs);
  gl::DeleteShader(fs);
  return prog;
}

Renderer::Renderer() = default;

Renderer::~Renderer() { destroy_resources(); }

void Renderer::initialize(GLFWwindow* window) {
  window_ = window;
  if (!window_) throw std::runtime_error("Renderer requires a valid GLFW window/context");
  glfwSetWindowUserPointer(window_, this);

  if (!gl::load((void* (*)(const char*))glfwGetProcAddress)) {
    throw std::runtime_error("OpenGL loader failed (glfwGetProcAddress returned nulls)");
  }

  gl::Enable(gl::GL_DEPTH_TEST_);
  gl::DepthFunc(gl::GL_LESS_);
  gl::Enable(gl::GL_CULL_FACE_);
  gl::CullFace(gl::GL_BACK_);

  create_cube_resources();

  // Default checker texture.
  const ImageData checker = make_checker(128, 128, 16);
  gl::GenTextures(1, &default_texture_);
  gl::BindTexture(gl::GL_TEXTURE_2D_, default_texture_);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_MIN_FILTER_, (int)gl::GL_LINEAR_MIPMAP_LINEAR_);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_MAG_FILTER_, (int)gl::GL_LINEAR_);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_WRAP_S_, (int)gl::GL_REPEAT_);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_WRAP_T_, (int)gl::GL_REPEAT_);
  gl::TexImage2D(gl::GL_TEXTURE_2D_, 0, (int)gl::GL_RGB_, checker.width, checker.height, 0, gl::GL_RGB_,
                 gl::GL_UNSIGNED_BYTE_, checker.pixels.data());
  gl::GenerateMipmap(gl::GL_TEXTURE_2D_);
  gl::BindTexture(gl::GL_TEXTURE_2D_, 0);
}

void Renderer::begin_frame(int framebuffer_w, int framebuffer_h) {
  gl::Viewport(0, 0, framebuffer_w, framebuffer_h);
}

void Renderer::create_cube_resources() {
  // Interleaved position (3), normal (3), uv (2).
  static const float cube_vertices[] = {
      // +X
      0.5f, -0.5f, -0.5f, 1, 0, 0,  0, 0,  0.5f, 0.5f,  -0.5f, 1, 0, 0,  1, 0,
      0.5f, 0.5f,  0.5f,  1, 0, 0,  1, 1,  0.5f, -0.5f, -0.5f, 1, 0, 0,  0, 0,
      0.5f, 0.5f,  0.5f,  1, 0, 0,  1, 1,  0.5f, -0.5f, 0.5f,  1, 0, 0,  0, 1,
      // -X
      -0.5f, -0.5f, 0.5f, -1, 0, 0,  0, 1,  -0.5f, 0.5f,  0.5f, -1, 0, 0,  1, 1,
      -0.5f, 0.5f,  -0.5f, -1, 0, 0,  1, 0,  -0.5f, -0.5f, 0.5f, -1, 0, 0,  0, 1,
      -0.5f, 0.5f,  -0.5f, -1, 0, 0,  1, 0,  -0.5f, -0.5f, -0.5f, -1, 0, 0,  0, 0,
      // +Y
      -0.5f, 0.5f, -0.5f, 0, 1, 0,  0, 0,  -0.5f, 0.5f,  0.5f, 0, 1, 0,  0, 1,
      0.5f,  0.5f,  0.5f,  0, 1, 0,  1, 1,  -0.5f, 0.5f, -0.5f, 0, 1, 0,  0, 0,
      0.5f,  0.5f,  0.5f,  0, 1, 0,  1, 1,  0.5f, 0.5f,  -0.5f, 0, 1, 0,  1, 0,
      // -Y
      -0.5f, -0.5f, 0.5f, 0, -1, 0,  0, 1,  -0.5f, -0.5f, -0.5f, 0, -1, 0,  0, 0,
      0.5f,  -0.5f, -0.5f, 0, -1, 0,  1, 0,  -0.5f, -0.5f, 0.5f, 0, -1, 0,  0, 1,
      0.5f,  -0.5f, -0.5f, 0, -1, 0,  1, 0,  0.5f, -0.5f, 0.5f,  0, -1, 0,  1, 1,
      // +Z
      -0.5f, -0.5f, 0.5f, 0, 0, 1,  0, 0,  0.5f,  -0.5f, 0.5f, 0, 0, 1,  1, 0,
      0.5f,  0.5f,  0.5f, 0, 0, 1,  1, 1,  -0.5f, -0.5f, 0.5f, 0, 0, 1,  0, 0,
      0.5f,  0.5f,  0.5f, 0, 0, 1,  1, 1,  -0.5f, 0.5f,  0.5f, 0, 0, 1,  0, 1,
      // -Z
      0.5f,  -0.5f, -0.5f, 0, 0, -1,  0, 0,  -0.5f, -0.5f, -0.5f, 0, 0, -1,  1, 0,
      -0.5f, 0.5f,  -0.5f, 0, 0, -1,  1, 1,  0.5f,  -0.5f, -0.5f, 0, 0, -1,  0, 0,
      -0.5f, 0.5f,  -0.5f, 0, 0, -1,  1, 1,  0.5f,  0.5f,  -0.5f, 0, 0, -1,  0, 1,
  };

  gl::GenVertexArrays(1, &cube_vao_);
  gl::BindVertexArray(cube_vao_);

  gl::GenBuffers(1, &cube_vbo_);
  gl::BindBuffer(gl::GL_ARRAY_BUFFER_, cube_vbo_);
  gl::BufferData(gl::GL_ARRAY_BUFFER_, (gl::GLsizeiptr)sizeof(cube_vertices), cube_vertices, gl::GL_STATIC_DRAW_);

  gl::EnableVertexAttribArray(0);
  gl::VertexAttribPointer(0, 3, gl::GL_FLOAT_, gl::GL_FALSE_, 8 * (gl::GLsizei)sizeof(float), (void*)0);
  gl::EnableVertexAttribArray(1);
  gl::VertexAttribPointer(1, 3, gl::GL_FLOAT_, gl::GL_FALSE_, 8 * (gl::GLsizei)sizeof(float),
                          (void*)(3 * sizeof(float)));
  gl::EnableVertexAttribArray(2);
  gl::VertexAttribPointer(2, 2, gl::GL_FLOAT_, gl::GL_FALSE_, 8 * (gl::GLsizei)sizeof(float),
                          (void*)(6 * sizeof(float)));

  gl::BindVertexArray(0);

  const char* vs_src = R"GLSL(
    #version 330 core
    layout(location=0) in vec3 aPos;
    layout(location=1) in vec3 aNormal;
    layout(location=2) in vec2 aUV;
    uniform mat4 uMVP;
    uniform mat4 uModel;
    out vec3 vNormal;
    out vec3 vWorldPos;
    out vec2 vUV;
    void main() {
      vec4 world = uModel * vec4(aPos, 1.0);
      vWorldPos = world.xyz;
      vNormal = mat3(uModel) * aNormal;
      vUV = aUV;
      gl_Position = uMVP * vec4(aPos, 1.0);
    }
  )GLSL";

  const char* fs_src = R"GLSL(
    #version 330 core
    in vec3 vNormal;
    in vec3 vWorldPos;
    in vec2 vUV;
    uniform vec3 uColor;
    uniform vec3 uLightDir;
    uniform vec3 uCamPos;
    uniform int uUseTex;
    uniform sampler2D uTex;
    out vec4 FragColor;
    void main() {
      vec3 base = uColor;
      if (uUseTex != 0) {
        base = texture(uTex, vUV).rgb;
      }
      vec3 N = normalize(vNormal);
      vec3 L = normalize(-uLightDir);
      float diff = max(dot(N, L), 0.0);
      vec3 V = normalize(uCamPos - vWorldPos);
      vec3 H = normalize(L + V);
      float spec = pow(max(dot(N, H), 0.0), 32.0);
      vec3 ambient = 0.08 * base;
      vec3 color = ambient + base * diff + vec3(1.0) * spec * 0.25;
      FragColor = vec4(color, 1.0);
    }
  )GLSL";

  const unsigned int vs = compile_shader(gl::GL_VERTEX_SHADER_, vs_src);
  const unsigned int fs = compile_shader(gl::GL_FRAGMENT_SHADER_, fs_src);
  cube_program_ = link_program(vs, fs);

  u_cube_mvp_ = gl::GetUniformLocation(cube_program_, "uMVP");
  u_cube_model_ = gl::GetUniformLocation(cube_program_, "uModel");
  u_cube_color_ = gl::GetUniformLocation(cube_program_, "uColor");
  u_cube_light_dir_ = gl::GetUniformLocation(cube_program_, "uLightDir");
  u_cube_cam_pos_ = gl::GetUniformLocation(cube_program_, "uCamPos");
  u_cube_use_tex_ = gl::GetUniformLocation(cube_program_, "uUseTex");
  u_cube_tex_ = gl::GetUniformLocation(cube_program_, "uTex");
}

void Renderer::ensure_ui_pipeline() {
  if (ui_program_ != 0) return;

  const char* vs_src = R"GLSL(
    #version 330 core
    layout(location=0) in vec2 aPosPx;
    uniform vec2 uResolution;
    void main() {
      vec2 ndc = vec2(
        (aPosPx.x / uResolution.x) * 2.0 - 1.0,
        1.0 - (aPosPx.y / uResolution.y) * 2.0
      );
      gl_Position = vec4(ndc, 0.0, 1.0);
    }
  )GLSL";

  const char* fs_src = R"GLSL(
    #version 330 core
    uniform vec3 uColor;
    out vec4 FragColor;
    void main() { FragColor = vec4(uColor, 1.0); }
  )GLSL";

  const unsigned int vs = compile_shader(gl::GL_VERTEX_SHADER_, vs_src);
  const unsigned int fs = compile_shader(gl::GL_FRAGMENT_SHADER_, fs_src);
  ui_program_ = link_program(vs, fs);
  u_ui_resolution_ = gl::GetUniformLocation(ui_program_, "uResolution");
  u_ui_color_ = gl::GetUniformLocation(ui_program_, "uColor");

  gl::GenVertexArrays(1, &ui_vao_);
  gl::BindVertexArray(ui_vao_);
  gl::GenBuffers(1, &ui_vbo_);
  gl::BindBuffer(gl::GL_ARRAY_BUFFER_, ui_vbo_);
  gl::BufferData(gl::GL_ARRAY_BUFFER_, (gl::GLsizeiptr)(sizeof(float) * 2 * 6 * 512), nullptr, gl::GL_DYNAMIC_DRAW_);
  gl::EnableVertexAttribArray(0);
  gl::VertexAttribPointer(0, 2, gl::GL_FLOAT_, gl::GL_FALSE_, 2 * (gl::GLsizei)sizeof(float), (void*)0);
  gl::BindVertexArray(0);
}

void Renderer::ensure_line_pipeline() {
  if (line_program_ != 0) return;

  const char* vs_src = R"GLSL(
    #version 330 core
    layout(location=0) in vec3 aPos;
    layout(location=1) in vec3 aColor;
    uniform mat4 uViewProj;
    out vec3 vColor;
    void main() {
      vColor = aColor;
      gl_Position = uViewProj * vec4(aPos, 1.0);
    }
  )GLSL";

  const char* fs_src = R"GLSL(
    #version 330 core
    in vec3 vColor;
    out vec4 FragColor;
    void main() { FragColor = vec4(vColor, 1.0); }
  )GLSL";

  const unsigned int vs = compile_shader(gl::GL_VERTEX_SHADER_, vs_src);
  const unsigned int fs = compile_shader(gl::GL_FRAGMENT_SHADER_, fs_src);
  line_program_ = link_program(vs, fs);
  u_line_viewproj_ = gl::GetUniformLocation(line_program_, "uViewProj");

  gl::GenVertexArrays(1, &line_vao_);
  gl::BindVertexArray(line_vao_);
  gl::GenBuffers(1, &line_vbo_);
  gl::BindBuffer(gl::GL_ARRAY_BUFFER_, line_vbo_);
  gl::BufferData(gl::GL_ARRAY_BUFFER_, (gl::GLsizeiptr)(sizeof(float) * 6 * 2048), nullptr, gl::GL_DYNAMIC_DRAW_);

  gl::EnableVertexAttribArray(0);
  gl::VertexAttribPointer(0, 3, gl::GL_FLOAT_, gl::GL_FALSE_, 6 * (gl::GLsizei)sizeof(float), (void*)0);
  gl::EnableVertexAttribArray(1);
  gl::VertexAttribPointer(1, 3, gl::GL_FLOAT_, gl::GL_FALSE_, 6 * (gl::GLsizei)sizeof(float),
                          (void*)(3 * sizeof(float)));

  gl::BindVertexArray(0);
}

void Renderer::ui_begin(int framebuffer_w, int framebuffer_h) {
  ensure_ui_pipeline();
  gl::Enable(gl::GL_BLEND_);
  gl::BlendFunc(gl::GL_SRC_ALPHA_, gl::GL_ONE_MINUS_SRC_ALPHA_);
  gl::Disable(gl::GL_DEPTH_TEST_);
  gl::UseProgram(ui_program_);
  gl::Uniform2f(u_ui_resolution_, (float)framebuffer_w, (float)framebuffer_h);
  gl::Uniform3f(u_ui_color_, 1.0f, 1.0f, 1.0f);
  gl::BindVertexArray(ui_vao_);
}

void Renderer::ui_draw_triangles_2d(const float* xy, int vertex_count) {
  gl::BindBuffer(gl::GL_ARRAY_BUFFER_, ui_vbo_);
  gl::BufferSubData(gl::GL_ARRAY_BUFFER_, 0, (gl::GLsizeiptr)(sizeof(float) * 2 * vertex_count), xy);
  gl::DrawArrays(gl::GL_TRIANGLES_, 0, vertex_count);
}

void Renderer::ui_end() {
  gl::BindVertexArray(0);
  gl::UseProgram(0);
  gl::Enable(gl::GL_DEPTH_TEST_);
  gl::Disable(gl::GL_BLEND_);
}

void Renderer::draw_scene(const Scene& scene) {
  int fb_w = 1, fb_h = 1;
  if (window_) glfwGetFramebufferSize(window_, &fb_w, &fb_h);
  const float aspect = fb_h > 0 ? (float)fb_w / (float)fb_h : 1.0f;

  const auto& bg = scene.background_color();
  gl::ClearColor(bg.x, bg.y, bg.z, 1.0f);
  gl::Clear(gl::GL_COLOR_BUFFER_BIT_ | gl::GL_DEPTH_BUFFER_BIT_);

  const auto& cam = scene.camera();
  const simple::math::Vec3 cam_pos = cam.transform.position;

  const float pitch = simple::math::radians(cam.transform.rotation.x);
  const float yaw = simple::math::radians(cam.transform.rotation.y);
  simple::math::Vec3 forward{
      std::cos(pitch) * std::sin(yaw),
      std::sin(pitch),
      -std::cos(pitch) * std::cos(yaw),
  };
  forward = simple::math::normalize(forward);

  const simple::math::Mat4 view = simple::math::look_at(cam_pos, cam_pos + forward, {0.0f, 1.0f, 0.0f});
  const simple::math::Mat4 proj = simple::math::perspective(simple::math::radians(cam.fov_degrees), aspect, cam.z_near,
                                                            cam.z_far);

  gl::UseProgram(cube_program_);
  gl::BindVertexArray(cube_vao_);
  gl::Uniform3f(u_cube_light_dir_, -0.3f, -1.0f, -0.6f);
  gl::Uniform3f(u_cube_cam_pos_, cam_pos.x, cam_pos.y, cam_pos.z);
  gl::ActiveTexture(gl::GL_TEXTURE0_);
  gl::Uniform1i(u_cube_tex_, 0);

  for (const auto& e : scene.entities()) {
    const auto* cube = dynamic_cast<const Cube*>(e.get());
    if (!cube) continue;

    const simple::math::Mat4 model = cube->transform().model_matrix();
    const simple::math::Mat4 mvp = proj * view * model;
    gl::UniformMatrix4fv(u_cube_mvp_, 1, gl::GL_FALSE_, mvp.data());
    gl::UniformMatrix4fv(u_cube_model_, 1, gl::GL_FALSE_, model.data());
    const auto& c = cube->color();
    gl::Uniform3f(u_cube_color_, c.x, c.y, c.z);
    const unsigned int tex = get_or_create_texture(cube->texture_path().empty() ? nullptr : cube->texture_path().c_str());
    gl::BindTexture(gl::GL_TEXTURE_2D_, tex);
    gl::Uniform1i(u_cube_use_tex_, cube->texture_path().empty() ? 0 : 1);
    gl::DrawArrays(gl::GL_TRIANGLES_, 0, 36);
  }

  gl::BindTexture(gl::GL_TEXTURE_2D_, 0);
  gl::BindVertexArray(0);
  gl::UseProgram(0);
}

void Renderer::draw_hud(const Scene& scene, int framebuffer_w, int framebuffer_h) {
  const auto& cmds = scene.hud_text();
  if (cmds.empty()) return;

  struct EasyFontVertex {
    float x, y, z;
    unsigned char c[4];
  };

  ui_begin(framebuffer_w, framebuffer_h);

  std::vector<EasyFontVertex> quad_verts;
  quad_verts.resize(16384);  // 4096 quads
  std::vector<float> tri_xy;
  tri_xy.reserve(6 * 2 * 1024);

  for (const auto& cmd : cmds) {
    if (cmd.text.empty()) continue;

    unsigned char white[4] = {255, 255, 255, 255};
    const int quads =
        stb_easy_font_print(0.0f, 0.0f, const_cast<char*>(cmd.text.c_str()), white, quad_verts.data(),
                            (int)(quad_verts.size() * sizeof(EasyFontVertex)));
    if (quads <= 0) continue;

    tri_xy.clear();
    tri_xy.reserve((size_t)quads * 6u * 2u);

    const float s = cmd.scale * 1.0f;
    for (int qi = 0; qi < quads; ++qi) {
      const EasyFontVertex* q = &quad_verts[(size_t)qi * 4u];

      const float x0 = cmd.x_px + q[0].x * s;
      const float y0 = cmd.y_px + q[0].y * s;
      const float x1 = cmd.x_px + q[1].x * s;
      const float y1 = cmd.y_px + q[1].y * s;
      const float x2 = cmd.x_px + q[2].x * s;
      const float y2 = cmd.y_px + q[2].y * s;
      const float x3 = cmd.x_px + q[3].x * s;
      const float y3 = cmd.y_px + q[3].y * s;

      // Two triangles for the quad: (0,1,2) and (0,2,3).
      tri_xy.push_back(x0);
      tri_xy.push_back(y0);
      tri_xy.push_back(x1);
      tri_xy.push_back(y1);
      tri_xy.push_back(x2);
      tri_xy.push_back(y2);

      tri_xy.push_back(x0);
      tri_xy.push_back(y0);
      tri_xy.push_back(x2);
      tri_xy.push_back(y2);
      tri_xy.push_back(x3);
      tri_xy.push_back(y3);
    }

    gl::Uniform3f(u_ui_color_, cmd.color.x, cmd.color.y, cmd.color.z);
    ui_draw_triangles_2d(tri_xy.data(), (int)(tri_xy.size() / 2u));
  }

  ui_end();
}

void Renderer::draw_debug_lines(const Scene& scene) {
  const auto& lines = scene.debug_lines();
  if (lines.empty()) return;

  ensure_line_pipeline();

  int fb_w = 1, fb_h = 1;
  if (window_) glfwGetFramebufferSize(window_, &fb_w, &fb_h);
  const float aspect = fb_h > 0 ? (float)fb_w / (float)fb_h : 1.0f;

  const auto& cam = scene.camera();
  const simple::math::Vec3 cam_pos = cam.transform.position;
  const float pitch = simple::math::radians(cam.transform.rotation.x);
  const float yaw = simple::math::radians(cam.transform.rotation.y);
  simple::math::Vec3 forward{
      std::cos(pitch) * std::sin(yaw),
      std::sin(pitch),
      -std::cos(pitch) * std::cos(yaw),
  };
  forward = simple::math::normalize(forward);
  const simple::math::Mat4 view = simple::math::look_at(cam_pos, cam_pos + forward, {0.0f, 1.0f, 0.0f});
  const simple::math::Mat4 proj = simple::math::perspective(simple::math::radians(cam.fov_degrees), aspect, cam.z_near,
                                                            cam.z_far);
  const simple::math::Mat4 viewproj = proj * view;

  struct LineVert {
    float x, y, z;
    float r, g, b;
  };
  std::vector<LineVert> verts;
  verts.reserve(lines.size() * 2u);
  for (const auto& l : lines) {
    verts.push_back({l.a.x, l.a.y, l.a.z, l.color.x, l.color.y, l.color.z});
    verts.push_back({l.b.x, l.b.y, l.b.z, l.color.x, l.color.y, l.color.z});
  }

  gl::BindVertexArray(line_vao_);
  gl::BindBuffer(gl::GL_ARRAY_BUFFER_, line_vbo_);
  gl::BufferData(gl::GL_ARRAY_BUFFER_, (gl::GLsizeiptr)(verts.size() * sizeof(LineVert)), verts.data(),
                 gl::GL_DYNAMIC_DRAW_);

  gl::Disable(gl::GL_DEPTH_TEST_);
  gl::UseProgram(line_program_);
  gl::UniformMatrix4fv(u_line_viewproj_, 1, gl::GL_FALSE_, viewproj.data());
  gl::LineWidth(2.0f);
  gl::DrawArrays(gl::GL_LINES_, 0, (gl::GLsizei)verts.size());

  gl::UseProgram(0);
  gl::BindVertexArray(0);
  gl::Enable(gl::GL_DEPTH_TEST_);
}

bool Renderer::capture_screenshot_ppm(const char* path, int framebuffer_w, int framebuffer_h) {
  if (!path || !path[0] || framebuffer_w <= 0 || framebuffer_h <= 0) return false;

  std::vector<std::uint8_t> rgb;
  rgb.resize((size_t)framebuffer_w * (size_t)framebuffer_h * 3u);
  gl::PixelStorei(gl::GL_PACK_ALIGNMENT_, 1);
  gl::ReadPixels(0, 0, framebuffer_w, framebuffer_h, gl::GL_RGB_, gl::GL_UNSIGNED_BYTE_, rgb.data());

  // Write P6, flipping vertically (OpenGL origin is bottom-left).
  std::ofstream out(path, std::ios::binary);
  if (!out) return false;
  out << "P6\n" << framebuffer_w << " " << framebuffer_h << "\n255\n";
  for (int y = framebuffer_h - 1; y >= 0; --y) {
    const std::uint8_t* row = &rgb[(size_t)y * (size_t)framebuffer_w * 3u];
    out.write(reinterpret_cast<const char*>(row), (std::streamsize)framebuffer_w * 3);
  }
  return (bool)out;
}

unsigned int Renderer::get_or_create_texture(const char* path) {
  if (!path || !path[0]) return default_texture_ ? default_texture_ : 0u;
  const std::string key(path);
  auto it = texture_cache_.find(key);
  if (it != texture_cache_.end()) return it->second;

  ImageData img;
  if (!load_ppm(key, img)) {
    // If file can't be loaded, fall back to default checker but keep cache entry
    // so we don't try every frame.
    texture_cache_[key] = default_texture_ ? default_texture_ : 0u;
    return texture_cache_[key];
  }

  unsigned int tex = 0;
  gl::GenTextures(1, &tex);
  gl::BindTexture(gl::GL_TEXTURE_2D_, tex);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_MIN_FILTER_, (int)gl::GL_LINEAR_MIPMAP_LINEAR_);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_MAG_FILTER_, (int)gl::GL_LINEAR_);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_WRAP_S_, (int)gl::GL_REPEAT_);
  gl::TexParameteri(gl::GL_TEXTURE_2D_, gl::GL_TEXTURE_WRAP_T_, (int)gl::GL_REPEAT_);

  const gl::GLenum fmt = (img.channels == 4) ? gl::GL_RGBA_ : gl::GL_RGB_;
  gl::TexImage2D(gl::GL_TEXTURE_2D_, 0, (int)fmt, img.width, img.height, 0, fmt, gl::GL_UNSIGNED_BYTE_,
                 img.pixels.data());
  gl::GenerateMipmap(gl::GL_TEXTURE_2D_);
  gl::BindTexture(gl::GL_TEXTURE_2D_, 0);

  texture_cache_[key] = tex;
  return tex;
}

void Renderer::destroy_resources() {
  if (cube_vbo_) {
    gl::DeleteBuffers(1, &cube_vbo_);
    cube_vbo_ = 0;
  }
  if (cube_vao_) {
    gl::DeleteVertexArrays(1, &cube_vao_);
    cube_vao_ = 0;
  }
  if (cube_program_) {
    gl::DeleteProgram(cube_program_);
    cube_program_ = 0;
  }

  if (ui_vbo_) {
    gl::DeleteBuffers(1, &ui_vbo_);
    ui_vbo_ = 0;
  }
  if (ui_vao_) {
    gl::DeleteVertexArrays(1, &ui_vao_);
    ui_vao_ = 0;
  }
  if (ui_program_) {
    gl::DeleteProgram(ui_program_);
    ui_program_ = 0;
  }

  if (line_vbo_) {
    gl::DeleteBuffers(1, &line_vbo_);
    line_vbo_ = 0;
  }
  if (line_vao_) {
    gl::DeleteVertexArrays(1, &line_vao_);
    line_vao_ = 0;
  }
  if (line_program_) {
    gl::DeleteProgram(line_program_);
    line_program_ = 0;
  }

  const unsigned int default_id = default_texture_;
  for (auto& kv : texture_cache_) {
    const unsigned int tex_id = kv.second;
    if (tex_id != 0 && tex_id != default_id) {
      unsigned int tmp = tex_id;
      gl::DeleteTextures(1, &tmp);
    }
  }
  texture_cache_.clear();

  if (default_texture_) {
    gl::DeleteTextures(1, &default_texture_);
    default_texture_ = 0;
  }
}

}  // namespace simple
