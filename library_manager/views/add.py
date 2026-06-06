from typing import Any, Optional

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse
from django.views import View

from library_manager.models.author import Author
from library_manager.models.book import Book


class AddView(View):
    def get(self, request: HttpRequest, entity: str) -> HttpResponse:
        AddView.check_entity(entity)

        context: dict[str, Any] = {"entity": entity}

        if entity == "book":
            context["inputs"] = [
                ("text", "Title", "title"),
                ("date", "Published Date", "published_date"),
                ("text", "ISBN", "isbn"),
            ]

            context["list_values"] = Author.objects.all()

        elif entity == "author":
            context["inputs"] = [
                ("text", "First Name", "first_name"),
                ("text", "Last Name", "last_name"),
                ("number", "Age", "age"),
            ]

            context["list_values"] = Book.objects.all()

        return render(request, "library_manager/add.html", context)

    def post(self, request: HttpRequest, entity: str) -> HttpResponse:
        AddView.check_entity(entity)

        print("***", "you are in post")
        print("***", request.POST)

        return redirect("lib_mngr:add", entity=entity)

    @staticmethod
    def check_entity(entity: str) -> HttpResponseNotFound | None:
        if entity not in ["book", "author"]:
            return HttpResponseNotFound()
        else:
            return None
