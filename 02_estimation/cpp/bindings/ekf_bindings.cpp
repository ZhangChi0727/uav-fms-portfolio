/**
 * @file ekf_bindings.cpp
 * @brief pybind11 Python bindings for C++ EKF
 *
 * Exposes EKF class to Python as ekf_cpp.EKF
 *
 * Status: placeholder — Phase 3D
 */
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include "ekf.hpp"

namespace py = pybind11;

PYBIND11_MODULE(ekf_cpp, m) {
    m.doc() = "C++17 EKF with pybind11 Python bindings";

    py::class_<uav_fms::EKF>(m, "EKF")
        .def(py::init<>())
        .def("predict", &uav_fms::EKF::predict,
             py::arg("accel"), py::arg("gyro"), py::arg("dt"))
        .def("update_gps", &uav_fms::EKF::update_gps,
             py::arg("z_gps"))
        .def("state", &uav_fms::EKF::state)
        .def("covariance", &uav_fms::EKF::covariance);
}
