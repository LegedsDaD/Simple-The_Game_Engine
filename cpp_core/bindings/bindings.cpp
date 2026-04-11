#include <pybind11/functional.h>
#include <pybind11/pybind11.h>

#include "../math/transform.h"
#include "../scene/entity.h"
#include "../scene/scene.h"

namespace py = pybind11;

namespace {

simple::math::Vec3 vec3_from_obj(const py::object& obj) {
  if (py::isinstance<py::tuple>(obj) || py::isinstance<py::list>(obj)) {
    py::sequence s = obj.cast<py::sequence>();
    if (py::len(s) != 3) throw std::runtime_error("Expected a 3-tuple/list");
    return {s[0].cast<float>(), s[1].cast<float>(), s[2].cast<float>()};
  }
  // Allow passing an existing Vec3.
  return obj.cast<simple::math::Vec3>();
}

py::tuple vec3_to_tuple(const simple::math::Vec3& v) { return py::make_tuple(v.x, v.y, v.z); }

}  // namespace

PYBIND11_MODULE(_simple_core, m) {
  m.doc() = "Simple Engine core (C++/OpenGL)";

  py::class_<simple::math::Vec3>(m, "Vec3")
      .def(py::init<>())
      .def(py::init<float, float, float>(), py::arg("x"), py::arg("y"), py::arg("z"))
      .def_readwrite("x", &simple::math::Vec3::x)
      .def_readwrite("y", &simple::math::Vec3::y)
      .def_readwrite("z", &simple::math::Vec3::z)
      .def("__iter__", [](const simple::math::Vec3& v) { return py::make_iterator(&v.x, (&v.x) + 3); },
           py::keep_alive<0, 1>())
      .def("__repr__", [](const simple::math::Vec3& v) {
        return "Vec3(" + std::to_string(v.x) + ", " + std::to_string(v.y) + ", " + std::to_string(v.z) + ")";
      });

  py::class_<simple::math::Transform>(m, "Transform")
      .def(py::init<>())
      .def_property(
          "position", [](const simple::math::Transform& t) { return vec3_to_tuple(t.position); },
          [](simple::math::Transform& t, const py::object& v) { t.position = vec3_from_obj(v); })
      .def_property(
          "rotation", [](const simple::math::Transform& t) { return vec3_to_tuple(t.rotation); },
          [](simple::math::Transform& t, const py::object& v) { t.rotation = vec3_from_obj(v); })
      .def_property(
          "scale", [](const simple::math::Transform& t) { return vec3_to_tuple(t.scale); },
          [](simple::math::Transform& t, const py::object& v) { t.scale = vec3_from_obj(v); })
      .def("model_matrix", [](const simple::math::Transform& t) {
        const simple::math::Mat4 m4 = t.model_matrix();
        py::list out;
        for (int i = 0; i < 16; ++i) out.append(m4.m[i]);
        return out;
      });

  py::class_<simple::Entity, simple::EntityPtr>(m, "Entity").def("update", &simple::Entity::update);

  py::class_<simple::Cube, simple::Entity, simple::CubePtr>(m, "Cube")
      .def(py::init<>())
      .def_property(
          "position", [](const simple::Cube& c) { return vec3_to_tuple(c.transform().position); },
          [](simple::Cube& c, const py::object& v) { c.transform().position = vec3_from_obj(v); })
      .def_property(
          "rotation", [](const simple::Cube& c) { return vec3_to_tuple(c.transform().rotation); },
          [](simple::Cube& c, const py::object& v) { c.transform().rotation = vec3_from_obj(v); })
      .def_property(
          "scale", [](const simple::Cube& c) { return vec3_to_tuple(c.transform().scale); },
          [](simple::Cube& c, const py::object& v) { c.transform().scale = vec3_from_obj(v); })
      .def_property(
          "color", [](const simple::Cube& c) { return vec3_to_tuple(c.color()); },
          [](simple::Cube& c, const py::object& v) { c.color() = vec3_from_obj(v); })
      .def_property(
          "spin", [](const simple::Cube& c) { return vec3_to_tuple(c.spin_deg_per_sec()); },
          [](simple::Cube& c, const py::object& v) { c.spin_deg_per_sec() = vec3_from_obj(v); })
      .def_property("texture", [](const simple::Cube& c) { return c.texture_path(); },
                    [](simple::Cube& c, const std::string& p) { c.texture_path() = p; });

  py::class_<simple::Camera>(m, "Camera")
      .def(py::init<>())
      .def_property(
          "position", [](const simple::Camera& cam) { return vec3_to_tuple(cam.transform.position); },
          [](simple::Camera& cam, const py::object& v) { cam.transform.position = vec3_from_obj(v); })
      .def_property(
          "rotation", [](const simple::Camera& cam) { return vec3_to_tuple(cam.transform.rotation); },
          [](simple::Camera& cam, const py::object& v) { cam.transform.rotation = vec3_from_obj(v); })
      .def_readwrite("fov_degrees", &simple::Camera::fov_degrees)
      .def_readwrite("z_near", &simple::Camera::z_near)
      .def_readwrite("z_far", &simple::Camera::z_far);

  py::class_<simple::Scene>(m, "Scene")
      .def(py::init<>())
      .def("add", &simple::Scene::add, py::arg("entity"))
      .def("remove", &simple::Scene::remove, py::arg("entity"))
      .def("clear", &simple::Scene::clear)
      .def("run", &simple::Scene::run, py::arg("width") = 900, py::arg("height") = 600, py::arg("title") = "Simple")
      .def("disable_branding", &simple::Scene::disable_branding)
      .def_property(
          "background",
          [](simple::Scene& s) { return vec3_to_tuple(s.background_color()); },
          [](simple::Scene& s, const py::object& v) { s.set_background_color(vec3_from_obj(v)); })
      .def_property_readonly("time_seconds", &simple::Scene::time_seconds)
      .def_property_readonly("fps", &simple::Scene::fps)
      .def_property_readonly("frame_index", &simple::Scene::frame_index)
      .def("draw_text",
           [](simple::Scene& s, const std::string& text, float x_px, float y_px, float scale, const py::object& color) {
             s.draw_text(text, x_px, y_px, scale, vec3_from_obj(color));
           },
           py::arg("text"), py::arg("x"), py::arg("y"), py::arg("scale") = 1.0f, py::arg("color") = py::make_tuple(1, 1, 1))
      .def("set_title", &simple::Scene::set_title, py::arg("title"))
      .def("set_vsync", &simple::Scene::set_vsync, py::arg("enabled"))
      .def("draw_line3d",
           [](simple::Scene& s, const py::object& a, const py::object& b, const py::object& color) {
             s.draw_line3d(vec3_from_obj(a), vec3_from_obj(b), vec3_from_obj(color));
           },
           py::arg("a"), py::arg("b"), py::arg("color") = py::make_tuple(1, 1, 1))
      .def("screenshot", &simple::Scene::request_screenshot, py::arg("path"))
      .def_property_readonly("camera", [](simple::Scene& s) -> simple::Camera& { return s.camera(); },
                             py::return_value_policy::reference_internal)
      .def("set_update_callback",
           [](simple::Scene& s, py::function fn) {
             s.set_update_callback([fn = std::move(fn)](float dt) {
               py::gil_scoped_acquire gil;
               fn(dt);
             });
           },
           py::arg("fn"))
      .def("key_down", &simple::Scene::key_down, py::arg("key"))
      .def("key_pressed", &simple::Scene::key_pressed, py::arg("key"))
      .def("mouse_down", &simple::Scene::mouse_down, py::arg("button"))
      .def("mouse_pressed", &simple::Scene::mouse_pressed, py::arg("button"))
      .def("mouse_position",
           [](const simple::Scene& s) {
             double x = 0.0, y = 0.0;
             s.mouse_position(x, y);
             return py::make_tuple(x, y);
           })
      .def("mouse_delta",
           [](const simple::Scene& s) {
             double dx = 0.0, dy = 0.0;
             s.mouse_delta(dx, dy);
             return py::make_tuple(dx, dy);
           });

  // Convenience: key/button constants (mirrors GLFW values users most often need).
  m.attr("KEY_ESCAPE") = py::int_(256);
  m.attr("KEY_W") = py::int_(87);
  m.attr("KEY_A") = py::int_(65);
  m.attr("KEY_S") = py::int_(83);
  m.attr("KEY_D") = py::int_(68);
  m.attr("KEY_P") = py::int_(80);
  m.attr("KEY_V") = py::int_(86);
  m.attr("KEY_R") = py::int_(82);
  m.attr("KEY_SPACE") = py::int_(32);
  m.attr("MOUSE_LEFT") = py::int_(0);
  m.attr("MOUSE_RIGHT") = py::int_(1);
}
