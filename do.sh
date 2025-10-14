#make clean
#autoreconf -i 
#./configure  --prefix=$(pwd)/MINSTALL --with-avholo=no --enable-quadninja=yes  --with-quadruple=no
#bear --output make.json -- make -j 10
#make install 
rm -rf BUILD
cmake -S . -B BUILD -DAVHOLO=OFF -DF90MODULE=ON  -DGOSAM=ON -DQUADNINJA=ON -DCMAKE_INSTALL_PREFIX=$(pwd)/CINSTALL -DCMAKE_INSTALL_LIBDIR=lib
bear --output cmake.json -- cmake --build BUILD -j 10
cmake --install BUILD
./file_differences.py  cmake.json make.json cm.txt m.txt
