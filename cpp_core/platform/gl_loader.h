#pragma once

#include "gl_api.h"

namespace simple {
namespace gl {

extern PFNGLCREATESHADERPROC CreateShader;
extern PFNGLSHADERSOURCEPROC ShaderSource;
extern PFNGLCOMPILESHADERPROC CompileShader;
extern PFNGLGETSHADERIVPROC GetShaderiv;
extern PFNGLGETSHADERINFOLOGPROC GetShaderInfoLog;
extern PFNGLDELETESHADERPROC DeleteShader;

extern PFNGLCREATEPROGRAMPROC CreateProgram;
extern PFNGLATTACHSHADERPROC AttachShader;
extern PFNGLLINKPROGRAMPROC LinkProgram;
extern PFNGLGETPROGRAMIVPROC GetProgramiv;
extern PFNGLGETPROGRAMINFOLOGPROC GetProgramInfoLog;
extern PFNGLUSEPROGRAMPROC UseProgram;
extern PFNGLDELETEPROGRAMPROC DeleteProgram;

extern PFNGLGETUNIFORMLOCATIONPROC GetUniformLocation;
extern PFNGLUNIFORMMATRIX4FVPROC UniformMatrix4fv;
extern PFNGLUNIFORM3FPROC Uniform3f;
extern PFNGLUNIFORM2FPROC Uniform2f;
extern PFNGLUNIFORM1IPROC Uniform1i;

extern PFNGLGENVERTEXARRAYSPROC GenVertexArrays;
extern PFNGLBINDVERTEXARRAYPROC BindVertexArray;
extern PFNGLDELETEVERTEXARRAYSPROC DeleteVertexArrays;

extern PFNGLGENBUFFERSPROC GenBuffers;
extern PFNGLBINDBUFFERPROC BindBuffer;
extern PFNGLBUFFERDATAPROC BufferData;
extern PFNGLBUFFERSUBDATAPROC BufferSubData;
extern PFNGLDELETEBUFFERSPROC DeleteBuffers;

extern PFNGLENABLEVERTEXATTRIBARRAYPROC EnableVertexAttribArray;
extern PFNGLVERTEXATTRIBPOINTERPROC VertexAttribPointer;

extern PFNGLVIEWPORTPROC Viewport;
extern PFNGLCLEARCOLORPROC ClearColor;
extern PFNGLCLEARPROC Clear;
extern PFNGLENABLEPROC Enable;
extern PFNGLDISABLEPROC Disable;
extern PFNGLDEPTHFUNCPROC DepthFunc;
extern PFNGLCULLFACEPROC CullFace;
extern PFNGLBLENDFUNCPROC BlendFunc;

extern PFNGLDRAWARRAYSPROC DrawArrays;
extern PFNGLLINEWIDTHPROC LineWidth;
extern PFNGLPIXELSTOREIPROC PixelStorei;
extern PFNGLREADPIXELSPROC ReadPixels;

extern PFNGLGENTEXTURESPROC GenTextures;
extern PFNGLBINDTEXTUREPROC BindTexture;
extern PFNGLTEXIMAGE2DPROC TexImage2D;
extern PFNGLTEXPARAMETERIPROC TexParameteri;
extern PFNGLGENERATEMIPMAPPROC GenerateMipmap;
extern PFNGLACTIVETEXTUREPROC ActiveTexture;
extern PFNGLDELETETEXTURESPROC DeleteTextures;

bool load(void* (*get_proc_address)(const char*));

}  // namespace gl
}  // namespace simple

