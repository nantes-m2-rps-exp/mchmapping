# Python bindings for MCH mapping library

> WARNING the original [MCH Mapping library](https://github.com/AliceO2Group/AliceO2/tree/dev/Detectors/MUON/MCH/Mapping) is using the hourglass pattern (C++ header only wide interface on top of a C narrow interface itself on top of a wider C++ library), and thus offers a C interface that should be the "natural" target for the Python bindings. 
> We might actually do that at some point, but here what we bind to is the C++ top-level interface. Not a big difference all in all, but should be noted.
