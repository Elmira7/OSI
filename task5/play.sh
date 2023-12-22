#!/bin/bash

RED='\e[31m'
GREEN='\e[32m'
RESET='\e[0m'

declare -i steps=0
declare -i counter=0
declare -i hit=0
declare -i miss=0
declare -a numbers

while :
do
    echo "Step: $((counter + 1))"
    
    read -p "Please enter number from 0 to 9 (q - quit): " input

    case "${input}" in
        [0-9])
            random_number=${RANDOM: -1}

            if [[ "${input}" -eq "${random_number}" ]]; then
                echo -e "Hit! My number: ${GREEN}${random_number}${RESET}"
                ((hit++))
            else
                echo -e "Miss! My number: ${RED}${random_number}${RESET}"
                ((miss++))
            fi

            total=$((hit + miss))
            hit_percent=$((hit * 100 / total))
            miss_percent=$((100 - hit_percent))

            echo "Hit: ${hit_percent}%" "Miss: ${miss_percent}%"
            
            echo -e "Numbers: ${numbers[@]: -10}"

            if [[ "${input}" -eq "${random_number}" ]]; then
                numbers+=("${GREEN}${input}${RESET}")
            else
                numbers+=("${RED}${input}${RESET}")
            fi

            ((counter++))
            ;;

        q)
            echo "Bye"
            exit 0
            ;;

        *)
            echo "Not valid input. Please repeat."
            ;;
    esac
done
