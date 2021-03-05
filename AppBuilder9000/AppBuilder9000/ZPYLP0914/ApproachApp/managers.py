from django.db import models


class ItemsQuerySet(models.QuerySet):
    def get_items(self, col1, col2, col3, col4):
        return self.values(col1, col2, col3, col4)


class ItemsViewer(models.Manager):
    def get_queryset(self):
        return ItemsQuerySet(self.model,  using=self._db)

    def get_items(self, col1, col2, col3, col4):
        return self.get_queryset().get_items(col1, col2, col3, col4)
