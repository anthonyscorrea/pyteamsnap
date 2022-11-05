from .base import BaseApiObject


class AvailabilitySummary(BaseApiObject):
    rel = "availability_summaries"
    type = "availability_summary"
    version = "3.866.0"

    @property
    def data(self):
        """Data dictionary for object

        :return: dict: dict with keys:
        """
        return super().data
