class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def zestarni(self):
        self.vek += 1

def test_zestarni():
    # Arrange
    my_osoba = Osoba("pavel", 40)

    # Act
    my_osoba.zestarni()
    # Assert
    assert my_osoba.vek == 41, "Osobe se nezvedl vek o jedna pri volani zestarni()"


