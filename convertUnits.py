'''
UnitConvertor class serves to hold unit conversions. 

Add source and destination units along with a ratio. Or, if conversion is more
than a simple ratio, provide convertor and invertor functions. This adds the
appropriate conversion to the internal conversions reference table.

Use the convert method to convert available units.
'''
class UnitConvertor:
  def __init__(self):
    self.conversions = {}

  def addConvertor(self, fromUnit, toUnit, ratio, convertor=None, invertor=None):
    '''
    Add conversion functions and unit mapper

    Input parameter includes a ratio or both a convertor and invertor function
    '''
    if not (ratio or (convertor and invertor)):
      raise Exception('ratio xor (convertor and invertor)')

    if ratio:
      convertor = lambda x : x * ratio
      invertor = lambda x : x * 1 / ratio

    self.conversions[(fromUnit, toUnit)] = convertor
    self.conversions[(toUnit, fromUnit)] = invertor


  def convert(self, srcUnits, dstUnits, value):
    '''
    return conversion if exists
    '''
    if (srcUnits,dstUnits) not in self.conversions:
      raise Exception('conversion does not exist.')

    return self.conversions[(srcUnits,dstUnits)](value)



###############################################################################

import unittest

class Test_EvaluateInorderExpression(unittest.TestCase):

    def setUp(self):

      self.unitConvertor = UnitConvertor()

      kg_to_lbs = 2.20462
      m_to_ft = 3.28084

      def CToF(value):
        return (value * 9 / 5) + 32

      def FToC(value):
        return (value - 32) * 5 / 9

      self.unitConvertor.addConvertor('kg', 'lbs', kg_to_lbs)
      self.unitConvertor.addConvertor('m', 'ft', m_to_ft)
      self.unitConvertor.addConvertor('c', 'f', ratio=None, convertor=CToF, invertor=FToC)

    def test_1(self):
        srcUnits = 'kg'
        dstUnits = 'lbs'
        convert = 2
        invert = 4.40924
        self.assertEqual(self.unitConvertor.convert(srcUnits, dstUnits, convert), invert)
        self.assertEqual(self.unitConvertor.convert(dstUnits, srcUnits, invert), convert)

    def test_2(self):
        srcUnits = 'm'
        dstUnits = 'ft'
        convert = 10
        invert = 32.8084
        self.assertEqual(self.unitConvertor.convert(srcUnits, dstUnits, convert), invert)
        self.assertEqual(self.unitConvertor.convert(dstUnits, srcUnits, invert), convert)

    def test_3(self):
        srcUnits = 'c'
        dstUnits = 'f'
        convert = 0.0
        invert = 32.0
        self.assertEqual(self.unitConvertor.convert(srcUnits, dstUnits, convert), invert)
        self.assertEqual(self.unitConvertor.convert(dstUnits, srcUnits, invert), convert)

    def test_4(self):
        srcUnits = 'c'
        dstUnits = 'f'
        convert = -40
        invert = -40
        self.assertEqual(self.unitConvertor.convert(srcUnits, dstUnits, convert), invert)
        self.assertEqual(self.unitConvertor.convert(dstUnits, srcUnits, invert), convert)

if __name__ == '__main__':
        unittest.main()
