#include "entity.h"

namespace simple {

Cube::Cube() = default;

void Cube::update(float dt_seconds) {
  auto& rot = transform().rotation;
  rot.x += spin_deg_per_sec_.x * dt_seconds;
  rot.y += spin_deg_per_sec_.y * dt_seconds;
  rot.z += spin_deg_per_sec_.z * dt_seconds;
}

}  // namespace simple

