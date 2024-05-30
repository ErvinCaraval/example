from hypothesis import given
import hypothesis.strategies as st

# Ejemplo de función que sumará dos números
def add(a, b):
    return a + b

# Definición de estrategias para generar números enteros aleatorios
@st.composite
def integers_strategy(draw):
    return draw(st.integers())

# Prueba usando Hypothesis
@given(integers_strategy(), integers_strategy())
def test_addition(x, y):
    assert add(x, y) == x + y
