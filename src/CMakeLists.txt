add_subdirectory(Interface)
add_subdirectory(Impl4)

if(BUILD_PYTHON_BINDINGS)
  add_subdirectory(bindings)
endif()

