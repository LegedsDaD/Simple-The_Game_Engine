#pragma once

#include <cstddef>

namespace simple {
namespace gl {

using GLenum = unsigned int;
using GLboolean = unsigned char;
using GLbitfield = unsigned int;
using GLint = int;
using GLuint = unsigned int;
using GLsizei = int;
using GLfloat = float;
using GLchar = char;
using GLintptr = std::ptrdiff_t;
using GLsizeiptr = std::ptrdiff_t;

#if defined(_WIN32)
#  ifndef APIENTRY
#    define APIENTRY __stdcall
#  endif
#endif
#ifndef APIENTRY
#  define APIENTRY
#endif

// Note: Many OpenGL SDK headers define GL_* tokens as preprocessor macros
// (e.g. GL_FALSE). To avoid macro collisions, our constants use a trailing "_".
inline constexpr GLenum GL_FALSE_ = 0;
inline constexpr GLenum GL_TRUE_ = 1;
inline constexpr GLenum GL_TRIANGLES_ = 0x0004;
inline constexpr GLenum GL_LINES_ = 0x0001;
inline constexpr GLenum GL_FLOAT_ = 0x1406;
inline constexpr GLenum GL_UNSIGNED_BYTE_ = 0x1401;
inline constexpr GLenum GL_ARRAY_BUFFER_ = 0x8892;
inline constexpr GLenum GL_STATIC_DRAW_ = 0x88E4;
inline constexpr GLenum GL_DYNAMIC_DRAW_ = 0x88E8;
inline constexpr GLenum GL_VERTEX_SHADER_ = 0x8B31;
inline constexpr GLenum GL_FRAGMENT_SHADER_ = 0x8B30;
inline constexpr GLenum GL_COMPILE_STATUS_ = 0x8B81;
inline constexpr GLenum GL_LINK_STATUS_ = 0x8B82;
inline constexpr GLenum GL_INFO_LOG_LENGTH_ = 0x8B84;
inline constexpr GLenum GL_COLOR_BUFFER_BIT_ = 0x00004000;
inline constexpr GLenum GL_DEPTH_BUFFER_BIT_ = 0x00000100;
inline constexpr GLenum GL_DEPTH_TEST_ = 0x0B71;
inline constexpr GLenum GL_LESS_ = 0x0201;
inline constexpr GLenum GL_CULL_FACE_ = 0x0B44;
inline constexpr GLenum GL_BACK_ = 0x0405;
inline constexpr GLenum GL_BLEND_ = 0x0BE2;
inline constexpr GLenum GL_SRC_ALPHA_ = 0x0302;
inline constexpr GLenum GL_ONE_MINUS_SRC_ALPHA_ = 0x0303;
inline constexpr GLenum GL_PACK_ALIGNMENT_ = 0x0D05;

inline constexpr GLenum GL_TEXTURE_2D_ = 0x0DE1;
inline constexpr GLenum GL_TEXTURE0_ = 0x84C0;
inline constexpr GLenum GL_TEXTURE_MIN_FILTER_ = 0x2801;
inline constexpr GLenum GL_TEXTURE_MAG_FILTER_ = 0x2800;
inline constexpr GLenum GL_TEXTURE_WRAP_S_ = 0x2802;
inline constexpr GLenum GL_TEXTURE_WRAP_T_ = 0x2803;
inline constexpr GLenum GL_LINEAR_ = 0x2601;
inline constexpr GLenum GL_LINEAR_MIPMAP_LINEAR_ = 0x2703;
inline constexpr GLenum GL_REPEAT_ = 0x2901;
inline constexpr GLenum GL_RGB_ = 0x1907;
inline constexpr GLenum GL_RGBA_ = 0x1908;

using PFNGLCREATESHADERPROC = GLuint(APIENTRY*)(GLenum);
using PFNGLSHADERSOURCEPROC = void(APIENTRY*)(GLuint, GLsizei, const GLchar* const*, const GLint*);
using PFNGLCOMPILESHADERPROC = void(APIENTRY*)(GLuint);
using PFNGLGETSHADERIVPROC = void(APIENTRY*)(GLuint, GLenum, GLint*);
using PFNGLGETSHADERINFOLOGPROC = void(APIENTRY*)(GLuint, GLsizei, GLsizei*, GLchar*);
using PFNGLDELETESHADERPROC = void(APIENTRY*)(GLuint);

using PFNGLCREATEPROGRAMPROC = GLuint(APIENTRY*)();
using PFNGLATTACHSHADERPROC = void(APIENTRY*)(GLuint, GLuint);
using PFNGLLINKPROGRAMPROC = void(APIENTRY*)(GLuint);
using PFNGLGETPROGRAMIVPROC = void(APIENTRY*)(GLuint, GLenum, GLint*);
using PFNGLGETPROGRAMINFOLOGPROC = void(APIENTRY*)(GLuint, GLsizei, GLsizei*, GLchar*);
using PFNGLUSEPROGRAMPROC = void(APIENTRY*)(GLuint);
using PFNGLDELETEPROGRAMPROC = void(APIENTRY*)(GLuint);

using PFNGLGETUNIFORMLOCATIONPROC = GLint(APIENTRY*)(GLuint, const GLchar*);
using PFNGLUNIFORMMATRIX4FVPROC = void(APIENTRY*)(GLint, GLsizei, GLboolean, const GLfloat*);
using PFNGLUNIFORM3FPROC = void(APIENTRY*)(GLint, GLfloat, GLfloat, GLfloat);
using PFNGLUNIFORM2FPROC = void(APIENTRY*)(GLint, GLfloat, GLfloat);
using PFNGLUNIFORM1IPROC = void(APIENTRY*)(GLint, GLint);

using PFNGLGENVERTEXARRAYSPROC = void(APIENTRY*)(GLsizei, GLuint*);
using PFNGLBINDVERTEXARRAYPROC = void(APIENTRY*)(GLuint);
using PFNGLDELETEVERTEXARRAYSPROC = void(APIENTRY*)(GLsizei, const GLuint*);

using PFNGLGENBUFFERSPROC = void(APIENTRY*)(GLsizei, GLuint*);
using PFNGLBINDBUFFERPROC = void(APIENTRY*)(GLenum, GLuint);
using PFNGLBUFFERDATAPROC = void(APIENTRY*)(GLenum, GLsizeiptr, const void*, GLenum);
using PFNGLBUFFERSUBDATAPROC = void(APIENTRY*)(GLenum, GLintptr, GLsizeiptr, const void*);
using PFNGLDELETEBUFFERSPROC = void(APIENTRY*)(GLsizei, const GLuint*);

using PFNGLENABLEVERTEXATTRIBARRAYPROC = void(APIENTRY*)(GLuint);
using PFNGLVERTEXATTRIBPOINTERPROC = void(APIENTRY*)(GLuint, GLint, GLenum, GLboolean, GLsizei, const void*);

using PFNGLVIEWPORTPROC = void(APIENTRY*)(GLint, GLint, GLsizei, GLsizei);
using PFNGLCLEARCOLORPROC = void(APIENTRY*)(GLfloat, GLfloat, GLfloat, GLfloat);
using PFNGLCLEARPROC = void(APIENTRY*)(GLbitfield);
using PFNGLENABLEPROC = void(APIENTRY*)(GLenum);
using PFNGLDISABLEPROC = void(APIENTRY*)(GLenum);
using PFNGLDEPTHFUNCPROC = void(APIENTRY*)(GLenum);
using PFNGLCULLFACEPROC = void(APIENTRY*)(GLenum);
using PFNGLBLENDFUNCPROC = void(APIENTRY*)(GLenum, GLenum);

using PFNGLDRAWARRAYSPROC = void(APIENTRY*)(GLenum, GLint, GLsizei);
using PFNGLLINEWIDTHPROC = void(APIENTRY*)(GLfloat);
using PFNGLPIXELSTOREIPROC = void(APIENTRY*)(GLenum, GLint);
using PFNGLREADPIXELSPROC = void(APIENTRY*)(GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, void*);

using PFNGLGENTEXTURESPROC = void(APIENTRY*)(GLsizei, GLuint*);
using PFNGLBINDTEXTUREPROC = void(APIENTRY*)(GLenum, GLuint);
using PFNGLTEXIMAGE2DPROC = void(APIENTRY*)(GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, const void*);
using PFNGLTEXPARAMETERIPROC = void(APIENTRY*)(GLenum, GLenum, GLint);
using PFNGLGENERATEMIPMAPPROC = void(APIENTRY*)(GLenum);
using PFNGLACTIVETEXTUREPROC = void(APIENTRY*)(GLenum);
using PFNGLDELETETEXTURESPROC = void(APIENTRY*)(GLsizei, const GLuint*);

}  // namespace gl
}  // namespace simple

