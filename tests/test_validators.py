import pytest

from app.validators import validate_cnpj, validate_cpf


# Tests for the validate_cpf function
@pytest.mark.parametrize("cpf, expected", [
    ("123.456.789-01", False),  # Invalid CPF
    ("111.111.111-11", False),  # CPF with all identical digits
    ("529.982.247-25", True),   # Valid CPF
    ("52998224725", True),      # Valid CPF without punctuation
    ("000.000.000-00", False),  # Invalid CPF with zeros
    ("abc.def.ghi-jk", False),  # Non-numeric input
    ("5299822472", False),      # CPF with fewer than 11 digits
    ("529982247251", False),    # CPF with more than 11 digits
])
def test_validate_cpf(cpf, expected):
    assert validate_cpf(cpf) == expected


# Tests for the validate_cnpj function
@pytest.mark.parametrize("cnpj, expected", [
    ("12.345.678/0021-95", False),  # Invalid CNPJ
    ("11.111.111/1111-11", False),  # CNPJ with all identical digits
    ("08.258.163/0001-80", True),   # Valid CNPJ
    ("04252011000110", True),       # Valid CNPJ without punctuation
    ("00.000.000/0000-00", False),  # Invalid CNPJ with zeros
    ("abc.def/ghi-jk", False),      # Non-numeric input
    ("0425201100011", False),       # CNPJ with fewer than 14 digits
    ("042520110001100", False),     # CNPJ with more than 14 digits
])
def test_validate_cnpj(cnpj, expected):
    assert validate_cnpj(cnpj) == expected
