import random 
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Witch components should your username be of")
    
    parser.add_argument("--movie", type=bool, default=False, help="Use movie titels list")
    parser.add_argument("--firstnames", type=bool, default=False, help="Use firstnames list")
    parser.add_argument("--lastnames", type=bool, default=False, help="Use lastnames list")
    parser.add_argument("--locations", type=bool, default=False, help="Use location list")
    parser.add_argument("--english", type=bool, default=False, help="Use the list of the 1000 most used english words")
    parser.add_argument("--digits", type=bool, default=False, help="Use random numbers")
    parser.add_argument("--point", type=bool, default=False, help="Use a point on a random position")
    
    return parser.parse_args()

def get_list_entry(list_entrys):
    
    with open(list_entrys, 'r') as file:
        content = file.read()
        file.close()
        
    word_list = content.split('\n')
    return random.choice(word_list)

def main():
    args = parse_arguments()
    
    username = []
    
    if args.firstnames:
        username.append(get_list_entry("firstnames.txt"))
    if args.movie:
        username.append(get_list_entry("movies.txt"))
    if args.lastnames:
        username.append(get_list_entry("lastnames.txt"))
    if args.locations:
        username.append(get_list_entry("locations.txt"))
    if args.english:
        username.append(get_list_entry("1000_english_words.txt"))
    if args.digits:
        username.append(str(random.randint(0, 9)))
    if args.point:
        username.append('.')
        
    random.shuffle(username)
    username = ''.join(username)
    print(username)
    
    
if __name__ == "__main__":
    main()   
    