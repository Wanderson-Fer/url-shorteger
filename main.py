import pyshorteners

if __name__ == '__main__':
    long_url = str(input('Informe a URL a ser encurtada: '))

    # Tiny shortener service
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)

    print('Here your url shorted ' + short_url)
    input('Enter to exit')
