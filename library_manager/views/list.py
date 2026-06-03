from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from library_manager.models.author import Author
from library_manager.models.book import Book


class ListView(View):
    def get(self, request: HttpRequest, entity: str) -> HttpResponse:
        if entity not in ["book", "author"]:
            return HttpResponseNotFound()
            # design a page that shows the error
            # provide a link to return home

        context: dict[str, Any] = {"entity": entity}

        if entity == "book":
            context["header"] = (
                "Title",
                "Published Date",
                "ISBN",
                "Authors",
            )
            print("*** book.objects", list(enumerate(Book.objects.all())))
            context["data"] = enumerate(Book.objects.all())
        elif entity == "author":
            context["header"] = (
                "First Name",
                "Last Name",
                "Age",
                "Books",
                "# of Books",
            )
            print("*** author.objects", list(enumerate(Author.objects.all())))
            context["data"] = enumerate(Author.objects.all())

        return render(request, "library_manager/list.html", context)
