#pragma once

#include <memory>
#include <string>

#include "../math/transform.h"

namespace simple {

class Entity {
 public:
  virtual ~Entity() = default;

  simple::math::Transform& transform() { return transform_; }
  const simple::math::Transform& transform() const { return transform_; }

  virtual void update(float dt_seconds) { (void)dt_seconds; }

 private:
  simple::math::Transform transform_{};
};

class Cube final : public Entity {
 public:
  Cube();

  simple::math::Vec3& color() { return color_; }
  const simple::math::Vec3& color() const { return color_; }

  simple::math::Vec3& spin_deg_per_sec() { return spin_deg_per_sec_; }
  const simple::math::Vec3& spin_deg_per_sec() const { return spin_deg_per_sec_; }

  // Empty => no texture, use color.
  std::string& texture_path() { return texture_path_; }
  const std::string& texture_path() const { return texture_path_; }

  void update(float dt_seconds) override;

 private:
  simple::math::Vec3 color_{0.2f, 0.6f, 1.0f};
  simple::math::Vec3 spin_deg_per_sec_{0.0f, 45.0f, 0.0f};
  std::string texture_path_{};
};

using EntityPtr = std::shared_ptr<Entity>;
using CubePtr = std::shared_ptr<Cube>;

}  // namespace simple
