find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(mchmapping SHARED python-bindings.cxx THIN_LTO)
target_link_libraries(mchmapping PUBLIC MCHMappingImpl4)

# Support for running from build directory
file(WRITE "${PROJECT_BINARY_DIR}/pytest.ini" "[pytest]\n" 
                                              "testpaths = ${CMAKE_CURRENT_SOURCE_DIR}\n")

# Support plain "pytest" in addition to "python -m pytest"
file(WRITE "${PROJECT_BINARY_DIR}/conftest.py" "import sys\n"
                                               "sys.path.insert(0, '${PROJECT_BINARY_DIR}')\n")

# Look for all the tests
file(GLOB MCHMAPPING_PY_TESTS CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/test_*.py")

# Add each test
foreach(TEST_FILE IN LISTS MCHMAPPING_PY_TESTS)
  get_filename_component(TEST_NAME "${TEST_FILE}" NAME_WE)
  add_test(
        NAME ${TEST_NAME}
        COMMAND ${PYTHON_EXECUTABLE} -m pytest "${TEST_FILE}" --rootdir=.
        WORKING_DIRECTORY "${PROJECT_BINARY_DIR}")
  set_tests_properties(${TEST_NAME} PROPERTIES LABELS python)
endforeach()

add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND} --verbose)

install(TARGETS mchmapping LIBRARY DESTINATION lib/python${Python_VERSION_MAJOR}.${Python_VERSION_MINOR}/site-packages)
