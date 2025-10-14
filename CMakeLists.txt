cmake_minimum_required(VERSION 3.15)
project(NinjaQuadruple LANGUAGES C CXX Fortran)
include(GNUInstallDirs)
# Options for conditional features
option(QUADNINJA "Enable quadruple precision sources" OFF)
option(AVHOLO "Enable AVHolo interface" OFF)
option(GOSAM "Enable GoSam interface" OFF)
option(F90MODULE "Enable Fortran 90 module" OFF)
option(NINJAGOSAMCONTRIB "Use GoSam contrib mode" OFF)

add_definitions("-DVERSION=\"1.2.3\"")
add_definitions("-DNINJA_CONFIG_H_INTERNAL")
if (QUADNINJA)
add_definitions("-DQUADNINJA")
add_definitions("-DNINJA_QUADRUPLE")
endif()

# Include subdirectories
add_subdirectory(src)
#add_subdirectory(examples)



# Define extra distribution files (for packaging or install scripts)
set(EXTRA_DIST
    README.md
    PACKAGE_DESCRIPTION
    VERSION
    utils/setup.py
    utils/ninjanumgen/ninjanumgen
    utils/ninjanumgen/__init__.py
    utils/ninjanumgen/ninjanumgen.py
    utils/ninjanumgen/templates/ninja_laurent.frm
    utils/ninjanumgen/templates/ninjanumgen_template.cc
    utils/ninjanumgen/templates/ninjanumgen_template.hh
    utils/ninjanumgen/templates/ninja_opt.frm
)

# Optionally install or package these files
# install(FILES ${EXTRA_DIST} DESTINATION share/ninjaquadruple)

# Custom targets to mimic .PHONY rules
add_custom_target(examples-run
    COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target examples
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/examples
    COMMENT "Building examples target"
)

add_custom_target(thread-examples-run
    COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target thread-examples
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/examples
    COMMENT "Building thread-examples target"
)
