import unittest
import math

"""
    Norwegian beskriver reglene for bagasje slik:
    * Hvert enkelt kolli må ikke veie mer enn 32 kg eller mindre enn 2 kg.
    * Du må betale overvekt for kolli som veier over 23 kg. Prisen for overvekt er 135 NOK  per kilo

    Skriv en kalkulator som beregner hvor mye man må betale for en gitt vekt.
    Input vil være et desimaltall mellom 2 og 32 kilo.
    Prisen er per begynte kilo rundet oppover.
"""
def bagasje_overvekt(vekt):
    pris = 0
    if vekt > 23:
        a = math.ceil(vekt)
        ekstra_pris = 135
        ekstra_kilo = a - 23
        pris = ekstra_pris * ekstra_kilo
    
    return pris

class BaggageCalc(unittest.TestCase):
    def test_underweight(self):
        self.assertEquals(bagasje_overvekt(5.5), 0)

    def test_overweight(self):
        self.assertEquals(bagasje_overvekt(30), 945)
    
    def test_rounded(self):
        self.assertEqual(bagasje_overvekt(23.5), 135)
        

if __name__ == '__main__':
    unittest.main()