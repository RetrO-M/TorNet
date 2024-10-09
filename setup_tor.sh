#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
WHITE='\033[1;37m'
NC='\033[0m'

echo -e "${GREEN}                    =----- "
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

echo -e "${PURPLE}[*]$ Installation of TOR${NC}"

sudo apt-get update
sudo apt-get tor

if [ $? -eq 0 ]; then
    echo -e "${GREEN}[*] Tor has been installed successfully!${NC}"
else
    echo -e "${YELLOW}[!] There was an issue installing Tor. Please check your package manager settings.${NC}"
    exit 1
fi

read -sp "Enter a password for Tor: " password
echo

hash_password=$(tor --hash-password "$password")

if [ $? -eq 0 ]; then
    echo -e "${GREEN}[*] Password hash generated successfully!${NC}"
    echo -e "${WHITE}Password hash: $hash_password${NC}"
else
    echo -e "${YELLOW}[!] Failed to generate password hash. Please ensure Tor is installed correctly.${NC}"
    exit 1
fi

echo -e "${PURPLE}[*]${WHITE} Configuration Instructions:${NC}"
echo -e "To secure your Tor setup, add the following line to your Tor configuration file (torrc):"
echo -e "${WHITE}ControlPort 9051${NC}"
echo -e "${WHITE}HashedControlPassword $hash_password${NC}"
echo -e "${PURPLE}[*]${WHITE} You can find the torrc file typically at /etc/tor/torrc.${NC}"
echo -e "${PURPLE}[*]${WHITE} After updating the configuration, restart the Tor service:${NC}"
echo -e "${GREEN}sudo systemctl restart tor${NC}"


echo -e "${GREEN}[*] Thank you ! ${NC}"