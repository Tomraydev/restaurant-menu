from rest_framework import filters
from rest_framework.compat import coreapi


class MenuFilter(filters.BaseFilterBackend):
    """Filter defined so that swagger can properly display query parameters."""

    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(name="sort", description="Sort by name|num_dishes", required=False, location="query"),
            coreapi.Field(name="name", description="Filter by name", required=False, location="query"),
            coreapi.Field(
                name="added_after",
                description="Only show items added after given date.",
                required=False,
                location="query",
            ),
            coreapi.Field(
                name="added_before",
                description="Only show items added before given date.",
                required=False,
                location="query",
            ),
            coreapi.Field(
                name="updated_after",
                description="Only show items updated after given date.",
                required=False,
                location="query",
            ),
            coreapi.Field(
                name="updated_before",
                description="Only show items updated before given date.",
                required=False,
                location="query",
            ),
        ]

        return fields
