PROJECT := flight-time
MK	:= mk

all:

include $(MK)/python.mk
include $(MK)/help.mk
include $(MK)/jupyter.mk

