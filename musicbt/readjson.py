import json

def main():
    try:
        with open('2.json') as f:
            j = json.load(f)
            print(len(j))
            for i in range(len(j)):
                if len(j[i]) != 0:
                    with open('b7t.txt','a+') as f:
                        n = j[i]['bt_url'][0] + '<br/>'
                        print(n)
                        f.write(n)
            print('suseess')
    except Exception as e:
        raise e
    finally:
        f.close()


if __name__ == '__main__':
    main()
