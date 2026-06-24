from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer


class ProductSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        query = request.GET.get("q", "").lower()

        if not query:
            return Response({
                "error": "Search query required"
            }, status=400)

        category_matches = Product.objects.filter(
            category__icontains=query
        )

        tag_matches = Product.objects.filter(
            tags__icontains=query
        ).exclude(
            category__icontains=query
        )

        text_matches = Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(product_description__icontains=query)
        ).exclude(
            category__icontains=query
        ).exclude(
            tags__icontains=query
        )

        results = []

        for product in category_matches:
            results.append({
                "id": product.id,
                "product_name": product.product_name,
                "category": product.category,
                "tags": product.tags,
                "relevance_score": 0.95,
                "rank_reason": "Category match"
            })

        for product in tag_matches:
            results.append({
                "id": product.id,
                "product_name": product.product_name,
                "category": product.category,
                "tags": product.tags,
                "relevance_score": 0.70,
                "rank_reason": "Tag match"
            })

        for product in text_matches:
            results.append({
                "id": product.id,
                "product_name": product.product_name,
                "category": product.category,
                "tags": product.tags,
                "relevance_score": 0.40,
                "rank_reason": "Description/Name match"
            })

        return Response({
            "query": query,
            "total_results": len(results),
            "results": results
        })