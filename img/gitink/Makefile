SRCS = $(wildcard *.txt)
OBJS = $(patsubst %.txt,%.svg,$(SRCS))

all: $(OBJS)

%.svg: %.txt
	gitink $< > $@

clean: 
	rm *.svg
