#pragma once

#include <cmath>
#include <cstdint>
#include <ostream>

namespace simple::math {

inline constexpr float kPi = 3.14159265358979323846f;

inline float radians(float degrees) { return degrees * (kPi / 180.0f); }

struct Vec2 {
  float x{0};
  float y{0};
};

struct Vec3 {
  float x{0};
  float y{0};
  float z{0};
};

inline Vec3 operator+(const Vec3& a, const Vec3& b) { return {a.x + b.x, a.y + b.y, a.z + b.z}; }
inline Vec3 operator-(const Vec3& a, const Vec3& b) { return {a.x - b.x, a.y - b.y, a.z - b.z}; }
inline Vec3 operator*(const Vec3& v, float s) { return {v.x * s, v.y * s, v.z * s}; }

inline float dot(const Vec3& a, const Vec3& b) { return a.x * b.x + a.y * b.y + a.z * b.z; }

inline Vec3 cross(const Vec3& a, const Vec3& b) {
  return {a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x};
}

inline float length(const Vec3& v) { return std::sqrt(dot(v, v)); }

inline Vec3 normalize(const Vec3& v) {
  const float len = length(v);
  if (len <= 1e-8f) return {0, 0, 0};
  return v * (1.0f / len);
}

struct Mat4 {
  // Column-major (OpenGL-style).
  float m[16]{};

  static Mat4 identity() {
    Mat4 r;
    r.m[0] = r.m[5] = r.m[10] = r.m[15] = 1.0f;
    return r;
  }

  const float* data() const { return m; }
  float* data() { return m; }
};

inline Mat4 operator*(const Mat4& a, const Mat4& b) {
  Mat4 r{};
  for (int c = 0; c < 4; ++c) {
    for (int row = 0; row < 4; ++row) {
      float sum = 0.0f;
      for (int k = 0; k < 4; ++k) sum += a.m[k * 4 + row] * b.m[c * 4 + k];
      r.m[c * 4 + row] = sum;
    }
  }
  return r;
}

inline Mat4 translate(const Vec3& t) {
  Mat4 r = Mat4::identity();
  r.m[12] = t.x;
  r.m[13] = t.y;
  r.m[14] = t.z;
  return r;
}

inline Mat4 scale(const Vec3& s) {
  Mat4 r = Mat4::identity();
  r.m[0] = s.x;
  r.m[5] = s.y;
  r.m[10] = s.z;
  return r;
}

inline Mat4 rotate_x(float rad) {
  Mat4 r = Mat4::identity();
  const float c = std::cos(rad);
  const float s = std::sin(rad);
  r.m[5] = c;
  r.m[6] = s;
  r.m[9] = -s;
  r.m[10] = c;
  return r;
}

inline Mat4 rotate_y(float rad) {
  Mat4 r = Mat4::identity();
  const float c = std::cos(rad);
  const float s = std::sin(rad);
  r.m[0] = c;
  r.m[2] = -s;
  r.m[8] = s;
  r.m[10] = c;
  return r;
}

inline Mat4 rotate_z(float rad) {
  Mat4 r = Mat4::identity();
  const float c = std::cos(rad);
  const float s = std::sin(rad);
  r.m[0] = c;
  r.m[1] = s;
  r.m[4] = -s;
  r.m[5] = c;
  return r;
}

inline Mat4 euler_xyz_deg(const Vec3& degrees_xyz) {
  const float rx = radians(degrees_xyz.x);
  const float ry = radians(degrees_xyz.y);
  const float rz = radians(degrees_xyz.z);
  // Intrinsic XYZ (model space) -> equivalent to Rz * Ry * Rx in column-major multiplication order.
  return rotate_z(rz) * rotate_y(ry) * rotate_x(rx);
}

inline Mat4 perspective(float fov_y_rad, float aspect, float z_near, float z_far) {
  Mat4 r{};
  const float f = 1.0f / std::tan(fov_y_rad * 0.5f);
  r.m[0] = f / aspect;
  r.m[5] = f;
  r.m[10] = (z_far + z_near) / (z_near - z_far);
  r.m[11] = -1.0f;
  r.m[14] = (2.0f * z_far * z_near) / (z_near - z_far);
  return r;
}

inline Mat4 look_at(const Vec3& eye, const Vec3& center, const Vec3& up) {
  const Vec3 f = normalize(center - eye);
  const Vec3 s = normalize(cross(f, up));
  const Vec3 u = cross(s, f);

  Mat4 r = Mat4::identity();
  r.m[0] = s.x;
  r.m[4] = s.y;
  r.m[8] = s.z;
  r.m[1] = u.x;
  r.m[5] = u.y;
  r.m[9] = u.z;
  r.m[2] = -f.x;
  r.m[6] = -f.y;
  r.m[10] = -f.z;
  r.m[12] = -dot(s, eye);
  r.m[13] = -dot(u, eye);
  r.m[14] = dot(f, eye);
  return r;
}

struct Transform {
  Vec3 position{0, 0, 0};
  Vec3 rotation{0, 0, 0};  // Degrees, XYZ.
  Vec3 scale{1, 1, 1};

  Mat4 model_matrix() const { return translate(position) * euler_xyz_deg(rotation) * simple::math::scale(scale); }
};

inline std::ostream& operator<<(std::ostream& os, const Vec3& v) {
  os << "Vec3(" << v.x << ", " << v.y << ", " << v.z << ")";
  return os;
}

}  // namespace simple::math

