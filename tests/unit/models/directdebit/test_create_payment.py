import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.direct_debit import payment_response
from xendit.models import DirectDebit


# fmt: off
class TestCreatePayment(ModelBaseTest):
    @pytest.fixture
    def default_direct_debit_payment_data(self):
        tested_class = DirectDebit
        class_name = "DirectDebit"
        method_name = "create_payment"
        http_method_name = "post"
        args = ()
        kwargs = {
            "reference_id": "mock-direct-debit-ref-123",
            "payment_method_id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
            "currency": "IDR",
            "amount": "60000",
            "callback_url": "http://webhook.site/",
            "idempotency_key": "idemp_key",
        }
        params = (args, kwargs)
        url = "/direct_debits"
        expected_correct_result = payment_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_direct_debit_payment_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_direct_debit_payment_data
        headers = {"Idempotency-key": "idemp_key"}
        body = {
            "reference_id": "mock-direct-debit-ref-123",
            "payment_method_id": "pm-b6116aea-8c23-42d0-a1e6-33227b52fccd",
            "currency": "IDR",
            "amount": "60000",
            "callback_url": "http://webhook.site/",
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [payment_response()], indirect=True)
    def test_return_direct_debit_payment_on_correct_params(
        self, mocker, mock_correct_response, default_direct_debit_payment_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_direct_debit_payment_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_direct_debit_payment_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_direct_debit_payment_data)

    @pytest.mark.parametrize("mock_correct_response", [payment_response()], indirect=True)
    def test_return_direct_debit_payment_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_direct_debit_payment_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_direct_debit_payment_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_direct_debit_payment_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_direct_debit_payment_data)

    @pytest.mark.parametrize("mock_correct_response", [payment_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
