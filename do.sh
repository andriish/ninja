make clean
autoreconf -i 
./configure  --with-avholo=no --enable-quadninja=no --disable-f90module --with-quadruple=no
bear --output make.json -- make 
rm -rf BUILD
cmake -S . -B BUILD -DAVHOLO=OFF
bear --output cmake.json -- cmake --build BUILD
./file_differences.py  cmake.json make.json cm.txt m.txt
