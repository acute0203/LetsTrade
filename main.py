from Platform.MT5Platform import MT5Platform

if __name__ == "__main__":
    with MT5Platform() as p:
        print("terminalInfo:",p.terminalInfo())
        print("version:",p.version())
