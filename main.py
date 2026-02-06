import sys
from cli.menu_cli import CLIMenu


def main():
    # Checks if the user passed an argument
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        # Verify cli argument
        if mode == "--cli":
            app = CLIMenu()
        else:
            print(f"Unknown mode: {mode}. Use --cli")
    else:
        #Default: If no arguments, opens CLI verson
        CLIMenu()

if __name__ == "__main__":
    main()