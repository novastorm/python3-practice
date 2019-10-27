import pytest
import swiftEnum


class Barcode(swiftEnum.SwiftEnum):
    upca = (int, int, int, int)
    qrcode = (str,)
    handwritten = (str,)


class Test_Barcode:

    def test_initialization(self):

        barcodes = [
            Barcode.upca(8, 85909, 51226, 3),
            Barcode.qrcode('ABCDEFGHIJKLMNOP'),
            Barcode.handwritten('ABCDEFGHIJKLMNOP')
        ]

        for e in barcodes:
            print(e)

        assert barcodes[0] == barcodes[0]
        assert barcodes[0] != barcodes[1]

        print(hash(barcodes[0]))
        print(repr(barcodes[0]))

    def test_initialization_failure(self):
        with pytest.raises(TypeError):
            barcode = Barcode.upca()
        with pytest.raises(TypeError):
            barcode = Barcode.qrcode()
        with pytest.raises(TypeError):
            barcode = Barcode.handwritten()
