#include "texture.h"

#include <algorithm>
#include <cctype>
#include <cstdio>
#include <fstream>
#include <sstream>
#include <stdexcept>

namespace simple {

static void skip_ws_and_comments(std::istream& in) {
  while (true) {
    int c = in.peek();
    if (c == '#') {
      std::string dummy;
      std::getline(in, dummy);
      continue;
    }
    if (c == EOF) return;
    if (std::isspace(c)) {
      in.get();
      continue;
    }
    return;
  }
}

static bool read_token(std::istream& in, std::string& out) {
  skip_ws_and_comments(in);
  out.clear();
  while (true) {
    int c = in.peek();
    if (c == EOF) break;
    if (c == '#') break;
    if (std::isspace(c)) break;
    out.push_back((char)in.get());
  }
  return !out.empty();
}

bool load_ppm(const std::string& path, ImageData& out) {
  std::ifstream f(path, std::ios::binary);
  if (!f) return false;

  std::string magic;
  if (!read_token(f, magic)) return false;
  if (magic != "P6" && magic != "P3") return false;

  std::string tok;
  if (!read_token(f, tok)) return false;
  int w = std::stoi(tok);
  if (!read_token(f, tok)) return false;
  int h = std::stoi(tok);
  if (!read_token(f, tok)) return false;
  int maxv = std::stoi(tok);
  if (w <= 0 || h <= 0 || maxv <= 0 || maxv > 65535) return false;

  out.width = w;
  out.height = h;
  out.channels = 3;
  out.pixels.resize((size_t)w * (size_t)h * 3u);

  if (magic == "P6") {
    // One single whitespace after header; consume exactly one.
    // (Some files may have multiple; tolerate them.)
    char c = 0;
    f.read(&c, 1);
    while (f && std::isspace((unsigned char)c)) {
      if (f.peek() == EOF) break;
      f.read(&c, 1);
    }
    if (f) f.unget();

    if (maxv <= 255) {
      f.read(reinterpret_cast<char*>(out.pixels.data()), (std::streamsize)out.pixels.size());
      return (bool)f;
    }

    // 16-bit big-endian per channel.
    for (size_t i = 0; i < out.pixels.size(); ++i) {
      unsigned char hi = 0, lo = 0;
      f.read(reinterpret_cast<char*>(&hi), 1);
      f.read(reinterpret_cast<char*>(&lo), 1);
      if (!f) return false;
      const int v = ((int)hi << 8) | (int)lo;
      out.pixels[i] = (std::uint8_t)std::clamp((v * 255) / maxv, 0, 255);
    }
    return true;
  }

  // P3 ASCII
  for (size_t i = 0; i < out.pixels.size(); ++i) {
    if (!read_token(f, tok)) return false;
    const int v = std::stoi(tok);
    out.pixels[i] = (std::uint8_t)std::clamp((v * 255) / maxv, 0, 255);
  }
  return true;
}

ImageData make_checker(int w, int h, int check) {
  ImageData img;
  img.width = w;
  img.height = h;
  img.channels = 3;
  img.pixels.resize((size_t)w * (size_t)h * 3u);

  for (int y = 0; y < h; ++y) {
    for (int x = 0; x < w; ++x) {
      const bool on = (((x / check) + (y / check)) % 2) == 0;
      const std::uint8_t v = on ? (std::uint8_t)230 : (std::uint8_t)40;
      const size_t idx = ((size_t)y * (size_t)w + (size_t)x) * 3u;
      img.pixels[idx + 0] = v;
      img.pixels[idx + 1] = v;
      img.pixels[idx + 2] = v;
    }
  }
  return img;
}

}  // namespace simple

