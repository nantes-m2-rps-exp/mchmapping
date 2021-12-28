# Copyright CERN and copyright holders of ALICE O2. This software is distributed
# under the terms of the GNU General Public License v3 (GPL Version 3), copied
# verbatim in the file "COPYING".
#
# See http://alice-o2.web.cern.ch/license for full licensing information.
#
# In applying this license CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.

add_library(MCHMappingImpl4)
target_sources(MCHMappingImpl4 PRIVATE
        src/CreateSegmentation.cxx
        src/GenDetElemId2SegType.cxx
        src/GenDetElemId2SegType.h
        src/PadGroup.h
        src/PadGroupType.cxx
        src/PadGroupType.h
        src/CathodeSegmentationCImpl4.cxx
        src/CathodeSegmentationCreator.cxx
        src/CathodeSegmentationCreator.h
        src/CathodeSegmentationImpl4.cxx
        src/CathodeSegmentationImpl4.h
)
foreach(segtype RANGE 20)
        target_sources(MCHMappingImpl4 PRIVATE
                src/GenCathodeSegmentationCreatorForSegType${segtype}.cxx)
endforeach()

target_link_libraries(MCHMappingImpl4 PUBLIC Boost::headers 
                      MCHMappingInterface ${GSL} fmt::fmt)
target_include_directories(MCHMappingImpl4 
    PUBLIC 
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>)

include(GenerateExportHeader)
generate_export_header(MCHMappingImpl4 BASE_NAME o2mchmappingimpl4)

set_target_properties(MCHMappingImpl4 PROPERTIES CXX_VISIBILITY_PRESET hidden)
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
        target_compile_options(MCHMappingImpl4 PRIVATE -fext-numeric-literals)
endif()

install(TARGETS MCHMappingImpl4 EXPORT mchmapping)
