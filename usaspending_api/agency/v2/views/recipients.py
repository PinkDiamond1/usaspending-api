from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any
from usaspending_api.agency.v2.views.agency_base import AgencyBase
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.common.helpers.sql_helpers import execute_sql_to_ordered_dictionary


class RecipientList(AgencyBase):
    """
    Obtain the count of recipients for a specific agency in a single
    fiscal year as well as the percentile data needed for a box-and-whisker plot.
    """

    endpoint_doc = "usaspending_api/api_contracts/contracts/v2/agency/toptier_code/recipients.md"

    @cache_response()
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        self.params_to_validate = ["fiscal_year"]
        results = self.get_recipients_queryset()
        return Response(results)

    def get_recipients_queryset(self):
        SQL = """
        select
        count(recipient_hash),
        max(recipient_amount),
        min(recipient_amount),
        percentile_disc(0.25) within group (order by recipient_agency.recipient_amount) as "25th_percentile",
        percentile_disc(0.5) within group (order by recipient_agency.recipient_amount) as "50th_percentile",
        percentile_disc(0.75) within group (order by recipient_agency.recipient_amount) as "75th_percentile"
        from recipient_agency  where fiscal_year={fiscal_year} and toptier_code='{toptier_code}';
        """.format(
            fiscal_year=self.fiscal_year, toptier_code=self.toptier_code
        )

        results = execute_sql_to_ordered_dictionary(SQL)
        return {
            "toptier_code": self.toptier_code,
            "fiscal_year": self.fiscal_year,
            "results": results,
            "messages": self.standard_response_messages,
        }
        return results
