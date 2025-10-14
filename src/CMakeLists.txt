set(LIBNINJA_SOURCES
  basis.cc cuts_utils.cc ninja.cc Xcuts.cc
  cuts.cc Xninja.cc spinors.cc tensor_ninja.cc
  coefficient_level_subs.cc integral_library.cc
  avholo_interface.cc rambo.cc ninja_wraps.cc
)

if(QUADNINJA)
  set(QUAD_SOURCES
    quadsources/basis.cc quadsources/cuts_utils.cc quadsources/ninja.cc
    quadsources/Xcuts.cc quadsources/cuts.cc quadsources/Xninja.cc
    quadsources/spinors.cc quadsources/tensor_ninja.cc
    quadsources/coefficient_level_subs.cc quadsources/integral_library.cc
    quadsources/avholo_interface.cc quadsources/rambo.cc
    quadsources/ninja_wraps.cc
  )
  list(APPEND LIBNINJA_SOURCES ${QUAD_SOURCES})
endif()

if(AVHOLO)
  list(APPEND LIBNINJA_SOURCES avholo_wrapper.F90 ninjavholo_wraps.cc ninjavholo.F90)
  if(QUADNINJA)
    list(APPEND LIBNINJA_SOURCES quadsources/avholo_wrapper.F90)
  endif()
endif()

if(LOOPTOOLS)
  list(APPEND LIBNINJA_SOURCES looptools_interface.cc)
endif()

if(GOSAM)
  list(APPEND LIBNINJA_SOURCES gosam_interface.cc ninjago.F90)
endif()

if(F90MODULE)
  list(APPEND LIBNINJA_SOURCES mninja.F90)
endif()

if(QUADNINJA)
  find_program(SED NAMES gsed sed)
  make_directory(${CMAKE_BINARY_DIR}/src/quadsources/)
  set(GENQUADSCRIPT ${CMAKE_SOURCE_DIR}/src/quadsources/genquadsources.sed)
  foreach(src IN LISTS QUAD_SOURCES)
    get_filename_component(base ${src} NAME)
    list(APPEND LIBNINJA_SOURCES  ${CMAKE_BINARY_DIR}/src/${src})
    add_custom_command(
      OUTPUT ${src}
      COMMAND ${SED} -f ${GENQUADSCRIPT} < ${CMAKE_SOURCE_DIR}/src/${base} > ${CMAKE_BINARY_DIR}/src/${src}
      DEPENDS ${CMAKE_SOURCE_DIR}/src/${base} ${GENQUADSCRIPT}
      COMMENT "Generating ${src} from ${base}"
    )
  endforeach()
endif()


add_library(ninja SHARED ${LIBNINJA_SOURCES})

set_target_properties(ninja PROPERTIES OUTPUT_NAME ninja SOVERSION 0
  ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/outputs/${CMAKE_INSTALL_LIBDIR}/$<0:>
  LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/outputs/${CMAKE_INSTALL_LIBDIR}/$<0:>
  RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/outputs/${CMAKE_INSTALL_LIBDIR}/$<0:>
  EXPORT_NAME ninja::ninja)
set_target_properties(ninja PROPERTIES
  VERSION 0.0.0
)

target_include_directories(ninja PUBLIC 

$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
  $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)
# Optional Fortran include flags
if(AVHOLO)
  if(NINJAGOSAMCONTRIB)
    target_compile_options(ninja PRIVATE -I${CMAKE_SOURCE_DIR}/avh_olo-2.2.1)
  else()
    target_compile_options(ninja PRIVATE ${FCINCLUDE})
  endif()
endif()

# Optional library links
target_link_libraries(ninja PRIVATE ${AVHFLAGS} ${QUADRUPLEFLAGS})


# Set the module output directory (optional but recommended)
set_target_properties(ninja PROPERTIES
  Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
)

if(F90MODULE)

# Install the module file
install(
  FILES ${CMAKE_CURRENT_BINARY_DIR}/modules/mninja.mod
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
endif()

if(GOSAM)
  install(
  FILES ${CMAKE_CURRENT_BINARY_DIR}/modules/ninjago_module.mod
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
endif()

# Executable
add_executable(ninja-config ninja_config.cc)
target_link_libraries(ninja-config PRIVATE ninja)


#if(QUADNINJA)
#  add_subdirectory(quadninja)
#endif()
# Generated sources (QUADNINJA)


# Headers (not installed)
set(NINJA_HEADERS
  ninja_implem.cxx polys_implem.cxx basis.hh cuts.hh cuts_utils.hh Xcuts.hh
  cuts_utils-inl.hh coefficient_level_subs.hh integermath.hh tmp_utils.hh
  ninja_scoped_array.hh cuts_vector.hh integral_library_wrapper.hh
  s_mat_wrapper.hh avholo_decls.hh ninja_hash_table.hh integral_cache.hh
  gosam_interface.hh
)

if(QUADNINJA)
  list(APPEND NINJA_HEADERS
    quadsources/ninja_implem.cxx quadsources/polys_implem.cxx
    quadsources/basis.hh quadsources/cuts.hh quadsources/cuts_utils.hh
    quadsources/Xcuts.hh quadsources/cuts_utils-inl.hh
    quadsources/coefficient_level_subs.hh quadsources/integermath.hh
    quadsources/tmp_utils.hh quadsources/ninja_scoped_array.hh
    quadsources/cuts_vector.hh quadsources/integral_library_wrapper.hh
    quadsources/s_mat_wrapper.hh quadsources/avholo_decls.hh
    quadsources/ninja_hash_table.hh quadsources/integral_cache.hh
  )
endif()

# Clean rule for generated quad sources
if(QUADNINJA)
  set_directory_properties(PROPERTIES ADDITIONAL_MAKE_CLEAN_FILES
    "quadsources/*.cc;quadsources/*.hh;quadsources/*.cxx;quadsources/*.F90")
endif()

install(FILES
ninja/integral_library.hh  
ninja/ninja_config.h  
ninja/ninja_in.hh     
ninja/num_defs.hh  
ninja/s_mat.hh    
ninja/static_arrays.hh  
ninja/thread_safe_integral_library.hh  
ninja/zero_float.hh
ninja/momentum.hh          
ninja/ninja.hh       
ninja/ninjanumgen.hh  
ninja/rambo.hh     
ninja/spinors.hh  
ninja/tensor_ninja.hh   
ninja/types.hh
DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/ninja/
)
# Install the executable to the system's binary directory
install(TARGETS ninja-config
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)


# Install the library
install(TARGETS ninja 
  EXPORT ninjaTargets

  DESTINATION ${CMAKE_INSTALL_LIBDIR}
  #INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

# Export targets for use in other projects
install(EXPORT ninjaTargets
  FILE ninjaTargets.cmake
 # NAMESPACE ninja::
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/ninja
)
