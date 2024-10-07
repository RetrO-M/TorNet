#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
WHITE='\033[1;37m'
NC='\033[0m'

echo -e "${PURPLE}                    =----- "
echo -e "                   =++== "
echo -e "                  +*++ "
echo -e "                 =-*# "
echo -e "                 %:+*@ "
echo -e "              @%*::-=+%@ "
echo -e " /00000000   @*:..::=-+=@@ "
echo -e "|__  00__/ @#:.::..:---*++@ "
echo -e "   | 00    @::-..:::=--#***@   /000000 "
echo -e "   | 00   @#:=.:-..:--*#***@  /00__  00 "
echo -e "   | 00    @:=:-..-:+=*%###@ | 00  \__/ "
echo -e "   | 00    @#:--::::*-*%##@  | 00 "
echo -e "   | 00      @#-=--:+%##@@   | 00 "
echo -e "   |__/        @@@@@@@@      |__/ "

packages=(
    "requests"
    "colorama"
    "stem"
)

echo -e "${WHITE}Do you want to install Python3? Y/N${NC}"
read -p ">> " response

if [[ "$response" == "Y" || "$response" == "y" ]]; then
    echo -e "${GREEN}Installing Python 3...${NC}"
    sudo apt-get update
    sudo apt-get install python3
    echo -e "${GREEN}Python 3 has been successfully installed!${NC}"
else
    echo -e "${PURPLE}Skipping Python 3 installation.${NC}"
fi

echo -e "${YELLOW}[*] ${WHITE}Starting installation of Python packages...${NC}"

for package in "${packages[@]}"; do
    echo -e "${YELLOW}-------[ Installing ${package} ]-------${NC}"
    pip install $package
done

echo -e "${GREEN}[+]${WHITE} All packages have been successfully installed!${NC}"



