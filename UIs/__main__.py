def main():
    import os
    if(os.path.exists("../assets/hash.txt") and os.path.exists("../temp/passwords.enc")):
        import LoginPage
    else:
        import PasswordStartupUI

if(__name__=='__main__'):
    main()