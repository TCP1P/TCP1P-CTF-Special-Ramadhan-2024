import sys
import asyncio
import challenges

def print_help():
    print("Usage: python script.py [add-all | remove-all | start-all | stop-all | help]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add-all":
        asyncio.run(challenges.add())
    elif command == "remove-all":
        asyncio.run(challenges.remove())
    elif command == "start-all":
        asyncio.run(challenges.start())
    elif command == "stop-all":
        asyncio.run(challenges.stop())
    elif command == "help":
        print_help()
    else:
        print_help()
        sys.exit(1)
