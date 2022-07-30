"""Unittest for the Customer API."""

import pytest
from httpx import AsyncClient

from app.api_server import api_app


@pytest.mark.anyio
async def test_get_customer_by_phone():
    """Test get customer by phone."""
    async with AsyncClient(app=api_app) as api_client:
        response = await api_client.get("/customers/0909445408")
    assert response.status_code == 200
