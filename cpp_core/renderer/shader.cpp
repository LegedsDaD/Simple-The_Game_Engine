#include "shader.h"

#include <stdexcept>
#include <string>

#include "renderer.h"

namespace simple {

Shader::Shader() = default;
Shader::~Shader() { destroy(); }

static unsigned int compile1(simple::gl::GLenum type, const std::string& src) {
  const char* s = src.c_str();
  unsigned int sh = simple::gl::CreateShader(type);
  simple::gl::ShaderSource(sh, 1, &s, nullptr);
  simple::gl::CompileShader(sh);
  simple::gl::GLint ok = 0;
  simple::gl::GetShaderiv(sh, simple::gl::GL_COMPILE_STATUS_, &ok);
  if (!ok) {
    simple::gl::GLint len = 0;
    simple::gl::GetShaderiv(sh, simple::gl::GL_INFO_LOG_LENGTH_, &len);
    std::string log;
    log.resize(len > 1 ? (size_t)len : 1u);
    simple::gl::GLsizei out_len = 0;
    simple::gl::GetShaderInfoLog(sh, (simple::gl::GLsizei)log.size(), &out_len, log.data());
    simple::gl::DeleteShader(sh);
    throw std::runtime_error("Shader compile failed: " + log);
  }
  return sh;
}

void Shader::build_from_sources(const std::string& vertex_src, const std::string& fragment_src) {
  destroy();
  const unsigned int vs = compile1(simple::gl::GL_VERTEX_SHADER_, vertex_src);
  const unsigned int fs = compile1(simple::gl::GL_FRAGMENT_SHADER_, fragment_src);
  program_ = simple::gl::CreateProgram();
  simple::gl::AttachShader(program_, vs);
  simple::gl::AttachShader(program_, fs);
  simple::gl::LinkProgram(program_);
  simple::gl::GLint ok = 0;
  simple::gl::GetProgramiv(program_, simple::gl::GL_LINK_STATUS_, &ok);
  simple::gl::DeleteShader(vs);
  simple::gl::DeleteShader(fs);
  if (!ok) {
    simple::gl::GLint len = 0;
    simple::gl::GetProgramiv(program_, simple::gl::GL_INFO_LOG_LENGTH_, &len);
    std::string log;
    log.resize(len > 1 ? (size_t)len : 1u);
    simple::gl::GLsizei out_len = 0;
    simple::gl::GetProgramInfoLog(program_, (simple::gl::GLsizei)log.size(), &out_len, log.data());
    destroy();
    throw std::runtime_error("Program link failed: " + log);
  }
}

void Shader::destroy() {
  if (program_ != 0) {
    simple::gl::DeleteProgram(program_);
    program_ = 0;
  }
}

}  // namespace simple
