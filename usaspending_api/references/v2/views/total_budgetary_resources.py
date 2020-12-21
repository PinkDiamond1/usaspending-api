from django.db.models import Sum
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.references.models.gtas_sf133_balances import GTASSF133Balances

from rest_framework.response import Response
from rest_framework.views import APIView
from usaspending_api.common.exceptions import InvalidParameterException, UnprocessableEntityException


class TotalBudgetaryResources(APIView):
    """
    This route sends a request to the backend to retrieve GTAS totals by FY/FP.
    """

    endpoint_doc = "usaspending_api/api_contracts/contracts/v2/references/total_budgetary_resources.md"

    @cache_response()
    def get(self, request):
        fiscal_year = request.query_params.get("fiscal_year")
        fiscal_period = request.query_params.get("fiscal_period")
        gtas_queryset = GTASSF133Balances.objects.values("fiscal_year", "fiscal_period")

        if fiscal_period:
            if not fiscal_year:
                raise InvalidParameterException("fiscal_period was provided without any fiscal_year.")
            else:
                if int(fiscal_period) < 2 or int(fiscal_period) > 12:
                    raise UnprocessableEntityException("fiscal_period must be in the range 2-12")
                gtas_queryset = gtas_queryset.filter(fiscal_year=fiscal_year, fiscal_period=fiscal_period)

        elif fiscal_year:
            gtas_queryset = gtas_queryset.filter(fiscal_year=fiscal_year)

        results = []
        for gtas in gtas_queryset.annotate(total_budgetary_resources=Sum("total_budgetary_resources_cpe")).order_by(
            "fiscal_year", "fiscal_period"
        ):
            results.append(
                {
                    "fiscal_year": gtas["fiscal_year"],
                    "fiscal_period": gtas["fiscal_period"],
                    "total_budgetary_resources": float(gtas["total_budgetary_resources"]),
                },
            )

        return Response({"results": results, "messages": []})
