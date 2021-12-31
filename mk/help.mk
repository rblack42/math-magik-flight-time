# Makefile help system

.PHONY: help
help:	## display help messages
	@python $(MK)/pyhelp.py$(MAKEFILE_LIST)
