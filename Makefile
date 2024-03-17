obj = spidey
src = *.cpp

all: $(obj)
$(obj) : $(src)
	@g++ -std=c++11 -o $(obj) $(src)
	@echo $(obj) ready to go ...!
fclean:
	@rm -rf $(obj)
	@echo clean ...!
re: fclean all