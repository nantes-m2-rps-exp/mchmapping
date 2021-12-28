include(CMakeFindDependencyMacro)
find_dependency(ROOT)
find_dependency(fmt)
find_dependency(Microsoft.GSL)
find_dependency(Boost)

include(${CMAKE_CURRENT_LIST_DIR}/mchmapping.cmake)

