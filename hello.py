
def main():
  print("Hello")

def test_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "Hello World!\n"
