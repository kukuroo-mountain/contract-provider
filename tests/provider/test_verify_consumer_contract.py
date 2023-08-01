"""Test to verify the consumer contract."""
import os
import pytest
from pact import Verifier

from project import Project

PACT_BROKER_URL = "https://dragondive.pactflow.io/"
PACT_BROKER_TOKEN = os.environ["PACT_BROKER_TOKEN"]


@pytest.fixture
def verifier():
    return Verifier(
        provider="contract_provider",
        provider_base_url=f"https://jsonplaceholder.typicode.com",
    )


def test_verify_consumer_contract_with_contract_published_on_pact_broker_contract_is_fulfilled(
    verifier,
):
    """Verify the contracts published on the pact broker.

    Parameters
    ----------
    verifier : pact.Verifier
        Fixture for the contract verifier.
    """    
    return_code, __unused_logs = verifier.verify_with_broker(
        broker_url=PACT_BROKER_URL,
        broker_token=PACT_BROKER_TOKEN,
        publish_version=Project.get_version(),
        provider_version_branch="main",
        publish_verification_results=True,
        verbose=True,
    )
    assert return_code == 0
