import random

random_list = []

def generate_random_list():
    for _ in range(4):
        random_number = random.randint(1, 6)
        random_list.append(random_number)
    print(random_list)
    
def verify_proposals(proposal_list, random_list):
    verify_number_in_list = ["[ ]","[ ]","[ ]","[ ]"]
    for index_proposal in range(len(proposal_list)):
        if proposal_list[index_proposal] == random_list[index_proposal]:
            verify_number_in_list[index_proposal] = "[*]"
        else :
            for index_verify in range(len(random_list)):
                if random_list[index_verify] == proposal_list[index_proposal]:
                    verify_number_in_list[index_proposal] = "[-]"
                    break
    return verify_number_in_list

    

try:
    number_of_input = 0
    proposal_list = []
    turn_numbers = 1
    generate_random_list()

    while turn_numbers < 11:
        print(f"vous etes au tour {turn_numbers}")
        while number_of_input < 4 :
            proposals = 0
            while proposals not in range(1, 7):
                try:
                    proposals = int(input("Enter your proposal of your list between 1 to 6 include, index number " + str(number_of_input + 1) + " : "))
                except ValueError:
                    proposals = 0
            proposal_list.append(proposals)
            number_of_input += 1
        print("Your proposals are:", proposal_list)
        proposals = verify_proposals(proposal_list, random_list)
        if proposals == ["[*]","[*]","[*]","[*]"]:
            print('You win !')
            break
        print("".join(map(str, proposals)))
        number_of_input = 0
        proposal_list = []
        turn_numbers += 1
        if turn_numbers == 11:
            print("You lose !")

except ValueError:
    print("Please enter a valid number.")

