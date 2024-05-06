if __name__ == "__main__":
    try:
        while True:
            try:
                x = input()
            except EOFError:
                exit(0)
                
            try:
                complex(x)
            except ValueError:
                continue
            exit(0)
    except KeyboardInterrupt:
        exit(0)
        