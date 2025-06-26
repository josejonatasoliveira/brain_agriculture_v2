from fastapi.testclient import TestClient

from app.utils.utils import validate_cpf_cnpj, validate_farm_area
from app.main import app

client = TestClient(app)

def test_validate_cpf_cnpj_should_return_true_with_valid_cpf():
    # GIVEN
    valid_cpf = "529.982.247-25"

    # WHEN
    result = validate_cpf_cnpj(valid_cpf)

    # THEN
    assert result is True

def test_validate_cpf_cnpj_should_return_false_with_invalid_cpf():
    # GIVEN
    invalid_cpf = "111.111.111-11"

    # WHEN
    result = validate_cpf_cnpj(invalid_cpf)

    # THEN
    assert result is False

def test_validate_cpf_cnpj_should_return_true_with_valid_cnpj():
    # GIVEN
    valid_cnpj = "33.014.556/0001-96"

    # WHEN
    result = validate_cpf_cnpj(valid_cnpj)

    # THEN
    assert result is True

def test_validate_cpf_cnpj_should_return_false_with_invalid_cnpj():
    # GIVEN
    invalid_cnpj = "11.111.111/1111-11"

    # WHEN
    result = validate_cpf_cnpj(invalid_cnpj)

    # THEN
    assert result is False

def test_validate_cpf_cnpj_should_return_false_with_invalid_length():
    # GIVEN
    invalid_input = "12345"

    # WHEN
    result = validate_cpf_cnpj(invalid_input)

    # THEN
    assert result is False

def test_validate_cpf_cnpj_must_accept_numbers_without_formatting():
    # GIVEN
    valid_cpf = "52998224725"

    # WHEN
    result = validate_cpf_cnpj(valid_cpf)

    # THEN
    assert result is True

def test_validate_farm_area_should_return_true_when_areas_sum_is_less_than_total():
    # GIVEN
    result = validate_farm_area(100.0, 60.0, 30.0)

    # WHEN/THEN
    assert result is True

def test_validate_farm_area_should_return_true_when_areas_sum_equals_total():
    # GIVEN
    result = validate_farm_area(100.0, 50.0, 50.0)

    # WHEN/THEN
    assert result is True

def test_validate_farm_area_should_return_false_when_areas_sum_exceeds_total():
    # GIVEN
    result = validate_farm_area(100.0, 70.0, 40.0)

    # WHEN/THEN
    assert result is False

def test_validate_farm_area_must_handle_zero_values_correctly():
    # GIVEN
    result = validate_farm_area(0.0, 0.0, 0.0)

    # WHEN/THEN
    assert result is True

def test_validate_farm_area_should_work_with_float_precision():
    # GIVEN
    result = validate_farm_area(100.5, 50.25, 50.25)

    # WHEN/THEN
    assert result is True