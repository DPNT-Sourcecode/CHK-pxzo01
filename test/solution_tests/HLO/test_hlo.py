from solutions.HLO import hello

class TestHello():
    def test_hello(self):
        assert hello("Tom") == "Hello Tom!"