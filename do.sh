
rm -rf BUILD
cmake -S . -B BUILD -DAVHOLO=OFF -DF90MODULE=OFF  -DGOSAM=OFF -DQUADNINJA=OFF -DCMAKE_INSTALL_PREFIX=$(pwd)/CINSTALL -DCMAKE_INSTALL_LIBDIR=lib
bear --output cmake.json -- cmake --build BUILD -j 10
cmake --install BUILD


./file_differences.py  cmake.json ../makeninja/make.json cm.txt m.txt
nm -D BUILD/src/libninja.so | tr -s ' '| cut -f 2,3 -d' ' | sort > socm.txt
nm -D ../makeninja/src/.libs/libninja.so | tr -s ' '| cut -f 2,3 -d' ' | sort > som.txt

exit
make clean
autoreconf -i 
./configure  --prefix=$(pwd)/MINSTALL --with-avholo=no --enable-quadninja=no  --with-quadruple=no --disable-f90module --disable-gosam
bear --output make.json -- make -j 10
make install 
