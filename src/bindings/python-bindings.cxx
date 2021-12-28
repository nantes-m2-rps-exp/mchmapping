#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
using namespace pybind11::literals;
#include "MCHMappingInterface/Segmentation.h"
#include <utility>

namespace py = pybind11;
using namespace o2::mch::mapping;

#include <iostream>

void test(const char *name) {
  std::cout << "Big Hello from test, " << name << " !\n";
}

PYBIND11_MODULE(mchmapping, m) {
  m.doc() = "mchmapping plugin";

  m.def("test", &test, "A dummy function to say hello", "name"_a = "zob");

  py::class_<Segmentation>(m, "Segmentation")
      .def(py::init<int>())
      .def("nofPads", &Segmentation::nofPads)
      .def("isValid", &Segmentation::isValid, "paduid"_a)
      .def("findPadByFEE", &Segmentation::findPadByFEE, "dualSampaId"_a,
           "dualSampaChannel"_a)
      .def("padDualSampaId", &Segmentation::padDualSampaId, "paduid"_a)
      .def("padDualSampaChannel", &Segmentation::padDualSampaChannel,
           "paduid"_a)
      .def("padPositionX", &Segmentation::padPositionX, "paduid"_a)
      .def("padPositionY", &Segmentation::padPositionY, "paduid"_a)
      .def("padSizeX", &Segmentation::padSizeX, "paduid"_a)
      .def("padSizeY", &Segmentation::padSizeY, "paduid"_a)
      .def("isBendingPad", &Segmentation::isBendingPad, "paduid"_a)
      .def("padAsString", &Segmentation::padAsString, "paduid"_a)
      .def(
          "findPadPairByPosition",
          [](const Segmentation &seg, float x, float y) {
            int b, nb;
            bool ok = seg.findPadPairByPosition(x, y, b, nb);
            return std::tuple<bool, int, int>(ok, b, nb);
          },
          "x"_a, "y"_a)
      .def(
          "neighbours",
          [](const Segmentation &seg, int paduid) {
            std::vector<int> nei;
            seg.forEachNeighbouringPad(paduid, [&nei](int depadindex) {
              nei.emplace_back(depadindex);
            });
            return nei;
          },
          "paduid"_a);
}
