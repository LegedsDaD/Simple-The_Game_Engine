#include "gl_loader.h"

#include <stdexcept>
#include <string>

namespace simple {
namespace gl {

PFNGLCREATESHADERPROC CreateShader = nullptr;
PFNGLSHADERSOURCEPROC ShaderSource = nullptr;
PFNGLCOMPILESHADERPROC CompileShader = nullptr;
PFNGLGETSHADERIVPROC GetShaderiv = nullptr;
PFNGLGETSHADERINFOLOGPROC GetShaderInfoLog = nullptr;
PFNGLDELETESHADERPROC DeleteShader = nullptr;

PFNGLCREATEPROGRAMPROC CreateProgram = nullptr;
PFNGLATTACHSHADERPROC AttachShader = nullptr;
PFNGLLINKPROGRAMPROC LinkProgram = nullptr;
PFNGLGETPROGRAMIVPROC GetProgramiv = nullptr;
PFNGLGETPROGRAMINFOLOGPROC GetProgramInfoLog = nullptr;
PFNGLUSEPROGRAMPROC UseProgram = nullptr;
PFNGLDELETEPROGRAMPROC DeleteProgram = nullptr;

PFNGLGETUNIFORMLOCATIONPROC GetUniformLocation = nullptr;
PFNGLUNIFORMMATRIX4FVPROC UniformMatrix4fv = nullptr;
PFNGLUNIFORM3FPROC Uniform3f = nullptr;
PFNGLUNIFORM2FPROC Uniform2f = nullptr;
PFNGLUNIFORM1IPROC Uniform1i = nullptr;

PFNGLGENVERTEXARRAYSPROC GenVertexArrays = nullptr;
PFNGLBINDVERTEXARRAYPROC BindVertexArray = nullptr;
PFNGLDELETEVERTEXARRAYSPROC DeleteVertexArrays = nullptr;

PFNGLGENBUFFERSPROC GenBuffers = nullptr;
PFNGLBINDBUFFERPROC BindBuffer = nullptr;
PFNGLBUFFERDATAPROC BufferData = nullptr;
PFNGLBUFFERSUBDATAPROC BufferSubData = nullptr;
PFNGLDELETEBUFFERSPROC DeleteBuffers = nullptr;

PFNGLENABLEVERTEXATTRIBARRAYPROC EnableVertexAttribArray = nullptr;
PFNGLVERTEXATTRIBPOINTERPROC VertexAttribPointer = nullptr;

PFNGLVIEWPORTPROC Viewport = nullptr;
PFNGLCLEARCOLORPROC ClearColor = nullptr;
PFNGLCLEARPROC Clear = nullptr;
PFNGLENABLEPROC Enable = nullptr;
PFNGLDISABLEPROC Disable = nullptr;
PFNGLDEPTHFUNCPROC DepthFunc = nullptr;
PFNGLCULLFACEPROC CullFace = nullptr;
PFNGLBLENDFUNCPROC BlendFunc = nullptr;

PFNGLDRAWARRAYSPROC DrawArrays = nullptr;
PFNGLLINEWIDTHPROC LineWidth = nullptr;
PFNGLPIXELSTOREIPROC PixelStorei = nullptr;
PFNGLREADPIXELSPROC ReadPixels = nullptr;

PFNGLGENTEXTURESPROC GenTextures = nullptr;
PFNGLBINDTEXTUREPROC BindTexture = nullptr;
PFNGLTEXIMAGE2DPROC TexImage2D = nullptr;
PFNGLTEXPARAMETERIPROC TexParameteri = nullptr;
PFNGLGENERATEMIPMAPPROC GenerateMipmap = nullptr;
PFNGLACTIVETEXTUREPROC ActiveTexture = nullptr;
PFNGLDELETETEXTURESPROC DeleteTextures = nullptr;

static void* load1(void* (*get_proc_address)(const char*), const char* name) {
  void* p = get_proc_address(name);
  if (!p) throw std::runtime_error(std::string("Failed to load OpenGL function: ") + name);
  return p;
}

bool load(void* (*get_proc_address)(const char*)) {
  try {
    CreateShader = (PFNGLCREATESHADERPROC)load1(get_proc_address, "glCreateShader");
    ShaderSource = (PFNGLSHADERSOURCEPROC)load1(get_proc_address, "glShaderSource");
    CompileShader = (PFNGLCOMPILESHADERPROC)load1(get_proc_address, "glCompileShader");
    GetShaderiv = (PFNGLGETSHADERIVPROC)load1(get_proc_address, "glGetShaderiv");
    GetShaderInfoLog = (PFNGLGETSHADERINFOLOGPROC)load1(get_proc_address, "glGetShaderInfoLog");
    DeleteShader = (PFNGLDELETESHADERPROC)load1(get_proc_address, "glDeleteShader");

    CreateProgram = (PFNGLCREATEPROGRAMPROC)load1(get_proc_address, "glCreateProgram");
    AttachShader = (PFNGLATTACHSHADERPROC)load1(get_proc_address, "glAttachShader");
    LinkProgram = (PFNGLLINKPROGRAMPROC)load1(get_proc_address, "glLinkProgram");
    GetProgramiv = (PFNGLGETPROGRAMIVPROC)load1(get_proc_address, "glGetProgramiv");
    GetProgramInfoLog = (PFNGLGETPROGRAMINFOLOGPROC)load1(get_proc_address, "glGetProgramInfoLog");
    UseProgram = (PFNGLUSEPROGRAMPROC)load1(get_proc_address, "glUseProgram");
    DeleteProgram = (PFNGLDELETEPROGRAMPROC)load1(get_proc_address, "glDeleteProgram");

    GetUniformLocation = (PFNGLGETUNIFORMLOCATIONPROC)load1(get_proc_address, "glGetUniformLocation");
    UniformMatrix4fv = (PFNGLUNIFORMMATRIX4FVPROC)load1(get_proc_address, "glUniformMatrix4fv");
    Uniform3f = (PFNGLUNIFORM3FPROC)load1(get_proc_address, "glUniform3f");
    Uniform2f = (PFNGLUNIFORM2FPROC)load1(get_proc_address, "glUniform2f");
    Uniform1i = (PFNGLUNIFORM1IPROC)load1(get_proc_address, "glUniform1i");

    GenVertexArrays = (PFNGLGENVERTEXARRAYSPROC)load1(get_proc_address, "glGenVertexArrays");
    BindVertexArray = (PFNGLBINDVERTEXARRAYPROC)load1(get_proc_address, "glBindVertexArray");
    DeleteVertexArrays = (PFNGLDELETEVERTEXARRAYSPROC)load1(get_proc_address, "glDeleteVertexArrays");

    GenBuffers = (PFNGLGENBUFFERSPROC)load1(get_proc_address, "glGenBuffers");
    BindBuffer = (PFNGLBINDBUFFERPROC)load1(get_proc_address, "glBindBuffer");
    BufferData = (PFNGLBUFFERDATAPROC)load1(get_proc_address, "glBufferData");
    BufferSubData = (PFNGLBUFFERSUBDATAPROC)load1(get_proc_address, "glBufferSubData");
    DeleteBuffers = (PFNGLDELETEBUFFERSPROC)load1(get_proc_address, "glDeleteBuffers");

    EnableVertexAttribArray = (PFNGLENABLEVERTEXATTRIBARRAYPROC)load1(get_proc_address, "glEnableVertexAttribArray");
    VertexAttribPointer = (PFNGLVERTEXATTRIBPOINTERPROC)load1(get_proc_address, "glVertexAttribPointer");

    Viewport = (PFNGLVIEWPORTPROC)load1(get_proc_address, "glViewport");
    ClearColor = (PFNGLCLEARCOLORPROC)load1(get_proc_address, "glClearColor");
    Clear = (PFNGLCLEARPROC)load1(get_proc_address, "glClear");
    Enable = (PFNGLENABLEPROC)load1(get_proc_address, "glEnable");
    Disable = (PFNGLDISABLEPROC)load1(get_proc_address, "glDisable");
    DepthFunc = (PFNGLDEPTHFUNCPROC)load1(get_proc_address, "glDepthFunc");
    CullFace = (PFNGLCULLFACEPROC)load1(get_proc_address, "glCullFace");
    BlendFunc = (PFNGLBLENDFUNCPROC)load1(get_proc_address, "glBlendFunc");

    DrawArrays = (PFNGLDRAWARRAYSPROC)load1(get_proc_address, "glDrawArrays");
    LineWidth = (PFNGLLINEWIDTHPROC)load1(get_proc_address, "glLineWidth");
    PixelStorei = (PFNGLPIXELSTOREIPROC)load1(get_proc_address, "glPixelStorei");
    ReadPixels = (PFNGLREADPIXELSPROC)load1(get_proc_address, "glReadPixels");

    GenTextures = (PFNGLGENTEXTURESPROC)load1(get_proc_address, "glGenTextures");
    BindTexture = (PFNGLBINDTEXTUREPROC)load1(get_proc_address, "glBindTexture");
    TexImage2D = (PFNGLTEXIMAGE2DPROC)load1(get_proc_address, "glTexImage2D");
    TexParameteri = (PFNGLTEXPARAMETERIPROC)load1(get_proc_address, "glTexParameteri");
    GenerateMipmap = (PFNGLGENERATEMIPMAPPROC)load1(get_proc_address, "glGenerateMipmap");
    ActiveTexture = (PFNGLACTIVETEXTUREPROC)load1(get_proc_address, "glActiveTexture");
    DeleteTextures = (PFNGLDELETETEXTURESPROC)load1(get_proc_address, "glDeleteTextures");
  } catch (...) {
    return false;
  }
  return true;
}

}  // namespace gl
}  // namespace simple

