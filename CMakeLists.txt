cmake_minimum_required(VERSION 3.15)
project(ninja VERSION 1.2.0 LANGUAGES C CXX Fortran)
include(GNUInstallDirs)
# Options for conditional features
option(QUADNINJA "Enable quadruple precision sources" OFF)
option(AVHOLO "Enable AVHolo interface" OFF)
option(GOSAM "Enable GoSam interface" OFF)
option(F90MODULE "Enable Fortran 90 module" OFF)
option(NINJAGOSAMCONTRIB "Use GoSam contrib mode" OFF)

add_definitions("-DHAVE_CONFIG_H")
add_definitions("-DPIC")
set(CAPITAL_CMAKE_PROJECT_NAME "Ninja")
set(NINJA_CONFIG_H_INTERNAL 1)
set(NINJA_USE_ONELOOP OFF)
#set(NINJA_USE_ONELOOP_WITH_CACHE 1)
#set(NINJA_USE_LOOPTOOLS 1)
set(NINJA_MASSLESS 1)
set(NINJA_X1RANK 1)
#if (QUADNINJA)
#set("-DQUADNINJA")
#set("-DNINJA_QUADRUPLE")
#endif()


set(CONFIG_H_CONTENT 
"/* config.h.  Generated from config.h.in by configure.  */\n\
/* config.h.in.  Generated from configure.ac by autoheader.  */\n\n\
/* Define to 1 if you have C++11 random numbers library compatible with\n   __float128 type of libquadmath. */\n\
$<IF:$<BOOL:${HAVE_CXX11_FLOAT128_RANDOM}>,#define HAVE_CXX11_FLOAT128_RANDOM 1,/* #undef HAVE_CXX11_FLOAT128_RANDOM */>\n\n\
/* Define to 1 if you have C++11 random numbers library. */\n\
#define HAVE_CXX11_RANDOM 1\n\n\
/* Define to 1 if you have C++11 `decltype' operator and std::common_type\n   traits. */\n\
#define HAVE_DECLTYPE 1\n\n\
/* Define to 1 if you have the <dlfcn.h> header file. */\n\
#define HAVE_DLFCN_H 1\n\n\
/* Define to 1 if you have C++11 initizializer lists in array-data-members\n   initialization. */\n\
#define HAVE_INIT_LIST 1\n\n\
/* Define to 1 if you have the <inttypes.h> header file. */\n\
#define HAVE_INTTYPES_H 1\n\n\
/* Define if you have POSIX threads libraries and header files. */\n\
#define HAVE_PTHREAD 1\n\n\
/* Have PTHREAD_PRIO_INHERIT. */\n\
#define HAVE_PTHREAD_PRIO_INHERIT 1\n\n\
/* Define to 1 if you have the <stdint.h> header file. */\n\
#define HAVE_STDINT_H 1\n\n\
/* Define to 1 if you have the <stdio.h> header file. */\n\
#define HAVE_STDIO_H 1\n\n\
/* Define to 1 if you have the <stdlib.h> header file. */\n\
#define HAVE_STDLIB_H 1\n\n\
/* Define to 1 if you have the <strings.h> header file. */\n\
#define HAVE_STRINGS_H 1\n\n\
/* Define to 1 if you have the <string.h> header file. */\n\
#define HAVE_STRING_H 1\n\n\
/* Define to 1 if you have the <sys/stat.h> header file. */\n\
#define HAVE_SYS_STAT_H 1\n\n\
/* Define to 1 if you have the <sys/types.h> header file. */\n\
#define HAVE_SYS_TYPES_H 1\n\n\
/* Define to 1 if you have the <unistd.h> header file. */\n\
#define HAVE_UNISTD_H 1\n\n\
/* Define to the sub-directory where libtool stores uninstalled libraries. */\n\
#define LT_OBJDIR \".libs/\"\n\n\
/* Define to 1 if this an internal is a source file. */\n\
$<IF:$<BOOL:${NINJA_CONFIG_H_INTERNAL}>,#define NINJA_CONFIG_H_INTERNAL 1,/* #undef NINJA_CONFIG_H_INTERNAL */>\n\n\
/* Define to 1 massless specialization is enabled. */\n\
$<IF:$<BOOL:${NINJA_MASSLESS}>,#define NINJA_MASSLESS 1,/* #undef NINJA_MASSLESS */>\n\n\
/* Define to 1 if Ninja is compiled in quadruple precision. */\n\
$<IF:$<BOOL:${NINJA_QUADRUPLE}>,#define NINJA_QUADRUPLE 1,/* #undef NINJA_QUADRUPLE */>\n\n\
/* Define if you have LoopTools. */\n\
$<IF:$<BOOL:${NINJA_USE_LOOPTOOLS}>,#define NINJA_USE_LOOPTOOLS 1,/* #undef NINJA_USE_LOOPTOOLS */>\n\n\
/* Define to 1 if you have OneLoop. */\n\
$<IF:$<BOOL:${NINJA_USE_ONELOOP}>,#define NINJA_USE_ONELOOP 1,/* #undef NINJA_USE_ONELOOP */>\n\n\
/* Define to 1 if a cache of Master Integrals is implemented for OneLoop. */\n\
$<IF:$<BOOL:${NINJA_USE_ONELOOP_WITH_CACHE}>,#define NINJA_USE_ONELOOP_WITH_CACHE 1,/* #undef NINJA_USE_ONELOOP_WITH_CACHE */>\n\n\
/* Define to 1 if higher-rank support is enabled. */\n\
$<IF:$<BOOL:${NINJA_X1RANK}>,#define NINJA_X1RANK 1,/* #undef NINJA_X1RANK */>\n\n\
/* Name of package */\n\
#define PACKAGE \"${CMAKE_PROJECT_NAME}\"\n\n\
/* Define to the address where bug reports for this package should be sent. */\n\
#define PACKAGE_BUGREPORT \"tiziano.peraro@ed.ac.uk\"\n\n\
/* Define to the full name of this package. */\n\
#define PACKAGE_NAME \"${CAPITAL_CMAKE_PROJECT_NAME}\"\n\n\
/* Define to the full name and version of this package. */\n\
#define PACKAGE_STRING \"${CAPITAL_CMAKE_PROJECT_NAME} ${CMAKE_PROJECT_VERSION}\"\n\n\
/* Define to the one symbol short name of this package. */\n\
#define PACKAGE_TARNAME \"${CMAKE_PROJECT_NAME}\"\n\n\
/* Define to the home page for this package. */\n\
#define PACKAGE_URL \"\"\n\n\
/* Define to the version of this package. */\n\
#define PACKAGE_VERSION \"${CMAKE_PROJECT_VERSION}\"\n\n\
/* Define to necessary symbol if this constant uses a non-standard name on\n   your system. */\n\
$<IF:$<BOOL:${PTHREAD_CREATE_JOINABLE}>,#define PTHREAD_CREATE_JOINABLE 1,/* #undef PTHREAD_CREATE_JOINABLE */>\n\n\
/* Define to 1 if QuadNinja is built. */\n\
$<IF:$<BOOL:${QUADNINJA}>,#define QUADNINJA 1,/* #undef QUADNINJA */>\n\n\
/* Macro for QuadNinja */\n\
$<IF:$<BOOL:${QUADNINJA_CONFIG_H_INTERNAL}>,#define QUADNINJA_CONFIG_H_INTERNAL 1,/* #undef QUADNINJA_CONFIG_H_INTERNAL */>\n\n\
/* Macro for QuadNinja */\n\
$<IF:$<BOOL:${QUADNINJA_MASSLESS}>,#define QUADNINJA_MASSLESS 1,/* #undef QUADNINJA_MASSLESS */>\n\n\
/* Macro for QuadNinja */\n\
$<IF:$<BOOL:${QUADNINJA_USE_ONELOOP}>,#define QUADNINJA_USE_ONELOOP 1,/* #undef QUADNINJA_USE_ONELOOP */>\n\n\
/* Macro for QuadNinja */\n\
$<IF:$<BOOL:${QUADNINJA_USE_ONELOOP_WITH_CACHE}>,#define QUADNINJA_USE_ONELOOP_WITH_CACHE 1,/* #undef QUADNINJA_USE_ONELOOP_WITH_CACHE */>\n\n\
/* Macro for QuadNinja */\n\
$<IF:$<BOOL:${QUADNINJA_X1RANK}>,#define QUADNINJA_X1RANK 1,/* #undef QUADNINJA_X1RANK */>\n\n\
/* Define to 1 if all of the C89 standard headers exist (not just the ones\n\
   required in a freestanding environment). This macro is provided for\n\
   backward compatibility; new code need not use it. */\n\
#define STDC_HEADERS 1\n\
\n\
/* Version number of package */\n\
#define VERSION \"${CMAKE_PROJECT_VERSION}\"")


set(NINJA_CONFIG_H_CONTENT
"\n\
\n\
/* Define to 1 if ninja is compiled in quadruple precision. */\n\
#ifndef NINJA_QUADRUPLE\n\
#undef NINJA_QUADRUPLE\n\
#endif\n\
\n\
/* Define if you have LoopTools. */\n\
#ifndef NINJA_USE_LOOPTOOLS\n\
#undef NINJA_USE_LOOPTOOLS\n\
#endif\n\
\n\
/* Define if you have OneLoop. */\n\
#ifndef NINJA_USE_ONELOOP\n\
#undef NINJA_USE_ONELOOP\n\
#endif\n\
\n\
/* Define to 1 if quadninja is compiled. */\n\
#ifndef QUADNINJA\n\
#undef QUADNINJA\n\
#endif\n\
") 


file(GENERATE OUTPUT ${CMAKE_BINARY_DIR}/config.h CONTENT "${CONFIG_H_CONTENT}")

file(GENERATE OUTPUT ${CMAKE_BINARY_DIR}/src/ninja/ninja_config.h CONTENT "${NINJA_CONFIG_H_CONTENT}")


include(CheckCXXCompilerFlag)
set(GNU_CXX_FLAGS_TO_CHECK "-fcx-fortran-rules;-O2;-g")
foreach(fl ${${CMAKE_CXX_COMPILER_ID}_CXX_FLAGS_TO_CHECK})
  CHECK_CXX_COMPILER_FLAG(${fl} CXX_COMPILER_SUPPORTS_${fl})
    if(CXX_COMPILER_SUPPORTS_${fl})
      set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${fl}")
    endif()
endforeach()
#add_definitions("-DNINJA_CONFIG_H_INTERNAL")
#add_definitions("-DNINJA_USE_ONELOOP")
#add_definitions("-DNINJA_USE_ONELOOP_WITH_CACHE")
#add_definitions("-DNINJA_USE_LOOPTOOLS")
#add_definitions("-DNINJA_MASSLESS")
#add_definitions("-DNINJA_X1RANK")

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
