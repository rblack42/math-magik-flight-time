PROJECT := flight-time
MK	:= ~/_sys/mk

all:

include $(MK)/python.mk
include $(MK)/help.mk
include $(MK)/jupyter.mk

