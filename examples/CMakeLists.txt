# Define common include and link flags
set(OTHEREXAMPLES_CPPFLAGS ${CMAKE_INSTALL_INCLUDEDIR})
set(OTHEREXAMPLES_LDADD ninja ${AVHFLAGS} ${LTFLAGS} ${QUADRUPLEFLAGS})

# Helper macro to define an example
function(add_example name)
  add_executable(${name} ${ARGN})
  target_include_directories(${name} PRIVATE ${OTHEREXAMPLES_CPPFLAGS})
  target_link_libraries(${name} PRIVATE ${OTHEREXAMPLES_LDADD})
endfunction()

# Standard examples
add_example(simple_test simple_test.cc mynum.cc)
add_example(simple_higher_rank_test simple_higher_rank_test.cc mynumhr.cc)
add_example(4photons 4photons.cc 4photons_num.cc 4photons_init.cc)
add_example(6photons 6photons.cc 6photons_num.cc 6photons_init.cc)
add_example(ttbarh ttbarh.cc ttbarh_num.cc ttbarh_init.cc)
add_example(tensor_test tensor_test.cc)
add_example(tensor_higher_rank_test tensor_higher_rank_test.cc)

# Threaded examples
add_executable(thread_6photons thread_6photons.cc 6photons_num.cc 6photons_init.cc)
target_include_directories(thread_6photons PRIVATE ${OTHEREXAMPLES_CPPFLAGS} ${PTHREAD_CFLAGS})
target_link_libraries(thread_6photons PRIVATE ${OTHEREXAMPLES_LDADD} ${PTHREAD_LIBS})

add_executable(thread_4photons thread_4photons.cc 4photons_num.cc 4photons_init.cc)
target_include_directories(thread_4photons PRIVATE ${OTHEREXAMPLES_CPPFLAGS} ${PTHREAD_CFLAGS})
target_link_libraries(thread_4photons PRIVATE ${OTHEREXAMPLES_LDADD} ${PTHREAD_LIBS})

# Optional QUADNINJA example
if(QUADNINJA)
  add_example(quadninja_test quadninja_test.cc quadmynum.cc mynum.cc)
endif()

# Extra distribution files (for packaging or install scripts)
set(EXTRA_DIST
  mynum.frm mynumhr.frm 4photons.frm 6photons.frm ttbarh.frm
  simple_test.sh simple_higher_rank_test.sh 4photons.sh 6photons.sh ttbarh.sh
  simple_test.py simple_higher_rank_test.py 4photons.py 6photons.py ttbarh.py
)

# Optional: install or package these files
# install(FILES ${EXTRA_DIST} DESTINATION share/ninja/examples)

# Custom phony-style targets
add_custom_target(examples DEPENDS
  simple_test simple_higher_rank_test 4photons 6photons ttbarh
  tensor_test tensor_higher_rank_test
  $<$<BOOL:${QUADNINJA}>:quadninja_test>
)

add_custom_target(thread-examples DEPENDS thread_6photons thread_4photons)
