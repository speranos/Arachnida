#include <iostream>
#include "Arachnida.hpp"


void	ft_welcome(){
	std::cout << R"(

##########################################################
# __        __   _                            _____      #
# \ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__   #
#  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \  #
#   \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) | #
#    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/  #
#  ____        _     _                                   #
# / ___| _ __ (_) __| | ___ _   _          / - \       	 #
# \___ \| '_ \| |/ _` |/ _ \ | | |       \_\(_)/_/   	 #
#  ___) | |_) | | (_| |  __/ |_| |       __//"\__        #
# |____/| .__/|_|\__,_|\___|\__, |         /   \         #
#       |_|                 |___/      By Speranos       #
# Spider is slow, but its web catches the fastest flies. #
##########################################################

)" << std::endl;

}

void	ft_option(){
std::cout << R"(
		./spidey [-rlp] URL

• Option -r : recursively downloads the images from the URL.

• Option -r -l [N] : indicates the maximum depth level of the recursive download.
If not indicated, it will be 5.

• Option -p [PATH] : indicates the path where the downloaded files will be saved.
If not specified, ./data/ will be used.

)" << std::endl;
}

void	ft_exit(){
	ft_option();
	exit(EXIT_FAILURE);
}

void    ft_parsse_input(int ac, char **av, Arachnida *MyArachnida){
	try{
	int	i = 1;
	std::string	input;

	while (i < ac)
	{
		input = av[i];
		if(input == "-r")
			MyArachnida->recursive = true;
		else if(input == "-l"){
			if(!MyArachnida->recursive || (++i >= ac))
				ft_exit();
			else
				MyArachnida->max_rec = std::stoi(av[i]);

		}
		i++;

	}
	}
	catch(const std::exception& e)
	{
		std::cerr << e.what() << '\n';
		ft_exit();
	}
	
	

}


int main(int ac, char **av){

	Arachnida MyArachnida;
	ft_welcome();
	// ft_option();
    ft_parsse_input(ac, av, &MyArachnida);

}
