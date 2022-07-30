"""Decorators for the app."""

from functools import wraps

from fastapi import HTTPException, status

from app.exceptions import CustomerNotFoundException
from app.grpc_services import customer_client as grpc_customer_client


def build_activity_content(kwargs):
    """Build activity content.
    This function is used to build activity content.
    """
    content = "Search service {} and sort by {} in {}"
    order_by = kwargs.get("order_by")
    sort_asc = kwargs.get("sort_asc")
    search_code = kwargs.get("search_code", None)
    search_name = kwargs.get("search_name", None)

    search_content = ""
    if search_code:
        search_content = f"with code {search_code}"
    if search_name:
        search_content = f"with name {search_name}"

    sort_content = "ascending" if not sort_asc else "descending"
    content = content.format(search_content, order_by, sort_content)

    return content


def track_customer_activity(func):
    """Track customer activity.
    This decorator is used to track customer activity.
    This decorator is only suported for async functions.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        """Wrapper."""
        customer_id = kwargs.get("customer_id")
        activity_content = build_activity_content(kwargs)
        try:
            await grpc_customer_client.set_customer_activity(
                customer_id,
                activity_content,
            )
        except CustomerNotFoundException as exception:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found",
            ) from exception

        try:
            return await func(*args, **kwargs)
        except Exception as exception:
            raise exception from exception

    return wrapper
