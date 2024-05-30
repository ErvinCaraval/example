from hypothesis import given
import hypothesis.strategies as st

# La función que quieres probar
def add(a, b):
    return a + b

# Estrategias de Hypothesis para generar entradas de prueba
@st.composite
def integers_strategy(draw):
    return draw(st.integers())

# Prueba usando Hypothesis
@given(integers_strategy(), integers_strategy())
def test_addition(x, y):
    assert add(x, y) == x + y

# Ejecutar la prueba
if __name__ == "__main__":
    test_addition()
