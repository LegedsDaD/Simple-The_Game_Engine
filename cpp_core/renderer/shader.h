#pragma once

#include <string>

namespace simple {

class Shader {
 public:
  Shader();
  ~Shader();

  Shader(const Shader&) = delete;
  Shader& operator=(const Shader&) = delete;

  void build_from_sources(const std::string& vertex_src, const std::string& fragment_src);
  void destroy();

  unsigned int program() const { return program_; }

 private:
  unsigned int program_{0};
};

}  // namespace simple

