import sys
from cli.menu_cli import CLIMenu
from gui.menu_gui import GUIMenu

def main():
    # Checks if the user passed an argument
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        # Verify cli argument
        if mode == "--cli":
            app = CLIMenu()
        elif mode == "--gui":
            # Verify gui argument
            app = GUIMenu()
        else:
            print(f"Unknown mode: {mode}. Use --cli or --gui")
    else:
        #Default: If no arguments, opens GUI verson
        GUIMenu()

if __name__ == "__main__":
    main()