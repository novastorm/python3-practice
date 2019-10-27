import pytest
import swiftEnum


class Barcode(swiftEnum.SwiftEnum):
    upca = (int, int, int, int)
    qrcode = (str,)
    handwritten = (str,)


class Test_Barcode:

    I = 'input'
    E = 'expected'

    def test_initialization(self):

        I = self.__class__.I
        E = self.__class__.E

        barcodes = [
            {
                I: Barcode.upca(8, 85909, 51226, 3),
                E: "Barcode.upca(8, 85909, 51226, 3)"
            },
            {
                I: Barcode.qrcode('ABCDEFGHIJKLMNOP'),
                E: "Barcode.qrcode('ABCDEFGHIJKLMNOP')"
            },
            {
                I: Barcode.handwritten('ABCDEFGHIJKLMNOP'),
                E: "Barcode.handwritten('ABCDEFGHIJKLMNOP')"
            }
        ]

        for t in barcodes:
            i, e = t[I], t[E]
            assert str(i) == e

        assert barcodes[0][I] == barcodes[0][I]
        assert barcodes[0][I] != barcodes[1][I]
        assert barcodes[1][I] != barcodes[2][I]

        assert isinstance(hash(barcodes[0][I]), int)
        assert repr(barcodes[0][I]) == barcodes[0][E]

    def test_initialization_failure(self):
        with pytest.raises(TypeError):
            barcode = Barcode.upca()
        with pytest.raises(TypeError):
            barcode = Barcode.qrcode()
        with pytest.raises(TypeError):
            barcode = Barcode.handwritten()
