from django.urls import path

from .views import (
    AsyncExampleClassView,
    ExampleListView,
    HomeView,
    admin_section,
    example_messages,
    example_task_view,
    example_toasts,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin-section/", admin_section, name="admin_section"),
    path(
        "examples/",
        ExampleListView.as_view(),
        name="example_list",
    ),
    path(
        "examples/messages/",
        example_messages,
        name="example_messages",
    ),
    path(
        "examples/toasts/",
        example_toasts,
        name="example_toasts",
    ),
    path(
        "async-class-view/",
        AsyncExampleClassView.as_view(),
        name="example_async_class_view",
    ),
    path(
        "example-task/",
        example_task_view,
        name="example_task",
    ),
]
