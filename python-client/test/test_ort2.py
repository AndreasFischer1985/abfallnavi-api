"""
    Abfallnavi API

    Termine für Leerung des Abfalls nach Abfallart (Papier, Restmüll, ...). Beispielswerte sind für das Rathaus Nürnberg (Hauptmarkt 18, Nürnberg).  # Kommunen / Regionen  Das System ist in diverse Regionen unterteilt. Zu einer `Region` gehören ein oder mehrere Kommunen.  * `aachen`: Aachen * `zew2`: AWA Entsorgungs GmbH * `aw-bgl2`: Bergisch Gladbach * `bav`: Bergischer Abfallwirtschaftverbund * `din`: Dinslaken * `dorsten`: Dorsten * `gt2`: Gütersloh * `hlv`: Halver * `coe`: Kreis Coesfeld * `krhs`: Kreis Heinsberg * `pi`: Kreis Pinneberg * `krwaf`: Kreis Warendorf * `lindlar`: Lindlar * `stl`: Lüdenscheid * `nds`: Norderstedt * `nuernberg`: Nürnberg * `roe`: Roetgen * `solingen`: Solingen * `wml2`: EGW Westmünsterland  # Benutzung  Für die Abfrage von Terminen ist eine Reihe von IDs (von Orten, Straßen und/oder Hausnummern) in Erfahrung zu bringen. Vorsicht:IDs können sich mit der Zeit ändern  1. Orte aus System holen 2. Mit Ort die Straßen abfragen 3. Mit Straße die Hausnummern abfragen 4. Mit Haunummer die möglichen Fraktionen (Müllsorten) abfragen 5. Mit Hausnummer und Fraktionen alle Termine abrufen  Manchmal wird nicht nach Hausnummer unterschieden   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.abfallnavi.model.ort2 import Ort2

from deutschland import abfallnavi


class TestOrt2(unittest.TestCase):
    """Ort2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrt2(self):
        """Test Ort2"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Ort2()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
