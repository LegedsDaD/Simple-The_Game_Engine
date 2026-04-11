#pragma once

#include <cstdint>
#include <string>
#include <vector>

namespace simple {

struct ImageData {
  int width{0};
  int height{0};
  int channels{0};  // 3 or 4
  std::vector<std::uint8_t> pixels{};
};

// Minimal PPM loader (P6 + P3) for repo-friendly, text/binary assets.
// Returns true on success.
bool load_ppm(const std::string& path, ImageData& out);

// Fallback: generate a checkerboard image.
ImageData make_checker(int w = 128, int h = 128, int check = 16);

}  // namespace simple

