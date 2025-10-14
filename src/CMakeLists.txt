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

add_library(ninja STATIC ${LIBNINJA_SOURCES})
target_include_directories(ninja PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

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

# Executable
add_executable(ninja-config ninja_config.cc)
target_link_libraries(ninja-config PRIVATE ninja)

# Generated sources (QUADNINJA)
if(QUADNINJA)
  set(GENQUADSCRIPT ${CMAKE_SOURCE_DIR}/src/quadsources/genquadsources.sed)
  foreach(src IN LISTS QUAD_SOURCES)
    get_filename_component(base ${src} NAME)
    add_custom_command(
      OUTPUT ${src}
      COMMAND ${SED} -f ${GENQUADSCRIPT} < ${CMAKE_SOURCE_DIR}/src/${base} > ${src}
      DEPENDS ${CMAKE_SOURCE_DIR}/src/${base} ${GENQUADSCRIPT}
      COMMENT "Generating ${src} from ${base}"
    )
  endforeach()
endif()

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
