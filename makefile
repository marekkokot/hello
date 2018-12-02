CC = g++
CFLAGS = -O3 -m64
hello: hello.cpp
  $(CC) $(CFLAGS) -o $@ @^
  
