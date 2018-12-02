CC = g++
CFLAGS = -O3 -m64

hello: main.cpp
	$(CC) $(CFLAGS) -o $@ $^
  
