PROJECT := mmflyer
MK	:= mk

all:

include $(MK)/python.mk
include $(MK)/help.mk
include $(MK)/jupyter.mk
include $(MK)/sphinx.mk
include $(MK)/version.mk
include $(MK)/pypi.mk

