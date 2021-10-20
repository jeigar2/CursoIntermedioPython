
def run():
    palindromo = lambda string : string.lower().replace(' ','') == string[::-1].lower().replace(' ','')
    print("dabale arroz a la zorra el abad es palindromo", palindromo("dabale arroz a la zorra el abad"))
    print("Ana es palindromo",palindromo("Ana"))

if __name__ == "__main__":
    run()