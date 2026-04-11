#include "branding.h"

#include <cstdlib>
#include <cstring>
#include <stdexcept>

#include "platform/glfw.h"

#include "../renderer/renderer.h"

namespace simple {

Branding::Branding() = default;

Branding::~Branding() {
  if (vertices_) std::free(vertices_);
  vertices_ = nullptr;
  vertex_count_ = 0;
  capacity_floats_ = 0;
}

void Branding::initialize() {
  if (initialized_) return;
  build_text_mesh();
  initialized_ = true;
}

// Tiny 5x7 bitmap font for the specific letters used by "Made with Simple".
// Each glyph is 7 rows, 5 bits per row, MSB on the left.
static unsigned char glyph_5x7(char c, int row) {
  auto rowbits = [](const unsigned char rows[7], int r) -> unsigned char { return rows[r]; };
  switch (c) {
    case 'M': {
      static const unsigned char r[7] = {0x11, 0x1B, 0x15, 0x11, 0x11, 0x11, 0x11};
      return rowbits(r, row);
    }
    case 'S': {
      static const unsigned char r[7] = {0x0F, 0x10, 0x10, 0x0E, 0x01, 0x01, 0x1E};
      return rowbits(r, row);
    }
    case 'a': {
      static const unsigned char r[7] = {0x00, 0x00, 0x0E, 0x01, 0x0F, 0x11, 0x0F};
      return rowbits(r, row);
    }
    case 'd': {
      static const unsigned char r[7] = {0x01, 0x01, 0x0D, 0x13, 0x11, 0x13, 0x0D};
      return rowbits(r, row);
    }
    case 'e': {
      static const unsigned char r[7] = {0x00, 0x00, 0x0E, 0x11, 0x1F, 0x10, 0x0E};
      return rowbits(r, row);
    }
    case 'h': {
      static const unsigned char r[7] = {0x10, 0x10, 0x1E, 0x11, 0x11, 0x11, 0x11};
      return rowbits(r, row);
    }
    case 'i': {
      static const unsigned char r[7] = {0x04, 0x00, 0x0C, 0x04, 0x04, 0x04, 0x0E};
      return rowbits(r, row);
    }
    case 'l': {
      static const unsigned char r[7] = {0x0C, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E};
      return rowbits(r, row);
    }
    case 'm': {
      static const unsigned char r[7] = {0x00, 0x00, 0x1A, 0x15, 0x15, 0x15, 0x15};
      return rowbits(r, row);
    }
    case 'p': {
      static const unsigned char r[7] = {0x00, 0x00, 0x1E, 0x11, 0x1E, 0x10, 0x10};
      return rowbits(r, row);
    }
    case 't': {
      static const unsigned char r[7] = {0x04, 0x04, 0x1F, 0x04, 0x04, 0x04, 0x03};
      return rowbits(r, row);
    }
    case 'w': {
      static const unsigned char r[7] = {0x00, 0x00, 0x11, 0x11, 0x15, 0x1B, 0x11};
      return rowbits(r, row);
    }
    default:
      return 0;
  }
}

static void push_rect(float*& out, float x0, float y0, float x1, float y1) {
  // Two triangles.
  *out++ = x0;
  *out++ = y0;
  *out++ = x1;
  *out++ = y0;
  *out++ = x1;
  *out++ = y1;

  *out++ = x0;
  *out++ = y0;
  *out++ = x1;
  *out++ = y1;
  *out++ = x0;
  *out++ = y1;
}

void Branding::build_text_mesh() {
  const char* text = "Made with Simple";
  const int pixel = 2;     // glyph pixel size in screen pixels
  const int spacing = 2;   // spacing between glyphs in pixels
  const int glyph_w = 5;
  const int glyph_h = 7;

  int glyphs = 0;
  for (const char* p = text; *p; ++p) glyphs++;

  // Worst-case estimate: every pixel set -> 35 rects -> 210 vertices per glyph.
  const int max_verts = glyphs * 210;
  const int max_floats = max_verts * 2;

  if (capacity_floats_ < max_floats) {
    vertices_ = (float*)std::realloc(vertices_, sizeof(float) * (size_t)max_floats);
    if (!vertices_) throw std::runtime_error("Branding mesh allocation failed");
    capacity_floats_ = max_floats;
  }

  float* out = vertices_;
  int verts = 0;

  float x_cursor = 0.0f;
  for (const char* p = text; *p; ++p) {
    const char c = *p;
    if (c == ' ') {
      x_cursor += (glyph_w * pixel) + (spacing + 6);
      continue;
    }
    for (int row = 0; row < glyph_h; ++row) {
      const unsigned char bits = glyph_5x7(c, row);
      for (int col = 0; col < glyph_w; ++col) {
        const unsigned char mask = (unsigned char)(1u << (glyph_w - 1 - col));
        if ((bits & mask) == 0) continue;
        const float x0 = x_cursor + (float)(col * pixel);
        const float y0 = (float)(row * pixel);
        const float x1 = x0 + (float)pixel;
        const float y1 = y0 + (float)pixel;
        push_rect(out, x0, y0, x1, y1);
        verts += 6;
      }
    }
    x_cursor += (glyph_w * pixel) + spacing;
  }

  vertex_count_ = verts;
}

void Branding::draw_overlay(int framebuffer_w, int framebuffer_h) {
  if (!initialized_) initialize();
  if (!vertices_ || vertex_count_ <= 0) return;

  const float pad = 10.0f;
  const float x_off = pad;
  const float y_off = pad;

  const int floats = vertex_count_ * 2;
  float* tmp = (float*)std::malloc(sizeof(float) * (size_t)floats);
  if (!tmp) return;
  std::memcpy(tmp, vertices_, sizeof(float) * (size_t)floats);
  for (int i = 0; i < vertex_count_; ++i) {
    tmp[i * 2 + 0] += x_off;
    tmp[i * 2 + 1] += y_off;
  }

  // Renderer instance is stored on the current context's window user pointer.
  GLFWwindow* win = glfwGetCurrentContext();
  auto* renderer = win ? reinterpret_cast<Renderer*>(glfwGetWindowUserPointer(win)) : nullptr;
  if (renderer) {
    renderer->ui_begin(framebuffer_w, framebuffer_h);
    renderer->ui_draw_triangles_2d(tmp, vertex_count_);
    renderer->ui_end();
  }

  std::free(tmp);
}

}  // namespace simple
