if __name__ == "__main__":
    try:
        while True:
            try:
                x = input()
                complex(x)
                exit(0)
            except EOFError:
                exit(0)
            except ValueError:
                continue
    except KeyboardInterrupt:
        exit(0)
        