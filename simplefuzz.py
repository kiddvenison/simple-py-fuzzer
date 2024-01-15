import sys
import requests

def test_ip_resources(ip, wordlist_file, extensions_file, verbose=False):
    with open(wordlist_file, 'r') as file:
        wordlist = file.read().split('\n')
    
    with open(extensions_file, 'r') as file:
        extensions = file.read().split('\n')

    try:
        for word in wordlist:
            for extension in extensions:
                url = f"{ip}/{word}.{extension}"
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Resource found at {url}")
                elif verbose:
                    print(f"No resource found at {url}")
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    verbose = '-v' in sys.argv
    if verbose:
        sys.argv.remove('-v')

    if len(sys.argv) != 4:
        print("Usage: python test.py <ip> <wordlist_file> <extensions_file> [-v]")
        sys.exit(1)
    
    ip = sys.argv[1]
    wordlist_file = sys.argv[2]
    extensions_file = sys.argv[3]
    test_ip_resources(ip, wordlist_file, extensions_file, verbose)
