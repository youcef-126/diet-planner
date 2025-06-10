"""Minimal wrapper around Supabase client."""
import os
from typing import Any, Dict

try:
    from supabase import create_client, Client  # type: ignore
except ImportError:  # pragma: no cover - library not installed in tests
    Client = Any  # type: ignore
    def create_client(*args: str, **kwargs: str) -> Any:
        raise RuntimeError(
            "supabase-py package is required to use Supabase features")


def get_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be set")
    return create_client(url, key)


def save_results(data: Dict[str, Any]) -> None:
    """Store calculation results in Supabase table `calculations`."""
    client = get_client()
    client.table("calculations").insert(data).execute()
