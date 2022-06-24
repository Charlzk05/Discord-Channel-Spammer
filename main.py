import requests
import os
import time
from colorama import Fore
from colorama import Style

if __name__ == "__main__":
    try:
        os.system("cls")
        print(f"{Fore.LIGHTBLUE_EX}Discord Simple Channel Spammer by Charlzk")
        print("Press Ctrl + C to Stop")
        authorization = input(f"{Fore.LIGHTGREEN_EX}\nInsert your Token: ")
        spam_option = input("Limited Spam (1) / Infinite Spam (2): ")

        if "1" in spam_option:
            headers = {
                "authorization": f"{authorization}"
            }

            channel_id = input("Channel ID: ")
            number_of_spam = input("Number of Spams: ")
            spam_delay = input("Delay (Seconds): ")
            message_content = input("Message Content: ")
            content = message_content

            payload = {
                "content": f"{content}"
            }

            os.system("cls")
            print(f"{Fore.LIGHTBLUE_EX}Press Ctrl + C to Stop\n")
            for zero in range(int(number_of_spam)):
                try:
                    requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, data=payload)
                    print(f"{Fore.GREEN}Message Sent to {channel_id}!\nContent: {content}\n{Style.RESET_ALL}")
                except:
                    print(f"{Fore.RED}Something went wrong :/{Style.RESET_ALL}")
                    break

                time.sleep(int(float(spam_delay)))
            print(f"{Fore.WHITE}Operation Done!{Style.RESET_ALL}")
        elif "2" in spam_option:
            headers = {
                "authorization": f"{authorization}"
            }
            channel_id = input("Channel ID: ")
            spam_delay = input("Delay (Seconds): ")
            message_content = input("Message Content: ")
            content = message_content

            payload = {
                "content": f"{content}"
            }

            os.system("cls")
            print(f"{Fore.LIGHTBLUE_EX}Press Ctrl + C to Stop\n")
            num1 = 0
            while num1 <= 10:
                try:
                    requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, data=payload)
                    print(f"{Fore.GREEN}Message Sent to {channel_id}!\nContent: {content}\n{Style.RESET_ALL}")
                except:
                    print(f"{Fore.RED}Something went wrong :/{Style.RESET_ALL}")
                    break

                time.sleep(int(float(spam_delay)))
        else:
            print(f"{Fore.RED}\nInvalid Option :/{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"{Fore.RED}\nProgram is closed!{Style.RESET_ALL}")